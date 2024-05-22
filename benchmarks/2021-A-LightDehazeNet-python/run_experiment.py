import os

os.environ["CUDA_VISIBLE_DEVICES"] = "1"
import torch
import torch.nn as nn
import torchvision
import torch.backends.cudnn as cudnn
import torch.optim

import sys
import argparse
import time
import image_data_loader
import lightdehazeNet
import numpy as np
from torchvision import transforms


def weights_init(m):
    classname = m.__class__.__name__
    if classname.find("Conv") != -1:
        m.weight.data.normal_(0.0, 0.02)
    elif classname.find("BatchNorm") != -1:
        m.weight.data.normal_(1.0, 0.02)
        m.bias.data.fill_(0)


def train(args):

    ld_net = lightdehazeNet.LightDehaze_Net().cuda()
    ld_net.apply(weights_init)

    training_data = image_data_loader.hazy_data_loader(args["train_dir"])
    validation_data = image_data_loader.hazy_data_loader(args["val_dir"], mode="val")
    training_data_loader = torch.utils.data.DataLoader(
        training_data, batch_size=16, shuffle=True, num_workers=4, pin_memory=True
    )
    validation_data_loader = torch.utils.data.DataLoader(
        validation_data, batch_size=1, shuffle=False, num_workers=0, pin_memory=True
    )

    criterion = nn.MSELoss().cuda()
    optimizer = torch.optim.Adam(
        ld_net.parameters(), lr=float(args["learning_rate"]), weight_decay=0.0001
    )

    ld_net.train()

    num_of_epochs = int(args["epochs"])
    dataset_name = args["dataset_name"]
    if not os.path.exists(f"trained_weights/{dataset_name}/"):
        os.makedirs(f"trained_weights/{dataset_name}/")
    if not os.path.exists(f"training_data_captures/{dataset_name}/"):
        os.makedirs(f"training_data_captures/{dataset_name}/")

    for epoch in range(num_of_epochs):
        print(">> train")
        for iteration, (hazefree_image, hazy_image) in enumerate(training_data_loader):
            hazefree_image = hazefree_image.cuda()
            hazy_image = hazy_image.cuda()

            dehaze_image = ld_net(hazy_image)

            loss = criterion(dehaze_image, hazefree_image)

            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm(ld_net.parameters(), 0.1)
            optimizer.step()

            if ((iteration + 1) % 1) == 0:
                print("Loss at iteration", iteration + 1, ":", loss.item())
            if ((iteration + 1) % int(args["save_epoch"])) == 0:

                torch.save(
                    ld_net.state_dict(),
                    f"trained_weights/{dataset_name}/" + "Epoch" + str(epoch) + ".pth",
                )

        print(">> val")
        # Validation Stage
        for iter_val, (hazefree_image, hazy_image) in enumerate(validation_data_loader):

            hazefree_image = hazefree_image.cuda()
            hazy_image = hazy_image.cuda()

            dehaze_image = ld_net(hazy_image)

            torchvision.utils.save_image(
                torch.cat((hazy_image, dehaze_image, hazefree_image), 0),
                f"training_data_captures/{dataset_name}/" + str(iter_val + 1) + ".jpg",
            )

        torch.save(
            ld_net.state_dict(),
            f"trained_weights/{dataset_name}/" + "trained_LDNet.pth",
        )


if __name__ == "__main__":

    ap = argparse.ArgumentParser()
    ap.add_argument(
        "-dn",
        "--dataset_name",
        default="RESIDE",
    )
    ap.add_argument(
        "-se",
        "--save_epoch",
        default=3605,
    )
    ap.add_argument(
        "-td",
        "--train_dir",
        default="/home/lx/nas/Dataset/03_RWIDE/05_other_datasets/RESIDE/train",
    )
    ap.add_argument(
        "-vd",
        "--val_dir",
        default="/home/lx/nas/Dataset/03_RWIDE/05_other_datasets/RESIDE/test",
    )
    ap.add_argument(
        "-e", "--epochs", default=1000, help="number of epochs for training"
    )
    ap.add_argument(
        "-lr",
        "--learning_rate",
        default=0.0001,
        help="learning rate for training",
    )

    args = vars(ap.parse_args())

    train(args)

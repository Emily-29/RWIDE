# @author: hayat
import os
import sys
import torch
import torch.utils.data as data
import numpy as np
from PIL import Image
import glob
import random
import cv2
import torchvision.transforms.functional as TF
from torchvision import transforms

random.seed(1143)


def preparing_training_data(images_dir):

    train_data = []
    hazefree_images_dir = os.path.join(images_dir, "clear/")
    hazeeffected_images_dir = os.path.join(images_dir, "hazy/")

    hazy_data = glob.glob(hazeeffected_images_dir + "*.jpg")

    data_holder = {}

    for h_image in hazy_data:
        h_image = h_image.split("/")[-1]
        id_ = h_image
        # id_ = h_image.split("_")[0] + "_" + h_image.split("_")[1] + ".jpg"
        if id_ in data_holder.keys():
            data_holder[id_].append(h_image)
        else:
            data_holder[id_] = []
            data_holder[id_].append(h_image)

    train_ids = []
    # val_ids = []

    num_of_ids = len(data_holder.keys())
    for i in range(num_of_ids):
        if True:  # i < num_of_ids*9/10
            train_ids.append(list(data_holder.keys())[i])
        # else:
        # val_ids.append(list(data_holder.keys())[i])

    for id_ in list(data_holder.keys()):

        if id_ in train_ids:
            for hazy_image in data_holder[id_]:

                train_data.append(
                    [hazefree_images_dir + id_, hazeeffected_images_dir + hazy_image]
                )

        # else:
        # 	for hazy_image in data_holder[id_]:

        # 		validation_data.append([hazefree_images_dir + id_, hazeeffected_images_dir + hazy_image])

    random.shuffle(train_data)
    # random.shuffle(validation_data)

    return train_data
    # return train_data, validation_data


class hazy_data_loader(data.Dataset):

    def __init__(self, images_dir, mode="train"):

        self.data = preparing_training_data(images_dir)

        self.data_dict = self.data
        print(f"Number of {mode} Images:", len(self.data))
        self.mode = mode

    def __getitem__(self, index):

        hazefree_image_path, hazy_image_path = self.data_dict[index]

        hazefree_image = Image.open(hazefree_image_path).convert("RGB")
        hazy_image = Image.open(hazy_image_path).convert("RGB")

        if self.mode == "train":
            i, j, h, w = transforms.RandomCrop.get_params(
                hazy_image, output_size=(128, 128)
            )
            hazy_image = TF.crop(hazy_image, i, j, h, w)
            hazefree_image = TF.crop(hazefree_image, i, j, h, w)

        width, height = hazy_image.size
        new_width = width // 2
        new_height = height // 2
        hazy_image = hazy_image.resize((new_width, new_height))
        hazefree_image = hazefree_image.resize((new_width, new_height))

        # hazefree_image = hazefree_image.resize((480, 640), Image.ANTIALIAS)
        # hazy_image = hazy_image.resize((480, 640), Image.ANTIALIAS)

        hazefree_image = np.asarray(hazefree_image) / 255.0
        hazy_image = np.asarray(hazy_image) / 255.0

        hazefree_image = torch.from_numpy(hazefree_image).float()
        hazy_image = torch.from_numpy(hazy_image).float()

        return hazefree_image.permute(2, 0, 1), hazy_image.permute(2, 0, 1)

    def __len__(self):
        return len(self.data_dict)

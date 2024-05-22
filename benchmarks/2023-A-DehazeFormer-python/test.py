import os

os.environ["CUDA_VISIBLE_DEVICES"] = "1"
import argparse
import time
import torch
import torch.nn as nn
import torch.nn.functional as F
from pytorch_msssim import ssim
from torch.utils.data import DataLoader
from collections import OrderedDict

from utils import AverageMeter, write_img, chw_to_hwc
from datasets.loader import PairLoader
from models import *


parser = argparse.ArgumentParser()
parser.add_argument("--model", default="dehazeformer-b", type=str, help="model name")
parser.add_argument("--num_workers", default=0, type=int, help="number of workers")
parser.add_argument("--data_dir", default="./data/", type=str, help="path to dataset")
parser.add_argument(
    "--save_dir", default="./saved_models/", type=str, help="path to models saving"
)
parser.add_argument(
    "--result_dir", default="./results/", type=str, help="path to results saving"
)
parser.add_argument("--dataset", default="RESIDE-IN", type=str, help="dataset name")
parser.add_argument("--exp", default="indoor", type=str, help="experiment setting")
args = parser.parse_args()


def single(save_dir):
    state_dict = torch.load(save_dir)["state_dict"]
    new_state_dict = OrderedDict()

    for k, v in state_dict.items():
        # name = k[7:]
        name = k
        new_state_dict[name] = v

    return new_state_dict


def test(test_loader, network, result_dir):
    # PSNR = AverageMeter()
    # SSIM = AverageMeter()

    torch.cuda.empty_cache()

    network.eval()

    os.makedirs(result_dir, exist_ok=True)
    # f_result = open(os.path.join(result_dir, 'results.csv'), 'w')
    count = 0
    total_time = 0

    for idx, batch in enumerate(test_loader):
        input = batch["source"].cuda()
        # target = batch['target'].cuda()

        filename = batch["filename"][0]

        with torch.no_grad():
            start_time = time.time()
            output = network(input).clamp_(-1, 1)
            end_time = time.time()

            # [-1, 1] to [0, 1]
            output = output * 0.5 + 0.5
            # target = target * 0.5 + 0.5

            # psnr_val = 10 * torch.log10(1 / F.mse_loss(output, target)).item()
            #
            # _, _, H, W = output.size()
            # down_ratio = max(1, round(min(H, W) / 256))		# Zhou Wang
            # ssim_val = ssim(F.adaptive_avg_pool2d(output, (int(H / down_ratio), int(W / down_ratio))),
            # 				F.adaptive_avg_pool2d(target, (int(H / down_ratio), int(W / down_ratio))),
            # 				data_range=1, size_average=False).item()
        operation_time = end_time - start_time
        total_time += operation_time
        count += 1

        # PSNR.update(psnr_val)
        # SSIM.update(ssim_val)

        # print('Test: [{0}]\t'
        # 	  'PSNR: {psnr.val:.02f} ({psnr.avg:.02f})\t'
        # 	  'SSIM: {ssim.val:.03f} ({ssim.avg:.03f})'
        # 	  .format(idx, psnr=PSNR, ssim=SSIM))

        # f_result.write('%s,%.02f,%.03f\n'%(filename, psnr_val, ssim_val))

        out_img = chw_to_hwc(output.detach().cpu().squeeze(0).numpy())
        write_img(os.path.join(result_dir, filename), out_img)

    average_time = total_time / count
    print("Average time:", average_time, " seconds")

    # f_result.close()

    # os.rename(os.path.join(result_dir, 'results.csv'),
    # 		  os.path.join(result_dir, '%.02f | %.04f.csv'%(PSNR.avg, SSIM.avg)))

    # dehazeName = 'DehazeFormer-t'
    # # folderName = '04_road'
    # folderName = '05_alone'
    # rootPath = r'E:\Data\MyDataSet\HazyImages'
    # folderPath = os.path.join(rootPath, folderName)
    # SaveFolderPath = os.path.join(rootPath, '08_dehaze', folderName, dehazeName)


if __name__ == "__main__":
    dehazeName = "DehazeFormer_type1"
    folderName = "01_set"
    rootPath = r"/home/lx/nas/Dataset/03_RWIDE"
    FolderPath = os.path.join(rootPath, folderName, "type/type1")
    SaveFolderPath = os.path.join(rootPath, folderName, "dehaze", dehazeName)

    model_path = f"/home/lx/nas/Code/03_RWIDE/01_dehaze-algorithm/02_network/2023-A-DehazeFormer-python/saved_models/RWIDE-type1/dehazeformer-b_17.563497151647294.pth"

    network = eval(args.model.replace("-", "_"))()
    network.cuda()
    if os.path.exists(model_path):
        print("==> Start testing, current model name: " + args.model)
        network.load_state_dict(single(model_path))
    else:
        print("==> No existing trained model!")
        exit(0)
    dataset_dir = FolderPath
    test_dataset = PairLoader(dataset_dir, "test", "test", resize=False)
    test_loader = DataLoader(
        test_dataset, batch_size=1, num_workers=args.num_workers, pin_memory=True
    )
    result_dir = SaveFolderPath
    test(test_loader, network, result_dir)

import os

os.environ["CUDA_VISIBLE_DEVICES"] = "4"
import time
import argparse
import numpy as np
import torch
import torchvision.transforms as tfs
import torchvision.utils as vutils
from PIL import Image
from tqdm import tqdm

from metrics import psnr, ssim
from models.C2PNet import C2PNet

parser = argparse.ArgumentParser()
parser.add_argument(
    "-d",
    "--dataset_name",
    help="name of dataset",
    choices=["indoor", "outdoor"],
    default="outdoor",
)
parser.add_argument(
    "--save_dir", type=str, default="dehaze_images", help="dehaze images save path"
)
parser.add_argument("--save", default=True, help="save dehaze images")
opt = parser.parse_args()

dataset = opt.dataset_name

dehazeName = "C2P"
folderName = "02_alone"
rootPath = r"/home/lx/nas/Dataset/03_RWIDE"
SaveFolderPath = os.path.join(rootPath, folderName, "dehaze", dehazeName)
model_path = "/home/lx/nas/Code/03_RWIDE/01_dehaze-algorithm/02_network/2023-A-C2PNet-python/trained_models/train_C2PNet_3_19_RWIDE.pk"

if opt.save:
    if not os.path.exists(SaveFolderPath):
        os.mkdir(SaveFolderPath)
    output_dir = SaveFolderPath

if dataset == "indoor":
    haze_dir = "data/SOTS/indoor/hazy/"
    clear_dir = "data/SOTS/indoor/clear/"
    model_dir = "trained_models/ITS.pkl"
elif dataset == "outdoor":
    haze_dir = os.path.join(rootPath, folderName, "hazy_align")
    clear_dir = os.path.join(rootPath, folderName, "clear_align")
    model_dir = model_path

device = "cuda:0" if torch.cuda.is_available() else "cpu"

net = C2PNet(gps=3, blocks=19)
ckp = torch.load(model_dir)
net = net.to(device)

# state_dict = ckp["model"]
state_dict = {k.replace("module.", ""): v for k, v in ckp["model"].items()}
net.load_state_dict(state_dict)
net.eval()
# psnr_list = []
# ssim_list = []
count = 0
total_time = 0

for im in tqdm(os.listdir(haze_dir)):
    haze = Image.open(os.path.join(haze_dir, im)).convert("RGB")
    if dataset == "indoor" or dataset == "outdoor":
        clear_im = im
    else:
        clear_im = im
    clear = Image.open(os.path.join(clear_dir, clear_im)).convert("RGB")
    haze1 = tfs.ToTensor()(haze)[None, ::]
    haze1 = haze1.to(device)
    clear_no = tfs.ToTensor()(clear)[None, ::]
    with torch.no_grad():
        start_time = time.time()
        pred = net(haze1)
        end_time = time.time()
    operation_time = end_time - start_time
    total_time += operation_time
    count += 1
    ts = torch.squeeze(pred.clamp(0, 1).cpu())
    # pp = psnr(pred.cpu(), clear_no)
    # ss = ssim(pred.cpu(), clear_no)
    # psnr_list.append(pp)
    # ssim_list.append(ss)
    if opt.save:
        vutils.save_image(ts, os.path.join(output_dir, im))
average_time = total_time / count
print("Average time:", average_time, " seconds")

# print(f'Average PSNR is {np.mean(psnr_list)}')
# print(f'Average SSIM is {np.mean(ssim_list)}')

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
os.chdir("..")

import cv2
import torch
import random
import pickle
import natsort
import numpy as np
from copy import deepcopy
import matplotlib.cm as cm
from src.loftr import LoFTR, default_cfg
from src.utils.plotting import make_matching_figure

# The default config uses dual-softmax.
# The outdoor and indoor models share the same config.
# You can change the default values like thr and coarse_match_type.
_default_cfg = deepcopy(default_cfg)
_default_cfg['coarse']['temp_bug_fix'] = True  # set to False when using the old ckpt
matcher = LoFTR(config=_default_cfg)
matcher.load_state_dict(torch.load("weights/outdoor_ds.ckpt")['state_dict'])
matcher = matcher.eval().cuda()

clear_dir = ''
hazy_dir = ''
dataset_name = ''
pkl_name = f'{dataset_name}.pkl'

save_data = []
hazy_image_names = natsort.natsorted(os.listdir(hazy_dir))
for i in range(len(hazy_image_names)):
    if hazy_image_names[i].endswith('.jpg') or hazy_image_names[i].endswith('.png'):
        tmp_data = {}
        # clear_image_name = hazy_image_names[i][:-9] + '_GT.jpg'  # O-HAZE
        # clear_image_name = hazy_image_names[i][:-9] + '_GT.png'  # NH-HAZE
        # clear_image_name = hazy_image_names[i][:-6] + '.jpg'  # RW-HAZE
        # clear_image_name = hazy_image_names[i].split('_')[0]+'.jpg'  # MRFID/RESIDE/RWMHDE
        # clear_image_name = hazy_image_names[i].split('_')[0]+'_clear.png'  # BeDDE

        clear_image_path = os.path.join(clear_dir, hazy_image_names[i])  # RWSHDE/RWRSDE/RWIDE-alpha
        # clear_image_path = os.path.join(clear_dir, clear_image_name)
        hazy_image_path = os.path.join(hazy_dir, hazy_image_names[i])
        
        # Load example images
        img0_raw = cv2.imread(clear_image_path, cv2.IMREAD_GRAYSCALE)
        img1_raw = cv2.imread(hazy_image_path, cv2.IMREAD_GRAYSCALE)
        img0_raw = cv2.resize(img0_raw, (1024, 1024))
        img1_raw = cv2.resize(img1_raw, (1024, 1024))
        
        if img0_raw.shape != img1_raw.shape:
            print('shape error:', hazy_image_names[i])

        img0 = torch.from_numpy(img0_raw)[None][None].cuda() / 255.
        img1 = torch.from_numpy(img1_raw)[None][None].cuda() / 255.
        batch = {'image0': img0, 'image1': img1}

        # Inference with LoFTR and get prediction
        with torch.no_grad():
            matcher(batch)
            mkpts0 = batch['mkpts0_f'].cpu().numpy()
            mkpts1 = batch['mkpts1_f'].cpu().numpy()
            mconf = batch['mconf'].cpu().numpy()
                
            tmp_data['hazy_image_name'] = hazy_image_names[i]
            tmp_data['mkpts0'] = mkpts0
            tmp_data['mkpts1'] = mkpts1
            tmp_data['hw'] = img1_raw.shape
                
            save_data.append(tmp_data)
            print(hazy_image_path)

with open(pkl_name, 'wb') as file:
    pickle.dump(save_data, file)
    print('done!')
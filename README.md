# RWIDE: A Real-World Image Dehazing Dataset

This repository contains the dataset and benchmark DHAs of the paper "RWIDE: A Real-World Image Dehazing Dataset". The datasheets for datasets is available in this repository as a pdf file.

# What is RWIDE?

RWIDE is the real-world hazy image dataset with annotations for multiple outdoor scenes. It comprises two parts: RWIDE-$\alpha$ and RWIDE-$\beta$, which total contain 2,450 pairs of haze-free and hazy images. Annotations include six haze scene types and five sky region types. RWIDE-$\alpha$ is captured by digital cameras, while RWIDE-$\beta$ is sourced from webcams.  We have incorporated annotations into our dataset to improve the performance of dehazing models for natural-haze image restoration.

# Why make this?

Haze degrades the quality of captured images, significantly impacting the performance of various image processing algorithms and vision-driven applications such as image segmentation, object detection, and video surveillance. Image dehazing is a meaningful but ill-posed task aimed at generating clear images from hazy ones. Current research typically employs synthetic or artificial haze datasets, constraining their utility in real-world contexts. Moreover, natural haze datasets are often deficient in paired samples and fail to offer a broad spectrum of scene diversity. To the best of our knowledge, RWIDE is the first real-world hazy image dataset with annotations for multiple scenes.

# Data versions and structure

You can acquire the download link of our dataset at <link>

# How can I use this?

The dataset can be downloaded from the provided link. During training, validation, and inference, simply normalize in your PyTorch DataLoader as typically done in most image dehazing models. It's worth noting that diverse shooting angles yield varied hazy image effects within the same scene. RWIDE-$\alpha$ consists of manually captured images, while RWIDE-$\beta$ is sourced from public webcams. RWIDE-$\alpha$ is ideal for restoring hazy images captured by humans, while RWIDE-$\beta$ is suited for webcam or surveillance perspectives. However, models trained solely on RWIDE may struggle to effectively dehaze images from alternative viewpoints, such as indoor or remote sensing scenarios.

# Annotation details

**Scene classification.** The hazy scenes in RWIDE are categorized into six groups: Mountains and Hills (MH), Lakes and Rivers (LR), Forests and Jungles (FJ), Buildings and Cityscape (BC), Roadscape (RS), and Snowscape (SS). 
**Sky-type classification.** The skies depicted by haze-free images in RWIDE are classified into four types: Overcast with a Clear Sky (OCS), Sunny with a Clear Blue Sky (SCBS), Overcast with a Cloudy Sky (OCCS), and Sunny with a Blue Sky and some Clouds (SBSC).

Scene classifications exhibit interdependence owing to overlap. A "1" label is assigned when specific scene elements are present; otherwise, it's labeled "0". In contrast, sky-type classification remains independent. Annotation information for all RWIDE images can be found in the provided xxx file.

# Who created this dataset?

The dataset is created by the authors of the paper as well as the members of the Cyber Security Laboratory at Chongqing University

# Licences

Copyright (c) 2024 Cyber Security Laboratory

RWIDE dataset is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). This license requires that reusers give credit to the creator. It allows reusers to distribute, remix, adapt, and build upon the material in any medium or format, for noncommercial purposes only. If others modify or adapt the material, they must license the modified material under identical terms.

All software for benchmark dehazing algorithms (DHAs) models adheres to the license of the original authors. You can find the original source codes and their respective licenses for LGP, SLP, Light-DehazeNet (LD-Net),  DehazeFormer, PSMB-Net and C$^2$P-Net in the links below.

LGP (<https://github.com/zhengchaobing/Multi-scale-Single-Image-Dehazing-Using-Laplacian-and-Gaussian-Pyramids>)<br>SLP (<https://github.com/LPengYang/Saturation-Line-Prior>)<br>
Light-DehazeNet (LD-Net) (<https://github.com/hayatkhan8660-maker/Light-DehazeNet>)<br>
DehazeFormer (<https://github.com/IDKiro/DehazeFormer>)<br>
PSMB-Net (<https://github.com/thislzm/PSMB-Net>)<br>
C$^2$P-Net (<https://github.com/Polaris-F/C2PNet>)

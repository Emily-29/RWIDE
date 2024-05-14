## RWIDE: A Real-World Image Dehazing Dataset
> ###### [Overview](#RWIDE) | [Download](#download) | [License](#license) 
> 
> <img src="https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-blue.svg" />&nbsp;

This repository contains the dataset and benchmark dehazing algorithms (DHAs) of the paper "RWIDE: A Real-World Image Dehazing Dataset". The datasheets for datasets is available in this repository as a pdf file.

The **RWIDE** is the real-world hazy image dataset with annotations for multiple outdoor scenes. It comprises two parts: RWIDE-α and RWIDE-β, which total contain 2,450 pairs of haze-free and hazy images. Annotations include six haze scene types and five sky region types. RWIDE-α is captured by digital cameras, while RWIDE-β is sourced from webcams.  We have incorporated annotations into our dataset to improve the performance of dehazing models for natural-haze image restoration.

## Why make this?

Haze degrades the quality of captured images, significantly impacting the performance of various image processing algorithms and vision-driven applications such as image segmentation, object detection, and video surveillance. Image dehazing is a meaningful but ill-posed task aimed at generating clear images from hazy ones. Current research typically employs synthetic or artificial haze datasets, constraining their utility in real-world contexts. Moreover, natural haze datasets are often deficient in paired samples and fail to offer a broad spectrum of scene diversity. To the best of our knowledge, RWIDE is the first real-world hazy image dataset with annotations for multiple scenes.

## Download

You can download RWIDE-α (~600 MB) and RWIDE-β (~950 MB) separately:<br>
**[RWIDE-α](xxx)**<br>
RWIDE-β: **[RWMHDE](https://www.icloud.com.cn/iclouddrive/063rSWDbK7D3e-4UdItO43-cw#RWMHDE)**   **[RWSHDE](https://www.icloud.com.cn/iclouddrive/0e9pH6FRinChU4A6KfIcuYDPw#RWSHDE)**   **[RWRSDE](https://www.icloud.com.cn/iclouddrive/0e8wJycmkT27M2qgcIuUS_Y0g#RWRSDE)**<br>

## How can I use this?

The dataset can be downloaded from the provided link. During training, validation, and inference, simply normalize in your PyTorch DataLoader as typically done in most image dehazing models. It's worth noting that diverse shooting angles yield varied hazy image effects within the same scene. RWIDE-α consists of manually captured images, while RWIDE-β is sourced from public webcams. RWIDE-α is ideal for restoring hazy images captured by humans, while RWIDE-β is suited for webcam or surveillance perspectives. However, models trained solely on RWIDE may struggle to effectively dehaze images from alternative viewpoints, such as indoor or remote sensing scenarios.

## Annotation details

**Scene classification.** The hazy scenes in RWIDE are categorized into six groups: Mountains and Hills (MH), Lakes and Rivers (LR), Forests and Jungles (FJ), Buildings and Cityscape (BC), Roadscape (RS), and Snowscape (SS). <br>
**Sky-type classification.** The skies depicted by haze-free images in RWIDE are classified into five types:  No Sky Visible (NSV), Overcast with a Clear Sky (OCS), Sunny with a Clear Blue Sky (SCBS), Overcast with a Cloudy Sky (OCCS), and Sunny with a Blue Sky and some Clouds (SBSC).

Scene classifications exhibit interdependence owing to overlap. A "1" label is assigned when specific scene elements are present; otherwise, it's labeled "0". In contrast, sky-type classification remains independent. Annotation information for all RWIDE images can be found in the provided **xxx file**.

## Who created this dataset?

The dataset is created by the authors of the paper as well as the members of the Cyber Security Laboratory at Chongqing University.

## License

Copyright (c) 2024 Cyber Security Laboratory

This dataset is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). This license requires that reusers give credit to the creator. It allows reusers to distribute, remix, adapt, and build upon the material in any medium or format, for noncommercial purposes only. If others modify or adapt the material, they must license the modified material under identical terms.

All benchmark DHAs models adheres to the license of the original authors. You can find the original source codes and their respective licenses for LGP, SLP, Light-DehazeNet (LD-Net),  DehazeFormer, PSMB-Net and C2P-Net in the links below.

| Year | Title                                                        | DHA          | Paper                                                        | Code                                                         |
| ---- | ------------------------------------------------------------ | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 2021 | Multi-scale single image dehazing using Laplacian and Gaussian pyramids | LGP          | <a href="https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=9606591&ref=aHR0cHM6Ly9pZWVleHBsb3JlLmllZWUub3JnL2Fic3RyYWN0L2RvY3VtZW50Lzk2MDY1OTE="><img src="https://img.shields.io/badge/paper-7F7F7F"/></a> | <a href="https://github.com/zhengchaobing/Multi-scale-Single-Image-Dehazing-Using-Laplacian-and-Gaussian-Pyramids"><img src="https://img.shields.io/badge/code-ffff00"/></a> |
| 2023 | Single Image Dehazing Using Saturation Line Prior            | SLP          | <a href="https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=10141557&ref=aHR0cHM6Ly9pZWVleHBsb3JlLmllZWUub3JnL2Fic3RyYWN0L2RvY3VtZW50LzEwMTQxNTU3"><img src="https://img.shields.io/badge/paper-7F7F7F"/></a> | <a href="https://github.com/LPengYang/Saturation-Line-Prior"><img src="https://img.shields.io/badge/code-ffff00"/></a> |
| 2021 | Light-DehazeNet: a novel lightweight CNN architecture for single image dehazing | LD-Net       | <a href="https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=9562276&ref=aHR0cHM6Ly9pZWVleHBsb3JlLmllZWUub3JnL2Fic3RyYWN0L2RvY3VtZW50Lzk1NjIyNzY="><img src="https://img.shields.io/badge/paper-7F7F7F"/></a> | <a href="https://github.com/hayatkhan8660-maker/Light-DehazeNet"><img src="https://img.shields.io/badge/code-ffff00"/></a> |
| 2023 | Vision transformers for single image dehazing                | DehazeFormer | <a href="https://ieeexplore.ieee.org/ielx7/83/9991910/10076399.pdf?tp=&arnumber=10076399&isnumber=9991910&ref=aHR0cHM6Ly9pZWVleHBsb3JlLmllZWUub3JnL2Fic3RyYWN0L2RvY3VtZW50LzEwMDc2Mzk5"><img src="https://img.shields.io/badge/paper-7F7F7F"/></a> | <a href="https://github.com/IDKiro/DehazeFormer"><img src="https://img.shields.io/badge/code-ffff00"/></a> |
| 2023 | Partial Siamese with Multiscale Bi-codec Networks for Remote Sensing Image Haze Removal | PSMB-Net     | <a href="https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=10268954&ref=aHR0cHM6Ly9pZWVleHBsb3JlLmllZWUub3JnL2Fic3RyYWN0L2RvY3VtZW50LzEwMjY4OTU0"><img src="https://img.shields.io/badge/paper-7F7F7F"/></a> | <a href="https://github.com/thislzm/PSMB-Net"><img src="https://img.shields.io/badge/code-ffff00"/></a> |
| 2023 | Curricular contrastive regularization for physics-aware single image dehazing | C2P-Net      | <a href="https://openaccess.thecvf.com/content/CVPR2023/papers/Zheng_Curricular_Contrastive_Regularization_for_Physics-Aware_Single_Image_Dehazing_CVPR_2023_paper.pdf"><img src="https://img.shields.io/badge/paper-7F7F7F"/></a> | <a href="https://github.com/Polaris-F/C2PNet"><img src="https://img.shields.io/badge/code-ffff00"/></a> |

Likewise, you can find all referenced hazy image datasets and their respective licenses at the link below.

| Year | Title                                                        | Dataset      | Paper                                                        | Download                                                     |
| ---- | ------------------------------------------------------------ | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 2018 | Benchmarking single-image dehazing and beyond                | RESIDE (OTS) | <a href="https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8451944"><img src="https://img.shields.io/badge/paper-7F7F7F"/></a> | <a href="https://sites.google.com/view/reside-dehaze-datasets/reside-%CE%B2"><img src="https://img.shields.io/badge/dataset-0000ff"/></a> |
| 2018 | O-HAZE: a dehazing benchmark with real hazy and haze-free outdoor images | O-HAZE       | <a href="chrome-extension://ikhdkkncnoglghljlkmcimlnlhkeamad/pdf-viewer/web/viewer.html?file=https%3A%2F%2Fopenaccess.thecvf.com%2Fcontent_cvpr_2018_workshops%2Fpapers%2Fw13%2FAncuti_O-HAZE_A_Dehazing_CVPR_2018_paper.pdf#=&zoom=220.00000000000003"><img src="https://img.shields.io/badge/paper-7F7F7F"/></a> | <a href="https://data.vision.ee.ethz.ch/cvl/ntire18//o-haze/"><img src="https://img.shields.io/badge/dataset-0000ff"/></a> |
| 2020 | NH-HAZE: an image dehazing benchmark with non-homogeneous hazy and haze-free images | NH-HAZE      | <a href="chrome-extension://ikhdkkncnoglghljlkmcimlnlhkeamad/pdf-viewer/web/viewer.html?file=https%3A%2F%2Fopenaccess.thecvf.com%2Fcontent_CVPRW_2020%2Fpapers%2Fw31%2FAncuti_NH-HAZE_An_Image_Dehazing_Benchmark_With_Non-Homogeneous_Hazy_and_Haze-Free_CVPRW_2020_paper.pdf#=&zoom=220.00000000000003"><img src="https://img.shields.io/badge/paper-7F7F7F"/></a> | <a href="https://data.vision.ee.ethz.ch/cvl/ntire20/nh-haze/"><img src="https://img.shields.io/badge/dataset-0000ff"/></a> |
| 2020 | Dehazing evaluation: real-world benchmark datasets, criteria, and baselines | BeDDE        | <a href="https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9099036"><img src="https://img.shields.io/badge/paper-7F7F7F"/></a> | <a href="https://github.com/xiaofeng94/BeDDE-for-defogging?tab=readme-ov-file"><img src="https://img.shields.io/badge/dataset-0000ff"/></a> |
| 2020 | Image defogging quality assessment: real-world database and method | MRFID        | <a href="https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9244631"><img src="https://img.shields.io/badge/paper-7F7F7F"/></a> | <a href="http://www.vistalab.ac.cn/MRFID-for-defogging/"><img src="https://img.shields.io/badge/dataset-0000ff"/></a> |
| 2022 | RW-HAZE: a real-world benchmark dataset to evaluate quantitatively dehazing algorithms | RW-HAZE      | <a href="https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9897706"><img src="https://img.shields.io/badge/paper-7F7F7F"/></a> | <a href="https://github.com/jiyouchen103/Image-Dehazing-Assessment-A-Real-World-Dataset-and-A-Haze-Density-Aware-Criteria-and-RW_Haze"><img src="https://img.shields.io/badge/dataset-0000ff"/></a> |


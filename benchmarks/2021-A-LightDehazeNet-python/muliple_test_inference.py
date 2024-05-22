import os

os.environ["CUDA_VISIBLE_DEVICES"] = "1"
from inference import image_haze_removel
from PIL import Image
import torchvision
import argparse
import time


def multiple_dehaze_test(directory, SaveFolderPath, model_path):
    count = 0
    total_time = 0
    for filename in sorted(os.listdir(directory)):
        img = Image.open(os.path.join(directory, filename))
        # width, height = img.size
        # new_width = width // 2
        # new_height = height // 2
        # img = img.resize((new_width, new_height))

        start_time = time.time()
        dehaze_image = image_haze_removel(img, model_path)
        end_time = time.time()

        operation_time = end_time - start_time
        total_time += operation_time
        count += 1

        torchvision.utils.save_image(
            dehaze_image, os.path.join(SaveFolderPath, filename)
        )
        print(os.path.join(SaveFolderPath, filename))
    average_time = total_time / count
    print("Average time:", average_time, " seconds")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-td", "--test_directory", help="path to test images directory")
    args = vars(ap.parse_args())

    dehazeName = "LightDehazeNet"
    folderName = "RESIDE"
    rootPath = r"/home/lx/nas/Dataset/03_RWIDE/05_other_datasets"
    FolderPath = os.path.join(rootPath, folderName, "test/hazy")
    SaveFolderPath = os.path.join(rootPath, folderName, "dehaze", dehazeName)

    args["test_directory"] = FolderPath
    if not os.path.exists(SaveFolderPath):
        os.mkdir(SaveFolderPath)

    model_path = rf"trained_weights/{folderName}/trained_LDNet.pth"
    multiple_dehaze_test(args["test_directory"], SaveFolderPath, model_path)

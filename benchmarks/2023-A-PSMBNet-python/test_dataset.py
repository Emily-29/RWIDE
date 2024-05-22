import os

from PIL import Image
import torchvision.transforms.functional as TF
from torch.utils.data import Dataset
from torchvision import transforms


class dehaze_test_dataset(Dataset):
    def __init__(self, test_dir, test_name, tag=False, resize=True):
        self.transform = transforms.Compose([transforms.ToTensor()])
        self.list_test = []
        for line in open(os.path.join(test_dir, "test.txt")):
            line = line.strip("\n")
            if line != "":
                self.list_test.append(line)
        hazy, clean = test_name.split(",")
        self.tag = tag
        self.resize = resize
        self.root_hazy = os.path.join(test_dir, "{}/".format(hazy))
        self.root_clean = os.path.join(test_dir, "{}/".format(clean))
        self.file_len = len(self.list_test)

    def __getitem__(self, index):
        # if self.tag in ['nhhaze', 'outdoor', 'dense', 'else', 'UHRI']:
        test_name = self.list_test[index]  # .split('_')[0] + '.png'
        # else:
        # test_name = self.list_test[index].split('-')[0] + '-targets.png'
        hazy = Image.open(os.path.join(self.root_hazy, self.list_test[index])).convert(
            "RGB"
        )
        clean = Image.open(
            os.path.join(self.root_clean, self.list_test[index])
        ).convert("RGB")

        if self.resize:
            width, height = hazy.size
            new_width = width // 2
            new_height = height // 2
            hazy_ = hazy.resize((new_width, new_height))
            clean_ = clean.resize((new_width, new_height))
        else:
            hazy_ = hazy
            clean_ = clean

        hazy = self.transform(hazy_)
        clean = self.transform(clean_)
        return hazy, clean, test_name

    def __len__(self):
        return self.file_len

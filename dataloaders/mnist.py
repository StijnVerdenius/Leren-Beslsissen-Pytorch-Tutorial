import torch
from torch.utils import data
from torchvision import datasets, transforms

"""
For this one, the dataset gets provided by pytorch. However, you still need to initialise the dataloader
"""


def get_mnist_loaders(batch_size: int):
    train_loader = torch.utils.data.DataLoader(
        datasets.MNIST("./data", train=True, download=True,
                       transform=transforms.Compose([transforms.ToTensor(),
                                                     transforms.Normalize((0.1307,), (0.3081,))
                                                     ])),
        batch_size=batch_size,
        shuffle=True,
        pin_memory=True,
    )

    test_loader = torch.utils.data.DataLoader(
        datasets.MNIST("./data", train=False, download=True,
                       transform=transforms.Compose([transforms.ToTensor(),
                                                     transforms.Normalize((0.1307,), (0.3081,))
                                                     ])),
        batch_size=batch_size,
        shuffle=True,
        pin_memory=True,
    )

    return train_loader, test_loader

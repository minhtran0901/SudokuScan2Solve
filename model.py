import torch
import torchvision
import numpy as np
from PIL import Image


def transform(x):
    pil_img = Image.fromarray(np.uint8(x))
    transform = torchvision.transforms.Compose([
        torchvision.transforms.Resize((32, 32)),
        torchvision.transforms.ToTensor()
    ])
    return transform(pil_img).numpy()


def get_predict(boxes, model):
    imgs = torch.Tensor(np.array(list(map(transform, boxes))))
    y_hat = model(imgs)
    y_hat = torch.softmax(y_hat, dim=1)
    value, indices = torch.max(y_hat, dim=1)
    getClass = np.where(value < 0.75, 0, indices.numpy())
    return getClass.reshape(9, 9)

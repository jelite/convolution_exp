
import torch.nn

x = torch.randn(torch.Size([16, 256, 56, 56])).to("cuda")
layer = torch.nn.Conv2d(256, 128, kernel_size=(1, 1), stride=(1, 1), bias=False).to("cuda")
y = []

def func():
    y = layer(x)
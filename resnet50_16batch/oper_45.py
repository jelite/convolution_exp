
import torch.nn

x = torch.randn(torch.Size([16, 256, 56, 56])).to("cuda")
layer = torch.nn.Conv2d(256, 512, kernel_size=(1, 1), stride=(2, 2), bias=False).to("cuda")
y = []

def func():
    y = layer(x)

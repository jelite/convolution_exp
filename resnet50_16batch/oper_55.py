
import torch.nn

x = torch.randn(torch.Size([16, 128, 28, 28])).to("cuda")
layer = torch.nn.Conv2d(128, 512, kernel_size=(1, 1), stride=(1, 1), bias=False).to("cuda")
y = []

def func():
    y = layer(x)

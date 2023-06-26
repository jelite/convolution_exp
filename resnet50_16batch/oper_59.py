
import torch.nn

x = torch.randn(torch.Size([16, 512, 28, 28])).to("cuda")
layer = torch.nn.Conv2d(512, 128, kernel_size=(1, 1), stride=(1, 1), bias=False).to("cuda")
y = []

def func():
    y = layer(x)

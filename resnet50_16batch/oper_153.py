
import torch.nn

x = torch.randn(torch.Size([16, 2048, 7, 7])).to("cuda")
layer = torch.nn.Conv2d(2048, 512, kernel_size=(1, 1), stride=(1, 1), bias=False).to("cuda")
y = []

def func():
    y = layer(x)

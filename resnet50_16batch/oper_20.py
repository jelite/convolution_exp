
import torch.nn

x = torch.randn(torch.Size([16, 64, 56, 56])).to("cuda")
layer = torch.nn.Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False).to("cuda")
y = []

def func():
    y = layer(x)

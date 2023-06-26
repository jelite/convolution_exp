
import torch.nn

x = torch.randn(torch.Size([16, 128, 56, 56])).to("cuda")
layer = torch.nn.Conv2d(128, 128, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), bias=False).to("cuda")
y = []

def func():
    y = layer(x)

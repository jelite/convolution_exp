
import torch.nn

x = torch.randn(torch.Size([16, 1024, 14, 14])).to("cuda")
layer = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False).to("cuda")
y = []

def func():
    y = layer(x)

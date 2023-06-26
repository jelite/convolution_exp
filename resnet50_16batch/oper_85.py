
import torch.nn

x = torch.randn(torch.Size([16, 256, 14, 14])).to("cuda")
layer = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), stride=(1, 1), bias=False).to("cuda")
y = []

def func():
    y = layer(x)

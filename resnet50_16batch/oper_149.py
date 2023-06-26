
import torch.nn

x = torch.randn(torch.Size([16, 1024, 14, 14])).to("cuda")
layer = torch.nn.Conv2d(1024, 2048, kernel_size=(1, 1), stride=(2, 2), bias=False).to("cuda")
y = []

def func():
    y = layer(x)

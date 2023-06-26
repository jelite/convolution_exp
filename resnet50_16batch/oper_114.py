
import torch.nn

x = torch.randn(torch.Size([16, 256, 14, 14])).to("cuda")
layer = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False).to("cuda")
y = []

def func():
    y = layer(x)

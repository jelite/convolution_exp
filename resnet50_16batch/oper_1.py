
import torch.nn

x = torch.randn(torch.Size([16, 3, 224, 224])).to("cuda")
layer = torch.nn.Conv2d(3, 64, kernel_size=(7, 7), stride=(2, 2), padding=(3, 3), bias=False).to("cuda")
y = []

def func():
    y = layer(x)

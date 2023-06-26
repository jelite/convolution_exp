
import torch.nn

x = torch.randn(torch.Size([16, 512, 28, 28])).to("cuda")
layer = torch.add
y = []

def func():
    y = layer(x,x)

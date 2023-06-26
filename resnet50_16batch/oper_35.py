
import torch.nn

x = torch.randn(torch.Size([16, 256, 56, 56])).to("cuda")
layer = torch.add
y = []

def func():
    y = layer(x,x)

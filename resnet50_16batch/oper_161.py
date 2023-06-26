
import torch.nn

x = torch.randn(torch.Size([16, 2048, 7, 7])).to("cuda")
layer = torch.add
y = []

def func():
    y = layer(x,x)

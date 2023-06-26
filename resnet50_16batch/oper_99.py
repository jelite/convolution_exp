
import torch.nn

x = torch.randn(torch.Size([16, 1024, 14, 14])).to("cuda")
layer = torch.add
y = []

def func():
    y = layer(x,x)

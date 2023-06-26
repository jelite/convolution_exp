
import torch.nn

x = torch.randn(torch.Size([16, 256, 14, 14])).to("cuda")
layer = torch.nn.ReLU(inplace=True).to("cuda")
y = []

def func():
    y = layer(x)

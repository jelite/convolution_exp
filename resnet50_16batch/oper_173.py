
import torch.nn

x = torch.randn(torch.Size([16, 2048, 7, 7])).to("cuda")
layer = torch.nn.AdaptiveAvgPool2d(output_size=(1, 1)).to("cuda")
y = []

def func():
    y = layer(x)

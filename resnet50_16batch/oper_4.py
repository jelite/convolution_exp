
import torch.nn

x = torch.randn(torch.Size([16, 64, 112, 112])).to("cuda")
layer = torch.nn.MaxPool2d(kernel_size=3, stride=2, padding=1, dilation=1, ceil_mode=False).to("cuda")
y = []

def func():
    y = layer(x)

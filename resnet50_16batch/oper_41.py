
import torch.nn

x = torch.randn(torch.Size([16, 128, 28, 28])).to("cuda")
layer = torch.nn.BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True).to("cuda")
y = []

def func():
    y = layer(x)

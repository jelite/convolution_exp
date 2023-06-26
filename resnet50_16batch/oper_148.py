
import torch.nn

x = torch.randn(torch.Size([16, 2048, 7, 7])).to("cuda")
layer = torch.nn.BatchNorm2d(2048, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True).to("cuda")
y = []

def func():
    y = layer(x)

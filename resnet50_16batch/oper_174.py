
import torch.nn

x = torch.randn(torch.Size([16, 2048])).to("cuda")
layer = torch.nn.Linear(in_features=2048, out_features=1000, bias=True).to("cuda")
y = []

def func():
    y = layer(x)

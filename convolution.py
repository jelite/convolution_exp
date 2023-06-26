import importlib
import torch

#resnet50
conv_list = "1 5 8 11 13 17 20 23 27 30 33 37 40 43 45 49 52 55 59 62 65 \
69 72 75 79 82 85 87 91 94 97 101 107 111 114 117 121 124 \
127 131 134 137 141 144 147 149 153 156 159 163 166 169".split(" ")

for oper_num in conv_list:
    print(f"{oper_num} start")        
    module_1 = importlib.import_module("resnet50_16batch.oper_"+oper_num)
    func = module_1.func
    func()

    print(f"{oper_num} end")
    
        
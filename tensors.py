import numpy as np
import torch

#x = torch.rand(3, 2)
#print(x)
#print(x.add(1))
#print(x)
#print(x.add_(1))
#print(x)

#print(x.size())

a = np.random.rand(4, 2)
print("=====> numpy")
print(a)
b = torch.from_numpy(a)
print(b.mul_(2))
print(a)
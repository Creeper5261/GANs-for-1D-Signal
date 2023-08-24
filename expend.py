import torch
import numpy as np
import os
import matplotlib.pyplot as plt
nz = 512
num = 50
device = torch.device("cuda:0")

netG = torch.load('./module/wgan_gp_netG.pkl')

noise = torch.randn(nz, 100, 1, device=device)

fake = netG(noise).detach().cpu().numpy()


for i in range(num):
    filename = f'./wavelet/fake/fake_data_{i}.csv'
    np.savetxt(filename, fake[i].flatten(), delimiter=',')

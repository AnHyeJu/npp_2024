#!/opt/homebrew/Caskroom/miniforge/base/envs/oparcels/bin/python
import glob
import os

#sould run chmod +x ./makenc.py first
path = '/Users/hyeju_mac/Documents/GitHub/npp_2024/Data/1degree'
os.chdir(path)

a=['1d_vgpm.nc', '1d_sst.nc']
d=['nppa.nc', 'ssta.nc']
steps=['climatology_', '']

for i in range(2):
    os.system(f'cdo ymonmean {a[i]} {steps[0]}{d[i]}')
    os.system(f'cdo ymonsub {a[i]} {steps[0]}{d[i]} {steps[1]}{d[i]}')
    os.system(f'cdo runmean,5 {steps[1]}{d[i]} 5m_running_{d[i]}')
    
for f in glob.glob(f'{path}/{steps[0]}*.nc'):
    os.remove(f)
    
#5year running mean
ts = 5*12
for i in range(2):
    os.system(f'cdo runmean,{ts} {steps[1]}{d[i]} 5y_running_{d[i]}')
    
#make linear npp
i=0
os.system(f'cdo -sellonlatbox,126,131,18,22 {a[i]} t_{d[i]}')
os.system(f'cdo fldmean t_{d[i]} tmp_{d[i]}')
os.system(f'cdo ymonmean tmp_{d[i]} {steps[0]}{d[i]}')
os.system(f'cdo ymonsub tmp_{d[i]} {steps[0]}{d[i]} l_{steps[1]}{d[i]}')
os.system(f'cdo runmean,5 l_{steps[1]}{d[i]} l_5m_running_{d[i]}')
os.system(f'cdo runmean,{ts} l_{steps[1]}{d[i]} l_5y_running_{d[i]}')

delist=['tmp_', 'climatology_','t_']
for i in range(3):
    [os.remove(f) for f in glob.glob(f'{path}/{delist[i]}*.nc')]
#!/opt/homebrew/Caskroom/miniforge/base/envs/oparcels/bin/python
import glob
import os

#sould run chmod +x ./makenc.py first
path = '/Users/hyeju_mac/Documents/GitHub/npp_2024/Data/originals'
os.chdir(path)

a=['sst.mon.mean.nc']
d=['nino.nc']
steps=['climatology_', '']

i=0
os.system(f'cdo -sellonlatbox,190,240,-5,5 {a[i]} t_{d[i]}')
os.system(f'cdo fldmean t_{d[i]} tmp_{d[i]}')
os.system(f'cdo ymonmean tmp_{d[i]} {steps[0]}{d[i]}')
os.system(f'cdo ymonsub tmp_{d[i]} {steps[0]}{d[i]} l_{steps[1]}{d[i]}')
os.system(f'cdo runmean,3 l_{steps[1]}{d[i]} results/handmade_{d[i]}')

delist=['tmp_', 'climatology_','t_',]
for i in range(3):
    [os.remove(f) for f in glob.glob(f'{path}/{delist[i]}*.nc')]
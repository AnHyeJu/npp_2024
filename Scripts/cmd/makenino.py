#!/opt/homebrew/Caskroom/miniforge/base/envs/oparcels/bin/python
import glob
import os

#sould run chmod +x ./makenc.py first
path = '/Users/hyeju_mac/Documents/GitHub/npp_2024/Data/originals'
os.chdir(path)

a=['sst.mon.mean.nc']
d=['nino34.nc']
steps=['climatology_', '']

i=0
#(5N-5S, 170W-120W) -> -5,-5
#경도를 설정할 때, 서경(West longitude)은 360도 시스템을 사용해 표현해야 한다는 점.
#서경 170도(W)는 360 - 170 = 190도 동경(E)로, 서경 120도(W)는 360 - 120 = 240도 동경(E)로 변환
os.system(f'cdo -sellonlatbox,190,240,-5,5 {a[i]} t_{d[i]}')
os.system(f'cdo fldmean t_{d[i]} tmp_{d[i]}')
os.system(f'cdo ymonmean tmp_{d[i]} {steps[0]}{d[i]}')
os.system(f'cdo ymonsub tmp_{d[i]} {steps[0]}{d[i]} results/handmade_{d[i]}')
#3 month running mean 안해도 된댜
#os.system(f'cdo runmean,3 l_{steps[1]}{d[i]} results/handmade_{d[i]}')

delist=['tmp_', 'climatology_','t_',]
for i in range(3):
    [os.remove(f) for f in glob.glob(f'{path}/{delist[i]}*.nc')]
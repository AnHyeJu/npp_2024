#!/opt/homebrew/Caskroom/miniforge/base/envs/oparcels/bin/python
import glob
import os

#sould run chmod +x ./makenc.py first
path = '/Users/hyeju_mac/Documents/GitHub/npp_2024/Data/originals/'
os.chdir(path)

a='vgpm.nc'
t='tmp_'

os.system(f'cdo setgrid,source_grid.txt {a} good_{a}')
#  제대로 grid.text 넣어 줬더니 이거 안해줘도 댐! os.system(f'cdo invertlat {t}{a} good_{a}')
# [os.remove(f) for f in glob.glob(f'{path}{t}*.nc')]

a=['sst.mon.mean.nc','good_vgpm.nc']
b=['1d_sst.nc', '1d_vgpm.nc']

[os.system(f'cdo remapbil,r360x181 {a[i]} results/{b[i]}') for i in range(2)]

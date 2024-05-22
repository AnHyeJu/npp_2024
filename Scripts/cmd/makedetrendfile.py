#!/opt/homebrew/Caskroom/miniforge/base/envs/oparcels/bin/python
import glob
import os
import fnmatch

#sould run chmod +x ./makenc.py first
path = '/Users/hyeju_mac/Documents/GitHub/npp_2024/Data/1degree/'
os.chdir(path)

# 모든 파일 찾기
all_files = glob.glob(path+'*.nc')

# '1d_'로 시작하는 파일 제외
filtered_files = [os.path.basename(f) for f in all_files if not fnmatch.fnmatch(f, f'{path}1d_*')]

# 결과 출력
for f in filtered_files:
    os.system(f'cdo detrend {f} d_{f}')

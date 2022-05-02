# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 17:22:34 2022

@author: WinfredMa
"""

from pathlib import Path
from PIL import Image
src_folder = Path("C:\\Users\\WinfredMa\\Documents\\Python Automation\\files operations\\srcImages")
des_folder = Path("C:\\Users\\WinfredMa\\Documents\\Python Automation\\files operations\\convertedImages")
file_list = list(src_folder.glob('*.jpg'))
if not des_folder.exists():
    des_folder.mkdir(parents=True)
for img in file_list:
    des_file = des_folder/img.name
    des_file = des_file.with_suffix('.png')
    print(des_file)
    Image.open(img).save(des_file)
    print(f'{img.name} converted')
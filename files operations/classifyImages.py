# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 17:46:04 2022

@author: WinfredMa
"""

from pathlib import Path
from datetime import datetime
from exifread import process_file
src_folder = Path("C:\\Users\\WinfredMa\\Documents\\Python Automation\\files operations\\images")
des_folder = Path("C:\\Users\\WinfredMa\\Documents\\Python Automation\\files operations\\classifiedImages")
if not des_folder.exists():
    des_folder.mkdir(parents=True)
file_list = list(src_folder.glob('*.jpg'))
for file in file_list:
    with open(file, 'rb') as f:
        tags = process_file(f, details=False)
        if 'EXIF dateTimeOriginal' in tags.keys():
            dto = str(tags['EXIF DateTimeOrignal'])
            folder_name = datetime.strptime(dto, '%Y:%m:%d %H: %M:%S').strftime('%Y-%m-%d')
            des_path = des_folder/folder_name
            if not des_path.exists():
                des_path.mkdir(parents=True)
                file.replace(des_path/file.name)
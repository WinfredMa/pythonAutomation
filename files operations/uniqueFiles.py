# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 16:56:20 2022

@author: WinfredMa
"""

from pathlib import Path
from filecmp import cmp
src_folder = Path("C:\\Users\\WinfredMa\\Documents\\Python Automation\\files operations\\srcFolder")
des_folder = Path("C:\\Users\\WinfredMa\\Documents\\Python Automation\\files operations\\duplicatedFiles")
if not des_folder.exists():
    des_folder.mkdir(parents=True)
result = list(src_folder.glob('*'))
file_list = []
for file in result:
    if file.is_file():
        file_list.append(file)
for m in file_list:
    for n in file_list:
        if m != n and m.exists() and n.exists():
            if cmp(m, n):
                n.replace(des_folder/n.name)
                # n.unlink()
    
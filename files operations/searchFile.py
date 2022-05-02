# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 17:25:01 2022

@author: WinfredMa
"""

from pathlib import Path
while True:
    folder = input('input a folder')
    folder = Path(folder.strip())
    if folder.exists() and folder.is_dir():
        keyword = input('input file or folder').strip()
        # result = list(folder.rglob(f'*{keyword}*'))
        result = list(folder.rglob(keyword))
        if len(result) != 0:
            print(f'find below files by {keyword} in {folder}')
            for file in result:
                print(file)
        else:
            print(f'not found')
        break
    else:
        print('invalid path')
    
    
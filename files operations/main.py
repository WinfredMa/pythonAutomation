import os
import shutil

src_folder = "C:\\Users\\WinfredMa\\Documents\\Python Automation\\files operations\\srcFolder"
des_folder = "C:\\Users\\WinfredMa\\Documents\\Python Automation\\files operations\\desFolder"

files = os.listdir(src_folder)
for i in files:
    src_path = src_folder + "\\" + i
    if os.path.isfile(src_path):
        des_path = des_folder + "\\" + i.split('.')[-1]
        print(des_path)
        if not os.path.exists(des_path):
            os.makedirs(des_path)
            shutil.move(src_path, des_path)
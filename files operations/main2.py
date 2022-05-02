from pathlib import Path

src_folder = Path("C:\\Users\\WinfredMa\\Documents\\Python Automation\\files operations\\srcFolder")
des_folder = Path("C:\\Users\\WinfredMa\\Documents\\Python Automation\\files operations\\desFolder")

files = src_folder.glob('*')
for i in files:
    if i.is_file:
        des_path = des_folder/i.suffix.strip('.')
        if not des_path.exists():
            des_path.mkdir(parents=True)
            i.replace(des_path/i.name)
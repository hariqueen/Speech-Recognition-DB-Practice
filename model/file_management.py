import os

__all__ = ["create_folders"]

def create_folders(db_folders):
    for folder in db_folders:
        os.makedirs(os.path.join(folder, 'etc'), exist_ok=True)
        os.makedirs(os.path.join(folder, 'wav'), exist_ok=True)

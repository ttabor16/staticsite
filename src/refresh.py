import os
import shutil

def static_to_public():
    source = './static'
    destination = './public'
    if not os.path.exists(source):
        raise Exception(f'Source director "{source}" does not exist.')
    if os.path.exists(destination):
        shutil.rmtree("./public")
    os.mkdir(destination)
    shutil.copytree(source,destination, dirs_exist_ok=True)


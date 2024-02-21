import os

def rename_files():
    # 获取当前目录下所有的文件
    files = os.listdir()

    # 过滤出所有的图片文件
    image_files = [file for file in files if file.endswith('.jpg')]

    # 遍历图片文件并重命名
    for i, file in enumerate(image_files):
        new_name = f"{i+1}.jpg"
        os.rename(file, new_name)
        print(f"Renamed {file} to {new_name}")

if __name__ == "__main__":
    rename_files()

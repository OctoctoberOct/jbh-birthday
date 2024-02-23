import os
from PIL import Image

# 获取当前目录下所有文件
files = os.listdir()

# 计数器
count = 1

# 遍历所有文件
for file in files:
    # 判断文件是否为图像文件
    if file.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
        # 打开图像文件
        try:
            image = Image.open(file)
        except Exception as e:
            print(f"Error: {e} - Skipping {file}")
            continue
        
        # 将图像转换为JPEG格式
        new_filename = f"{count}.jpg"
        image = image.convert("RGB")
        image.save(new_filename)
        
        # 删除原始文件
        os.remove(file)
        
        # 更新计数器
        count += 1

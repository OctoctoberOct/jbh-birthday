# 生成包含74个图像链接的HTML代码
html_code = ""
for i in range(1, 75):  # 从1到74
    image_url = f"./2img/{i}.jpg"  # 假设图像的命名格式为1.jpg、2.jpg、...、74.jpg
    html_code += f'''
    <div class="col">
        <a href="#">
            <div class="hover">
                <div class="pad align-bottom">
                    <h2></h2>
                </div>
            </div>
            <div class="bg-img" style="background-image:url({image_url});">
            </div>
        </a>
    </div>
    '''

# 输出HTML代码
print(html_code)

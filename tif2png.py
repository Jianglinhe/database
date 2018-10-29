from PIL import Image
import os


# 需要修改图片所在文件夹路径
path = "F:/hezhiqiang_file/yanqiuxueguan/mask/"
# 修改后将图片保存的路径
savePath = "F:/hezhiqiang_file/yanqiuxueguan/mask_png/"

# 要修改的文件的格式
pic_ext = ['.TIF', '.tif', '.gif']

path_list = os.listdir(path)

i = 0  # a counter(compute the amount of modified figures )
for file in path_list:
    name, ext = os.path.splitext(file)
    if ext in pic_ext:

        im = Image.open(path+file)
        im.save(savePath+name+".png")
        i = i + 1

print("successful change ", i, "pictures")



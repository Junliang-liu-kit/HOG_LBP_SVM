
#coding=utf-8
from PIL import Image
import os
image_width = 100
image_height = 128
def fixed_size(filePath,savePath):
    """按照固定尺寸处理图片"""
    im = Image.open(filePath)
    out = im.resize((image_width, image_height), Image.ANTIALIAS)
    out.save(savePath)


def changeSize():
    filePath = r'C:\Users\Liu\Desktop\SVM\HOG_SVM-master\Dataset\猫狗数据集\train\train'
    destPath = r'C:\Users\Liu\Desktop\SVM\HOG_SVM-master\Dataset\猫狗数据集\train128'
    if not os.path.exists(destPath):
        os.makedirs(destPath)
    for root, dirs, files in os.walk(filePath):
        for file in files:
            print(file)
            if file[-1]=='g': #g 是 jpg 的 g
                fixed_size(os.path.join(filePath, file), os.path.join(destPath, file))
                #print('ing')
    print('Done')

if __name__ == '__main__':
    changeSize()

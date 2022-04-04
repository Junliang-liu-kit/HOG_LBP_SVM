# -*- coding=utf-8 -*-
import glob
import platform
import time
from PIL import Image
from skimage.feature import hog
import numpy as np
import os
import joblib
from sklearn.svm import LinearSVC
import shutil
import sys



from hog_svm import get_image_list, rgb2gray, write_to_txt, mkdir

# 第一个是你的类别   第二个是类别对应的名称   输出结果的时候方便查看
label_map = {1: 'cat',
             2: 'dog',
             }

#预测图片的位置
predict_image_path = 'image_predict128'
predict_name_path = os.path.join('image_predict128', 'predict.txt')

image_height = 128
image_width = 100

model_path = 'model/'
predict_feat_path = 'predict/'

#预测图片的HOG检测并提取特征
def get_feature(image_list, name_list, savePath):
    i = 0
    for image in image_list:
        try:
            image = np.reshape(image, (image_height,image_width, 3))
        except:
            print('发送了异常，图片大小size不满足要求：',name_list[i])
            continue
        gray = rgb2gray(image) /225.0
        fd = hog(gray, orientations=9, block_norm='L1', pixels_per_cell=[8, 8], cells_per_block=[4,4], visualize=False,
                 transform_sqrt=True)
        fd_name = name_list[i] + '.feat'
        fd_path = os.path.join(savePath, fd_name)
        joblib.dump(fd, fd_path)
        i += 1
    print("Test features are extracted and saved.")


def get_name(file_path):
    print("read name from ",file_path)
    name_list = []
    with open(file_path) as f:
        for line in f.readlines():
            name_list.append(line.split(' ')[0].replace('\n','')) #.replace('\r','')
    return name_list

def predict():
    t0 = time.time()
    features = [] 
    result_list = [] 
    total = 0

    #加载模型
    clf = joblib.load(model_path+'model')
    print("predict using trained SVM-Model")
    for feat_path in glob.glob(os.path.join(predict_feat_path, '*.feat')):
        #加载predict数据
        #data = joblib.load(feat_path)
        #features.append(data[:-1])
        total += 1
        if platform.system() == 'Windows': #platform.system()返回当前操作系统的名字，例如Linux , Windows , Java , …如果不能确定会返回空字符串
            symbol = '\\'
        else:
            symbol = '/'
        image_name = feat_path.split(symbol)[1].split('.feat')[0]
        data_predict = joblib.load(feat_path)
        data_predict_feat = data_predict[:].reshape((1, -1)).astype(np.float64)
        result = clf.predict(data_predict_feat)
        result_list.append(image_name + ' ' + label_map[int(result[0])] + '\n')
    
    write_to_txt(result_list)
    t1 = time.time()
    print('耗时是 : %f' % (t1 - t0))

if __name__ == '__main__':
    #shutil.rmtree(predict_feat_path)
    #mkdir()
    predict_name = get_name(predict_name_path)
    predict_image = get_image_list(predict_image_path, predict_name)
    get_feature(predict_image, predict_name, predict_feat_path)
    
    predict()


    



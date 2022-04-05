# HOG_LBP_SVM

## 1.Principle introduction

Feature extraction methods HOG (Histogram of Oriented Gradient) and LBP (Local Binary Pattern), both features have been proven successful in various vision tasks such as object classification, texture analysis and face recognition。<br>

About HOG:
HOG focuses more on shape information. <br>
[Introduction in WIKI](https://en.wikipedia.org/wiki/Histogram_of_oriented_gradients)<br>
[Intorduction in chinese](https://blog.csdn.net/hujingshuang/article/details/47337707)<br>

About LBP:
LBP emphasizes texture information within each patch.<br>
[Introduction in WIKI](https://en.wikipedia.org/wiki/Local_binary_patterns)<br>
[Intorduction in chinese](https://www.cnblogs.com/hyb965149985/p/10743022.html)<br>

SVM (support vector machines, SVM) is a common binary classification model of machine learning.Hier i recommend the AndrewNg "machine learning" course on coursera to learn SVM.<br>

## 2.About code
* environment: python 3.6.13; scikits.learn 0.22.1
* hog_svm.py is used to train and test SVM model using HOG featrue. 
* LBP_svm is used to train and test SVM model using LBP featrue.
* predict_svm.py can use a well-trained model to directly classify dog and cat. I have also saved two well-trained model in file "model"
* You need to set the image size and resize all images. change_size.py can help you to finish this work

## 3.some tips
* The model is obtained by extracting the hog feature of the picture, and then trained by SVM, and finally predicted by the model, and the result is written into the result.txt file.

## 4.Reference


1.方法介绍
2.关于代码
3.训练和检测的注意事项
4.Reference

上面的hog_svm.py是用于训练的，通过提取图片的hog特征，然后通过SVM进行训练得到model，最后通过model进行预测,将结果写入result.txt文件之中。


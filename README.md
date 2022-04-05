# HOG_LBP_SVM

## 1.Principle introduction

* Feature extraction methods HOG (Histogram of Oriented Gradient) and LBP (Local Binary Pattern), both features have been proven successful in various vision tasks such as object classification, texture analysis and face recognition。<br>

* About HOG:
HOG focuses more on shape information. <br>
[Introduction in WIKI](https://en.wikipedia.org/wiki/Histogram_of_oriented_gradients)<br>
[Intorduction in chinese](https://blog.csdn.net/hujingshuang/article/details/47337707)<br>

* About LBP:
LBP emphasizes texture information within each patch.<br>
[Introduction in WIKI](https://en.wikipedia.org/wiki/Local_binary_patterns)<br>
[Intorduction in chinese](https://www.cnblogs.com/hyb965149985/p/10743022.html)<br>

* SVM (support vector machines, SVM) is a common binary classification model of machine learning.Hier i recommend the AndrewNg "machine learning" course on coursera to learn SVM.<br>

## 2.About code
* environment: python-3.6.13; scikits.learn-0.22.1
* hog_svm.py is used to train and test SVM model using HOG featrue. 
* LBP_svm is used to train and test SVM model using LBP featrue.
* predict_svm.py can use a well-trained model to directly classify dog and cat. I have also saved two well-trained model in folder "model"
* You need to set the image size and resize all images. change_size.py can help you to finish this work

## 3.some tips
* The image feature is obtained by feature extraction method, and then is used to train SVM model, and finally predicted by the model, and the result is written into the result.txt file.
* The folder "predict", "test", "train", involved in this project, you need to creat it by yourself, and don't forget to change the path of saving the images and labels
* In this project, I use SVM to classify cat and dog based on the dataset “Kaggle”. If you want to train your own classifer, you need to modify parameter "label_map" to your labels

## 4.Reference

* Github: HOG_SVM of CHNicelee https://github.com/CHNicelee/HOG_SVM.git
* Dataset Kaggle https://www.kaggle.com/c/dogs-vs-cats/data


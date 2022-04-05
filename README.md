# HOG_LBP_SVM

## Principle introduction

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

## About code


## some tips
1.方法介绍
2.关于代码
3.训练和检测的注意事项

上面的hog_svm.py是用于训练的，通过提取图片的hog特征，然后通过SVM进行训练得到model，最后通过model进行预测,将结果写入result.txt文件之中。


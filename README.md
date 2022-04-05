# HOG+SVM

Feature extraction methods HOG (Histogram of Oriented Gradient) and LBP (Local Binary Pattern), Both features have been proven successful in various vision tasks such as object classification, texture analysis and face recognition, etc. HOG and LBP are complementary in the sense that HOG focuses more on shape information while LBP emphasizes texture information within each patch. The advantage of such combination was also reported in for human detection task.

1.方法介绍
2.关于代码
3.训练和检测的注意事项

上面的hog_svm.py是用于训练的，通过提取图片的hog特征，然后通过SVM进行训练得到model，最后通过model进行预测,将结果写入result.txt文件之中。


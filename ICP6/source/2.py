#import packages for support vector , accuracy, split train data and datasets
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import datasets
data=datasets.load_iris()
x=data.data
y=data.target
train_x, test_x, train_y, test_y=train_test_split(x, y, test_size=0.2)
lmodel=SVC(kernel='linear')
lmodel.fit(train_x, train_y)
prediction=lmodel.predict(test_x)
print("linear kernel Accuracy score is", accuracy_score(prediction, test_y))
print(prediction)

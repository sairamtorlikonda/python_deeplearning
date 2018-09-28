from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import datasets
data=datasets.load_iris()
x=data.data
y=data.target
train_x1, test_x1, train_y1, test_y1=train_test_split(x, y, test_size=0.2)
rmodel=SVC(kernel='rbf')
rmodel.fit(train_x1, train_y1)
pred=rmodel.predict(test_x1)
print("RBF kernel accuracy score is", accuracy_score(pred, test_y1))
print(pred)
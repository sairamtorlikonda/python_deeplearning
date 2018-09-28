#import packages for datasets,metrics,Gaussian NB model and test for training data
from sklearn import datasets,metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import csv

#irisdatasets = csv.reader("C:\Users\Sai Ram Torlikonda\Desktop\part-1\python\icp6\iris.csv", delimiter=',')
irisdatasets=datasets.load_iris()
x=irisdatasets.data
y=irisdatasets.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
model=GaussianNB()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
print("Accuracy : ",metrics.accuracy_score(y_test, y_pred))
print(y_pred)
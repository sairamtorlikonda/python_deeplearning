#import packages for support vector , accuracy, split train data and datasets
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import datasets
#load the iris datasets
data=datasets.load_iris()
#load x and y data
x=data.data
y=data.target
#split training and test data for both x and y for linear kernel
train_x, test_x, train_y, test_y=train_test_split(x, y, test_size=0.2, random_state=21)
#split training and test data for both x and y for rbf kernel
train_x1, test_x1, train_y1, test_y1=train_test_split(x, y, test_size=0.2, random_state=23)
#define the model for poly kernel
p_model = SVC(kernel="poly", degree=4)
#define the model for rbf kernel
rmodel=SVC(kernel='rbf')
#fit training data into linear kernel
p_model.fit(train_x, train_y)
#predict the test data using linear kernel
prediction=p_model.predict(test_x)
#calc accuracy score for linear kernel
print("poly kernel Accuracy score is", accuracy_score(prediction, test_y))
print(prediction)
#fit training data into rbc kernel
rmodel.fit(train_x1, train_y1)
#predict the test data for rbc kernel
pred=p_model.predict(test_x1)
#calc accuracy for rbc kernel
print("RBF kernel accuracy score is", accuracy_score(pred, test_y1))
print(pred)


gammas = [1,1000]
for gamma in gammas:
   #svc = SVC(kernel=’rbf’, gamma=gamma).fit(train_x1, train_y1)
   p_model = SVC(kernel="poly", degree=4,gamma=gamma)
   p_model.fit(train_x, train_y)
   prediction = p_model.predict(test_x)
   print("poly1 kernel Accuracy score is", accuracy_score(prediction, test_y))
   print(prediction)
   rmodel = SVC(kernel='rbf',gamma=gamma)
   rmodel.fit(train_x1, train_y1)
   pred = p_model.predict(test_x1)
   print("RBF2 kernel accuracy score is", accuracy_score(pred, test_y1))
   print(pred)
   # plotSVC(‘gamma=’ + str(gamma))

cs = [1,1000]
for c in cs:
   #svc = svm.SVC(kernel=’rbf’, C=c).fit(X, y)
   p_model = SVC(kernel="poly", degree=4,C=c)
   p_model.fit(train_x, train_y)
   prediction = p_model.predict(test_x)
   print("poly2 kernel Accuracy score is", accuracy_score(prediction, test_y))
   print(prediction)
   rmodel = SVC(kernel='rbf',)
   rmodel.fit(train_x1, train_y1)
   pred = p_model.predict(test_x1)
   print("RBF2 kernel accuracy score is", accuracy_score(pred, test_y1))
   print(pred)
   # plotSVC(‘C=’ + str(c))
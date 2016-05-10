from sklearn import linear_model
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsRegressor

class PriceModel(object):
    """Linear Regression Model used to predict future prices"""
    def __init__(self, algorithm='linear_regression'):
        if algorithm == 'knn':
            self.clf = KNeighborsRegressor(n_neighbors=2)
        else:
            self.clf = linear_model.LinearRegression()

    def train(self, X_train, y_train):
        self.clf.fit(X_train, y_train)

    def predict(self, x):
        return self.clf.predict(x)

    def score(self, X_test, y_test):
        return self.clf.score(X_test, y_test)

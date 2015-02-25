from sklearn.cross_validation import KFold
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
import numpy as np

class Marker():

    def __init__(self):
        self.model1=None
        self.model2=None

    def load(self):
        x1=[]
        x2=[]
        y=[]

        with open("learningData.txt") as f:
            line = f.readline()  # skip header
            line = f.readline()
            i=0
            while line:
                word=line.split('\t')
                print([float(word[0]),float(word[1])])
                x1.append([float(word[1])])
                x2.append([float(word[2])])
                y.append(float(word[0]))
#                y.append(i%2.0)  # good and bud presents alternately
                line=f.readline()
                i+=1

        j=0
        y=np.array(y)
        x1=np.array(x1)
        x2=np.array(x2)

        self.model1 = self.create_model()
        self.model1.fit(x1, y)
        self.model2 = self.create_model()
        self.model2.fit(x2, y)
        self.calculate_RMSE(x1,y)
        self.calculate_RMSE_at_fold_CV(x1,y)
        self.calculate_RMSE(x2,y)
        self.calculate_RMSE_at_fold_CV(x2,y)

    def calculate_RMSE(self, x, y):
        mod = self.create_model()
        mod.fit(x, y)
        p = np.array([mod.predict(xi) for xi in x])
        e = p - y
        total_error = np.sum(e * e)
        rmse_train = np.sqrt(total_error / len(p))
        print('RMSE on training: {}'.format(rmse_train))

    def calculate_RMSE_at_fold_CV(self, x, y):
        lr = self.create_model()
        kf = KFold(len(x), n_folds=10)
        err = 0
        for train, test in kf:
            lr.fit(x[train], y[train])
            p = np.array([lr.predict(xi) for xi in x[test]])
            e = p - y[test]
            err += np.dot(e, e)
        rmse = np.sqrt(err / len(x))
        print('RMSE on 10-fold CV: {}'.format(rmse))

    def create_model(self):
        return LinearRegression(fit_intercept=True)

    def cal_score(self, analyzed):

        xj=np.array(analyzed["speed"])
        send_score1=self.model1.predict(xj)
        xj=np.array(analyzed["sentenceSpeed"])
        send_score2=self.model2.predict(xj)
        return send_score1[0],send_score2[0]
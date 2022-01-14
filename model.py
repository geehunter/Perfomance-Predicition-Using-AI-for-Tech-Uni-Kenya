from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pickle
import math
import pandas as pd


def train(X,y):

    # train test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

    knn = KNeighborsClassifier(n_neighbors=4)

    # fit the model
    knn.fit(X_train, y_train)
    preds = knn.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f'Successfully trained model with an accuracy of {acc:.2f}')

    return knn

if __name__ == '__main__':

    performance_data = pd.read_csv('performance.csv')
    X = performance_data.iloc[:, :-1].values
    y = performance_data.iloc[:, -1].values


    mdl = train(X,y)

    # serializing model
    pickle.dump(mdl,open('perfomance.pkl','wb'))
    #model = pickle.load(open('perfomance.pkl','rb'))


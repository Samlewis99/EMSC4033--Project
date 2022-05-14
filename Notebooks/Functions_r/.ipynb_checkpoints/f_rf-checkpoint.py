# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

def get_data():
    """
    This function imports the iris dataset and converts it into a pandas data frame
    """
    from sklearn import datasets
    iris = datasets.load_iris()
    import pandas as pd
    data=pd.DataFrame({
    'sepal length':iris.data[:,0],
    'sepal width':iris.data[:,1],
    'petal length':iris.data[:,2],
    'petal width':iris.data[:,3],
    'species':iris.target
    })
    return data


def get_data1():
    """
    This function imports the random forest model and iris dataset.
    To use this function you must define x,y = then call this function
    Returns: clf and iris
    """
    from sklearn import datasets
    iris = datasets.load_iris()
    data = get_data()
    from sklearn.model_selection import train_test_split

    X=data[['sepal length', 'sepal width', 'petal length', 'petal width']]  # Features
    y=data['species']  # Labels

    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # 70% training and 30% test
    from sklearn.ensemble import RandomForestClassifier

    #Instantiate a model
    clf=RandomForestClassifier(n_estimators=100)

    #Train the model (fit) using the training features for the label
    clf.fit(X_train,y_train)
    
    return clf,iris


def Accuracy_test():
    """
    This function tests the accuracy of the random forest model with the sepal width variable dropped
    Returns: accuracy
    """
    from sklearn import datasets
    iris = datasets.load_iris()
    data = get_data()
    from sklearn.model_selection import train_test_split

    X=data[['sepal length', 'sepal width', 'petal length']]  # Features
    y=data['species']  # Labels

    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # 70% training and 30% test
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.ensemble import RandomForestClassifier

    #Create a Gaussian Classifier
    clf=RandomForestClassifier(n_estimators=100)

    #Train the model using the training sets y_pred=clf.predict(X_test)
    clf.fit(X_train,y_train)

    # prediction on test set
    y_pred=clf.predict(X_test)

    #Import scikit-learn metrics module for accuracy calculation
    from sklearn import metrics
    # Model Accuracy, how often is the classifier correct?
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))



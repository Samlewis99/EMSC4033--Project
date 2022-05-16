from Functions_r import f_rf as ft


def test_imports():
    import sys
    mods = []
    if 'pandas' in sys.modules:
        mods.append(1)
    if 'sklearn.model_selection' in sys.modules:
        mods.append(1)
    assert mods == [1,1], "***The imports have not worked"


def test_pandas(data):
    import pandas
    assert type(data) == pandas.core.frame.DataFrame, "*** The data is not in the required pandas dataframe"


def test_random_f(clf):
    from sklearn.ensemble import RandomForestClassifier
    assert type(clf) == RandomForestClassifier, "*** The variable is not a random forest model"


def test_onehot(dataframe):
    f = dataframe.dtypes
    assert 'str' not in f.unique(), "your dataframe still contains string values"

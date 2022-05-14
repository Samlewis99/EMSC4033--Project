def test_imports():
    import sys
    mods = []
    if 'pandas' in sys.modules:
        mods.append(1)
    if 'from sklearn.model_selection' in sys.modules:
        mods.append(1)
    assert mods == [1,1], "***The imports have not worked"


def test_pandas(data):
    import pandas
    assert type(data) == pandas.core.frame.DataFrame



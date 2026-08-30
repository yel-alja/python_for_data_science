import pandas as pd

def load(path: str) -> pd.DataFrame:
    """load data depending on path"""
    if path is None:
        return pd.DataFrame([])
    res = pd.read_csv(path)
    print("loading Dataset of dimensions", res.shape)
    return res.to_string(index=False)


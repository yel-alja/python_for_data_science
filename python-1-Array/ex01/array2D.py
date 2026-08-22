import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    try:
        lst = np.array(family)
    except:
        return []
    
    newlst = lst[start:end]
    print(f"my shape is : {lst.shape}")
    print(f"my new shape is : {newlst.shape}")
    return newlst.tolist()

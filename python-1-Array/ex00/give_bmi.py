
def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    if len(height) != len(weight):
            raise ValueError("Value Error")
    lst = []
    for i in range(len(height)):
        lst.append(weight[i] /( height[i] * height[i]))
    return lst

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    res = []
    for i in bmi:
        if i > limit:
            res.append(True)
        else:
            res.append(False)
    return res 


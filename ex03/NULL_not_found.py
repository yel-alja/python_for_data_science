from typing import Any

object_names = {
    str : "Empty",
    type(None) : "Nothing",
    float : "Cheese",
    int : "Zero",
    bool : "Fake"
}

def NULL_not_found(object : Any):
    object_type = type(object)
    object_name = object_names.get(object_type , "Not found")
    if object_type == str and object:
        print("Type not Found")
        return 1
    elif object_name != "Not found":
        print (f"{object_name}: {object} {object_type}")
        
    return 0
from typing import Any
type_names = {
    list: "List",
    tuple: "Tuple",
    set: "Set",
    dict: "Dict"
}
def all_thing_is_obj(object: Any) -> int:
    object_type = type(object)
    type_name = type_names.get(object_type, "Type not found")
    if object_type == str:
        print(f"{object} is in the kitchen : {object_type}")
    elif type_name != "Type not found":
        print(f"{type_name} : {object_type}")
    else:
        print(type_name)
    return 42


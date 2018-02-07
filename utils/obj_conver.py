# 对象转为字典
def class_to_dict(obj):
    dict = obj.__dict__
    return dict


# 将class转为支持java接口调用的jsonStr
def class_to_json_str(obj):
    full_dict = {}
    obj_dict = obj.__dict__
    for k, v in obj_dict.items():
        if v:
            full_dict = dict(full_dict, **{k: v})
    json_str = str(full_dict).replace(",", '"')
    return json_str


# 将class转为支持java接口调用的json
def class_to_json(obj):
    full_dict = {}
    obj_dict = obj.__dict__
    for k, v in obj_dict.items():
        if v:
            full_dict = dict(full_dict, **{k: v})
    return full_dict

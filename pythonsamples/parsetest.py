
from types import SimpleNamespace


# def todict(obj, classkey=None):
#     if isinstance(obj, dict):
#         data = {}
#         for (k, v) in obj.items():
#             data[k] = todict(v, classkey)
#         return data
#     elif hasattr(obj, "_ast"):
#         return todict(obj._ast())
#     elif hasattr(obj, "__iter__"):
#         return [todict(v, classkey) for v in obj]
#     elif hasattr(obj, "__dict__"):
#         data = dict([(key, todict(value, classkey))
#                      for key, value in obj.__dict__.items()
#                      if not callable(value) and not key.startswith('_') and key not in ['name']])
#         if classkey is not None and hasattr(obj, "__class__"):
#             data[classkey] = obj.__class__.__name__
#         return data
#     else:
#         return obj

def recursive_vars(dic):
    items = {}
    for key in dic:
        value = dic[key]
        if isinstance(value, list):
            list_items = []
            for item in value:
                list_items.append(recursive_vars(vars(item)))
            items [key] = list_items
        elif type(value) is SimpleNamespace:
            items [key] = recursive_vars(vars(value))
        else:
            items [key] = value
    return items

myobject = SimpleNamespace(opname='parse', params=SimpleNamespace(annotations=[SimpleNamespace(annotations=SimpleNamespace(ner=SimpleNamespace(time=0.9939869940280914)), end_pos=21, start_pos=9)], model='jiffy', text='wait for five minutes'))

tesDic = {'text': 'wait for five minutes\nwait for fifty minutes and thirty seconds\n', 'discourse_ctx': SimpleNamespace(), 'job': 'rpa', 'targets': ['jiffy'], 'debug': False}
print(recursive_vars(vars(tesDic)))

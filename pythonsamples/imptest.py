from importlib import import_module

mod = import_module('classtest')
cons = getattr(mod,'new_instance')
obj = cons()
obj.api_add_words()
obj.tag()

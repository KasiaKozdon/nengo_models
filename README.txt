The newest version of nengo_dl (3.4) produced an error
AttributeError: module 'collections' has no attribute 'Iterable'
Resolved by changing code in
progressbar/bar.py
From
isinstance(obj, collections.Iterable)
To 
isinstance(obj, collections.abc.Iterable)
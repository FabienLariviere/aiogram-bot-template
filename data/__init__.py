from data import config
from data.models import BaseModel

if config.DATABASE_URL:
    for obj in BaseModel.__subclasses__():
        try:
            obj.create_table()
            print('Table', obj.__name__, 'loaded')
        except:
            print(obj, 'load error')

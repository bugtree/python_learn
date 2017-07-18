# -*- coding: UTF-8 -*-

class Field(object):
    def __init__(self, name, col_type):
        self.name = name
        self.col_type = col_type

    def __str__(self):
        print("%s, <%s-%s>"%(self.__class__.__name__, self.name, self.col_type))

class IntField(Field):
    def __init__(self, name):
        super(IntField, self).__init__(name, "valchar(100)")

class StrField(Field):
    def __init__(self, name):
        super(StrField, self).__init__(name, "bigint")

class ModelMetaClass(type):
    def __new__(cls, name, bases, attr):
        if name == "Model":
            return super(ModelMetaClass, cls).__new__(cls, name, bases, attr)

        maps = dict()

        for k, v in attr.items():
            if isinstance(v, Field):
                maps[k] = v

        for k in maps.keys():
            attr.pop(k)

        attr["__mapping__"] = maps
        attr["__name__"] = name
        print("list: %s" % attr.items())
        return super(ModelMetaClass, cls).__new__(cls, name, bases, attr)

        

class Model(dict, metaclass = ModelMetaClass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        return self[key]

    def save(self):
        files = []
        params = []
        argvs = []

        for k, v in self.__mapping__.items():
            files.append(v.name)
            params.append("?")
            argvs.append(getattr(self, k, None))  
            #print("%s--%s" % (v.name, v.col_type))
            # 这种用法也可以
            #argvs.append(self.__getattr__(k))

        sql = "insert into %s (%s) values (%s)"%(self.__name__, ",".join(files), ",".join(params))
        print("%s"%sql)
        print("%s"%str(argvs))

class User(Model):
    # 定义类的属性到列的映射：
    id = IntField("user_id")
    name = StrField("user_name")
    email = StrField("user_email")
    pwd = StrField("user_pwd")


if __name__ == "__main__":
    # 创建一个实例：
    #u = User(**{"id":1, "name":"Jack", "email":"xx@126.com", "pwd":"xx"})
    u = User(id=1, name="Jack", email="xx@126.com", pwd="xx")
    # 保存到数据库：
    u.save()

    c = IntField("xx")
    c.__str__()


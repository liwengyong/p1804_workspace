
class DogLwy(object):
    __instance = None
    def __init__(self):
        pass
    def __new__(cls,*a):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls,*a)
        return cls.__instance

a = DogLwy()
print(a)
b = DogLwy()
print(b)


class Addition:
    a=2
    b=1
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def compute1(self):
        return self.a+self.b
    def compute2(self):
        return Addition.a+Addition.b
    
    @classmethod
    def class_method(cls):
        return cls.a+cls.b
    
    @staticmethod
    def static_method():
        return Addition.a+Addition.b


obj=Addition(3,2)

print(obj.compute1())
print(obj.compute2())


# print(obj.a)
# print(obj.b)

# print(Addition.a)
# print(Addition.b)
    
print(Addition.class_method())
print(Addition.static_method())

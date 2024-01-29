class MyClass:
    def instance_method(self):
        return 'instance method', self
    
    @classmethod
    def class_method(cls):
        return 'class method', cls
    
    @staticmethod
    def static_method():
        return 'static method'
    
instance = MyClass()
print(MyClass.class_method())
print(MyClass.class_method(MyClass))
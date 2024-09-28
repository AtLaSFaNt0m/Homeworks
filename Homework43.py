def introspection_info(obj):
    obj_type = type(obj).__name__
    obj_module = obj.__class__.__module__
    obj_attrs = dir(obj)
    obj_methods = [method for method in obj_attrs if callable(getattr(obj, method)) and not method.startswith('__')]
    obj_non_methods = [attr for attr in obj_attrs if not callable(getattr(obj, attr)) and not attr.startswith('__')]

    return {
        'type': obj_type,
        'module': obj_module,
        'attributes': obj_non_methods,
        'methods': obj_methods
    }


number_info = introspection_info(42)
print("Интроспекция для целого числа:")
print(number_info)


class Aboba:
    def __init__(self, value):
        self.value = value

    def greet(self):
        return f"Hello, I have value {self.value}"


my_object = Aboba(10)
class_info = introspection_info(my_object)
print("\nИнтроспекция для объекта пользовательского класса:")
print(class_info)

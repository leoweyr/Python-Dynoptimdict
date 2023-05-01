class DynamicDataDict(dict):
    def __init__(self):
        self.__get_value_operate_queue = []
        self.__get_value_operate_arg_list = []

    def __repr__(self):  # Called when the object does not use the dictionary access operator, which is distinguished from calling method:special<__getitem__>.
        self.__get_value(None)  # Get all dynamic data.
        return super().__repr__()

    def __getitem__(self, key):
        self.__get_value(key)  # Get the specified dynamic data.
        return super().__getitem__(key)

    def __setitem__(self, dynamic_data_name, get_dynamic_data_func: callable):
        self.__get_value_operate_queue.append(self.__get_value_operate)
        self.__get_value_operate_arg_list.append((dynamic_data_name, get_dynamic_data_func))

    def keys(self):
        self.__get_value(None)
        return super().keys()

    def values(self):
        self.__get_value(None)
        return super().values()

    def items(self):
        self.__get_value(None)
        return super().items()

    def __get_value_operate(self, key, dynamic_data_name, get_dynamic_data_func: callable):
        if key == dynamic_data_name or key is None:
            super().__setitem__(dynamic_data_name, get_dynamic_data_func())

    def __get_value(self, key):
        for get_value_operate, get_value_operate_arg in zip(self.__get_value_operate_queue, self.__get_value_operate_arg_list):
            get_value_operate(key, get_value_operate_arg[0], get_value_operate_arg[1])

import time
from dynoptimdict import DynamicDataDict


def get_status_data_1():
    time.sleep(1)  # Here is just assuming this function takes 1 second to perform the calculation before returning the result.
    return "data_1_example"  # Must have a return value.


def get_status_data_2():
    time.sleep(10)  # In the same way, here is just a hypothesis, for the convenience of comparison later.
    return "data_2_example"


def get_status_data_3():
    time.sleep(100)  # The same is just an assumption.
    return "data_3_example"


class MyClass:
    @property
    def status(self):
        status = DynamicDataDict()
        '''
        The following steps are necessary. If you want to obtain data from the dynamic data dict in real time, you must 
        define function which is used to get related data, and then pass in its function pointer through the method of 
        adding key-value pairs to dict. 
         
        '''
        status["data_1"] = get_status_data_1
        status["data_2"] = get_status_data_2
        status["data_3"] = get_status_data_3

        return status


def main():
    obj = MyClass()
    obj.status["data_1"]  # Only get the specified data, it takes 1 second, and achieve the optimized effect.
    obj.status  # Get all data, it takes about 100 + 10 + 1 seconds.


if __name__ == "__main__":
    main()
def func_in_module():
    print('I am a function')

def func_in_module_1():
    print('I am a function 1')

def func_in_module_2():
    print('I am a function 2')

def func_in_module_3():
    print('I am a function 3')

def func_in_module_4():
    print('I am a function 4')

def func_one_in():
    print('func() in mymodule.py')

print('top level is mymodule.py')

if __name__ == '__main__':
    print('module mymodule.py run directly')
else:
    print('module mymodule.py imported in another module')
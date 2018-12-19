from mymodule import func_one_in as one

print('top level is namevariable.py')

if __name__ == '__main__':
    print('module namevariable run directly')
else:
    print('module imported in another module')
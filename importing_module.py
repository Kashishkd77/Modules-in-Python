#imports sum1(),sum2() from "modules1" module
#Alias name used for sum2() --> which means that now to use sum2() we need to use it's alias name
from module_sum import sum1,sum2 as s2

#To import all the functions of modules
'''
from module_print import *
'''

#When we use "from" keyword , we can import items from a single module
#WE cannot use comma separable list of modules to get imported
'''
from module_print import *,from module_sum import sum1,sum2 as s2
from module_print,module_sum import sum1,sum2
'''

#Giving alias name for module --> creates invalid syntax
'''
from module_sum as m1 import sum1,sum2 as s2
'''

#Alias name created for module
#When we use "import" keyword , we can import items from many module
#WE can use comma separable list of modules to get imported
import module_multiply as m2,module_print

#In case function name is used in place of alias name then error of "name not defined" pop ups
'''
print(sum2(4,5,6,7))  --> use s2 in place of sum2
print(module_multiply.mul1(3,5,6))--> use m2 in place of module_multiply
'''

#function which is not imported cannot be used , error of "name not defined" pop ups
'''
print(sum3(7,8))
'''

#when a particular function is imported from a module then module name is not used at the time of referencing the function
'''
print(modules1.s2(4,5,6,7))
'''
print(s2(4,5,6,7))
print(sum1(6,7,8))

print(m2.mul2(2,3,5,6))
print(module_print.print3())
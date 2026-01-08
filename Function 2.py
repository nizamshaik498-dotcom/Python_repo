#program made using function
global_variable="i am global variable"      #it prints this one cause it is outside the funtion
def my_function():
    local_variable="i am local variable"
    print(global_variable)
    print(local_variable)
var=my_function()
print(global_variable)
#print(local_variable)        #it does not print this one because it is inside the function
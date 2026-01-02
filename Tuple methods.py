#program using tuple methods and f-string

nums=(10,20,30,20,40,20,50)
t=nums.count(20)                #used count() method
t1=nums.index(20)               #used index() method 
print(t)
print(t1)                
print(f"20 appeared {t}times.")                         #used f-string
print(f"first occurence of 20 is:{t1}")                 #used f-string

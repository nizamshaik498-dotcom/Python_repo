#program created for (server resource monitor).

cpu_capacity=input("Enter total CPU capacity: ")                    #value should be in percentage, e.g., 100%
cpu_capacity=float(cpu_capacity.replace("%",""))                    #removing the percentage sign and converting to float for calculations
cpu_usage=input("Enter CPU usage: ")                                #value should be in percentage, e.g., 75%
cpu_usage=float(cpu_usage.replace("%",""))                          #removing the percentage sign and converting to float for calculations
total_memory=input("Enter total memory in GB: ")                    #value should be in GB, e.g., 32GB
total_memory=float(total_memory.replace("GB",""))                   #removing the GB unit and converting to float for calculations
used_memory=input("Enter used memory in GB: ")                      #value should be in GB, e.g., 16GB
used_memory=float(used_memory.replace("GB",""))                     #removing the GB unit and converting to float for calculations

rem_cpu=cpu_capacity-cpu_usage                                      #calculating remaining CPU by subtracting CPU usage from total CPU capacity
print("Remaining CPU: ",rem_cpu)

rem_mem=total_memory-used_memory                                    #calculating remaining memory by subtracting used memory from total memory
print("Remaining Memory: ",rem_mem)

if cpu_usage >=80 or used_memory>=16:
    print("Server Under High Load ⚠️")
else:
    print("Server Running Normally 👌")
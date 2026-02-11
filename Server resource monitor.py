#program created for (server resource monitor).

cpu_capacity=input("Enter total CPU capacity: ")
cpu_capacity=float(cpu_capacity.replace("%",""))
cpu_usage=input("Enter CPU usage: ")
cpu_usage=float(cpu_usage.replace("%",""))
total_memory=input("Enter total memory in GB: ")
total_memory=float(total_memory.replace("GB",""))
used_memory=input("Enter used memory in GB: ")
used_memory=float(used_memory.replace("GB",""))

rem_cpu=cpu_capacity-cpu_usage
print("Remaining CPU: ",rem_cpu)

rem_mem=total_memory-used_memory
print("Remaining Memory: ",rem_mem)

if cpu_usage >=80 or used_memory>=16:
    print("Server Under High Load ⚠️")
else:
    print("Server Running Normally 👌")
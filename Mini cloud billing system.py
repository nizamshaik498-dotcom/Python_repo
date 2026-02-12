#program made for (mini cloud billing system) in (AWS) style.

instances=int(input("Enter no.of.instances: "))
inst_hours=8
inst_cost=float(input("Enter cost per hour of instance: "))
s3_storage=int(input("Enter the s3 storage in GB: "))
s3_cost=2

ec2_total=instances*inst_hours*inst_cost
s3_total=s3_storage*s3_cost
total_bill=ec2_total*s3_total

if total_bill > 15000:
    discount=total_bill*0.10
    final_amount=total_bill-discount
    print("Enterprise Customer ")
    print("Discount applied: ",discount)
    print("FInal_amount: ",final_amount)
elif total_bill > 10000:
    print("Enterprise Customer ")
elif total_bill >5000:
    print("Business customer")
else:
    print(("Startup customer"))
print("Total Bill: ",total_bill)

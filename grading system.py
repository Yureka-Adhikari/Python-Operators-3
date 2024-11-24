print("Machhapuchchhre IB World School")
print("Terminal result")

math= int(input("Enter marks for maths: "))
english= int(input("Enter marks for english: "))
science= int(input("Enter marks science: "))
health= int(input("Enter marks for health: "))
computer= int(input("Enter marks for computer: "))
optional= int(input("Enter marks for optional maths: "))

total= math+english+health+science+computer+optional

avg = total/6
print(f"\nYour total marks is {total}")

print(f"\nAverage is {avg}")

if avg>= 90:
    print("\n your grade is: A+")
elif avg>= 80:
    print("\n your grade is: A")
    
elif avg>= 70:
    print("\n your grade is: B+")
elif avg>= 60:
    print("\n your grade is: B")
elif avg>= 50:
    print("\n your grade is: C")
else:
    print("\nSorry Youve failed")
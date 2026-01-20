marks=[]
for i in range(1,6):
   mark=int(input(f"Enter the marks {i}: "))
   marks.append(mark)

total=sum(marks)
average=total/len(marks)
print("Total Marks of Student",total)
print("Average of Marks:", average)
print("Highest Marks", max(marks))
print("lowest marks ", min(marks))




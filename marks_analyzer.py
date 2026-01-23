marks = []

while len(marks) < 5:
    mark = int(input(f"Enter marks for subject {len(marks) + 1}: "))

    if mark < 0 or mark > 100:
        print("Invalid input! Marks must be between 0 and 100.")
        continue

    marks.append(mark)

avg = sum(marks) / len(marks)

print("\n--- Result ---")

if avg >= 95:
    print("Your Grade = O")
elif avg >= 90:
    print("Your Grade = A")
elif avg >= 80:
    print("Your Grade = B")
elif avg >= 70:
    print("Your Grade = C")
elif avg >= 60:
    print("Your Grade = D")
else:
    print("Your Grade = Fail")

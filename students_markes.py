students = []

num = int(input("How many students? "))

for i in range(num):
    print(f"\nEnter details for Student {i+1}")
    
    name = input("Name: ")
    m1 = int(input("Subject 1: "))
    m2 = int(input("Subject 2: "))
    m3 = int(input("Subject 3: "))
    
    total = m1 + m2 + m3
    average = total / 3
    
    students.append({
        "name": name,
        "total": total,
        "average": average
    })

# Display Results
print("\n------ ALL RESULTS ------")
for student in students:
    print(f"{student['name']} - Total: {student['total']} - Avg: {student['average']}")

# Find Topper
topper = max(students, key=lambda x: x["average"])
print("\n🏆 Topper:", topper["name"])
print("Average:", topper["average"])
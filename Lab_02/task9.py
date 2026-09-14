print("Task 9 — Collections")

student_name = "Anna"
student_age = 22
student_skills = ["Python", "Mathematics", "Machine Learning"]
student_university = "NSU"

# A dict maps keys -> values. Keys here are strings.
student = {
    "name": student_name,
    "age": student_age,
    "skills": student_skills,          # value is a list
    "university": student_university,
}

# Accessing a value by key: student["name"]
print(f"Name: {student['name']}")
print(f"University: {student['university']}")

# Nested access: student["skills"] is a list, [0] gets its first item.
print(f"First skill: {student['skills'][0]}")

# len() on the list counts how many skills there are.
print(f"Number of skills: {len(student['skills'])}")

print()

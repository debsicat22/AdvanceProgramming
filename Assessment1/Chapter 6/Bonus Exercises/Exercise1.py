import json

# Step 1: Ask the user for student details and write to the JSON file
student_details = {}
student_details['Name'] = input("Enter student name: ")
student_details['ID'] = int(input("Enter student ID: "))
student_details['Course'] = input("Enter course: ")

# Add CourseDetails as a nested dictionary
course_details = {}
course_details['Group'] = input("Enter group: ")
course_details['Year'] = int(input("Enter year: "))
student_details['CourseDetails'] = course_details

with open('StudentJson.json', 'w') as json_file:
    json.dump(student_details, json_file)

print("Student details written to StudentJson.json")

# Step 2: Read and display the contents from the JSON file
with open('StudentJson.json', 'r') as json_file:
    student_details = json.load(json_file)

print("\nDetails of the Student are")
print(f"Name: {student_details['Name']}")
print(f"ID: {student_details['ID']}")
print(f"Course: {student_details['Course']}")
print(f"Group: {student_details['CourseDetails']['Group']}")
print(f"Year: {student_details['CourseDetails']['Year']}")

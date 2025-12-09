# student_info = {
#     "name": "Raman Sati",
#     "student_id": "123456789",
#     "course": "Python for DevOps",
#     "date": "2024-06-15"
# }

# print(student_info["name"])

# student_info =  [
#     {"name": "Raman Sati", "student_id": "123456789", "course": "Python for DevOps", "date": "2024-06-15"},
#     {"name": "John Doe", "student_id": "987654321", "course": "Python for DevOps", "date": "2024-06-16"},
#     {"name": "Jane Smith", "student_id": "456789123", "course": "Python for DevOps", "date": "2024-06-17"}
# ]

# for student in student_info:
#     print(student["name"])
    
ec2_instances = [
    {"id": "i-1234567890abcdef0", "type": "t2.micro", "state": "running"},
    {"id": "i-0abcdef1234567890", "type": "t2.small", "state": "stopped"},
    {"id": "i-0fedcba9876543210", "type": "t2.medium", "state": "running"}
]

print("EC2 Instances: of type " + ec2_instances[1]["type"])
print("EC2 Instances: of state " + ec2_instances[1]["state"])

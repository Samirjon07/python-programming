
student = {'name': 'John', 'age': 25,'courses': ['Math', 'CompSci']}
student['name']='Jane'
student['phone']='555-5555'
print(student.get('phone', 'Not Found'))
print(student)
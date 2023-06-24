students_grade=[]
students_grade.append((1,"a"))
students_grade.append((4,"b"))
students_grade.append((3,"c"))
students_grade.append((2,"d"))
students_grade.sort(reverse=True)
print("priority queue,highest num high priority")
print(students_grade)
print("original queue")
'''while students_grade:
    print(students_grade.pop())'''#pop deletes last element
students_grade.sort()
print(students_grade)
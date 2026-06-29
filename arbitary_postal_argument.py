def add(*args):
    if len(args)==0:
             return 'Please Enter something'
    total = 0
    for i in args:
        if isinstance(i,int):
            total = total +i
    return total



print(add(1,2,"sudna","tets"))
print(add(1,2,3))
print(add(1,2,3,4))
print(add())

#Key Word argument

def user_info(**kwargs):
     print(kwargs.get('age',0))
     print(type(kwargs))

print(user_info(name="Bidur",age=21,address='Ilam'))



def all(*args,**kwargs):
     print(*args)
     print(kwargs)


all(1,2,3,4,5,5,"hari",name='bidur')
all(1,2,3,4,5,6,'bidur')

print("------------------------------")
#Self Done
def marksheet(student_name, *subjects, **extra):
    total=0
    print(f"Student name:{student_name}")
    for i in subjects:
         total += (i[1])
    print(f"Total Marks: {total} ")
    print(f"Average: {total/len(subjects)} %")
    print(f'Class Teacher: {extra.get('class_teacher','No class Teacher is given')}')

marksheet(
    "Sudan Bhandari",
    ("Mathematics", 92),
    ("Science", 88),
    ("English", 85),
    ("Computer", 85),
    ("Social Studies", 81),
    class_teacher="Rajat",
    grade_level="Grade 10",
    attendance="96%"
)

#Sir le garnu vako
def marksheet(student_name, *subjects, **extra):
    total = 0
    for i in subjects:
        total = total + i[1]
        # total += i[1]
    return (f"{student_name}'s total marks is {total} and percentage is {total/len(subjects)} and class teacher is {extra.get('class_teacher')}")




print(marksheet(
    "Sudan Bhandari",
    ("Mathematics", 92),
    ("Science", 88),
    ("English", 85),
    ("Social Studies", 81),
    class_teacher="Mr. Sharma",
    grade_level="Grade 10",
    attendance="96"
))




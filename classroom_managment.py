classroom = [
    {
        'name': 'Alice',
        'email': 'alice@example.com',
        'grades': [
            ('math', 91),
            ('english', 78),
            ('math', 90),
            ('history', 34),
            ('math', 95),
        ],
    },
    {
        'name': 'Bob',
        'email': 'bob@example.com',
        'grades': [
            ('math', 85),
            ('english', 92),
            ('history', 75),
        ],
    },
    {
        'name': 'Charlie',
        'email': 'charlie@example.com',
        'grades': [
            ('physics', 78),
            ('english', 81),
            ('english', 89),
            ('history', 68),
            ('english', 82),
            ('physics', 91),
        ],
    },
]
def get_index(name):
    i=0
    for s in classroom:
        if name==s['name']:
            return i
        i+=1
    return -1       


def add_student(name, email=None):
    if email:
       student_email= email
    else:
        student_email=f'{name.lower()}@example.com'   

    classroom.append({'name':name,'email':student_email,'grades':[]})


def delete_student(name):
    index = get_index(name)
    classroom.remove(classroom[index])


def set_email(name, email):
     index = get_index(name)
     classroom[index]['email']=email
    


def add_grade(name, profession, grade):
    index = get_index(name)
    classroom[index]['grades'].append((profession,grade))


def avg_grade(name, profession):
    index = get_index(name)
    sum=0
    count=0
    for p in classroom[index]['grades']:
        if p[0]==profession:
            sum+=p[1]
            count+=1
    return sum/count


def get_professions(name):
   index = get_index(name)
   professions=set()
   
   for student in classroom[index]['grades']:
        professions.add(student[0]) 
   return list(professions)
   

##uppinp = inp.upper()
#####print(inp.replace("the", "this"))

students = [{"name":"Charles", "age":19, "major":"Computer Science"}, 
            { "name":"Conner", "age":20, "major":"Mechanical Engineering"},
             { "name": "Sarah", "age":19, "major":"English"}]

def remStu(students, name):
    nstudents = [stud for stud in students if stud.get("name") != name] #returns everything that meets the conditnois
    return nstudents
    
students = remStu(students, "Sarah")

def addStu(students, name, age, major) :
    if isinstance(name, str) & isinstance(age, int) & isinstance(major, str) 
    {

    }


    students.append({"name":name, "age":age, "major":major})
    return students

def findStu(students, name):
    try:
    fstud = [stud for stud in students if stud.get("name") == name]
    return fstud 

def printStu(students):
    for d in students:
        print(d)

printStu(students)

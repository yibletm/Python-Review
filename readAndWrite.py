with open('students.txt', 'a') as file:
    name = input("Add your name:")
    age = input("Add your age:")
    cla = input("add your class:")
    file.write(name+ " "+age+" "+cla)
    file.close
with open('students.txt', 'r') as file:
    contents = file.read()
    print(contents)
    file.close
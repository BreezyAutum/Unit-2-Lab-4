# Names and Grades
agrade = 0
hgrade = 0
studlist = {}
glist = {}
studentnum = int(input("Student Grades\n-------------\n\nHow many students are you entering grades for?\n"))
for iterations in range(studentnum + 1):
  studname = input("Enter student name:\n")
  if studname == "END":
    break
  studname = input("\nEnter student name:\n")
  studlist.append(studname)
  grade = float(input("\nEnter grade:\n"))
  glist.append(grade)
  agrade += grade
  if grade > hgrade:
    hgrade = grade
# Table
tablespace = 0
maxtablespace = len(print(                             ))
dash = "-"
print("\n------------------\nTable\n\nStudent Name          Grade\n-----------------------------")
for studname.value() in studlist:
  glist.value = studname.value in studlist
  tablespace = maxtablespace - len(studname)
  print(f"{studname+(dash*tablespace)+glist.value()}\n\nAverage grade is {agrade} and the highest grade is {hgrade}.")
# Data Collection
studlist = {}
scorelist = {}
studnum = int(input("How many students?\n"))
for studnum in studlist:
  studname = str(input("Enter student name:\n"))
  if "END" in studname:
    break
  studlist.extend(studname)
  studscore = float(input("Enter student score:\n"))
  scorelist.extend(studscore)
# Table
tablespace = 0
maxtablespace = len(str(print(                             )))
dash = "-"
print("\n------------------\nTable\n\nStudent Name          Grade\n-----------------------------")
check = 0
for index2 in studlist:
  studlist.values(check)
  scorelist.values(check)
  check += 1
  tablespace = maxtablespace - len(studlist.values(check))
  print(f"{studlist.values(check)+(dash*tablespace)+scorelist.values(check)}")
print(f"\n\n The average score is {scorelist.average}.\n{studlist.values(len(max(scorelist)))} achieved the highest score with {max(scorelist)}!")
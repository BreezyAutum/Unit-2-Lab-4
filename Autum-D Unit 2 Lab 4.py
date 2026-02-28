# Data Collection
studlist = {}
agrade = 0
hgrade = 0
studnum = int(input("How many students?\n"))
for index in range(studnum):
  studname = input("Enter student name\n")
  if "END" in studname:
    break
  score = input("Enter student score:\n")
  studlist[studname] = score
  agrade += float(score)
  if hgrade < float(score):
    hgrade = float(score)
    thebest = studname
# Table
print("\n------------------\nTable\n\nStudent Name          Grade\n-----------------------------")
for name , score in studlist.items():
  print(f"{name}               {score}")
print(f"\n\n The average score is {agrade / studnum}.\n{max(studlist)} achieved the highest score with {hgrade}!")
studentNumber = int(input("How many students on the course? "))
groupSize = int(input("Desired group size? "))
groupsFormed = studentNumber // groupSize
if studentNumber % groupSize != 0:
    groupsFormed += 1
print(f"Number of groups formed: {groupsFormed}")
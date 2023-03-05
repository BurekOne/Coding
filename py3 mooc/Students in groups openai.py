students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))

num_groups = students // group_size

if students % group_size != 0:
    num_groups += 1

print("Number of groups formed:", num_groups)
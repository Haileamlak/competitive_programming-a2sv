names = ["Abebe", "Kebede", "Aster", "Almaz", "Tolossa"]
jobs = ["Doctor", "Engineer", "Nurse", "Programmer", "Businessmann"]

names[1] = "Dereje"

print(names)
print(names[0])
print(names[1:3])
print(names[3:])

# extend)
names.extend(jobs)
# append
jobs.append("Jobless")
# insert
jobs.insert(3, "Driver")
# remove
jobs.remove("Nurse")
# clear
jobs.clear()
# pop
names.pop()
# index
names.index("Abebe")
# count
names.count("Almaz")
# sort
names.sort()
# reverse
names.reverse()
# copy
jobs = names.copy()

print(jobs)
print(names)
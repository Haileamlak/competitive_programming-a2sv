
my_file = open("python_track\\file_to_read.txt", )

file_lines = my_file.readlines()

for line in file_lines:
    print(line)

my_file.close()

my_file = open("python_track\\file_to_read.txt", "w")

my_file.write("Hungry and Foolish")

my_file.close()

with open("file1 (1).txt") as file_a:
        file_a_data=file_a.readlines()

with open("file2 (1).txt") as file_b:
        file_b_data=file_b.readlines()

result=[int(number) for number in file_a_data if number in file_b_data]

print(result)




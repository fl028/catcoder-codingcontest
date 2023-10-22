import os

input_folder = "Input"
output_folder = "Out"
fights = []
winners = []
input_files = ["level1_1.in","level1_2.in","level1_3.in","level1_4.in","level1_5.in"]
output_files = ["level1_1.out","level1_2.out","level1_3.out","level1_4.out","level1_5.out"]

def read_input_file(file_name):
    path_input_file = os.path.join(os.getcwd(), input_folder, file_name)
    with open(path_input_file) as file:
        lines = file.readlines()
        for index in range(len(lines)):
            if index == 0:
                print(lines[index])
            else:
                fights.append(lines[index].strip())

def get_winners():
    for element in fights:
        p1 = element[0]
        p2 = element[1]

        if p1 == p2:
            winners.append(element[0])
        elif p1 == "P" and p2 == "R":
            winners.append(element[0])
        elif p1 == "P" and p2 == "S":
            winners.append(element[1])
        elif p1 == "R" and p2 == "P":
            winners.append(element[1])
        elif p1 == "R" and p2 == "S":
            winners.append(element[0])
        elif p1 == "S" and p2 == "P":
            winners.append(element[0])
        elif p1 == "S" and p2 == "R":
            winners.append(element[1])
        else:
            raise Exception("false")


def write_output_file(file_name):
    path_output_file = os.path.join(os.getcwd(), output_folder, file_name)
    with open(path_output_file,'w+') as file:
        for index in range(len(winners)):
            file.write(winners[index]+'\n')

def clean():
    fights.clear()
    winners.clear()

# main
if __name__ == '__main__':
    for index in range(len(input_files)):
        read_input_file(input_files[index])
        get_winners()
        write_output_file(output_files[index])
        clean()
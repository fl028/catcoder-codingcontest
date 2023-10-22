import os

input_folder = "Input"
output_folder = "Out"
input_files = ["level2_1.in","level2_2.in","level2_3.in","level2_4.in","level2_5.in"]
output_files = ["level2_1.out","level2_2.out","level2_3.out","level2_4.out","level2_5.out"]

tournaments = []

def read_input_file(file_name):
    tournaments.clear()
    path_input_file = os.path.join(os.getcwd(), input_folder, file_name)
    with open(path_input_file) as file:
        lines = file.readlines()
        for index in range(len(lines)):
            if index == 0:
                print(lines[index])
            else:
                tournaments.append(lines[index].strip())

def get_winner(match):
    element = match

    if len(element) != 2:
        raise Exception("wrong len")

    p1 = element[0]
    p2 = element[1]

    if p1 == p2:
        return p1
    elif p1 == "P" and p2 == "R":
        return p1
    elif p1 == "P" and p2 == "S":
        return p2
    elif p1 == "R" and p2 == "P":
        return p2
    elif p1 == "R" and p2 == "S":
        return p1
    elif p1 == "S" and p2 == "P":
        return p1
    elif p1 == "S" and p2 == "R":
        return p2
    else:
        raise Exception("false")


def write_output_file(file_name, content):
    path_output_file = os.path.join(os.getcwd(), output_folder, file_name)
    with open(path_output_file,'a') as file:
        file.write(content+'\n')

def get_final_players(tournament):
    winners = ""

    for index in range(0,len(tournament),2):
        match = tournament[index] + tournament[index+1]
        winner = get_winner(match)
        winners = winners + winner

    return winners

# main
if __name__ == '__main__':
    for index in range(len(input_files)):
        read_input_file(input_files[index])

        #while len(winners) > 2:

        for tournament in tournaments:
            winners = tournament
            for round in range(2):
                winners = get_final_players(winners)
            #  p1 and p2
            write_output_file(output_files[index],winners)

import os
import random

input_folder = "Input"
output_folder = "Out"
#input_files = ["level3_example.in"]
#output_files = ["level3_example.out"]
input_files = ["level3_1.in","level3_2.in","level3_3.in","level3_4.in","level3_5.in"]
output_files = ["level3_1.out","level3_2.out","level3_3.out","level3_4.out","level3_5.out"]

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
                tournaments.append(parse_line_to_tournament_players(lines[index].strip()))

def parse_line_to_tournament_players(line):
    players = []

    parts = line.split()

    for element in parts:
        type = str(element[-1])
        count = int(element[:-1])

        for index in range(count):
            players.append(type)

    return players

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

def create_random_tournament_string(players):
    random.shuffle(players)
    tournament_string = "".join(players)
    return tournament_string

# main
if __name__ == '__main__':
    for index in range(len(input_files)):
        read_input_file(input_files[index])

        for players in tournaments:

            while True:
                tournament_string = create_random_tournament_string(players)
                winners = tournament_string
                for round in range(2):
                    winners = get_final_players(winners)

                if "S" in winners and "R" not in winners:
                    break

            write_output_file(output_files[index],tournament_string)

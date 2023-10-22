import os

input_folder = "Input"
output_folder = "OutTest"
tournaments = []
fights = []

input_files = ["level3_5.in","level3_4.in","level3_3.in","level3_2.in","level3_1.in"]
output_files = ["level3_5.out","level3_4.out","level3_3.out","level3_2.out","level3_1.out"]

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
        for elem in content:
            file.write(elem+'\n')

def get_final_players(tournament):
    winners = ""

    for index in range(0,len(tournament),2):
        match = tournament[index] + tournament[index+1]
        winner = get_winner(match)
        winners = winners + winner

    return winners

def getNextIndex(tournament, type):
    return tournament.index(type)

def getMagicSequence3R1P(tournament):
    result = ""
    Index_R = getNextIndex(tournament, "R")
    result += tournament.pop(Index_R)

    Index_R = getNextIndex(tournament, "R")
    result += tournament.pop(Index_R)

    Index_R = getNextIndex(tournament, "R")
    result += tournament.pop(Index_R)

    Index_P = getNextIndex(tournament, "P")
    result += tournament.pop(Index_P)

    return result

def getMagicSequenceRP(tournament):
    result = ""
    Index_R = getNextIndex(tournament, "R")
    result += tournament.pop(Index_R)

    Index_P = getNextIndex(tournament, "P")
    result += tournament.pop(Index_P)

    return result

def getMagicSequenceRX(tournament):
    result = ""
    Index_R = getNextIndex(tournament, "R")
    result += tournament.pop(Index_R)

    #wenn p -> dann p
    try:
        Index_P = getNextIndex(tournament, "P")
        result += tournament.pop(Index_P)
    #wenn s -> dann s
    except:
        Index_S = getNextIndex(tournament, "S")
        result += tournament.pop(Index_S)

    return result

def distribute_fighters(tournament):
    distribution = ""

    while tournament.count("R") >= 3 and tournament.count("P") >= 1:
        distribution += getMagicSequence3R1P(tournament)
    #2r -> RR PP
    if tournament.count("R") >= 2:
        #RP RS
        distribution += getMagicSequenceRP(tournament)

    #1r -> RP
    if tournament.count("R") >= 1:
        distribution += getMagicSequenceRX(tournament)

    distribution += "".join(tournament)

    return distribution

def parse_line_to_tournament_players(line):
    players = []

    parts = line.split()

    for element in parts:
        type = str(element[-1])
        count = int(element[:-1])

        for index in range(count):
            players.append(type)

    return players


# main
if __name__ == '__main__':

    for index in range(len(input_files)):
        read_input_file(input_files[index])
        output = []

        for tournament in tournaments:
            inital_winners = distribute_fighters(tournament)
            winners = inital_winners

            for round in range(2):
                winners = get_final_players(winners)

            if "S" not in winners:
                raise Exception("FALASCH!!!")

            if "R" in winners:
                raise Exception("FALASCH!!!")

            output.append(inital_winners)
        write_output_file(output_files[index], output)

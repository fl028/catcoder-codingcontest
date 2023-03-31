import os

content = ['Moin', 'Meister']
input_folder = "Inputs"
output_folder = "Outputs"
file_input_name = "Input.txt"
file_output_name = "Output.txt"
path_input_file = os.path.join(os.getcwd(), input_folder, file_input_name)
path_output_file = os.path.join(os.getcwd(), output_folder, file_output_name)

def read_input_file(path_input_file):
    with open(path_input_file) as file:
        lines = file.readlines()
        for index in range(len(lines)):
            print(lines[index])

def write_output_file(path_output_file,content):
    with open(path_output_file,'w+') as file:
        for index in range(len(content)):
            file.write(content[index]+'\n')

# main
if __name__ == '__main__':
    read_input_file(path_input_file)
    write_output_file(path_output_file,content)

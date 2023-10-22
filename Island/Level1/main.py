import os
#  ["level1_1.in","level1_2.in","level1_3.in","level1_4.in","level1_5.in"]
input_files = ["level1_1.in","level1_2.in","level1_3.in","level1_4.in","level1_5.in"]
base_folder_name = "Island"
level_folder_name = "Level1"
input_folder_name = "Input"
ouput_folder_name = "Output"
output = []

class Island():
    def __init__(self,filename) -> None:
        self.input_file_name = filename
        self.output_file_name = filename.split(".")[0] + ".out"
        self.tile_types_array = []
        self.search_cords = []
        self.map_2d = []
        self.size = -1
        self.size_search_cords = -1
        self.create_island_from_file()
    
    def create_island_from_file(self):
        print("Create Island from file")
        
        self.path_input_file = os.path.join(os.getcwd(),base_folder_name,level_folder_name,input_folder_name, self.input_file_name )
        with open(self.path_input_file) as file:
            lines = file.readlines()

            for index in range(len(lines)):
                #print(lines[index].strip())
                if index == 0:
                    #print("Map Size line")
                    self.size = int(lines[index].strip())
                elif index > 0 and index < self.size +1:
                    #print("Map line")
                    line = lines[index].strip()
                    line_chars = list(line)
                    self.map_2d.append(line_chars)
                elif index == self.size + 1:
                    #print("Cords Size line")
                    self.size_search_cords = int(lines[index].strip())
                else:
                    #print("Cords line")
                    line = lines[index].strip()
                    cords = line.split(",")
                    self.search_cords.append(cords)
    
    def show_island(self):   
        print("size: " + str(self.size))
        print("size_search_cords: " + str(self.size_search_cords))
        print("Map: " + str(self.map_2d))
        print("search_cords: " + str(self.search_cords))

    def show_map(self):
        """for index_y in range(len(self.map_2d)):
            for index_x in range(len(self.map_2d[index_y])):
                print("X: " + str(index_x) + " Y: " + str(index_y) + str(self.map_2d[index_y][index_x]))"""
        for y, row in enumerate(self.map_2d):
            for x, char in enumerate(row):
                print(f'({x},{y}) {char}', end=' ')
            print()

    def get_field_at_coordinates(self, x, y):
        print("Seraching for " + str(x) + " " + str(y))
        x = int(x)
        y = int(y)

        if 0 <= x < len( self.map_2d) and 0 <= y < len( self.map_2d[0]):
            return  self.map_2d[y][x] 
        else:
            raise Exception("Cords out of bounds")
        
    def get_type_of_cords(self):
        for cord in island.search_cords:
            tile_type = self.get_field_at_coordinates(cord[0],cord[1])
            self.tile_types_array.append(tile_type)

        print(self.tile_types_array)

    def save_output(self):
        self.path_output_file = os.path.join(os.getcwd(),base_folder_name,level_folder_name,ouput_folder_name, self.output_file_name)
        with open(self.path_output_file, 'w') as file:
            for row in self.tile_types_array:
                line = ' '.join(row)
                file.write(line + '\n')


# main
if __name__ == '__main__':
    for file in input_files:
        island = Island(file)
        #island.show_map()
        #island.show_island()
        island.get_type_of_cords()
        island.save_output()

        



import os

# ["level2_1.in"]
#  ["level2_1.in","level2_2.in","level2_3.in","level2_4.in","level2_5.in"]
input_files = ["level2_1.in","level2_2.in","level2_3.in","level2_4.in","level2_5.in"]
base_folder_name = "Island"
level_folder_name = "Level2"
input_folder_name = "Input"
ouput_folder_name = "Output"
output = []

class Island():
    def __init__(self,filename) -> None:
        self.input_file_name = filename
        self.output_file_name = filename.split(".")[0] + ".out"
        self.solution_array = []
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
                    line = lines[index].split(" ")
                    cords1 = line[0].strip().split(",")
                    cords2 = line[1].strip().split(",")
                    int_cords1 = [int(item) for item in cords1]
                    int_cords2 = [int(item) for item in cords2]
                    compare_cords = [int_cords1,int_cords2]
                    self.search_cords.append(compare_cords)
    
    def show_island_stats(self):   
        print("size: " + str(self.size))
        print("size_search_cords: " + str(self.size_search_cords))
        #print("Map: " + str(self.map_2d))
        print("search_cords: " + str(self.search_cords))

    def show_map(self):
        """for index_y in range(len(self.map_2d)):
            for index_x in range(len(self.map_2d[index_y])):
                print("X: " + str(index_x) + " Y: " + str(index_y) + str(self.map_2d[index_y][index_x]))"""
        for y, row in enumerate(self.map_2d):
            for x, char in enumerate(row):
                print(f'({x},{y}) {char}', end=' ')
            print()

    def show_map2(self):
        for row in self.map_2d:
            print(''.join(row))

    def get_field_at_coordinates(self, x, y):
        print("Seraching for " + str(x) + " " + str(y))
        x = int(x)
        y = int(y)

        if 0 <= x < len( self.map_2d) and 0 <= y < len( self.map_2d[0]):
            return  self.map_2d[y][x] 
        else:
            raise Exception("Cords out of bounds")
        
    def find_islands(self):
        islands = []
        rows, cols = len(self.map_2d), len(self.map_2d[0])
        visited = [[False] * cols for _ in range(rows)]

        for x in range(rows):
            for y in range(cols):
                if self.map_2d[y][x] == 'L' and not visited[y][x]:
                    island = set()
                    stack = [(x, y)]

                    while stack:
                        cx, cy = stack.pop()
                        if 0 <= cx < rows and 0 <= cy < cols and self.map_2d[cy][cx] == 'L' and not visited[cy][cx]:
                            visited[cy][cx] = True
                            island.add((cx, cy))

                            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                                stack.append((cx + dx, cy + dy))

                    islands.append(island)

        return islands

    def is_same_island(self, coord1, coord2):
        islands = self.find_islands()
        print(islands)

        coord1 = tuple(coord1)
        coord2 = tuple(coord2)
        
        for island in islands:
            if coord1 in island and coord2 in island:
                return True

        return False
    
    def check_all_cords(self):
        for cord_pair in self.search_cords:
            result = self.is_same_island(cord_pair[0], cord_pair[1])
            self.solution_array.append(result)


    def save_output(self):
        self.path_output_file = os.path.join(os.getcwd(),base_folder_name,level_folder_name,ouput_folder_name, self.output_file_name)
        with open(self.path_output_file, 'w') as file:
            for result in self.solution_array:
                if bool(result):
                    file.write("SAME" + '\n')
                else:
                    file.write("DIFFERENT" + '\n')


# main
if __name__ == '__main__':
    for file in input_files:
        island = Island(file)
        #island.show_map()
        #island.show_island_stats()
        island.check_all_cords()
        island.save_output()
        #island.show_map2()

        



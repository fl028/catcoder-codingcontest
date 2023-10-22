import os
import copy
# ["level3_1.in"]
#  ["level3_1.in","level3_2.in","level3_3.in","level3_4.in","level3_5.in"]
input_files = ["level3_1.in"]
base_folder_name = "Island"
level_folder_name = "Level3"
input_folder_name = "Input"
ouput_folder_name = "Output"
output = []

class Island():
    def __init__(self,filename) -> None:
        self.input_file_name = filename
        self.output_file_name = filename.split(".")[0] + ".out"
        self.solution_array = []
        self.sea_routes = []
        self.map_2d = []
        self.size = -1
        self.size_sea_routes = -1
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
                    self.size_sea_routes = int(lines[index].strip())
                else:
                    #print("Cords line")
                    sea_route = []
                    route = lines[index].split(" ")
                    for cord in route:
                        x_and_y = cord.strip().split(",")
                        int_cords = [int(item) for item in x_and_y]
                        cord_tuple = tuple(int_cords)
                        sea_route.append(cord_tuple)
                    self.sea_routes.append(sea_route)
    
    def show_island_stats(self):   
        print("size: " + str(self.size))
        print("size_sea_routes: " + str(self.size_sea_routes))
        print("sea_routes: " + str(self.sea_routes))
        print()

    def visits_all_sea_routes(self):
        for i, sea_route in enumerate(self.sea_routes):
            print(f"visits_all_sea_routes {i}")
            self.explorer_map = copy.deepcopy(self.map_2d)
            for cord in sea_route:
                x,y = cord
                self.set_visited_at_coordinates(x,y)
            
            is_searoute_intersected = self.check_is_searoute_intersected(sea_route)
            print(f"sea_routes {i} intersected: {is_searoute_intersected}")

    def check_is_searoute_intersected(self,sea_route):
        duplicated_cords = self.has_route_duplicated_cords(sea_route)
        rectangle_vs = self.check_vs_pattern_and_intersection(self.explorer_map,sea_route)
        print(f"duplicated_cords: {duplicated_cords} rectangle_vs: {rectangle_vs}")

        if (duplicated_cords == False) and (rectangle_vs == False):
            return False
        
        return True

    def do_segments_intersect(self,segment1_start, segment1_end, segment2_start, segment2_end):
        print(f"do_segments_intersect {segment1_start} {segment1_end} {segment2_start} {segment2_end}")
        # Check if two line segments intersect
        x1, y1 = segment1_start
        x2, y2 = segment1_end
        x3, y3 = segment2_start
        x4, y4 = segment2_end

        def orientation(p, q, r):
            val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
            if val == 0:
                return 0  # Collinear
            return 1 if val > 0 else 2  # Clockwise or Counterclockwise

        o1 = orientation((x1, y1), (x2, y2), (x3, y3))
        o2 = orientation((x1, y1), (x2, y2), (x4, y4))
        o3 = orientation((x3, y3), (x4, y4), (x1, y1))
        o4 = orientation((x3, y3), (x4, y4), (x2, y2))

        if o1 != o2 and o3 != o4:
            return True  # Segments intersect

        if o1 == 0 and self.is_on_segment((x1, y1), (x2, y2), (x3, y3)):
            return True

        if o2 == 0 and self.is_on_segment((x1, y1), (x2, y2), (x4, y4)):
            return True

        if o3 == 0 and self.is_on_segment((x3, y3), (x4, y4), (x1, y1)):
            return True

        if o4 == 0 and self.is_on_segment((x3, y3), (x4, y4), (x2, y2)):
            return True

        return False
    
    def is_on_segment(self, p, q, r):
        # Check if point q is on the line segment between p and r
        return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
                q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]))

    def check_vs_pattern_and_intersection(self, map, route):
        rows = len(map)
        if rows < 4:
            return False

        cols = len(map[0])
        if cols < 4:
            return False

        vs_coordinates = []
        for i in range(rows - 1):
            for j in range(cols - 1):
                if (map[i][j] == "V" and map[i][j + 1] == "V" and
                    map[i + 1][j] == "V" and map[i + 1][j + 1] == "V"):
                    vs_coordinates = [(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)]
                    break

        if not vs_coordinates:
            return False

        # Check if the sea routes intersect with the coordinates of the "V" pattern
        intersects = True  # Assume intersection until proven parallel
        parallel = True
        for i in range(len(route) - 1):
            for j in range(len(vs_coordinates) - 1):
                if not self.are_segments_parallel(route[i], route[i + 1], vs_coordinates[j], vs_coordinates[j + 1]):
                    parallel = False
                    break
            if not parallel:
                break
        if parallel:
            intersects = False

        return intersects

    def are_segments_parallel(self, seg1_start, seg1_end, seg2_start, seg2_end):
        print(seg1_start,seg1_end,seg2_start, seg2_end)
        x1, y1 = seg1_start
        x2, y2 = seg1_end
        x3, y3 = seg2_start
        x4, y4 = seg2_end

        return (x2 - x1) * (y4 - y3) == (y2 - y1) * (x4 - x3)

    def set_visited_at_coordinates(self, x, y):
        print("Visiting " + str(x) + " " + str(y))
        if 0 <= x < len( self.explorer_map) and 0 <= y < len(  self.explorer_map[0]):
             self.explorer_map[y][x] = "V"
        else:
            raise Exception("Cords out of bounds")
        
    def show_map(self):
        for row in self.explorer_map:
            print(''.join(row))

    def has_route_duplicated_cords(self,tuples_list):
        unique_tuples = set(tuples_list)

        # Check if there are duplicates by comparing the lengths
        if len(unique_tuples) < len(tuples_list):
            return True
        else:
            return False

# main
if __name__ == '__main__':
    for file in input_files:
        island = Island(file)
        island.show_island_stats()
        island.visits_all_sea_routes()
        #island.show_map()

        



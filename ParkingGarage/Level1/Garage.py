import os

class Garage:
    def __init__(self, file_input_name):
        self.parking_space = []
        self.parking_utilization = []
        self.file_input_name = file_input_name
        self._init_garage()
        self._simulate_parking()

    def __str__(self):
        return str(self.file_input_name) + " " + str(self.garage_size)

    def _init_garage(self):
        path = os.path.join(os.getcwd(),"Inputs",self.file_input_name)
        with open(path) as file:
            lines = file.readlines()
            for index in range(len(lines)):
                if index == 0:
                    self.garage_size = int(str(lines[index]).strip().split()[0])
                    self.expected_cars = int(str(lines[index]).strip().split()[1])
                if index == 1:
                    self.ticket_history = str(lines[index]).strip().split()

    def _simulate_parking(self):
        for ticket in self.ticket_history:
            self._handle_car(int(ticket))
            self._document_parking_utilization()

    def _handle_car(self,ticket):
        if not self._is_car_in_parking_space(abs(ticket)):
            # park
            self.parking_space.append(Car(abs(ticket)))
        else:
            self._car_leavs_parking_space(abs(ticket))


    def _is_car_in_parking_space(self, ticket_id):
        for car in self.parking_space:
            if car.car_id == ticket_id:
                return True
        return False

    def _car_leavs_parking_space(self, ticket_id):
        for car in self.parking_space:
            if car.car_id == ticket_id:
                car.state = CarState.OUT

    def _document_parking_utilization(self):
        current_utilization = 0
        for car in self.parking_space:
            if car.state == CarState.IN:
                current_utilization += 1
        self.parking_utilization.append(current_utilization)

    def get_highest_parking_utilization(self):
        self.parking_utilization.sort()
        return self.parking_utilization[-1]


class Car:
    def __init__(self,car_id):
        self.car_id = car_id
        self.state = CarState.IN

    def __str__(self):
        return str(self.car_id) + " " + str(self.state)

class CarState:
    IN = 1
    OUT = 2



# main
if __name__ == '__main__':
    inputs = ["input.1","input.2","input.3"]

    for item in inputs:
        garage = Garage(item)
        print(str(item) + " -> " + str(garage.get_highest_parking_utilization()))


        '''
        input.1 -> 6
        input.2 -> 15
        input.3 -> 50
        '''
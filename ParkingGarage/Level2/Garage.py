import os

class Garage:
    def __init__(self, file_input_name):
        self.parking_space = []
        self.parking_utilization = []
        self.parking_queue = []
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
            if len(self.parking_space) >= self.garage_size:
                # queue
                self.parking_queue.append(Car(abs(ticket)))
            else:
                # park
                self.parking_space.append(Car(abs(ticket)))
        else:
            self._car_leavs_parking_space(abs(ticket))
            self._refill_empty_parking_space_from_queue()


    def _is_car_in_parking_space(self, ticket_id):
        for car in self.parking_space:
            if car.car_id == ticket_id:
                return True
        return False

    def _car_leavs_parking_space(self, ticket_id):
        for index in range(len(self.parking_space)):
            if self.parking_space[index].car_id == ticket_id:
                leaving_car = self.parking_space.pop(index)
                break

    def _document_parking_utilization(self):
        self.parking_utilization.append([len(self.parking_space),len(self.parking_queue)])

    def get_highest_parking_utilization(self):
        self.parking_utilization.sort()
        return self.parking_utilization[-1]

    def _refill_empty_parking_space_from_queue(self):
        if len(self.parking_queue) > 0:
            first_car = self.parking_queue.pop(0)
            self.parking_space.append(Car(first_car.car_id))

class Car:
    def __init__(self,car_id):
        self.car_id = car_id

    def __str__(self):
        return str(self.car_id)




# main
if __name__ == '__main__':
    inputs = ["input.1","input.2","input.3","input.4","input.5"]

    for item in inputs:
        garage = Garage(item)
        print(str(item) + " -> " + str(garage.get_highest_parking_utilization()))


        '''
        nput.1 -> [6, 0]
        input.2 -> [10, 1]
        input.3 -> [10, 52]
        input.4 -> [4, 2]
        input.5 -> [200, 808]
        '''
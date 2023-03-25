import os
import math

class Garage:
    def __init__(self, file_input_name):
        self.available_parking_space_ids = []
        self.parking_space_prices = {}
        self.car_weights = {}
        self.parking_space = []
        self.parking_utilization = []
        self.parking_queue = []
        self.file_input_name = file_input_name
        self.total_revenue = 0
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
                    prices = str(lines[index]).strip().split()
                    for price_index in range(len(prices)):
                        self.available_parking_space_ids.append(price_index)
                        self.parking_space_prices[price_index] = prices[price_index]
                if index == 2:
                    weights = str(lines[index]).strip().split()
                    for weights_index in range(len(weights)):
                        self.car_weights[weights_index +1] = weights[weights_index]
                if index == 3:
                    self.ticket_history = str(lines[index]).strip().split()

    def _simulate_parking(self):
        for ticket in self.ticket_history:
            self._handle_car(int(ticket))
            self._document_parking_utilization()

    def _handle_car(self,ticket):
        if not self._is_car_in_parking_space(abs(ticket)):
            if len(self.parking_space) >= self.garage_size:

                if ticket > 0:
                    # enters queue
                    self.parking_queue.append(Car(abs(ticket),-1))
                else:
                    # leaves queue
                    for index in range(len(self.parking_queue)):
                        if self.parking_queue[index].car_id == abs(ticket):
                            leaving_car = self.parking_queue.pop(index)
                            break
            else:
                # park
                self.available_parking_space_ids.sort()
                self.parking_space.append(Car(abs(ticket),self.available_parking_space_ids.pop(0)))
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
                self.available_parking_space_ids.append(leaving_car.parking_space_id)
                self._calcualte_new_revenue(leaving_car)
                break

    def _calcualte_new_revenue(self, leaving_car):
        # (Gewicht des Autos / 100) * Preis pro 100 Kilogramm
        car_weight = int(self.car_weights[leaving_car.car_id])
        car_weight_rounded = self.roundup(car_weight)
        price_per_hundred_kg =int(self.parking_space_prices[leaving_car.parking_space_id])
        price_per_kg = price_per_hundred_kg/100
        parking_price = car_weight_rounded * price_per_kg
        self.total_revenue = int(self.total_revenue) + parking_price

    def roundup(self,x):
        return int(math.ceil(x / 100.0)) * 100

    def _document_parking_utilization(self):
        self.parking_utilization.append([len(self.parking_space),len(self.parking_queue)])

    def get_highest_parking_utilization(self):
        self.parking_utilization.sort()
        return self.parking_utilization[-1]

    def _refill_empty_parking_space_from_queue(self):
        if len(self.parking_queue) > 0:
            first_car = self.parking_queue.pop(0)
            self.available_parking_space_ids.sort()
            self.parking_space.append(Car(first_car.car_id, self.available_parking_space_ids.pop(0)))

    def get_revenue(self):
        return int(self.total_revenue)

class Car:
    def __init__(self,car_id,parking_space_id):
        self.car_id = car_id
        self.parking_space_id = parking_space_id

    def __str__(self):
        return str(self.car_id)




# main
if __name__ == '__main__':
    inputs = ["input.1","input.2","input.3","input.4","input.5"]

    for item in inputs:
        garage = Garage(item)
        print(str(item) + " -> " + str(garage.get_revenue()))


        '''
        input.1 -> 24
        input.2 -> 41
        input.3 -> 63
        input.4 -> 102
        input.5 -> 209378
        '''
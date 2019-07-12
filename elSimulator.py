# codding=utf-8
from random import randrange, choice

import logging
import threading
import time

from elevator import Elevator

class ElSimulator:
    def __init__(self, n, x):
        self.floor_number = n
        self.elevator_number = x
        self.elevator_list = []
        self.current_floor_request = None

    def __call__(self):
        # create elevators
        for i in range(self.elevator_number):
            elevator = Elevator(i)
            self.elevator_list.append(elevator)

    def request_simulation(self, n):
        floor_request = randrange(self.floor_number)
        call_type = choice(['outside_call', 'inside_call'])

        logging.info('request %d %s: floor request %d',n, call_type, floor_request)

        # choose elevator
        # elevator_number = randrange(self.elevator_number)
        # elevator = self.elevator_list[elevator_number]
        elevator = self.choose_elevator(floor_request, n)

        # move elevator with move time simulation
        if elevator.position != floor_request:
            if elevator.position < floor_request:
                direction = 'move_up'
            else:
                direction = 'move_down'
            # direction = choice(['move_up', 'move_down'])
            logging.info('%s elevator %d for request %d',direction, elevator.id, n)
            elevator.move(direction, call_type, floor_request)
            logging.info('stop elevator %d for request %d',elevator.id, n)

    def choose_elevator(self, cur_request, nrequest):
        elevator_list_free = [x for x in self.elevator_list if not x.locked or x.position == cur_request]
        elevator =min(elevator_list_free, key=lambda x:abs(x.position-cur_request))
        if elevator :
            elevator.locked = True
        logging.info('choose elevator %d which is at position %d for request %d',elevator.id, elevator.position, nrequest)
        return elevator

if __name__ == '__main__':

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    # initialize simulator
    elSimulator = ElSimulator(10, 4)

    # create elevators list
    elSimulator()

    # request simulation
    threads = list()
    for n_request in range(10):
        x = threading.Thread(target=elSimulator.request_simulation, args=(n_request,))
        threads.append(x)
        x.start()
        time.sleep(randrange(5))


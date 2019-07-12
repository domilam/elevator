from elevator import Elevator
from random import randrange, choice

elevator_list = list()

for i in range(10):
    elevator = Elevator(i)
    elevator_list.append(elevator)

for i in range(10):
    request_floor = randrange(10)
    elevator =min(elevator_list, key=lambda x:abs(x.position-request_floor))
    print('request floor {2} - elevator {0} at position {1}'.format(elevator.id, elevator.position, request_floor))
    elevator.position = request_floor

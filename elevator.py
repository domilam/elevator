# coding=utf-8
import time

class Elevator:
    def __init__(self, id):
        self.id = id
        self.position = 1
        self.direction = None
        self.call_type = None
        self.request_number = 0
        self.locked = False

    def move(self, direction, call_type, floor_request):
        self.direction = direction
        self.call_type = call_type
        self.request_number += 1

        # simulate move time
        if self.direction == 'move_up':
            step = 1
            shift = 1
        elif self.direction == 'move_down':
            step = -1
            shift = -1

        for m in range(self.position, floor_request+shift, step):
            time.sleep(0.5)
            self.position = m
            print('Elevator {} at floor {}'.format(self.id, self.position))
        
        self.direction = None
        self.call_type = None
        self.position = floor_request
        self.locked = False

    def goto_default_position(self):
        self.position = 1
        self.direction = None
        self.call_type = None

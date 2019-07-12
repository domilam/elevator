from elevator import Elevator
from elSimulator import ElSimulator
from random import randrange, choice

import unittest

class RandomTest(unittest.TestCase):
    def setUp(self):
        self.elevator_list = list()
        # initialize simulator
        self.elSimulator = ElSimulator(10, 4)

        # create elevators list
        self.elSimulator()
        self.elSimulator.elevator_list[1].position = 4
        self.elSimulator.elevator_list[3].position = 6



    def test_choose_elevator(self):
        select_elevator = self.elSimulator.choose_elevator(3, 0)        
        self.assertEqual(select_elevator.id, 1)

        select_elevator = self.elSimulator.choose_elevator(8, 0)        
        self.assertEqual(select_elevator.id, 3)

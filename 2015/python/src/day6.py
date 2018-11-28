#!/usr/bin/env python3
"""
Advent of Code 2015: Day #
toggle 936,774 through 937,775
turn off 116,843 through 533,934
turn on 950,906 through 986,993
"""
import os
from shared.readdayinput import readdayinput

class GridLights(object):

    def __init__(self, v2 = False):
        self.v2 = v2
        self.grid = self.make_grid()
        self.TASK_TO_FUNC = {
            'on': self.turn_on,
            'off': self.turn_off,
            'toggle': self.toggle,
            'on_v2': self.turn_on_v2,
            'off_v2': self.turn_off_v2,
            'toggle_v2': self.toggle_v2
        }

    def make_grid(self):
        grid = {}
        for y in range(1000):
            for x in range(1000):
                grid[(x, y)] = 0
        return grid

    def turn_on(self, coords):
        self.grid[coords] = 1
    
    def turn_off(self, coords):
        self.grid[coords] = 0

    def toggle(self, coords):
        state = self.grid.get(coords, 0)
        self.grid[coords] = 0 if state == 1 else 1

    def turn_on_v2(self, coords):
        self.grid[coords] += 1
    
    def turn_off_v2(self, coords):
        if self.grid[coords] > 0:
            self.grid[coords] -= 1

    def toggle_v2(self, coords):
        self.grid[coords] += 2

    def loop_and_do_task(self, corner_one, corner_two, f):
        for y in range(corner_one[1], corner_two[1] + 1):
            for x in range(corner_one[0], corner_two[0] + 1):
                f((x, y))

    def do_task(self, corner_one, corner_two, task):
        f = self.TASK_TO_FUNC[task]
        #print(corner_one, corner_two, task, f)
        self.loop_and_do_task(corner_one, corner_two, f)

    def string_to_coords(self, s):
        coords = s.split(',')
        x, y = int(coords[0]), int(coords[1])
        return (x, y)

    def parse_instructions_and_do(self, instruction):
        instruction_list = instruction.split(' ')
        corner_one = self.string_to_coords(instruction_list[-3])
        corner_two = self.string_to_coords(instruction_list[-1])
        task = instruction_list[0]
        if task == 'turn':
            task = instruction_list[1]
        if self.v2 == True:
            task += '_v2'
        #print(task, instruction_list)
        self.do_task(corner_one, corner_two, task)

    def on_lights_count(self):
        return sum(self.grid.values())

    def off_lights_count(self):
        return self.grid.values().count(0)


def first_half(dayinput):
    """
    first half solver:
    After following the instructions, how many lights are lit?
    """
    instructions = dayinput.split('\n')
    lights = GridLights()
    for instruction in instructions:
        lights.parse_instructions_and_do(instruction)
    return lights.on_lights_count()

def second_half(dayinput):
    """
    second half solver:
    What is the total brightness of all lights combined after following Santa's instructions?
    """
    instructions = dayinput.split('\n')
    lights = GridLights(True)
    for instruction in instructions:
        lights.parse_instructions_and_do(instruction)
    return lights.on_lights_count()

def app():
    """
    runs day application
    """
    dayinput = readdayinput()
    half_one = first_half(dayinput)
    print(half_one)
    half_two = second_half(dayinput)
    print(half_two)

if __name__ == "__main__":
    """
    MAIN APP
    """
    app()

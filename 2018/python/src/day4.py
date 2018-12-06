#!/usr/bin/env python3
"""
Advent of Code 2018: Day # 4
"""
import os
import collections
import dateutil.parser
from shared.readdayinput import readdayinput

def parse_all_data(lines):
    guards = collections.defaultdict(list)
    times = collections.defaultdict(int)
    for line in lines:
        time, action = line.split('] ')

        time = dateutil.parser.parse(time[1:])

        if action.startswith('Guard'):
            guard = int(action.split()[1][1:])
        elif action == 'falls asleep':
            start = time
        elif action == 'wakes up':
            end = time
            guards[guard].append((start.minute, end.minute))
            times[guard] += (end - start).seconds
    return guards, times

def first_half(dayinput):
    """
    first half solver:
    Find the guard that has the most minutes asleep.
    What minute does that guard spend asleep the most?

    What is the ID of the guard you chose multiplied by the minute you chose?
    """
    lines = dayinput.split('\n')
    guards, times = parse_all_data(sorted(lines))

    (sleepiest_guard, time) = max(times.items(), key=lambda i: i[1])
    (most_popular_minute, count) = max([
        (minute, sum(1 for start, end in guards[sleepiest_guard] if start <= minute < end))
    for minute in range(60)], key=lambda i: i[1])

    return sleepiest_guard * most_popular_minute

def second_half(dayinput):
    """
    second half solver:
    """
    lines = dayinput.split('\n')
    guards, _ = parse_all_data(sorted(lines))

    (sleepiest_guard, most_popular_minute, count) = max([
        (guard, minute, sum(1 for start, end in guards[guard] if start <= minute < end))
    for minute in range(60) for guard in guards], key=lambda i: i[2])

    return sleepiest_guard * most_popular_minute

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

#!/usr/bin/env python3
"""
creates template files
"""

def app():
    """
    runs day application
    """
    day = 10
    while day <= 25:
        filename = "day{}input.txt".format(day)
        with open(filename, mode='w', encoding='utf-8') as file_io:
            pass
        day += 1


if __name__ == "__main__":
    """
    MAIN APP
    """
    app()

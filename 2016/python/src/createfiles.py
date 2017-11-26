#!/usr/bin/env python3
"""
creates template files
"""

def app():
    """
    creates blank file for day#.py python files
    """
    day = 9
    while day <= 25:
        template = "template.py"
        with open(template, mode='r', encoding='utf-8') as file_io:
            template_text = file_io.read()
        filename = "day{}.py".format(day)
        with open(filename, mode='w', encoding='utf-8') as file_io:
            file_io.write(template_text)
        day += 1


if __name__ == "__main__":
    """
    MAIN APP
    """
    app()

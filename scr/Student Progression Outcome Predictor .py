
# Date:12/09/2023

from graphics import *

progress_count = 0
trailer_count = 0
exclude_count = 0
retriever_count = 0
inputs = []
all_inputs = []



def progression_outcome(num1, num2, num3):
    num_pass = int(num1 / 20)
    num_defer = int(num2 / 20)
    num_fail = int(num3 / 20)

    # Initialize counts
    num_01, num_02, num_03, num_04, num_05 = 0, 0, 0, 0, 0
    # Module outcome check
    if num_pass == 6:
        print("\n Progress")
        num_01 += 1
        num_05 += 1
        progression = "\n Progress"
    elif num_pass == 5:
        print("\n Progress(module trailer)")
        num_02 += 1
        num_05 += 1
        progression = "\n Progress(module trailer)"
    elif num_fail >= 4:
        print("\n Exclude")
        num_04 += 1
        num_05 += 1
        progression = "\n Exclude"
    else:
        print("\n Do not progress - module retriever")
        num_03 += 1
        num_05 += 1
        progression = "\n Module Retriever"
    inputs = [progression, num1, num2, num3]
    all_inputs.append(inputs)

    return num_01, num_02, num_03, num_04, num_05


def draw_text(win, content, size, color, x, y):
    text = Text(Point(x, y), content)
    text.setSize(size)
    text.setTextColor(color)
    text.draw(win)


def text_number(win, content, height, size, color, x, y):
    text = Text(Point(x + 45, (y - height * 20) - 15), content)
    text.setSize(size)
    text.setTextColor(color)
    text.draw(win)


def draw_bar(win, label, height, color, x, y):
    # Create the filled bar
    bar = Rectangle(Point(x, y), Point(x + 90, y - height * 20))
    bar.setFill(color)
    bar.draw(win)
    # Create and draw the text
    text = Text(Point(x + 45, y + 20), f"{label}")
    text.draw(win)


def outline(win, x, y):
    # Draw a line
    line = Line(Point(x, y), Point(x + 450, y))
    line.setWidth(3)
    line.draw(win)


def render_graph(progress, trailer, retriever, exclude, total, add_text1, add_text2, a, b):
    win = GraphWin("Progression Outcome Graph", 550, 600)
    win.setBackground("white")

    draw_bar(win, "Progress", progress, "light green", 100, 500)
    draw_bar(win, "Trailer", trailer, "yellow green", 200, 500)
    draw_bar(win, "Retriever", retriever, "olive", 300, 500)
    draw_bar(win, "Exclude", exclude, "pink", 400, 500)

    # Add additional text
    draw_text(win, add_text1, 13, "black", 150, 550)
    draw_text(win, total, 13, "black", 225, 550)
    draw_text(win, add_text2, 19, "black", 150, 50)

    text_number(win, progress, progress, 12, "black", 100, 500)
    text_number(win, trailer, trailer, 12, "black", 200, 500)
    text_number(win, retriever, retriever, 12, "black", 300, 500)
    text_number(win, exclude, exclude, 12, "black", 400, 500)

    outline(win, a, b)#bar line
    
def get_user_input():
    #pass mark check
    i = True
    while i:
        pass_mark = input("Please enter your credits at pass:")
        try:
            pass_mark = int(pass_mark)
        except ValueError:
            print("\n Integer required.")#error output
            i=True
            continue
        if pass_mark in [0, 20, 40, 60, 80, 100, 120]:#checke range 0, 20, 40, 60, 80, 100,120
            i = False
        else:
            print("\n Out of range.")#error output
            i = True
    #defer mark check
    j = True
    while (j):
        defer_mark = input("Please enter your credits at defer:")
        try:
            defer_mark = int(defer_mark)
            j = False
        except ValueError:
            print("\n Integer required.")#error output
            j = True
            continue
        if defer_mark in [0, 20, 40, 60, 80, 100, 120]:#checke range 0, 20, 40, 60, 80, 100,120
            j = False
        else:
            print("\n Out of range.")#error output
            j = True

    #fail mark check
    k= True
    while (k):
        fail_mark = input("Please enter your credits at fail:")
        try:
            fail_mark = int(fail_mark)
            k = False
        except ValueError:
            print("\n Integer required.")#error output
            k = True
            continue
        if fail_mark in [0, 20, 40, 60, 80, 100, 120]:#checke range 0, 20, 40, 60, 80, 100,120
            k = False
        else:
            print("\n Out of range.")#error output
            k = True
    return pass_mark, defer_mark, fail_mark


#Re enter all the marks again check
z = True
while (z):
    cumulative_counts = {'Progress': 0, 'Trailer': 0, 'Retriever': 0, 'Exclude': 0, 'Total': 0}
    print("part 1")

    #total check
    t = True
    while (t):
        pass_mark, defer_mark, fail_mark = get_user_input()
        
        if pass_mark + defer_mark + fail_mark != 120:
            print("\n Total incorrect.")
            t = True
        else:
            a1, a2, a3, a4, a5 = progression_outcome(pass_mark, defer_mark, fail_mark)
            cumulative_counts['Progress'] += a1
            cumulative_counts['Trailer'] += a2
            cumulative_counts['Retriever'] += a3
            cumulative_counts['Exclude'] += a4
            cumulative_counts['Total'] += a5
            print("")
            
            w = True
            while w:
                next_outcome = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")#loop input Y or Q
                if next_outcome == "y":
                    print("")
                    w = False
                    t = True
                elif next_outcome == "q":
                    print("")

                    # Render the graph with updated counts
                    render_graph(cumulative_counts['Progress'], cumulative_counts['Trailer'],
                                 cumulative_counts['Retriever'], cumulative_counts['Exclude'],
                                 cumulative_counts['Total'], "outcomes in total:","Histrogram Results",50,500)#call histogram text

                    w = False
                    t = False
                else:
                    print(" Invalid response. Try again.")
                    w = True

    print("\nPart 2 :\n")

    for data in all_inputs:
        print(data[0], "-", data[1], ",", data[2], ",", data[3])
    print("\nPart 3 :\n")

    with open("Programme_Inputs.txt", "w") as file:
        for data in all_inputs:
            file.write(f"{data[0]} - {data[1]} , {data[2]} , {data[3]}\n")

    with open("Programme_Inputs.txt", "r") as file:
        file_data = file.read()

    (file_data)
    z = False

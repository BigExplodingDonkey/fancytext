rich_text = ""
text = input("What do you want your text to say? ")
print(" ")
def return_color_code(color_check):
    if color_check == "red":
        return "#ff0000"
    if color_check == "orange":
        return "#FF7600"
    if color_check == "yellow":
        return "#FFFF00"
    if color_check == "green":
        return "#00FF00"
    if color_check == "cyan":
        return "#00FFFF"
    if color_check == "blue":
        return "#0000FF"
    if color_check == "purple":
        return "#9D00FF"
    if color_check == "pink":
        return "#FF10F0"
    if color_check == "white":
        return "#FFFFFF"
    if color_check == "black":
        return "#000000"
color_question = input("Do you want your text to have a color? ")
print(" ")
if (str(color_question).lower()) == "yes":
    color = input("What color do you want your text to be? (choices: red, orange, yellow, green, cyan, \nblue, purple, pink, white, black) ")
    rich_text = "<font color=\"" + str(return_color_code(str(color))) + "\">" + str(text) + "</font>"
    print(" ")
stroke_question = input("Do you want your text to have an outline? ")
print(" ")
if (str(stroke_question).lower()) == "yes":
    stroke_color = input("What color outline do you want on your text? (choices: red, orange, yellow, green, cyan,\nblue, purple, pink, white, black) ")
    print(" ")
    stroke_thickness = input("How thick do you want the outline to be? (A number 1-5) ")
    print(" ")
    if (str(color_question).lower()) == "yes":
        rich_text = "<stroke color=\"" + str(return_color_code(str(stroke_color))) + "\" " + "thickness=\"" + str(stroke_thickness) + "\">" + str(rich_text) + "</stroke>"
    if (str(color_question).lower()) == "no":
        rich_text = "<stroke color=\"" + str(return_color_code(str(stroke_color))) + "\" " + "thickness=\"" + str(stroke_thickness) + "\">" + str(text) + "</stroke>"
font_question = input("Do you want it to be a certain font? ")
print(" ")
if (str(font_question).lower()) == "yes":
    font = input("What font do you want your text to be? (fonts listed on\nhttps://developer.roblox.com/en-us/api-reference/enum/Font) ")
    print(" ")
    if font.islower():
        font = (str(font)).capitalize()
    if (str(color_question).lower()) == "yes" or (str(stroke_question).lower()) == "yes":
        rich_text = "<font face=\"" + str(font) + "\">" + rich_text + "</font>"
    if len(rich_text) == 0:
        rich_text = "<font face=\"" + str(font) + "\">" + text + "</font>"
size_question = input("Do you want to make your text have a certain size? \n(only works if you add this to other text) ")
print(" ")
if (str(size_question).lower()) == "yes":
    size = input("What size do you want your text to be? (A number 1-90) ")
    print(" ")
    if len(rich_text) == 0:
        rich_text = "<font size=\"" + str(size) + "\">" + str(text) + "</font>"
    if (str(color_question).lower()) == "yes" or (str(stroke_question).lower()) == "yes" or (str(font_question).lower()) == "yes":
        rich_text = "<font size=\"" + str(size) + "\">" + str(rich_text) + "</font>"
import pyperclip
pyperclip.copy(str(rich_text))
print("Fancy text here: ")
print(" ")
print(str(rich_text))
print(" ")
print("DISCLAIMER: If you did not answer with one of the listed colors, the code will not work.")

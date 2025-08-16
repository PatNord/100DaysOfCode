import colorgram

colors = colorgram.extract(r"C:\Users\Patrik\Documents\100DaysOfCode\hirst_painting\hirst.jpg", 30)
rgb_colors = []


for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color = (r,g,b)
    rgb_colors.append(color)

print(rgb_colors)
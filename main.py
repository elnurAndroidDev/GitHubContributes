from tkinter import *
import calendar

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

root = Tk()
window_width = 300
window_height = 300
root.title("Git activity")
root.geometry(f"{window_width}x{window_height}")


canvas = Canvas(bg="white", width=window_width, height=window_width)
canvas.pack(anchor=CENTER, expand=1)

sq_size = 30
year = 2025
month = 1
weeks = calendar.monthcalendar(year, month)
x = 0
y = 0
for w in weeks:
    for day in w:
        if day != 0:
            canvas.create_rectangle(x, y, x + sq_size, y + sq_size)
        y = y + sq_size
    x = x + sq_size
    y = 0

root.mainloop()
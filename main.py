from tkinter import *
import calendar

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

root = Tk()
window_width = 1000
window_height = 1000
root.title("Git activity")
root.geometry(f"{window_width}x{window_height}")


canvas = Canvas(bg="white", width=window_width, height=window_width)
canvas.pack(fill=BOTH, expand=True)

sq_size = 30
year = 2026
month = 1
x = 10
y = 10
for month in range(1, 13):
    weeks = calendar.monthcalendar(year, month)
    for w in weeks:
        for day in w:
            if day != 0:
                canvas.create_rectangle(x, y, x + sq_size, y + sq_size)
            y = y + sq_size
        x = x + sq_size
        y = 10

root.mainloop()
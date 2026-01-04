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
gap = 10
year = 2027
month = 1
x = 50
y = 50
for month in range(1, 13):
    weeks = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]
    canvas.create_text(x + (7 * sq_size) / 2, y - 10, text=month_name, font=("Arial", 16))
    for w in weeks:
        for day in w:
            if day != 0:
                canvas.create_rectangle(x, y, x + sq_size, y + sq_size)
            y = y + sq_size
        x = x + sq_size
        y = 50
    x = x + gap

root.mainloop()
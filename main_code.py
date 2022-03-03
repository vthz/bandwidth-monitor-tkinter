import time
import psutil
from tkinter import *
from tkinter.ttk import *

prev_recv = psutil.net_io_counters().bytes_recv
prev_sent = psutil.net_io_counters().bytes_sent
prev_total = prev_recv + prev_sent

root = Tk()
root.title("Band Width Monitor")
root.geometry("400x40")
monitor_label = Label(root, font=("calibri", 20),
                      background="grey",
                      foreground="black")
# root.wm_attributes('-type', 'splash')


def update():
    global prev_recv, prev_sent, prev_total

    curr_recv = psutil.net_io_counters().bytes_recv
    curr_sent = psutil.net_io_counters().bytes_sent
    curr_total = curr_recv + curr_sent

    change_recv = curr_recv - prev_recv
    change_sent = curr_sent - prev_sent
    change_total = curr_total + prev_total

    change_recv /= 1024 * 1024
    change_sent /= 1024 * 1024
    change_total /= 1024 * 1024

    string = f"R:{change_recv:.2f}MB|S:{change_sent:.2f}MB|T{change_total:.2f}MB"

    prev_recv = curr_recv
    prev_sent = curr_sent
    prev_total = curr_total

    monitor_label.config(text=string)
    monitor_label.after(1000, update)


monitor_label.pack(anchor="center")
update()
mainloop()

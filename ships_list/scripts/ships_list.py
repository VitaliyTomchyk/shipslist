# #!/usr/bin/env python3
# from ships_list.ships_list.ships_list import ships_list
# from ships_list.cli.cli import parcer


# def main():
#     parced_result = parcer()
#     ships_list(parced_result)


# if __name__ == '__main__':
#     main()

import tkinter as tk
# from tkinter import messagebox


def calculate_duration():
    try:
        leg_length = float(leg_entry.get())
        speed = float(speed_entry.get())
        wf = int(wf_entry.get())

        duration = leg_length / speed / 24 * (1 + wf / 100)
        result.set(f"Duration: {duration:.2f} days")
    except ValueError:
        result.set("Invalid input")


root = tk.Tk()
root.title("Leg Duration Calculator")

# Create input fields
leg_label = tk.Label(root, text="Length of Leg, nm:")
leg_entry = tk.Entry(root)
speed_label = tk.Label(root, text="Speed, kn:")
speed_entry = tk.Entry(root)
wf_label = tk.Label(root, text="WF, % (1-100):")
wf_entry = tk.Entry(root)

# Create button
calculate_button = tk.Button(
    root,
    text="Calculate Duration",
    command=calculate_duration)

# Create label to display result
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)

# Layout
leg_label.pack()
leg_entry.pack()
speed_label.pack()
speed_entry.pack()
wf_label.pack()
wf_entry.pack()
calculate_button.pack()
result_label.pack()

# Make the window full-screen
root.attributes('-fullscreen', True)

root.mainloop()

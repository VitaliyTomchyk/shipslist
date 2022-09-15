import tkinter


def open_txt_file(file):
    window = tkinter.Tk()
    window.geometry("1000x770")

    text = tkinter.Text(window, width=100, height=30, font=("Helvetica", 16))
    text_file = open(file, 'r')
    template = text_file.read()
    text.insert(tkinter.END, template)
    text_file.close()
    text.grid(columnspan=2)

    save_button = tkinter.Button(
        window,
        text="Save changes.",
        padx=30,
        pady=10,
        bg="grey",
        command=lambda: save_txt(
            file,
            text))
    save_button.grid(row=1, column=0)

    exit_button = tkinter.Button(window, text="Close window", bg="grey",
                                 command=window.destroy)
    exit_button.grid(row=1, column=1)

    window.mainloop()


def save_txt(file, text):
    text_file = open(file, 'w')
    text_file.write(text.get(1.0, tkinter.END))
    text_file.close()
    print("New template text has been saved.")

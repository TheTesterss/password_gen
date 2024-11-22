import tkinter
from genPassword import genPassword

# ? Starts the main loop.
def main() -> None:
    window = tkinter.Tk()
    window.title("Password Generator.")
    window.geometry("330x520")
    
    loadContent(window)
    
    window.mainloop()

# ? Adds every content
def loadContent(window: tkinter.Tk) -> None:
    global result_text, password_length_input, includes_numbers_input, includes_punctuation_input, includes_uppers_input, includes_numbers_int, includes_punctuation_int, includes_uppers_int
    # ? Text & Input for the password length
    password_length = tkinter.Label(window, text="Password length:", width=20, font=("sans-serif", 20))
    password_length.grid(row=0, column=0)
    password_length_input = tkinter.Entry(window)
    password_length_input.grid(row=1, column=0)
    
    # ? Text & CheckBox for the uppers acceptance
    includes_uppers = tkinter.Label(window, text="Includes uppers:", width=20, font=("sans-serif", 20))
    includes_uppers.grid(row=2, column=0)
    includes_uppers_int = tkinter.IntVar()
    includes_uppers_input = tkinter.Checkbutton(window, height=2, variable=includes_uppers_int, onvalue=1, offvalue=0)
    includes_uppers_input.grid(row=3, column=0)
    
    # ? Text & CheckBox for the numbers acceptance
    includes_numbers = tkinter.Label(window, text="Includes numbers:", width=20, font=("sans-serif", 20))
    includes_numbers.grid(row=4, column=0)
    includes_numbers_int = tkinter.IntVar()
    includes_numbers_input = tkinter.Checkbutton(window, height=2, variable=includes_numbers_int, onvalue=1, offvalue=0)
    includes_numbers_input.grid(row=5, column=0)
    
    # ? Text & CheckBox for the punctuation acceptance
    includes_punctuation = tkinter.Label(window, text="Includes punctuation:", width=20, font=("sans-serif", 20))
    includes_punctuation.grid(row=6, column=0)
    includes_punctuation_int = tkinter.IntVar()
    includes_punctuation_input = tkinter.Checkbutton(window, height=2, variable=includes_punctuation_int, onvalue=1, offvalue=0)
    includes_punctuation_input.grid(row=7, column=0)
    
    # ? Button
    button = tkinter.Button(window, text="Calcul", width=10, font=("sans-serif", 20))
    button.grid(row=8, column=0)
    button.bind("<Button-1>", generation)
    
    # ? Result
    result = tkinter.Label(window, text="Result:", width=20, height=2, font=("sans-serif", 20))
    result.grid(row=9, column=0)
    result_text = tkinter.Label(window, text="", width=20, font=("sans-serif", 20))
    result_text.grid(row=10, column=0)

# ? Event when the button to generate is pressed.
def generation(e) -> None:
    global result_text, password_length_input, includes_numbers_input, includes_punctuation_input, includes_uppers_input, includes_numbers_int, includes_punctuation_int, includes_uppers_int
    
    password = genPassword(
        int(password_length_input.get()), 
        True if includes_uppers_int.get() == 1 else 0, 
        True if includes_numbers_int.get() == 1 else 0, 
        True if includes_punctuation_int.get() == 1 else 0
    )
    result_text.config(text=password)
    
    # ? Deselects every check box once the button is pressed.
    if includes_numbers_int.get():
        includes_numbers_input.deselect()
    if includes_punctuation_int.get():
        includes_punctuation_input.deselect()
    if includes_uppers_int.get():
        includes_uppers_input.deselect()

main()
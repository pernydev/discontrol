import tkinter as tk
import sys

popup = tk.Tk()
popup.wm_title("WARNING!")

label = tk.Label(popup, text="The file you just opened is a RAT virus designed for educational purposes.")
label.pack(side="top", fill="x", pady=10)

cancel_button = tk.Button(popup, text="Cancel", command=sys.exit)
cancel_button.pack()

continue_button = tk.Button(popup, text="Continue (Giving access to your computer)", command=popup.destroy)
continue_button.pack()

popup.mainloop()

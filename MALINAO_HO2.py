import tkinter as tk

window = tk.Tk()
window.title("Kenneth's Profile")
window.geometry("600x600")
window.resizable(True,True)
window.config(bg="pink")

label=tk.Label(window, text ="Student Profile", font=("Arial", 32,"bold"), fg="black", bg="pink", anchor="s")
label.pack(padx=(10),pady=(20))
label=tk.Label(window, text="Name: Kenneth Cruzado Malinao", font=("Arial", 14,"bold"), fg="black", bg="pink")
label.pack(padx=(10), pady=(10), anchor="w")
label=tk.Label(window, text="Age: 20", font=("Arial", 14,"bold"), fg="black", bg="pink")
label.pack(padx=(10), pady=(10), anchor="w")
label=tk.Label(window, text="Course: BSIT 1-C", font=("Arial", 14,"bold"), fg="black", bg="pink")
label.pack(padx=(10), pady=(10), anchor="w")
label=tk.Label(window, text="Birthday: June 25, 2005", font=("Arial", 14,"bold"), fg="black", bg="pink")
label.pack(padx=(10), pady=(10), anchor="w")
label=tk.Label(window, text="Motto:", font=("Arial", 14,"bold"), fg="black", bg="pink")
label.pack(padx=(10), pady=(10), anchor="w")
label=tk.Label(window, text="     Life is a gamble so play it wisely.", font=("Time New Roman", 14,"italic"), fg="black", bg="pink")
label.pack(anchor="w")

window.mainloop()

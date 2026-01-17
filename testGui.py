# --- GUI VERSION ---
import tkinter as tk

# 1. The Function (The Logic)
# We define what happens strictly WHEN the button is clicked
def greet_user():
    user_name = entry_box.get()              # Get text from Entry widget [cite: 226]
    result_label.config(text=f"Hello, {user_name}!") # Update the Label

# 2. The Window (The Container) [cite: 118]
window = tk.Tk()
window.title("GUI Greeting App")
window.geometry("300x200") 

# 3. The Widgets (The Furniture)
# Label: Instructions [cite: 187]
instruction_label = tk.Label(window, text="What is your name?")
instruction_label.pack() 

# Entry: Input box [cite: 225]
entry_box = tk.Entry(window)
entry_box.pack()

# Button: Trigger [cite: 207]
# Notice command=greet_user (no parentheses!)
btn = tk.Button(window, text="Greet Me", command=greet_user) 
btn.pack()

chk = tk.Checkbutton(window, text="I agree to terms")
chk.pack()

var = tk.StringVar()
r1 = tk.Radiobutton(window, text="Option A", variable=var, value="A")
r2 = tk.Radiobutton(window, text="Option B", variable=var, value="B")
# var.pack()
# Label: Output area
result_label = tk.Label(window, text="")
result_label.pack()

# 4. The Loop (Keep window alive) [cite: 459]
window.mainloop()
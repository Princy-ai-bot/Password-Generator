import tkinter as tk
import random

# Full-screen GUI setup
root = tk.Tk()
root.title("Password Generator")
root.state('zoomed')  # Makes the window full screen

# Title
title = tk.Label(root, text="Password Generator", font=("Arial", 36), pady=20)
title.pack()

# Input frame
input_frame = tk.Frame(root)
input_frame.pack(pady=50)

# Inputs for letters, numbers, and special characters
tk.Label(input_frame, text="Number of Letters:", font=("Arial", 20)).grid(row=0, column=0, padx=20, pady=10)
entry_letters = tk.Entry(input_frame, font=("Arial", 20), width=10)
entry_letters.grid(row=0, column=1, padx=20, pady=10)

tk.Label(input_frame, text="Number of Numbers:", font=("Arial", 20)).grid(row=1, column=0, padx=20, pady=10)
entry_numbers = tk.Entry(input_frame, font=("Arial", 20), width=10)
entry_numbers.grid(row=1, column=1, padx=20, pady=10)

tk.Label(input_frame, text="Number of Special Characters:", font=("Arial", 20)).grid(row=2, column=0, padx=20, pady=10)
entry_special = tk.Entry(input_frame, font=("Arial", 20), width=10)
entry_special.grid(row=2, column=1, padx=20, pady=10)

# Result label
lbl_result = tk.Label(root, text="", font=("Arial", 24), pady=20)
lbl_result.pack()

# Generate button logic (using your code directly)
def on_generate():
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    special = ['!', '@', '#', '$', '%', '^', '&', '*']
    
    try:
        n_letter = int(entry_letters.get())
        n_num = int(entry_numbers.get())
        n_special = int(entry_special.get())
        
        password = ("")

        for i in range(1, n_letter + 1):
            char = random.choice(letter)
            password += char

        for i in range(1, n_num + 1):
            char = random.choice(num)
            password += char

        for i in range(1, n_special + 1):
            char = random.choice(special)
            password += char

        password_list = list(password)
        random.shuffle(password_list)
        shuffled_password = ''.join(password_list)

        lbl_result.config(text=f"Generated Password: {shuffled_password}")
    except ValueError:
        lbl_result.config(text="Error: Please enter valid numbers.")

# Generate button
btn_generate = tk.Button(root, text="Generate Password", font=("Arial", 20), command=on_generate)
btn_generate.pack(pady=20)

# Exit button
btn_exit = tk.Button(root, text="Exit", font=("Arial", 20), command=root.quit)
btn_exit.pack(pady=50)

# Run the application
root.mainloop()

import tkinter as tk
from tkinter import simpledialog
from datetime import datetime
import sqlite3

# Function to simulate AI response (replace this with actual AI integration)
def get_ai_response(message):
    # This is where you'd integrate with an AI API to get a response
    return "This is a simulated response to: " + message

# Function to save conversation to database
def save_conversation(user_message, ai_response):
    conn = sqlite3.connect('chatbot_database.db')
    c = conn.cursor()
    c.execute("INSERT INTO conversations (user_message, ai_response) VALUES (?, ?)", (user_message, ai_response))
    conn.commit()
    conn.close()

# Function to handle sending messages
def send_message(event=None):
    user_message = user_input.get()
    ai_response = get_ai_response(user_message)
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, "You: " + user_message + "\n")
    chat_history.insert(tk.END, "AI: " + ai_response + "\n")
    chat_history.yview(tk.END)
    chat_history.config(state=tk.DISABLED)
    save_conversation(user_message, ai_response)
    user_input.delete(0, tk.END)

# Setting up the GUI
root = tk.Tk()
root.title("AI Chatbot")

chat_history = tk.Text(root, state=tk.DISABLED)
chat_history.pack(padx=10, pady=10)

user_input = tk.Entry(root)
user_input.pack(padx=10, pady=10, fill=tk.X)
user_input.bind("<Return>", send_message)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=10)

root.mainloop()

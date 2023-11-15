import tkinter as tk
from datetime import datetime
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class SelfImprovingAI:
    def __init__(self):
        self.skill_level = 1.0
        self.conversations = []
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))

    def learn(self, feedback):
        if feedback == 'positive':
            self.skill_level += 0.1
        elif feedback == 'negative':
            self.skill_level -= 0.1

    def preprocess_text(self, text):
        tokens = word_tokenize(text.lower())
        filtered_tokens = [self.lemmatizer.lemmatize(token) for token in tokens if token.isalnum() and token not in self.stop_words]
        return filtered_tokens

    def generate_response(self, message):
        # Basic response generation using bag-of-words
        user_tokens = self.preprocess_text(message)
        # Implement more sophisticated NLP techniques for better responses
        return f"AI: Received '{message}'. Skill Level: {self.skill_level}. Tokens: {user_tokens}"

    def log_conversation(self, user_input, ai_response):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.conversations.append(f"{now} - User: {user_input} | {ai_response}\n")

    def learn_from_logged_conversations(self, file_name):
        try:
            with open(file_name, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if "User:" in line:
                        user_input = line.split("User: ")[1].split(" | ")[0].strip()
                        self.learn(user_input)
        except FileNotFoundError:
            print("Logged data file not found.")

# GUI and Chat functionality remain the same as previous code...

# Update the ChatGUI class to include learning from the logged data
class ChatGUI:
    def __init__(self, master):
        # Existing code...

        self.ai = SelfImprovingAI()
        self.ai.learn_from_logged_conversations("conversation_log.txt")

    # Existing methods...

# Run the GUI
root = tk.Tk()
chat = ChatGUI(root)
root.mainloop()

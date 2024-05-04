import nltk
from collections import defaultdict
import random

class SelfDevelopingAI:
    def __init__(self):
        self.data = defaultdict(list)
        self.functions = {'greeting': ['Hello!', 'Hi there!', 'Hey!']}
    
    def collect_data(self, user_input):
        # Collect user input data
        self.data['user_input'].append(user_input)
    
    def update_functions(self):
        # Analyze collected data and update functions
        # For simplicity, let's just randomly select a response for each category
        for category, inputs in self.data.items():
            if category not in self.functions:
                self.functions[category] = []
            for user_input in inputs:
                if user_input not in self.functions[category]:
                    self.functions[category].append(user_input)
    
    def respond(self, user_input):
        # Generate response based on user input
        self.collect_data(user_input)
        self.update_functions()
        category = nltk.word_tokenize(user_input)[0]  # Assume the first word as the category
        if category in self.functions:
            return random.choice(self.functions[category])
        else:
            return "I'm not sure how to respond to that."
    
    def chat(self):
        print("AI: Hello! I'm your self-developing AI. You can start chatting with me.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'bye':
                print("AI: Goodbye!")
                break
            response = self.respond(user_input)
            print("AI:", response)

# Example usage
ai = SelfDevelopingAI()
ai.chat()

import random
from termcolor import colored

def generate_quote():
    quotes = [
        '“Be yourself, everyone else is already taken.”― Oscar Wilde',
        'Be the change that you wish to see in the world.”― Mahatma Gandhi'
              ]
    
    colors = ['red', 'blue', 'orange']
    
    quote = random.choice(quotes)
    color = random.choice(colors)
    
    print(colored(quote, color))
    return quote

if __name__ == "__main__":
    generate_quote()

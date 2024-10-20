import random

class MarkovChainTextGenerator:
    def __init__(self):
        self.chain = {}

    def train(self, text, n=2):
        words = text.split()
        for i in range(len(words) - n):
            key = tuple(words[i:i+n])
            next_word = words[i+n]
            if key not in self.chain:
                self.chain[key] = []
            self.chain[key].append(next_word)

    def generate(self, seed, size=50):
        seed_words = seed.split()
        n = len(seed_words)
        result = seed_words[:]
        current_tuple = tuple(seed_words[-n:])
        
        last_words = set(result[-5:])  # Track the last 5 words to avoid repetition

        for _ in range(size):
            next_words = self.chain.get(current_tuple)
            print(f"Current tuple: {current_tuple}, Next words: {next_words}")  # Debugging line
            if not next_words:
                break
            next_word = random.choice(next_words)

            # Avoid adding the same word consecutively
            while next_word in last_words:
                next_word = random.choice(next_words)

            result.append(next_word)
            last_words.add(next_word)
            if len(last_words) > 5:  # Keep the last 5 words in the set
                last_words.pop()

            current_tuple = tuple(result[-n:])

        return ' '.join(result)

# Sample usage with rich content
text = """
Markov chains are used to model random systems. This simple implementation generates text based on a given input prompt. 
Markov models can predict the next item in a sequence based on prior items. The algorithm chooses the next word based on prior words, using probabilities from a trained dataset.
They are particularly useful in scenarios where the future state depends only on the current state, not the sequence of events that preceded it. 
Applications of Markov chains include natural language processing, stock price prediction, and various fields of science and engineering.
This allows for the generation of human-like text, predictions of sequences, and simulations of various processes.
In addition, Markov chains can be utilized in game design, music generation, and even in art creation. 
By analyzing past data, we can create models that not only predict but also generate new and unique outputs based on learned patterns.
"""

generator = MarkovChainTextGenerator()
generator.train(text, n=2)  # Use n=2

# Seed prompt for text generation
seed = "Markov chains"  # Change the seed to something more common
generated_text = generator.generate(seed, size=50)
print(generated_text)

# Step 1: Importing the required library
from spellchecker import SpellChecker

# Step 2: Creating the app class
class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self, text):
        words = text.split()  # e.g. 'hello world' → ['hello', 'world']
        corrected_words = []

        for word in words:  
            correction = self.spell.correction(word) 
            if correction and correction != word.lower():
                print(f'Correcting "{word}" to "{correction}"')
                corrected_words.append(correction)  
            else:
                corrected_words.append(word)  

        return " ".join(corrected_words)  

    # Step 5: Running the app
    def run(self):
        print("\n--- Spell Checker ---")

        while True:
            text = input('Enter text to check (or type "exit" to quit): ')

            if text.lower() == "exit":
                print("Closing the program...")
                break

            corrected_text = self.correct_text(text)
            print(f"Corrected Text: {corrected_text}")  


# Step 6: Running the main program
if __name__ == "__main__":
    SpellCheckerApp().run()
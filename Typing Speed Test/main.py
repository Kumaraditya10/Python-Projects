import time
import random

# Function to calculate typing errors
def calculate_mistakes(para_test, user_test):
    error = 0
    # Iterating through the reference paragraph
    for i in range(len(para_test)):
        try:
            # Comparing characters at the same index
            if para_test[i] != user_test[i]:
                error += 1
        except:
            # If user text is shorter than reference, count missing chars as errors
            error += 1
    return error

# Function to calculate typing speed
def calculate_speed(time_start, time_end, user_input):
    time_delay = time_end - time_start
    time_round = round(time_delay, 2)
    # Speed is calculated as number of characters divided by time taken
    speed = len(user_input) / time_round
    return round(speed, 2)

if __name__ == '__main__':
    while True:
        # Prompt to start the test
        check = input("Ready to test your typing speed? (yes / no): ")
        
        if check.lower() == "yes":
            # List of reference sentences
            test_sentences = [
                "A quick brown fox jumps over the lazy dog.",
                "My name is Gaurav Prajapat and I am a Python developer.",
                "Welcome to WsCube Tech, the best place to learn coding."
            ]
            
            # Randomly pick a sentence for the test
            test_sentence = random.choice(test_sentences)
            
            print("\n***** Typing Speed Test *****")
            print(test_sentence)
            print("\n")
            
            # Recording start time before user input
            time_1 = time.time()
            user_test_input = input("Start Typing: ")
            # Recording end time after user completes typing
            time_2 = time.time()
            
            # Calculating speed and mistakes
            typing_speed = calculate_speed(time_1, time_2, user_test_input)
            typing_errors = calculate_mistakes(test_sentence, user_test_input)
            
            print(f"\nSpeed: {typing_speed} words/sec")
            print(f"Errors: {typing_errors}")
            
        elif check.lower() == "no":
            print("Thank you for visiting! Bye.")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
import random

def main():
    quotes = [
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
        "The way to get started is to quit talking and begin doing. - Walt Disney",
        "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
        "If life were predictable it would cease to be life, and be without flavor. - Eleanor Roosevelt",
        "If you look at what you have in life, you'll always have more. - Oprah Winfrey",
        "Life is what happens when you're busy making other plans. - John Lennon",
    ]

    while True:
        # Randomly select a quote
        quote = random.choice(quotes)
        print("\nHere's a random quote for you:")
        print(f"\"{quote}\"\n")

        user_input = input("Do you want another quote (y/[n])? ")
        if user_input.lower() != 'y':
            print("Goodbye! Have a great day!")
            break

if __name__ == "__main__":
    main()

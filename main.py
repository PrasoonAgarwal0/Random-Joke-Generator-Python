import urllib.request
import json
import sys

def print_banner():
    banner = """
    =======================================
         WELCOME TO RANDOM JOKE GENERATOR  
         MADE BY UNKNOWN PYTHON DEVELOPER
         INSTAGRAM : bloody_._prasoon
    =======================================
    """
    print(banner)

def fetch_random_joke():
    url = "https://official-joke-api.appspot.com/jokes/random"
    try:
        response = urllib.request.urlopen(url)
        joke_data = json.load(response)
        return "{} - {}".format(joke_data['setup'], joke_data['punchline'])
    except Exception as e:
        return "Failed to fetch a joke! Please check your internet connection. ({})".format(e)

def main():
    print_banner()
    while True:
        print("\n[1] Generate a Random Joke")
        print("[2] Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("\nHere's your joke:")
            print(fetch_random_joke())
        elif choice == '2':
            print("\nThank you for using Random Joke Generator. Goodbye!")
            sys.exit()
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()
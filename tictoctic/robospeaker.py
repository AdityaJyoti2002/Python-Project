import os

if __name__ == "__main__":
    print("welcome to RoboSpeaker 1.1 made by Aditya Jyoti")
    os.system(f"say 'welcome to RoboSpeaker 1.1 made by Aditya Jyoti'")
    while True:

        x = input("Enter what you want me to speaker: ")
        if x == "q":
            os.system("say 'bye bye Friends'")
            break

        Command = f"say {x}"
        
        os.system(Command)

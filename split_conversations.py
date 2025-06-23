import json 
import os 

if __name__ == "__main__":
    folder = input("Please select the folder containing your ChatGPT history:\n")
    filepath = os.path.join(folder, "conversations.json")
    

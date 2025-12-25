question = [
   {"question": "What is the capital of Algeria?", "answer": "Algiers"},
    {"question": "What is the capital of Brazil?", "answer": "brasilia"},
    {"question": "What is the capital of Canada?", "answer": "Ottawa"},
    {"question": "What is the capital of Denmark?", "answer": "Copenhagen"},
    {"question": "What is the capital of Egypt?", "answer": "Cairo"},
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the capital of Germany?", "answer": "Berlin"},
    {"question": "What is the capital of Hungary?", "answer": "Budapest"},
    {"question": "What is the capital of India?", "answer": "New Delhi"},
    {"question": "What is the capital of Japan?", "answer": "Tokyo"},
]

def ask_question(q):
    print(q["question"])
    answer = input("Your answer: ").lower()

    return answer == q["answer"].lower()

def quiz():
    score = 0
    for q in question:
        if ask_question(q) == True:
            score += 1
            print("Correct!")
        else:
            print("Wrong!")
    print(f"You got {score} out of {len(question)} questions correct.")

x= input("Do you want to play? [Y or N]") 
if x == "n" or x == "N" :
    exit()
else :
    quiz()





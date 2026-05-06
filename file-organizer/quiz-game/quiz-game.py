questions = [
    {
        "question": "Where Joe would most like to travel?",
        "choices": ["Beach", "Mountains", "City", "Countryside"],
        "answer": "Mountains"
    },
    {
        "question": "What kind of weather do you enjoy?",
        "choices": ["Sunny", "Snowy", "Rainy", "Cool fall"],
        "answer": "Sunny"
    },
    {
        "question": "What is your ideal vacation day?",
        "choices": ["Relaxing", "Exploring", "Trying new food", "Outdoor adventures"],
        "answer": "Outdoor adventures"
    }
]
score = 0 
for question in questions:
    print(question["question"])
    
    for i, choice in enumerate(question["choices"],1):
        print (f"{i}.{choice}")
    select = input("Pick an answer from 1-4:  ")
    if select not in["1","2","3","4"]:
        print("Pick a number between 1 and 4!")
        continue
    if question["choices"][int(select) -1] == question["answer"]:
        print("Awesome! 🎉")
        score += 1
    else:
        print(f"Wrong answer! The answer was {question['answer']}")

print(f"you got {score} out of {len(questions)} Correct!")
print("🌍 Welcome to the Travel Quiz!")
print("--------------------------------")
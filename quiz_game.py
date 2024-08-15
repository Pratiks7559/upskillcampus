import random

# List of questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["A. Gold", "B. Iron", "C. Diamond", "D. Platinum"],
        "answer": "C"
    }
]

def ask_question(question):
    """Ask a question and return if the user's answer is correct."""
    print(question["question"])
    for option in question["options"]:
        print(option)
    answer = input("Your answer (A, B, C, or D): ").upper()
    return answer == question["answer"]

def main():
    random.shuffle(questions)
    score = 0

    print("Welcome to the Quiz Game!")
    
    for question in questions:
        if ask_question(question):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}.")
        print()

    print(f"Quiz over! Your final score is {score}/{len(questions)}")

if __name__ == "__main__":
    main()

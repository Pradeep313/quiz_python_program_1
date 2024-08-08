

#define questions and answers
quiz_data = [
    {
        "question": "What is the capital of india?",
        "options": ["A) New Delhi", "B) London", "C) Berlin", "D) Madrid"],
        "correct_answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
        "correct_answer": "B"
    },
    {
        "question": "Who wrote Python Programming?",
        "options": ["A) Guido van Rossum", "B) Jane Austen", "C) Mark Twain", "D) J.K. Rowling"],
        "correct_answer": "A"
    }
]


def ask_question(question_data):

    #question print and ask

    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    answer = input("Your answer (A, B, C, or D): ").strip().upper()

    return answer


def check_answer(user_answer, correct_answer):

    #check corect answer

    return user_answer == correct_answer


def main():
    # starting score =0
    score = 0
    # total question calculate
    total_questions = len(quiz_data)

    for question_data in quiz_data:
        user_answer = ask_question(question_data)

        if check_answer(user_answer, question_data["correct_answer"]):
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {question_data['correct_answer']}.\n")

    print(f"Your final score is {score} out of {total_questions}.")


if __name__ == "__main__":
    main()

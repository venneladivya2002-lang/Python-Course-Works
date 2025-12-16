def run_quiz():
    questions = [
        {
            "question": "Which of the following creates an empty tuple?",
            "options": {
                "a": "()",
                "b": "[]",
                "c": "{}",
                "d": "set()"
            },
            "answer": "a"
        },
        {
            "question": "What is the output of print(10 % 3)?",
            "options": {
                "a": "3",
                "b": "1",
                "c": "0",
                "d": "10"
            },
            "answer": "b"
        },
        {
            "question": "Which keyword is used to create a class in Python?",
            "options": {
                "a": "struct",
                "b": "object",
                "c": "class",
                "d": "define"
            },
            "answer": "c"
        },
        {
            "question": "What is the output of print(type(5))?",
            "options": {
                "a": "<class 'float'>",
                "b": "<class 'int'>",
                "c": "<class 'str'>",
                "d": "<class 'bool'>"
            },
            "answer": "b"
        },
        {
            "question": "Which function is used to find the maximum value?",
            "options": {
                "a": "top()",
                "b": "max()",
                "c": "largest()",
                "d": "high()"
            },
            "answer": "b"
        },
        {
            "question": "What is the output of print('Hello' + 'World')?",
            "options": {
                "a": "Hello World",
                "b": "HelloWorld",
                "c": "Error",
                "d": "Hello+World"
            },
            "answer": "b"
        },
        {
            "question": "Which of the following is a mutable data type?",
            "options": {
                "a": "tuple",
                "b": "str",
                "c": "list",
                "d": "int"
            },
            "answer": "c"
        },
        {
            "question": "What does the continue statement do?",
            "options": {
                "a": "Stops the loop",
                "b": "Skips current iteration",
                "c": "Ends program",
                "d": "Restarts loop"
            },
            "answer": "b"
        },
        {
            "question": "What is the output of print(len([1, 2, 3, 4]))?",
            "options": {
                "a": "3",
                "b": "4",
                "c": "5",
                "d": "Error"
            },
            "answer": "b"
        },
        {
            "question": "Which operator is used for exponentiation?",
            "options": {
                "a": "^",
                "b": "**",
                "c": "//",
                "d": "%"
            },
            "answer": "b"
        },
        {
            "question": "Which keyword is used to exit a function?",
            "options": {
                "a": "exit",
                "b": "break",
                "c": "return",
                "d": "stop"
            },
            "answer": "c"
        },
        {
            "question": "What is the output of print(bool(1))?",
            "options": {
                "a": "False",
                "b": "0",
                "c": "True",
                "d": "None"
            },
            "answer": "c"
        },
        {
            "question": "Which method adds an element to a list?",
            "options": {
                "a": "add()",
                "b": "insert()",
                "c": "append()",
                "d": "push()"
            },
            "answer": "c"
        },
        {
            "question": "Which function converts integer to string?",
            "options": {
                "a": "int()",
                "b": "str()",
                "c": "float()",
                "d": "bool()"
            },
            "answer": "b"
        },
        {
            "question": "What is the output of print(5 == '5')?",
            "options": {
                "a": "True",
                "b": "False",
                "c": "Error",
                "d": "None"
            },
            "answer": "b"
        },
        {
            "question": "Which data type does set() create?",
            "options": {
                "a": "list",
                "b": "tuple",
                "c": "dict",
                "d": "set"
            },
            "answer": "d"
        },
        {
            "question": "What is the default return value of a function?",
            "options": {
                "a": "0",
                "b": "False",
                "c": "None",
                "d": "Error"
            },
            "answer": "c"
        },
        {
            "question": "Which loop runs until condition becomes False?",
            "options": {
                "a": "for",
                "b": "while",
                "c": "do",
                "d": "repeat"
            },
            "answer": "b"
        },
        {
            "question": "Which function is used to sort a list?",
            "options": {
                "a": "sort()",
                "b": "order()",
                "c": "arrange()",
                "d": "sequence()"
            },
            "answer": "a"
        },
        {
            "question": "What is the output of print(type(True))?",
            "options": {
                "a": "<class 'int'>",
                "b": "<class 'str'>",
                "c": "<class 'bool'>",
                "d": "<class 'float'>"
            },
            "answer": "c"
        }
    ]

    score = 0
    print("🧪 Welcome to the Python Quiz Game!\n")

    for i, q in enumerate(questions, start=1):
        print(f"Question {i}: {q['question']}")
        for key, value in q["options"].items():
            print(f"{key}) {value}")

        user_answer = input("Your answer (a/b/c/d): ").lower()

        if user_answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is '{q['answer']}'\n")

    print(f"🎯 Your Final Score: {score}/{len(questions)}")
    print("🎉 Well done! Keep practicing Python!")


run_quiz()


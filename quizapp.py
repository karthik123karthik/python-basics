import random

questions = [
    {
        "question":"Who is the founder of google ?",
        "options": ["A.sunder","B.Mark","C.Henry","D.joseph"],
        "Answer":"A"
    },
    {
        "question":"Who is the father of our Nation ?",
        "options": ["A.subhash chandrabose","B.Mahathma Gandhi","C.sardhar vallabhai patel","D.Narendra Modi"],
        "Answer":"B"
    },
    {
        "question":"Java has pointers ?",
        "options": ["A.No","B.Yes","C.none","D.dont known"],
        "Answer":"A"
    },
    {
        "question":"Python is _______ language ?",
        "options": ["A.Dynamic","B.Interpreted","C.Both A and B","D.None"],
        "Answer":"C"
    },
    {
        "question":"What is the age of UVCE collage?",
        "options": ["A.100 years","B.101 years","C.102 years","D.104years"],
        "Answer":"C"
    },
    {
        "question":"Who is the CM of karnataka?",
        "options": ["A.Basavarj bommai","B.shiva","C.siddarammiah","D.yogi"],
        "Answer":"A"
    }
]

score  = 0
while(len(questions)>0):
    i = questions.index(random.choice(questions))
    print(questions[i]["question"])
    print(questions[i]["options"][0],"   ",questions[i]["options"][1])
    print(questions[i]["options"][2],"   ",questions[i]["options"][3])
    print("Enter your answer -----",end=" ")
    n = input().upper()
    if( n == questions[i]["Answer"]):
        score+=5
        print("YESSSSSSS you are correct and score is",score)
    else:
        print("NOOOOOO wrong answer try again ans score is",score)
    questions.remove(questions[i])
    print("-------------------------------------------------------------------------------------------------")

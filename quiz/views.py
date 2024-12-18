from django.shortcuts import render, redirect
from django.urls import reverse

questions = {
    1: "What is the capital of France?",
    2: "What is the currency of Japan?",
    3: "What is the largest planet in our solar system?",
    4: "What is the currency of Russia?",
    5: "What is the highest mountain in the world?",
    6: "What is the largest ocean in the world?",
    7: "What is the national animal of Australia?",
    8: "What is the smallest country in the world?",
    9: "What is the world’s largest desert?",
    10: "What is the largest bird in the world?"
}

options = {
    1: ['Paris', 'London', 'Berlin', 'Madrid'],
    2: ['Dollar', 'Yen', 'Euro', 'Pound'],
    3: ['Jupiter', 'Saturn', 'Mars', 'Earth'],
    4: ['Dollar', 'Yen', 'Euro', 'Ruble'],
    5: ['Mount Everest', 'K2', 'Kangchenjunga', 'Lhotse'],
    6: ['Pacific Ocean', 'Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean'],
    7: ['Kangaroo', 'Koala', 'Emu', 'Tasmanian Devil'],
    8: ['Vatican City', 'Monaco', 'Nauru', 'San Marino'],
    9: ['Sahara', 'Gobi', 'Arabian', 'Kalahari'],
    10: ['Ostrich', 'Emu', 'Albatross', 'Penguin']
}

answers = {
    1: 'Paris',
    2: 'Yen',
    3: 'Jupiter',
    4: 'Ruble',
    5: 'Mount Everest',
    6: 'Pacific Ocean',
    7: 'Kangaroo',
    8: 'Vatican City',
    9: 'Sahara',
    10: 'Ostrich'
}

results = {}

def index(request, question_no):
    if request.method == 'POST' and question_no - 1 < len(questions) + 1:
        answer = request.POST.get('answer')
        results[question_no - 1] = answer

    if len(results) == len(questions): 
        correct_answers = 0
        for i in range(1, len(questions) + 1):
            if results[i] == answers[i]:
                correct_answers += 1
        return redirect(f'{reverse("game_result")}?score={correct_answers}&total_questions={len(questions)}')

    question = questions[question_no]
    option_list = options[question_no]
    return render(request, 'gamePortal.html', {'question_no': question_no, 'question': question, 'options': option_list})

def result(request):
    score = request.GET.get('score')
    total_questions = request.GET.get('total_questions')
    return render(request, 'result.html', {'score': score, 'total_questions': total_questions})

def retry(request):
    global results
    results = {} 

    return redirect('game_portal', question_no=1)

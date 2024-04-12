from django.http import request
from django.shortcuts import render 


def index(request):
    data={}
    try:
        number1 = int(request.GET['first_number'])
        number2 = int(request.GET['Second_number'])
        if request.GET['add'] == '+':
            ans = number1 + number2
        if request.GET['subtract'] == '-':
            ans = number1 - number2
        if request.GET['multiply'] == '*':
            ans = number1 * number2
        if request.GET['divide'] == '/':
            ans = int(number1 / number2)
        print(ans)
        data={
            'ans': ans
        }
        
    except:
        pass
    return render(request, 'index.html', data)
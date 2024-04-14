from django.http import request
from django.shortcuts import render 


def index(request):
    data={}
    try:
        number1 = int(request.GET['first_number'])
        number2 = int(request.GET['Second_number'])
        if request.GET.get('add') == '+':
            ans = number1 + number2
        elif request.GET.get('subtract') == '-':
            ans = number1 - number2
        elif request.GET.get('multiply') == '*':
            ans = number1 * number2
        elif request.GET.get('divide') == '/':
                ans = int(number1 / number2)
        data={
            'ans': ans
        }
        
    except:
        pass
    return render(request, 'index.html', data)
from django.shortcuts import render
import datetime

def test(request):
    time = datetime.datetime.now().time()
    return render(request, 'test.html', {"c_time": time})
from django.shortcuts import render,HttpResponse
import json
# Create your views here.
def index(request):
    x = request.GET
    print(x)

    return render(request, 'h2.html', {'qq':['aa','bb','cc', 'dd']})

def jq1(request):
    print('111')
    x = request.POST
    print(x)
    rt = {
        'qq': '123'
    }
    rt1 = json.dumps(rt)
    x = json.dumps(x)
    return HttpResponse(x)

def jq2(request):
    print('111')
    x = request.POST
    print(x)
    rt = {
        'qq': '123'
    }
    rt1 = json.dumps(rt, ensure_ascii=False)
    x = json.dumps(x)
    return HttpResponse(x)


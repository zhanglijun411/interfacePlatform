from django.shortcuts import render

# Create your views here.

def homePage(request):
    return render(request, 'base.html')

def interfaceTools(request):
    page_title = "接口请求工具"
    return render(request, 'interfaceTools.html', locals())

def send(request):
    method = request.POST.get('method')
    url = request.POST.get('url')
    header = request.POST.get('header')
    body = request.POST.get('body')

    print('method:', method)
    print('url:', url)
    print('header:', header)
    print('body:', body)

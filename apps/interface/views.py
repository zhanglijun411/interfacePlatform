from django.shortcuts import render

# Create your views here.

def homePage(request):
    return render(request, 'base.html')

def interfaceTools(request):
    page_title = "接口请求工具"
    return render(request, 'interfaceTools.html', locals())




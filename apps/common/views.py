from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

def pageinator(obj, page_num):
    paginator = Paginator(obj, 10)

    try:
        pageInfo = paginator.page(page_num)
    except PageNotAnInteger:
        pageInfo = paginator.page(1)
    except EmptyPage:
        pageInfo = paginator.page(paginator.num_pages)

    return pageInfo

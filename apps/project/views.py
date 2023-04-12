from django.shortcuts import render
from apps.project.models import NeedsCategory, Needs
from apps.common.views import pageinator

# Create your views here.

# 需求池视图
def needsView(request, page):
    need_name = request.POST.get('need_name', '')
    need_status = request.POST.get('need_status', '')
    need_category = request.POST.get('need_category', '')
    search_dict = dict()
    data = None
    need_category_name = NeedsCategory.objects.all().order_by('id') # 需求分类名称
    if request.method == 'GET':
        data = Needs.objects.all().order_by('-create_time')
    else:
        if need_name:
            search_dict['need_name'] = need_name
        if need_status:
            search_dict['need_status'] = need_status
        if need_category:
            search_dict['need_category'] = need_category
        data = Needs.objects.filter(**search_dict).order_by('-create_time') # 组合条件查询结果
    pageInfo = pageinator(data, page)   # 分页数据
    return render(request, 'project/needsManager.html', locals())

def projectView(request):
    pass



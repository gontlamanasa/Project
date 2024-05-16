from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'testapp/index.html')

from testapp.models import hydjobs
def hydjobs_view(request):
    jobs_list = hydjobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/hydjobs.html',my_dict)

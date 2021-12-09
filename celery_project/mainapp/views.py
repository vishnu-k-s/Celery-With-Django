from django.shortcuts import HttpResponse

from .tasks import test_func
#from celery_project.celery import  debug_task

# Create your views here.
def test(request):
    #call function in tasks
    #debug_task.delay()
    test_func.delay()
    return HttpResponse("Done")
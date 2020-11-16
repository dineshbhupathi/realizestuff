from django.shortcuts import render
from django.shortcuts import HttpResponse
# from Online_Users import Las
# import Online
# from django.contrib.admin.models import OnlineUserActivity
# Create your views here.
from online_users.models import OnlineUserActivity
def test(request):
    return HttpResponse("hello")


from datetime import timedelta
def online(request):
    user_activity_objects = OnlineUserActivity.get_user_activities(timedelta(seconds=1))
    users = (user for user in user_activity_objects)
    # for i in users:
    #     onlineusers = i.user
    return render(request,'test.html',context={"users":users})
# def home_page_view(request):
#     return render(request,'index.html')
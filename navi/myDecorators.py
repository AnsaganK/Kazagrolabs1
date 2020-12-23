from .models import *
from django.shortcuts import render

def hasGroups(groups = []):
    def has_groups(func):
        def wrapper(request,*args,**kwargs):
            #print("1")
            g = False
            for i in groups:
                for j in list(request.user.groups.all()):
                    if i==str(j):
                        g = True
            if g:
                #print('2')
                return func(request,*args,**kwargs)
            else:
                #print("3")
                return render(request,'403.html')

        return wrapper
    return has_groups


def writeUserActivity(User, name):
    Activity.objects.create(user=User,name=name)



#@hasGroups(groups = [1,"user",3,4,5,6])
#def red(request):
#    print('123')

'''
@hasPermissions(permissions = ["1","2","3","4","5"])
def blue(request):
    print("1234")
    '''
from django.contrib.auth.models import User

def UserGroups(request):
    user = request.user
    groups = user.groups.all()
    list_group = []
    for i in groups:
        list_group.append(i.name)
    return {"userGroups":list_group}
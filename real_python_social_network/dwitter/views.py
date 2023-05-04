from django.shortcuts import render
from dwitter.models import Profile, Dweet

def dashboard(request):
    return render(request, template_name="base.html")

def profile_list(request):
    profiles = Profile.objects.exclude(id=request.user.id) #Get all user profiles except for your own
    context = {'profiles':profiles}
    return render(request, template_name="dwitter/profile_list.html", context=context)

def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()

    elif request.method == "GET":
        pass
    
    context = {'profile':profile}
    return render(request, template_name="dwitter/profile.html", context=context)
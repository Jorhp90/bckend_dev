from django.shortcuts import render
from dwitter.models import Profile, Dweet

def dashboard(request):
    """simple base view"""
    return render(request, template_name="base.html")

def profile_list(request):
    """show a list of all profiles except for the user"""
    profiles = Profile.objects.exclude(id=request.user.id) #Get all user profiles except for your own
    context = {'profiles':profiles}
    return render(request, template_name="dwitter/profile_list.html", context=context)

def profile(request, pk):
    """list of followers and followed by
        follow/unfollow
        list of dweets; straight from the template
    """
    profile = Profile.objects.get(pk=pk) #get the logged user
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
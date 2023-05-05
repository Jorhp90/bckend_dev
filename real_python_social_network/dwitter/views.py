from django.shortcuts import render, redirect
from dwitter.models import Profile, Dweet
from dwitter.forms import DweetForm

def dashboard(request):
    """create dweets by form; show dweets using templates"""
    form = DweetForm(request.POST or None) #avoid duplicate instantiation of DweetForm or get and post
    #or boolean operator only evaluates the second argument if the first one is False
    # If POST request that includes any data, the request.POST QueryDict will contain your form submission data. 
    # The request.POST object now has a truthy value
    
    if request.method == "POST":
        if form.is_valid(): #compares submitted data 2 xP data defined in form and model restrictions
            dweet = form.save(commit=False) #still missing user entry, commit=False prevent committing entry to db yet            
            dweet.email = request.user
            dweet.save()
            return redirect("dwitter_app:dashboard_view") #app_name:view_name
    
    followed_dweets = Dweet.objects.filter(
        email__profile__in=request.user.profile.follows.all()
    ).order_by("-created_at")
        
    context = {"form":form, "dweets":followed_dweets}
    return render(request, template_name="dwitter/dashboard.html", context=context)

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
    
    context = {'profile':profile}
    return render(request, template_name="dwitter/profile.html", context=context)
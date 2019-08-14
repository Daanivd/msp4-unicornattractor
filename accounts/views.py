from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.db.models.signals import post_save
from accounts.forms import LoginForm, UserRegoForm, ProfileForm, UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import Profile
from accounts.forms import UserForm, ProfileForm

# Views
def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        registration_form = UserRegoForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()
            

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
                                     
                  
            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'You have successfully registered with UPS')
            
                return redirect(reverse('index'))
            else:
                messages.error(request, 'Unable to register your account at this time')
                
                
    else:
        registration_form = UserRegoForm()
    return render(request, 'registration.html', {
        'registration_form': registration_form})  
    
def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            

            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, 'Your username or password is incorrect')
    else:
        login_form = LoginForm()
    return render(request, 'login.html', {'login_form': login_form})   

@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, 'You have successfully been logged out')
    return redirect(reverse('index'))
    
@login_required
def user_profile(request):
    """The user's profile page"""
    user = User.objects.get(id=request.user.id)
    profile = user.profile
    # profile = user.profile.objects.get_or_create(instance=user)
    
        
    userForm = UserForm(instance=user)
    profileForm = ProfileForm(instance=profile)
    edit_profile(request)
    
    if request.method == 'GET':
        return render(request, 'profile.html', {'user': user, 'userForm':userForm, 'profileForm':profileForm})
    if request.method == 'POST':
        return redirect('edit_profile')
        
  
        
    
@login_required
def edit_profile(request):
    """
    Create a view that allows us to edit your profile
    """
    user = request.user
    profile = user.profile

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        userForm = UserForm(request.POST)
        profileForm = ProfileForm(request.POST)

        # check whether it's valid:
        if userForm.is_valid() and profileForm.is_valid():

            # Save User model fields
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()

            # Save Employee model fields
            profile.info = request.POST['info']
            profile.photo = request.POST['photo']
            profile.save() 
            
    # if a GET (or any other method): create a blank form
    else:
        userForm = UserForm(instance=user)
        profileForm = ProfileForm(instance=profile)
    
    return render(request, 'profile.html', {'userForm': userForm, 'profileForm': profileForm})
    



   
    
    
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout,login
from django.contrib.auth import authenticate
from django.urls import reverse
from django.http import HttpResponseRedirect
from register.models import Company
from register.models import Project
from register.models import UserProfile
from projects.models import Task
from core.models import Contactus
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from django.views.generic.edit import CreateView

# Create your views here.
@login_required(login_url='/core/login')
def index(request):
    return render(request, 'core/index.html')

@login_required(login_url='/core/login')
def dashboard(request):
    users = User.objects.all()
    active_users = User.objects.all().filter(is_active=True)
    companies = Company.objects.all()
    projects = Project.objects.all()
    tasks = Task.objects.all()
    context = {
        'users' : users,
        'active_users' : active_users,
        'companies' : companies,
        'projects' : projects,
        'tasks' : tasks,
    }
    return render(request, 'core/dashboard.html', context)

@login_required(login_url='/core/login')
def aboutus(request):
    return render(request,'core/aboutus.html')

@login_required(login_url='/core/login')
def contactus(request):
    return render(request,'core/contactus.html')



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            authenticated_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, authenticated_user)
            return redirect('core:index')
        else:
            return render(request, 'register/login.html', {'login_form':form})
    else:
        form = AuthenticationForm()
    return render(request, 'register/login.html', {'login_form':form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('core:index'))


def context(request): # send context to base.html
    # if not request.session.session_key:
    #     request.session.create()
    users = User.objects.all()
    users_prof = UserProfile.objects.all()
    if request.user.is_authenticated:
        try:
            users_prof = UserProfile.objects.exclude(
                id=request.user.userprofile_set.values_list()[0][0])  # exclude himself from invite list
            user_id = request.user.userprofile_set.values_list()[0][0]
            logged_user = UserProfile.objects.get(id=user_id)
            friends = logged_user.friends.all()
            context = {
                'users': users,
                'users_prof': users_prof,
                'logged_user': logged_user,
                'friends' : friends,
            }
            return context
        except:
            users_prof = UserProfile.objects.all()
            context = {
                'users':users,
                'users_prof':users_prof,
            }
            return context
    else:
        context = {
            'users': users,
            'users_prof': users_prof,
        }
        return context
    
def Contact2(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = {'form':form}
        if form.is_valid():
            form.save()
            created = True
            form = ContactForm()
            context = {
                'created' : created,
                'form' : form,
                       }
            return render(request, 'core/dashboard.html', context)
        else:
            return render(request, 'core/contactus.html', context)
    else:
        form = ContactForm()
        context = {
            'form' : form,
        }
        return render(request, 'core/contactus.html', context)
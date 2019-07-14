from django.shortcuts import render
from .models import Resource,Like,Teacher,Comment
from .forms import TeacherSignUpForm
from django.contrib.auth import login
from .models import User
from django.views.generic import CreateView, ListView, UpdateView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.http import HttpResponseRedirect

def viewAll(request):
    v=Resource.objects.get(all)
    context= {'file': f,
              } 
    return render(request, 'templates/view_all.html', context)


def ResourceDetail(request, resource_pk):
    resource = get_object_or_404(Resource, pk=resource_pk)
    comments = Comment.objects.filter(resource_id=resource.id)
    return render(request, 'resource.html', {'resource': resource,
    'comments' : comments })

    # context= {'name' : Resource.objects.get(resource_id=resource_id).name,
    #           'file': Resource.objects.get(resource_id=resource_id).file,
    #           'description': Description.objects.get(resource_id=resource_id).description,
    #           'comment': Comment.objects.filter(resource_id=resource_id),
    #           }
    # return render(request, 'templates/view_pdf.html', context)


def IndexView(request):
    return redirect('/learnovate/home/')


def like(request, resource_id):
    new_like, created = Like.objects.get_or_create(user=Teacher.objects.get(user=request.user), resource_id=resource_id)

def comment(request, resource_id):
    new_comment, created = Comment.objects.create(user=Teacher.objects.get(user=request.user), resource_id=resource_id)

def homeView(request):
    resources = Resource.objects.all()
    return render(request, 'home.html', {'resources': resources})

def view_list(request,user_id):
    v_list = Video_log.objects.filter(user_id=user_id)

def category_search(request,category):
    if name == r'^(decision) +' | name==r'^(Decision) +':
        data=Resource.objects.filter(name="Decision Making")
    if name==r'^(relation) +' | name==r'^(Relation) +':
        data=Resource.objects.filter(name="Relationships")
    if name==r'^(social) +' | name==r'^(Social) +':
        data=Resource.objects.filter(name="Social Awareness")
    if name==r'^(self) +' | name==r'^(Self) +':
        data=Resource.objects.filter(name="Self Awareness")

def topic_search(request,name):
    data=Resource.objects.filter(category=category)

class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect(reverse('learnovate:home'))

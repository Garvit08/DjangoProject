from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForms
from bloog.models import BlogPost

def home_page(request):
    my_title='Hello there'
    qs = BlogPost.objects.all()[:5]
    context = {"title":"Welome to Blogs","blog_list":qs}
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html',{'title':'aboutus','content':'How Are You'})


def ContactPage(request):
    form=ContactForms(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form=ContactForms()
    context = {'title':"Contact us","form": form}
    return render(request,"form.html",context)
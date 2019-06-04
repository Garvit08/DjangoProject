from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render,get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogModel

# Create your views here.

def blog_post_details_view(request, slug):
    #obj = BlogPost.objects.filter(slug=slug)
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_details_page.html'
    context ={'object_list':obj}
    return render(request,template_name,context)

def blog_post_list_view(request):
    qs = BlogPost.objects.all()
    template_name='blog_post_list_page.html'
    context={'object_list':qs}
    return render(request,template_name,context)

# @login_required
@staff_member_required
def blog_post_create_view(request):
    #form = BlogPostNew(request.POST or None)
    form = BlogModel(request.POST or None)
    if form.is_valid():
        #obj=BlogPost.objects.create(**form.cleaned_data)
        #form=BlogPostNew()
        obj=form.save(commit=False)
        obj.user= request.user
        # obj.title=form.cleaned_data('title')+'O'   //can manipulate like this
        obj.save()
        form = BlogModel()
    template_name='form.html'
    context={'form':form}
    return render(request,template_name,context)

@staff_member_required
def blog_post_update_view(request,slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogModel(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'form.html'
    context ={'form':form,'title':f"Update {obj.title}"}
    return render(request,template_name,context)

@staff_member_required
def blog_post_delete_view(request,slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_delete_page.html'
    if request.method == "POST":
        obj.delete()
        return redirect("/blog")
    context ={'obj': obj}
    return render(request,template_name,context)
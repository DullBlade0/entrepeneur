from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post
# Create your views here.


def posts_create(request):
    form = PostForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Succesfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form': form
    }
    return render(request, 'post_form.html', context)

def posts_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    context = {
        'title': 'Detail',
        'instance': instance
    }
    return render(request, 'post_detail.html', context)

def posts_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title": "List"
    }
    return render(request, 'post_list.html', context)

def posts_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Successfully updated!', extra_tags='some-tag')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'title': 'Detail',
        'instance': instance,
        'form': form
    }
    return render(request, 'post_form.html', context)

def posts_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, 'Successfully deleted!')
    return redirect('posts:list')

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
# Create your views here.

class Home(ListView):
	model = Post
	template_name = 'home.html'

class Detail(DetailView):
	model = Post
	template_name = 'detail.html'

class Create(CreateView):
	model = Post
	template_name = 'post.html'
	fields = ['title', 'author', 'text', 'image']

class Update(UpdateView):
	model = Post
	template_name = 'edit.html'
	fields = ['title', 'text', 'image']

class Delete(DeleteView):
	model = Post
	template_name = 'delete.html'
	success_url = reverse_lazy('home')

class About(ListView):
	model = Post
	template_name = 'about.html'
	


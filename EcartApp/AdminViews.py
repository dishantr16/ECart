from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView,DetailView,UpdateView
from EcartApp.models import Categories
from django.contrib.messages.views import SuccessMessageMixin



@login_required(login_url="/admin/")

def admin_home(request):
    return render(request, "admin_templates/home.html")


class CategoriesListView(ListView):
    model=Categories
    template_name = "admin_templates/category_list.html"


class CategoriesCreate(SuccessMessageMixin, CreateView):
    model=Categories
    success_messages="Category Added!" 
    fields = "__all__"
    template_name = "admin_templates/category_create.html"
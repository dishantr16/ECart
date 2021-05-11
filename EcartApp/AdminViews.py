from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView,DetailView,UpdateView
from EcartApp.models import Categories



@login_required(login_url="/admin/")

def admin_home(request):
    return render(request, "admin_templates/home.html")


class CategoryListView(ListView):
    model=Categories
    template_name = "admin_templates/category_list.html"


class CategoriesCreate(CreateView):
    model=Categories
    fields = "__all__"
    template_name = ""
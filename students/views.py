from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Student
from .forms import UserForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    context_object_name = 'students'


class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'age', 'classroom', 'club', 'house', 'photo']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'age', 'classroom', 'club', 'house', 'photo']


class StudentDeleteView(DeleteView):
    model = Student
    success_url = '/'


def signup(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = form.save(commit=False)
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('students:student-index')

    return render(request, 'students/signup.html', {'form': form})

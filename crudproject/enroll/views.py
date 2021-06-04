from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.base import RedirectView, TemplateView
from django.views import View
from .forms import StudentRegistration
from .models import User
# Create your views here.

# This Class will Add new Item and Show All Items
class UserAddShowView(TemplateView):
    template_name = 'enroll/addandshow.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = StudentRegistration()
        stud = User.objects.all()
        context = {'form':fm, 'stu':stud}
        return context
    def post(self, request):
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            return HttpResponseRedirect('/')
# def add_show(request):
#     if request.method == 'POST':
#         fm = StudentRegistration(request.POST)
#         if fm.is_valid():
#             nm = fm.cleaned_data['name']
#             em = fm.cleaned_data['email']
#             pw = fm.cleaned_data['password']
#             reg = User(name=nm, email=em, password=pw)
#             reg.save()
#             fm = StudentRegistration()
#     else:
#         fm = StudentRegistration()
#     stud = User.objects.all()
#     return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})

# This Function will Update/Edit
class UserUpdateView(View):
    def get(self, request, id):
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
        return render(request, 'enroll/updatestudent.html', {'form':fm})
    def post(self, request, id):
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')
# def update_data(request, id):
#     if request.method == 'POST':
#         pi = User.objects.get(pk=id)
#         fm = StudentRegistration(request.POST, instance=pi)
#         if fm.is_valid():
#             fm.save()
#             return HttpResponseRedirect('/')
#     else:
#         pi = User.objects.get(pk=id)
#         fm = StudentRegistration(instance=pi)
#     return render(request, 'enroll/updatestudent.html', {'form':fm})

# This Function will Delete
class UserDeleteView(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)
# def delete_data(request, id):
#     if request.method == 'POST':
#         pi = User.objects.get(pk=id)
#         pi.delete()
#         return HttpResponseRedirect('/')
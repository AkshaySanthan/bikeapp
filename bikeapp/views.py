from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View,CreateView,ListView,DetailView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy
from bikeapp.models import Bikes,CompanyProfile
from bikeapp.forms import BikeForm,CompanyProfileForm
from django.contrib.auth.models import User
from bikeapp.forms import UserForm,LoginForm
from django.contrib.auth import authenticate,login,logout


# Create your views here.

class BikeHomeView(TemplateView):
    template_name="bk-home.html"

class AddBikeView(CreateView):
    model = Bikes
    form_class = BikeForm
    template_name = "bk-add.html"
    success_url = reverse_lazy('listbike')

class ListBike(ListView):
    model = Bikes
    context_object_name = "bikes"
    template_name = "bk-list.html"

class  BikeDetail(DetailView):
    model = Bikes
    context_object_name = "bikes"
    template_name ="bk-detail.html"
    pk_url_kwarg = "id"

class EditBikeView(UpdateView):
    model = Bikes
    form_class = BikeForm
    template_name = "bk-edit.html"
    success_url = reverse_lazy('listbike')
    pk_url_kwarg = "id"

class BikeDeleteView(DeleteView):
    model = Bikes
    template_name = "bk-delete.html"
    success_url = reverse_lazy("listbike")
    pk_url_kwarg = "id"

class UserSighnupView(CreateView):
    model = User
    form_class = UserForm
    template_name = "sighnup.html"
    success_url = reverse_lazy("listbike")

class LogInView(FormView):
    form_class = LoginForm
    template_name = "login.html"

    def post(self, request, *args, **kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                return redirect("listbike")
            else:
                return render(request,"login.html",{"form":form})


def sighnout_view(request,*args,**kwargs):
    logout(request)
    return redirect('login')


class ChangePasswordView(TemplateView):
    template_name = "changepass.html"
    def post(self,request,*args,**kwargs):
        pwd=request.POST.get("pwd")
        uname=request.user
        user=authenticate(request,username=uname,password=pwd)
        if user:
            return redirect('reset')
        else:
            return render(request,self.template_name)


class PasswordResetView(TemplateView):
    template_name = "resetpass.html"
    def post(self,request,*args,**kwargs):
        pwd1=request.POST.get("pwd1")
        pwd2=request.POST.get("pwd2")
        if pwd1 != pwd2:
            return render(request,self.template_name,{"msg":'password mismatching'})
        else:
            u=User.objects.get(username=request.user)
            u.set_password(pwd1)
            u.save()
            return redirect('login')

class CompanyProfileView(CreateView):
    model = CompanyProfile
    form_class = CompanyProfileForm
    template_name = "bk-addprofile.html"
    success_url = reverse_lazy('bk-home')
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)




class BkViewProfileView(TemplateView):
    template_name = "bk-viewprofile.html"

class BkEditProfileView(UpdateView):
    model = CompanyProfile
    form_class = CompanyProfileForm
    template_name = "bk-ediprofile.html"
    success_url = reverse_lazy('bk-profileview')
    pk_url_kwarg = "id"
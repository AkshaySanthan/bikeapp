from django.urls import path
from bikeapp import views

urlpatterns = [

                path('home',views.BikeHomeView.as_view(),name='bk-home'),
                path('bikes/add',views.AddBikeView.as_view(),name='addbike'),
                path('bikes/list',views.ListBike.as_view(),name='listbike'),
                path('bikes/detail/<int:id',views.BikeDetail.as_view(),name='detail'),
                path('bikes/edit/<int:id>',views.EditBikeView.as_view(),name='edit'),
                path('bikes/delete/<int:id>',views.BikeDeleteView.as_view(),name='delete'),
                path('user/account/sighup',views.UserSighnupView.as_view(),name="sighup"),
                path('user/account/login',views.LogInView.as_view(),name='login'),
                path('user/account/logout',views.sighnout_view,name='logout'),
                path('user/change/password',views.ChangePasswordView.as_view(),name='change-pass'),
               path('user/reset/password',views.PasswordResetView.as_view(),name='reset')


    ]
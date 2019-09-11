from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path(route='admin/', view=admin.site.urls),
    # убрать, когда все будет готово и оставить коммент,
    # что для работы нужно указать home
    path(
        route='',
        view=include(arg='project_name.main.urls')
    ),
    path(
        route='login/',
        view=auth_views.LoginView.as_view(
            template_name='auth/login.html',
            redirect_authenticated_user=True
        ),
        name='login'
    ),
    path(route='logout/', view=auth_views.LogoutView.as_view(), name='logout')
    # path(
    #     route='password-change/',
    #     view=auth_views.PasswordChangeView.as_view(),
    #     name='password_change'
    # ),
    # path(
    #     route='password-change/done/',
    #     view=auth_views.PasswordChangeDoneView.as_view(
    #         template_name='auth/password_change_done.html'
    #     ),
    #     name='password_change_done'
    # ),
    # path(
    #     route='password-reset/',
    #     view=auth_views.PasswordResetView.as_view(
    #         template_name='auth/password_reset_email.html'
    #     ),
    #     name='password_reset'
    # ),
    # path(
    #     route='password-reset/done/',
    #     view=auth_views.PasswordResetDoneView.as_view(
    #         template_name='auth/password_reset_done.html'
    #     ),
    #     name='password_reset_done'
    # ),
    # path(
    #     route='reset/<uidb64>/<token>/',
    #     view=auth_views.PasswordResetConfirmView.as_view(
    #         template_name='auth/password_reset_confirm.html'
    #     ),
    #     name='password_reset_confirm'
    # ),
    # path(
    #     route='reset/done/',
    #     view=auth_views.PasswordResetCompleteView.as_view(
    #         template_name='auth/password_reset_complete.html'
    #     ),
    #     name='password_reset_complete'
    # )
]
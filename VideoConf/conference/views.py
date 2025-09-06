from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, FormView
from django.conf import settings

from accounts.forms import SignUpForm
from conference.forms import JoinRoomForm


class IndexView(TemplateView):
    template_name = "conference/index.html"
    extra_context = {'title': 'Video Conference'}


class RegisterView(FormView):
    template_name = "conference/register.html"
    extra_context = {'title': 'Register'}
    form_class = SignUpForm
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(LoginView):
    template_name = "conference/login.html"
    extra_context = {'title': 'Login'}

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = "conference/dashboard.html"
    extra_context = {'title': 'Video Conference'}


@method_decorator(login_required, name='dispatch')
class VideoCallView(TemplateView):
    template_name = "conference/video_call.html"
    extra_context = {
        'title': 'Video Conference',
        "zegocloud": settings.ZEGOCLOUD
    }


@method_decorator(login_required, name='dispatch')
class JoinRoomView(FormView):
    template_name = "conference/join_room.html"
    extra_context = {'title': 'Video Conference'}
    form_class = JoinRoomForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return redirect("/meeting?roomID=" + form.cleaned_data['room_id'])
        return self.get(request, *args, **kwargs)

import logging
import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.views.generic import TemplateView, CreateView

from project_name.main.models import Article

logger = logging.getLogger('default')


class HomePageView(LoginRequiredMixin, TemplateView):
	template_name = 'main/home.html'

	def get_context_data(self, **kwargs):
		"""
		Place for base settings
		"""
		# send_mail(
		# 	subject='Subject here',
		# 	message='Here is the message.',
		# 	from_email='from@example.com',
		# 	recipient_list=['to@example.com']
		# )

		# logger.error('Something went wrong!')
		return super().get_context_data(**kwargs)


class ArticleCreateView(CreateView):
	model = Article
	fields = ['image']

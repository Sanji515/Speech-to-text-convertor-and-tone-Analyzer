from django.urls import path

from .views import MainPage, Translate

urlpatterns = [
	# path('recognize/',SpeechToText, name='speech'),
	path('',MainPage, name='MainPage'),
	path('translate/', Translate, name='translate')
]
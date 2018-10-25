from __future__ import print_function
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.urls import reverse
from googletrans import Translator
from watson_developer_cloud import ToneAnalyzerV3

import json
import speech_recognition as sr

tone_analyzer = ToneAnalyzerV3(
    username='5eb56774-16ea-454c-a583-ec27c61f4ade',
    password='U2D8LPWrojZ6',
    version='2017-09-26')


translator = Translator(service_urls=[
			'translate.google.com',
			'translate.google.co.kr',
		])


def MainPage(request):
	context = {}
	
	return render(request, 'blog/MainPage.html', context)

# def SpeechToText(request):
# 	context = {}
# 	r = sr.Recognizer()
# 	with sr.Microphone() as source:
# 		r.adjust_for_ambient_noise(source)
# 		print("Say something!")
# 		audio = r.listen(source)
# 		print("Done!")

# 	try:
# 		context = {
# 			"result": r.recognize_google(audio)
# 		}
# 		print("You said: " + r.recognize_google(audio))
# 	except Exception as e:
# 		print (e)

# 	return render(request, 'blog/Python.html', context)


def Translate(request):
	username = " "
	context={}
	result_text = " "
	print(1)
	print("inside translations before ",username)

	if request.method == 'GET':
		username = request.GET.get('username', None)
			# data = {
			# 	'is_taken': objects.filter(username__iexact=username).exists()
			# }
			# if data['is_taken']:
			# 	data['error_message'] = 'A user with this username already exists.'
		print("thsi is in translate after ",username)
		# if username == None:
		# 	username = "1"

		translations = translator.translate([username], dest='en')
		
		for translation in translations:
		# print(translation.origin, ' -> ', translation.text)
			result_text += translation.text

		print("Result = "  +result_text)

		

		text = result_text
		result = json.dumps(tone_analyzer.tone(tone_input=text,content_type="text/plain"), indent=2)
		print(result)
		json_object = json.loads(result)
		list12 = json_object["document_tone"]["tones"]
		data_return = []
		for i in range(0,len(list12)):
			data_return.append(list12[i]["tone_name"])
			data_return.append(list12[i]["score"])

			

		print("before render ")
		context = {
			"result": result_text,
			"data_list":data_return
		}


		obj = json.dumps(context)
		print("oo")
		return HttpResponse(obj, content_type='application/json')

from django.shortcuts import render
from .basic import pars, append_db
from django.http import HttpResponse
from HomePage.models import Followers
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

	

def index(request):
	#Calculation rate USD to EUR fot print on Home Page
	first_cur = 'EUR'
	second_cur = 'USD'
	first_par_form = '1'
	#Find rate and par in dictionary pars date
	for glossary in append_db.create():
		if glossary['title'] == first_cur:
			first_rate = glossary['rate']
			first_par = glossary['par']
			break
	for glossary in append_db.create():
		if glossary['title'] == second_cur:
			second_rate = glossary['rate']
			second_par = glossary['par']
			break
	#Calculation rate
	result_ = float(first_par_form)*(float(first_rate)*float(second_par))/(float(second_rate)*float(first_par))
	result = str(float("{0:.4f}".format(result_)))
	result_full = first_par_form + " " + first_cur + " = " + result + " " + second_cur
	#Send template Home Page and result calculation
	return render(request, 'HomePage/HomePage.html', {'tests': append_db.create(), "result_full": result_full})	

def give_result(request):
	#Get data from js-script(ajax)
	if request.GET:
		first_cur = request.GET.get('first_cur').upper()
		second_cur = request.GET.get('second_cur').upper()
		first_par_form = request.GET.get('first_par_form')
	#Check request.GET is None or ''
	if first_cur == '' or first_cur == None:
		first_cur = 'EUR'
	if second_cur == '' or second_cur == None:
		second_cur = 'USD'
	if first_par_form == '' or first_par_form == None:
		first_par_form = '1'
	#Try convert "int" or "float" data to "float"
	try:
		first_par_form_test = float(first_par_form)
	# If type first_par_form isn't float or int send data error
	except ValueError:
		return HttpResponse("Data error", content_type = 'text/html')
	#Find rate and par in dictionary pars date
	first_rate = ''
	second_rate = ''
	cur_list = append_db.create()
	for glossary in cur_list:
		if glossary['title'] == first_cur:
			first_rate = glossary['rate']
			first_par = glossary['par']
			break 
	for glossary in cur_list:
		if glossary['title'] == second_cur:
			second_rate = glossary['rate']
			second_par = glossary['par']
			break
	#Check correct data
	if first_rate == '' or second_rate == '':
		return HttpResponse("Data error", content_type = 'text/html')
	#Calculation rate
	result_ = float(first_par_form)*(float(first_rate)*float(second_par))/(float(second_rate)*float(first_par))
	result = str(float("{0:.4f}".format(result_)))
	result_full = first_par_form + " " + first_cur + " = " + result + " " + second_cur
	#Return result to js-script
	return HttpResponse(result_full, content_type = 'text/html')	

def user_follow(request):
	#Get data from js-script(ajax)
	if request.GET:
		user_email_form = request.GET.get('user_email')
		user_name_form = request.GET.get('user_name')
		#Check correct email
		try:
		    validate_email(user_email_form)
		    valid_email = True
		except ValidationError:
		    valid_email = False
		#Request to db. Ger emails everybody users
		user_emails = Followers.objects.all()
		#Check user_email in db
		for user_check in user_emails:
			if user_email_form == str(user_check):
				db_check_email = False
				return HttpResponse("You are follower already", content_type = 'text/html')
			else:
				db_check_email = True
		#Append new user
		if valid_email and db_check_email and len(user_email_form)<200 and len(user_name_form)<200:
			new_user = Followers(user_email = user_email_form, user_name = user_name_form)
			new_user.save()
			message = 'Congratulations! Regisration finished is successful! Until you will not get my messages. I develop this part.'
			send_mail('Welcome!', message, "Yasoob", [user_email_form], fail_silently=False)
			return HttpResponse("Congratulations! Regisration finished is successful!<br> Check your email!",
			 content_type = 'text/html')
		else:
			return HttpResponse("Email error", content_type = 'text/html')
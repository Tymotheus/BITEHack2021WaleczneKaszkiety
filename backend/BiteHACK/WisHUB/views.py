from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User as djangoUser
from django.contrib.auth import authenticate
from .models import User
from .models import Tag,Field
import json

@api_view(['GET'])
def tags(request):
	respond = {}
	data = Tag.nodes.all()
	respond["tags"] =[x.serialize for x in data]
	return Response(respond)




@api_view(['GET'])
def fields(request):
	respond = {}
	data = Field.nodes.all()
	respond["fields"] =[x.serialize for x in data]
	return Response(respond)


@api_view(['GET'])
def posts(request,tag_id):
	respond = {}
	data = Tag.nodes.all(tag_id = tag_id)
	data = data.posts.all()
	data = [x.serialize for x in data]
	return Response(data)




@api_view(['GET'])
def tag(request,tag_id):
	respond = {}
	data = Tag.nodes.get(tag_id = tag_id)
	respond = data.serialize
	return Response(respond)

@api_view(['GET'])
def field(request,field_id):
	respond = {}
	data = Field.nodes.get(field_id = field_id)
	data = data.serialize
	return Response(data)

@api_view(['GET','POST'])
def post(request,post_id):
	if request.method == 'GET':
		respond = {}
		data = Post.nodes.all(post_id = post_id)
		data = data.serialize
		return Response(data)
	if request.method == 'POST':
		




from django.contrib.auth.backends import BaseBackend
@api_view(['GET'])
def login_data(request):
	user =  BaseBackend.get_user(request)

@api_view(['POST'])
def login(request):
	data = json.loads(request.body)
	username = data["username"]
	password = data["password"]
	print(request.body)
	user = authenticate(username=username,password=password)
	if user is None:
		response = False
	else:
		response = True
	return Response(response)
	



@api_view(['POST'])
def register(request):
	data = json.loads(request.body)
	username = data["username"]
	password = data["password"]
	email = data["email"]
	try:
		u = djangoUser.objects.create_user(username=username,password=password,email=email)
		u.save()
		u = User(name=username,email=email)
		u.save()
		response = True 		
	except Exception as e:
		raise e
		response = False
	return Response(response)

# Create your views here.

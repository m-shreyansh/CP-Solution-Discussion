from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.



def main(request):
	context={}
	return render(request,'home/home.html',context)

def solution(request,id):
	solutions = Solution.objects.all()
	context={}
	context['comments']=[]
	sol=4
	form=textArea()
	context['form']=form
	for solution in solutions:
		if solution.id==id:
			context['hint']=solution.hint
			context['solution']=solution.soultion
			context['code']=solution.code	
			context['likes']=solution.likes	
			context['sol_id']=solution.id
			sol=solution
			try:
				liked=Liked_by.objects.get(user=request.user,solution=solution)
				context['liked']=True
			except:
				context['liked']=False
			break
	comments = Comment.objects.all()
	for comment in comments:
		if comment.level == 0 and comment.solution_of == sol :
			cur=comment
			while(cur!=None):
				context['comments'].append(cur)
				cur=cur.next_comment
	return render(request,'home/solution.html',context)

def question(request,question_number):
	solutions = Solution.objects.all()
	temp=[];
	for solution in solutions:
		if solution.question==question_number:
			temp.append(solution)
	context={'solutions':temp}
	return render(request,'home/question.html',context)

def new_sol(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form=new_sol_form(request.POST)
			if form.is_valid():
				question = form.cleaned_data['question']
				hint = form.cleaned_data['hint']
				solution = form.cleaned_data['solution']
				code = form.cleaned_data['code']
				new_Solution=Solution(user = request.user,likes = 0, hint = hint, soultion = solution, code = code, question = question)
				new_Solution.save()


		else:
			form=new_sol_form()
		context={'form':form}
		return render(request,'home/new_sol.html',context)
	else:
		return redirect('/login')

def login_user(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		manual_error=""
		if request.method == 'POST':
			form=login_form(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				print(username)
				password = form.cleaned_data['password']
				user = authenticate(request, username=username, password=password)
				if user is not None:
					login(request, user)
					return redirect('/')

				else:
					# invalid details message here
					manual_error="Username or Password Incorrect"
					print('hi')
					# return redirect('/login')

		else:
			form=login_form()
		context={'form':form,'manual_error':manual_error}
		return render(request,'home/login.html',context)

def logout_user(request):
	logout(request)
	return redirect('/')

def sign_up(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		if request.method == 'POST':
			form=UserCreationForm(request.POST)
			print(form)
			if form.is_valid():
				form.save()
				return redirect('/login')
			else:
				print("user not Created")
		else:
			form=UserCreationForm()
		context={'form':form}
		return render(request,'home/sign_up.html',context)


def like(request):
	if request.user.is_authenticated:
		sol_id=request.POST.get('sol_id')
		nex = request.POST.get('next','/')
		sol = Solution.objects.get(id=sol_id)
		try:
			liked=Liked_by.objects.get(user=request.user,solution=sol)
			sol.likes-=1
			liked.delete()
		except:
			sol.likes+=1
			new_like=Liked_by(user=request.user,solution=sol)
			new_like.save()
		sol.save()
		return redirect(nex)
	else:
		return redirect('/login')

def reply(request):
	nex = request.POST.get('next','/')
	try:
		parent=Comment.objects.get(id=request.POST.get('parent_id'))
		content=request.POST.get('content')
		# print(request.POST)
		# content=textArea(request.POST)
		print(content)
		new_comment=Comment(user=request.user,content=content,level=parent.level+100,solution_of=parent.solution_of,last_comment=parent,next_comment=parent.next_comment)
		new_comment.save()
		parent.next_comment=new_comment
		parent.save()
	except:
		return redirect(nex)
	return redirect(nex)









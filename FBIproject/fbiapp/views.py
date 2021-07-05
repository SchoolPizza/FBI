from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from .forms import UserLoginForm, UserSignupForm
from django.contrib import auth


def main(request):
    return render(request, 'fbiapp/index.html')

# Create your views here.
def signup(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["password_confirm"]:
            form = UserSignupForm(request.POST)
            print(form.errors)

            if form.is_valid():
                user = User.object.create_user(**form.cleaned_data)
                auth.login(request,user)
                return redirect('main')
            else:
                form = UserSignupForm()
                print('form not valid')
                return render(request, 'fbiapp/signup.html',{'form':form})
        else:
            form = UserSignupForm()
            print('비밀번호와 비밀번호 확인이 다름')
            return render(request, 'fbiapp/signup.html',{'form':form})
    else:
        form = UserSignupForm()
        print('request not post')
        return render(request, 'fbiapp/signup.html',{'form':form})


def login(request):
    if request.method == "POST":
        user_id = request.POST['user_id']
        password = request.POST['password']
        user = auth.authenticate(request, user_id=user_id, password=password)
        if user is not None:
            print("인증성공")
            auth.login(request,user)
            return redirect('main')
        else:
            print("인증실패")
            return render(request, 'fbiapp/login.html', {'error': '사용자ID 혹은 비밀번호가 잘못되었습니다.'})
    else:
        return render(request, 'fbiapp/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')
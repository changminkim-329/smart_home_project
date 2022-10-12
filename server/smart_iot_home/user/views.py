from django.shortcuts import render
from .models import User
# Create your views here.

def getLogin(request):
    print(request.method)
    if(request.method=="POST"):
        print(request.POST.get('signout',None))
        if(request.POST.get('signout',None)):
            del request.session['user_id']
            return render(request, 'login.html')

        res_data = {}
        useremail = request.POST.get('email',None)
        password = request.POST.get('password',None)
        try:
            user = User.objects.get(useremail=useremail)
            if(user.password == password):
                print("계정 확인")
                print(useremail)
                print(password == user.password)
                # print(request.session[user.username])
                
                request.session['user_id'] = user.id

  
                # request.session[user.username] = user.id
                return render(request, 'index.html')

            else:
                print("비밀번호가 틀립니다.")
                res_data['error'] = 'Incorrect password.'
                return render(request, 'login.html',res_data)
            
        except Exception as e:
            print("계정 없음")
            res_data['error'] = 'No Account Exist'
            return render(request, 'login.html',res_data)
    else:
        try:
            print(request.session['user_id'])
            return render(request, 'index.html')
        except Exception as e:
            print("Not cookie")
        return render(request, 'login.html')



def getRegister(request):
    print("값:",request.method)

    if(request.method=="GET"):

        return render(request, 'register.html/')
    else:
        username = request.POST.get('username',None)
        email = request.POST.get('email',None)
        password = request.POST.get('password',None)
        password_again = request.POST.get('password-again',None)

        res_data = {}

        print(username)
        print(email)
        print(password)
        print(password_again)
        if(password == password_again):
            exist = User.objects.filter(username=username).count()
            print("존재:",exist)
            if(exist!=0):
                res_data['error'] =  "Username "+username+" is not available."
            else:
                print("checkin")
            
                user = User(
                    username = username,
                    useremail = email,
                    password = password
                )
                res_data['error'] =  "Thank You for Sign up"
                user.save()

        else:
            res_data['error'] = "Incorrect password"

        return render(request, 'register.html/',res_data,)


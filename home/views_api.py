from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

#Login
class LoginView(APIView):

    # Login post işlemi
    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'

        # Validations
        try:
            data = request.data
            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')
            
            if data.get('password') is None:
                response['message'] = 'key password not found'
                raise Exception('key password not found')
            
            # Debug
            # print('hello world')

            # Kullanıcının varlığı Username üzerinden kontrol ediliıyor
            check_user = User.objects.filter(username = data.get('username')).first()

            if check_user is None:
                response['message'] = 'invalid username, user not found'
                raise Exception('invalid username, user not found')
            
            # Kullanıcı adı ve parola kontrolü
            user_obj = authenticate(username = data.get('username'), password = data.get('password'))

            if user_obj:
                response['status'] = 200
                response['message'] = 'Welcome ' + data.get('username')
            else:
                response['message'] = 'unauthorized'
                raise Exception('unauthorized')
        except Exception as e:
            print(e)
        
        return Response(response)
LoginView = LoginView.as_view()


#Register
class RegisterView(APIView):
    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data
            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')
            
            if data.get('password') is None:
                response['message'] = 'key password not found'
                raise Exception('key password not found')
            
            print('hello world')
            check_user = User.objects.filter(username = data.get('username')).first()

            if not check_user is None:
                response['message'] = 'username already taken, please try another'
                raise Exception('username already taken')
            
            user_objs = User.objects.create(username = data.get('username'))
            user_objs.set_password(data.get('password'))
            user_objs.save()
            response['message'] = 'Account has been created successfully'
            response['status'] = 200
        except Exception as e:
            print(e)
        return Response(response)
    
RegisterView = RegisterView.as_view()
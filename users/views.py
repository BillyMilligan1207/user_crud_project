from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import User
import json

@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):
    def post(self, request):
        """Создание пользователя"""
        try:
            data = json.loads(request.body)
            login = data.get('login')
            passwd = data.get('passwd')
            if login and passwd:
                user = User.objects.create(login=login, password=passwd)
                return JsonResponse({"id": user.id, "login": user.login, "status": "User created"})
            return JsonResponse({"error": "Invalid data"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    def get(self, request, user_id=None):
        """Получение пользователя по ID или всех пользователей"""
        if user_id:
            try:
                user = User.objects.get(id=user_id)
                return JsonResponse({"id": user.id, "login": user.login})
            except User.DoesNotExist:
                return JsonResponse({"error": "User not found"}, status=404)
        users = list(User.objects.all().values())
        return JsonResponse(users, safe=False)

    def put(self, request, user_id):
        """Обновление пользователя"""
        try:
            data = json.loads(request.body)
            login = data.get('login')
            passwd = data.get('passwd')
            user = User.objects.get(id=user_id)
            if login:
                user.login = login
            if passwd:
                user.password = passwd
            user.save()
            return JsonResponse({"status": "User updated"})
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    def delete(self, request, user_id):
        """Удаление пользователя"""
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return JsonResponse({"status": "User deleted"})
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)

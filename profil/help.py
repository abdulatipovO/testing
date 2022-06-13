from distutils.log import error
from django.contrib import messages
from django.contrib.auth.models import User

s = "<script, <?, <?php"

class CheckUserData:
    
    error = None

    def security(self, request):
        text = request.POST['msg'].strip()
        adres = request.POST['adres'].strip()

        if adres.startswith("<script") or adres.startswith("<?"):
            messages.add_message(request, messages.WARNING, "Ism va Familya harflardan iborat bo'lish kerak")
            self.error = True

        if text.startswith("<script") or adres.startswith("<?"):
            messages.add_message(request, messages.WARNING, "Ism va Familya harflardan iborat bo'lish kerak")
            self.error = True
        return self.error


    def check_data(self, request):
        if self.security(request):
            return self.error
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        if not first_name.isalpha() or not last_name.isalpha():
            messages.add_message(request, messages.WARNING, "Ism va Familya harflardan iborat bo'lish kerak")
            self.error = True
            return self.error
        if (len(first_name) < 2 or len(first_name) > 20) or \
                (len(last_name) < 2 or len(last_name) > 20):
            messages.add_message(request, messages.WARNING, "Ism va Familya xato kiritildi")
            self.error = True
            return self.error
        if len(username) < 8 or len(password) < 8:
            messages.add_message(request, messages.WARNING, "Username  va Parol 8 ta belgidan kam bo'lmasin")
            self.error = True
            return self.error
        if User.objects.filter(username=username).exists():
            messages.add_message(request, messages.WARNING, "Bu Username band ")
            self.error = True
            return self.error
        if password != password_confirm:
            messages.add_message(request, messages.WARNING, "Parollar bir xil emas")
            self.error = True
            return self.error
        return self.error


    
        
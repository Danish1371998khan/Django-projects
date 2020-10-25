from django.db import models


class New_User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    phone_no = models.CharField(max_length=20)
    password = models.CharField(max_length=1000)

    def add_profile_details(self):
        self.save()

    @staticmethod
    def get_user_by_email(email_address):
        try:
            return New_User.objects.get(email=email_address)
        except:
            return None

    @staticmethod
    def isExist(email):
        if New_User.objects.filter(email=email):
            return True
        else:
            return False

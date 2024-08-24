from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomClassManager(BaseUserManager):
    def create_user(self, username, password, **extras):
        if not username:
            raise ValueError("username must be filled")
        user = self.model(username=username, **extras)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password, **extras):
        extras.setdefault("is_staff", True)
        extras.setdefault("is_superuser", True)
        extras.setdefault("is_active", True)

        if extras.get("is_staff") is not True:
            raise ValueError(_("superuser must have is_staff.True"))
        if extras.get("is_superuser") is not True:
            raise ValueError(_("superuser must have is_superuser=True."))
        return self.create_superuser(username, password, **extras)
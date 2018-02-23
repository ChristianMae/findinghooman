from uuid import uuid4
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
    )
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    
    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefualt('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('birthday', None)
        extra_fields.setdefault('contact_number', None)
        extra_fields.setdefault('address', None)
        return self._create_user(email, password, **extra_fields)


    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('birthday', None)
        extra_fields.setdefault('contact_number', None)
        extra_fields.setdefault('address', None)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), blank=False, unique=True)
    first_name = models.CharField(_('first name'), max_length=50, blank=True)
    last_name = models.CharField(_('last name'), max_length=50, blank=True)
    address = models.CharField(_('address'), max_length=300, null=True, blank=True)
    contact_number = models.CharField(_('contact number'),null=True, max_length=11, blank=True)
    birthday = models.DateField(blank=True,null=True)
    is_confirmed = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False
        )
    is_active = models.BooleanField(
        _('active'),
        default=True
        )
    date_joined = models.DateTimeField(
        _('date_joined'), 
        default=timezone.now
        )
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'


    def clean(self):
        super(User, self).clean()
        self.email = self.__class__.objects.normalize_email(self.email)


    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()


    def get_short_name(self):
        return self.first_name


    def generate_token(self):
        from .models import TokenGenerator

        return TokenGenerator.objects.create(user=self)


    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class TokenGenerator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=300)
    is_used = models.BooleanField(default=False)    
    date_created = models.DateField(auto_now=True)


    def save(self, *args, **kwargs):
        if not self.id:
            self.token = self.generate_token()
        return super(TokenGenerator, self).save(*args, **kwargs)


    def generate_token(self):
        return uuid4().hex



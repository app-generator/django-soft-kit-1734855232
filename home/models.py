# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Article(models.Model):

    #__Article_FIELDS__
    article_title = models.TextField(max_length=255, null=True, blank=True)
    article_text = models.TextField(max_length=255, null=True, blank=True)
    article_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    article_id = models.IntegerField(null=True, blank=True)

    #__Article_FIELDS__END

    class Meta:
        verbose_name        = _("Article")
        verbose_name_plural = _("Article")


class Category(models.Model):

    #__Category_FIELDS__
    category_id = models.IntegerField(null=True, blank=True)

    #__Category_FIELDS__END

    class Meta:
        verbose_name        = _("Category")
        verbose_name_plural = _("Category")


class Tags(models.Model):

    #__Tags_FIELDS__
    tags = models.TextField(max_length=255, null=True, blank=True)

    #__Tags_FIELDS__END

    class Meta:
        verbose_name        = _("Tags")
        verbose_name_plural = _("Tags")



#__MODELS__END

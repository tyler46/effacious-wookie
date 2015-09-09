from django.db import models
from django.contrib.auth.models import User


EXPERTISE_CHOICES = (
    ('s', 'sport'),
    ('p', 'politics'),
    ('f', 'finance'),
    ('s', 'social'),
    ('e', 'enviromental'),
    ('t', 'technology'),
)


class Reporter(models.Model):
    user = models.OneToOneField(User)
    expertise = models.CharField(choices=EXPERTISE_CHOICES, max_length=3)

    def __unicode__(self):
        return self.user.get_full_name()


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField(auto_now_add=True)
    reporter = models.ForeignKey(Reporter,
                                 related_name='articles')

    def __unicode__(self):
        return self.headline

    class Meta:
        ordering = ('headline', )

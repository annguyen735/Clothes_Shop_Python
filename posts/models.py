from django.db import models
from users.models import CustomUser as User
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=254)
    description = models.TextField(_('description'))
    date_joined = models.DateTimeField(_('create at'), default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'posts'
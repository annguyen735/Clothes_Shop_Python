from django.db import models
from users.models import CustomUser as User
from posts.models import Post
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _ 

# Create your models here.
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    point = models.IntegerField()
    create_at = models.DateTimeField(_('created at'), default=timezone.now)

    class Meta:
        db_table = 'ratings'

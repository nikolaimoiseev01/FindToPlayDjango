from django.db import models


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    scheduled_at = models.DateTimeField()
    location = models.CharField(max_length=200)
    user_created = models.ForeignKey('users.User', on_delete=models.CASCADE)
    sport = models.ForeignKey('Sport', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    capacity = models.IntegerField(blank=True, null=True)
    repeat_pattern = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'


class Sport(models.Model):
    name = models.CharField(max_length=200)


class EventParticipant(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)




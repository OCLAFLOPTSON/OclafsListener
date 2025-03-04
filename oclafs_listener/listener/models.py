from django.db.models import Model, DateTimeField, CharField

class Log(Model):
    date=DateTimeField(max_length=500)
    player_id=CharField(max_length=500)
    app_id=CharField(max_length=500)
    code=CharField(max_length=500)
    access_token=CharField(max_length=500)
    message=CharField(max_length=500)

    def __str__(self):
        return self.player_id
from django.db.models import Model, DateTimeField, CharField

class Log(Model):
    date=DateTimeField()
    player_id=CharField()
    app_id=CharField()
    code=CharField()
    access_token=CharField()
    message=CharField()

    def __str__(self):
        return self.player_id
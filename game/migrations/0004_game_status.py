# Generated by Django 3.2.9 on 2021-11-19 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_game_host'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('TO BE PLAYED', 'To Be Played'), ('PLAYED', 'Played'), ('CANCELLED', 'Cancelled')], default='TO BE PLAYED', max_length=15),
        ),
    ]
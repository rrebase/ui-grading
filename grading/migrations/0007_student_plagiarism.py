# Generated by Django 2.0.1 on 2018-05-09 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grading', '0006_student_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='plagiarism',
            field=models.BooleanField(default=False),
        ),
    ]

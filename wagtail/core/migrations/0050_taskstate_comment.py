# Generated by Django 3.0.5 on 2020-05-28 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0049_workflow_rejected_to_needs_changes'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskstate',
            name='comment',
            field=models.TextField(blank=True),
        ),
    ]

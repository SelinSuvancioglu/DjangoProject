# Generated by Django 5.0.3 on 2024-05-23 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyCv', '0003_skills_rename_created_date_generalsetting_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Order'),
        ),
    ]
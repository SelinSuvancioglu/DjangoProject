# Generated by Django 5.0.3 on 2024-05-23 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyCv', '0004_skills_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skills',
            options={'ordering': ('order',), 'verbose_name': 'Skill', 'verbose_name_plural': 'Skills'},
        ),
    ]
# Generated by Django 4.0.4 on 2022-05-29 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('business', 'Business'), ('culture', 'Culture'), ('sport', 'Sport'), ('food', 'Food'), ('politics', 'Politics'), ('celebrity', 'Celebrity'), ('startups', 'Startups'), ('travel', 'Travel')], max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
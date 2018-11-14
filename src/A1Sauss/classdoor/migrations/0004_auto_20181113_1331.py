# Generated by Django 2.1.1 on 2018-11-13 18:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classdoor', '0003_auto_20181106_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassdoorUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15)),
                ('major', models.ManyToManyField(to='classdoor.Subject')),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='classdoor.University')),
            ],
            options={
                'ordering': ['username'],
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='major',
        ),
        migrations.RemoveField(
            model_name='user',
            name='writtenReviews',
        ),
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.ForeignKey(help_text='Select a user for this review', null=True, on_delete=django.db.models.deletion.SET_NULL, to='classdoor.ClassdoorUser'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='classdooruser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='classdooruser',
            name='writtenReviews',
            field=models.ManyToManyField(blank=True, to='classdoor.Review'),
        ),
    ]

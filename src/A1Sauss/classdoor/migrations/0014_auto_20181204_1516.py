# Generated by Django 2.1.2 on 2018-12-04 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classdoor', '0013_auto_20181129_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Tag', max_length=40)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.RemoveField(
            model_name='tags',
            name='courseOfTag',
        ),
        migrations.AlterField(
            model_name='review',
            name='tags',
            field=models.ManyToManyField(blank=True, help_text='Select tags for this class', to='classdoor.Tag'),
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
        migrations.AddField(
            model_name='tag',
            name='reviews',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='classdoor.Review'),
        ),
    ]

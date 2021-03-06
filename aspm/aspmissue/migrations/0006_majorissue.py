# Generated by Django 2.2 on 2021-01-05 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aspmissue', '0005_auto_20201229_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='MajorIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.CharField(blank=True, choices=[('Camera Blur', 'Camera Blur'), ('Sound Noise', 'Sound Noise'), ('Network', 'Network')], max_length=200, null=True)),
                ('modelname', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aspmissue.ModelName')),
            ],
        ),
    ]

# Generated by Django 3.0.5 on 2020-05-18 18:41

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('sid', models.IntegerField()),
                ('uid', models.IntegerField()),
                ('bids', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User_Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='M', max_length=10)),
                ('dob', models.DateField(auto_now_add=True, null=True)),
                ('nationality', models.CharField(max_length=50)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('img', models.ImageField(upload_to='uploads/')),
                ('pin', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_Professional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(max_length=50)),
                ('specialization', models.CharField(max_length=50)),
                ('domains', models.CharField(max_length=50)),
                ('work_exp', models.CharField(choices=[('Fresher', 'Fresher'), ('Student', 'Student'), ('2 yr', '2 yr')], max_length=10)),
            ],
        ),
    ]

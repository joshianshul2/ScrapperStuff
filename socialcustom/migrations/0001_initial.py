# Generated by Django 3.1.2 on 2021-03-16 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property_TypeMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Prop_Id2', models.IntegerField(default=0)),
                ('Type_Id2', models.IntegerField(default=0)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PropertyMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountId', models.BigIntegerField()),
                ('acres', models.FloatField()),
                ('adTargetingCountyId', models.BigIntegerField()),
                ('address', models.CharField(max_length=255)),
                ('baths', models.BigIntegerField()),
                ('beds', models.BigIntegerField()),
                ('brokerCompany', models.CharField(max_length=255)),
                ('brokerName', models.CharField(max_length=255)),
                ('Url', models.URLField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('cityID', models.BigIntegerField()),
                ('companyLogoDocumentId', models.BigIntegerField()),
                ('county', models.CharField(max_length=255)),
                ('countyId', models.BigIntegerField()),
                ('description', models.TextField(max_length=255)),
                ('hasHouse', models.BooleanField()),
                ('hasVideo', models.BooleanField()),
                ('hasVirtualTour', models.BigIntegerField()),
                ('imageCount', models.BigIntegerField()),
                ('imageAltTextDisplay', models.CharField(max_length=255)),
                ('isHeadlineAd', models.BooleanField()),
                ('lwPropertyId', models.BigIntegerField()),
                ('isALC', models.BigIntegerField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('price', models.FloatField()),
                ('types', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('status', models.BigIntegerField()),
                ('zip', models.BigIntegerField()),
                ('Rate', models.FloatField(default=0)),
                ('Descrpt', models.TextField(default='!', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='StatusMaster',
            fields=[
                ('status', models.IntegerField(primary_key=True, serialize=False)),
                ('StatusName', models.CharField(max_length=255)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TypeMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TypeId', models.IntegerField()),
                ('TypeName', models.CharField(max_length=255)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
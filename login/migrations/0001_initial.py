# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('TerminalCompany', models.CharField(default=b'l', max_length=30)),
                ('TerminalName', models.CharField(default=b'l', max_length=30)),
                ('AccountCompany', models.CharField(default=b'l', max_length=30)),
                ('AccountNumber', models.CharField(default=b'l', max_length=30)),
                ('AccountCurrency', models.CharField(default=b'l', max_length=30)),
                ('AccountLeverage', models.DecimalField(default=0.0, max_digits=30, decimal_places=4)),
                ('AccountBalance', models.DecimalField(default=0.0, max_digits=30, decimal_places=4)),
                ('AccountEquity', models.DecimalField(default=0.0, max_digits=30, decimal_places=4)),
                ('AccountMargin', models.DecimalField(default=0.0, max_digits=30, decimal_places=4)),
                ('AccountProfit', models.DecimalField(default=0.0, max_digits=30, decimal_places=4)),
                ('MarginReq', models.DecimalField(default=0.0, max_digits=30, decimal_places=4)),
                ('AccountFreeMargin', models.DecimalField(default=0.0, max_digits=30, decimal_places=4)),
                ('Spread', models.DecimalField(default=0.0, max_digits=30, decimal_places=4)),
                ('OrderCommission', models.DecimalField(default=0.0, max_digits=30, decimal_places=4)),
                ('AllAmount', models.DecimalField(default=0.0, max_digits=30, decimal_places=4)),
                ('Profit', models.DecimalField(default=0.0, max_digits=30, decimal_places=4)),
                ('HoldProfit', models.DecimalField(default=0.0, max_digits=30, decimal_places=4)),
                ('updatetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Login_fail_log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('groupname', models.CharField(max_length=30)),
                ('reserve', models.CharField(max_length=30)),
                ('reason', models.CharField(max_length=50)),
                ('login_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Login_log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('login_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('groupname', models.CharField(max_length=30)),
                ('content', models.TextField(max_length=1000)),
                ('updatetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('groupname', models.CharField(max_length=30)),
                ('reserve', models.CharField(max_length=30)),
                ('validity', models.DateTimeField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set([('username', 'groupname')]),
        ),
        migrations.AlterUniqueTogether(
            name='market',
            unique_together=set([('username', 'groupname')]),
        ),
    ]

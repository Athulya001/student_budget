# Generated by Django 5.1.5 on 2025-02-02 02:03

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_expense_user_alter_expense_budget_alter_expense_date_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='budget',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='date',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='description',
        ),
        migrations.AddField(
            model_name='expense',
            name='date_spent',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='expense',
            name='reason',
            field=models.CharField(default='No Reason', max_length=255),
        ),
        migrations.AlterField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

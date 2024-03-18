# Generated by Django 5.0.3 on 2024-03-18 16:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutoring_center', '0007_alter_tutor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='tutor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='tutoring_center.tutor'),
        ),
    ]

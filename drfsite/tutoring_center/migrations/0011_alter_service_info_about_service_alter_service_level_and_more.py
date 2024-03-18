# Generated by Django 5.0.3 on 2024-03-18 17:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutoring_center', '0010_alter_service_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='info_about_service',
            field=models.CharField(max_length=50, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='service',
            name='level',
            field=models.CharField(choices=[('PRESCHOLAR', 'Дошкольники'), ('SCHOLAR', 'Школьники'), ('STUDENT', 'Студенты'), ('OTHER', 'Другин')], max_length=15, verbose_name='Уровень'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.FloatField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='service',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tutoring_center.subject', verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='service',
            name='tutor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='tutoring_center.tutor', verbose_name='Репетитор'),
        ),
    ]

# Generated by Django 5.0.2 on 2024-03-10 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_remove_time_table_admin_student_marks_total_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_notice',
            name='tag',
        ),
        migrations.AddField(
            model_name='student_notice',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='attachments/'),
        ),
    ]

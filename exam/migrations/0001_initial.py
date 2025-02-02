# Generated by Django 3.2.12 on 2025-02-02 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_code', models.CharField(max_length=50)),
                ('course_title', models.CharField(max_length=150)),
                ('exam_duration', models.IntegerField()),
                ('sem', models.IntegerField()),
                ('syllabus_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_id', models.AutoField(primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('exam_id', models.AutoField(primary_key=True, serialize=False)),
                ('sem', models.IntegerField()),
                ('year', models.IntegerField()),
                ('level', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('month', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('room_no', models.CharField(max_length=50)),
                ('no_of_rows', models.IntegerField()),
                ('no_of_columns', models.IntegerField()),
                ('block_no', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('session', models.CharField(choices=[('Forenoon', 'Forenoon'), ('Afternoon', 'Afternoon')], max_length=50)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.course')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.exam')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('phone_num', models.CharField(blank=True, max_length=10, null=True)),
                ('designation', models.CharField(choices=[('Assistant Professor', 'Assistant Professor'), ('Associate Professor', 'Associate Professor'), ('Guest Lecturer', 'Guest Lecturer'), ('Junior Lecturer', 'Junior Lecturer'), ('Professor', 'Professor')], default='Assistant Professor', max_length=50)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], default='Female', max_length=10)),
                ('role', models.CharField(default='Teacher', max_length=100)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.department')),
            ],
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programme_name', models.CharField(max_length=255)),
                ('level', models.CharField(choices=[('UG', 'Undergraduate'), ('PG', 'Postgraduate'), ('FYUG', 'Four year UG'), ('IPG', 'Integrated PG')], max_length=20)),
                ('duration', models.IntegerField()),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.department')),
            ],
        ),
        migrations.CreateModel(
            name='DutyPreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pref_date', models.DateField()),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='DutyAllotment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('hours', models.IntegerField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.room')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='pgm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.programme'),
        ),
    ]

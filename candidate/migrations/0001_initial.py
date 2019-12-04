# Generated by Django 2.2.7 on 2019-12-04 21:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectTemplate',
            fields=[
                ('template_id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('domain', models.CharField(max_length=20)),
                ('title', models.TextField()),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.BigIntegerField()),
                ('reg_no', models.CharField(max_length=9)),
                ('email', models.EmailField(max_length=254)),
                ('hostel', models.CharField(max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('interests', models.CharField(max_length=50)),
                ('times_snoozed', models.IntegerField(default=0)),
                ('called', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('room_number', models.IntegerField()),
                ('round_1_comment', models.TextField(blank=True)),
                ('round_1_call', models.BooleanField(default=None, null=True)),
                ('round_2_project_modification', models.TextField(blank=True, default=None, null=True)),
                ('round_2_comment', models.TextField(default=None, null=True)),
                ('round_2_project_completion', models.IntegerField(default=0, null=True)),
                ('round_2_project_understanding', models.IntegerField(default=0, null=True)),
                ('round_2_call', models.BooleanField(default=False, null=True)),
                ('round_2_project_template', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='candidate.ProjectTemplate')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_answers', to='candidate.Candidate')),
            ],
        ),
    ]

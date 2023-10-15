
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalOperator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.SmallIntegerField()),
                ('fqdn', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
                ('name', models.CharField(max_length=60)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PortabilityDatabase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_certificate', models.BinaryField(blank=True, editable=True, null=True)),
                ('status', models.SmallIntegerField()),
                ('access_credentials', models.JSONField(default=dict)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('access_type', models.SmallIntegerField()),
                ('access_private_key', models.BinaryField(blank=True, editable=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.country')),
                ('number_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.numbertype')),
            ],
        )
    ]

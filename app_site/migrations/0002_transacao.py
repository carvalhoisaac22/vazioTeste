# Generated by Django 4.2.1 on 2023-05-08 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('descricao', models.CharField(max_length=200)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=7)),
                ('observacoes', models.TextField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_site.categoria')),
            ],
        ),
    ]

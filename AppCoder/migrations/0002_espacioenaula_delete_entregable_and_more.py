# Generated by Django 4.0.4 on 2022-05-19 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EspacioEnAula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institucion', models.CharField(max_length=50)),
                ('espacio', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.RenameField(
            model_name='profesor',
            old_name='apellido',
            new_name='comision',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='profesion',
        ),
        migrations.AddField(
            model_name='estudiante',
            name='comision',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

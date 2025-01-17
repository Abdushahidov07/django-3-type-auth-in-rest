# Generated by Django 4.2.16 on 2024-11-20 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('castumername', models.CharField(max_length=50)),
                ('total_sum', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_dish', models.CharField(max_length=50)),
                ('descriptions', models.TextField()),
                ('time_category', models.CharField(choices=[('BREAKFEST', 'Завтрак'), ('LUNCH', 'Обед'), ('DINNER', 'Ужин'), ('dessert', 'Десерт'), ('Drinks', 'Напитки'), ('Snacks', 'Салаты')], max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('prf_time', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='media/images')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('vip', 'vip'), ('table', 'Стол'), ('Cud', 'Кад')], max_length=50)),
                ('max_person', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.bill')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.dish')),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.table'),
        ),
    ]

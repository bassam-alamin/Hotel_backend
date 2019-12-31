# Generated by Django 2.2.5 on 2019-10-14 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
                ('category_image', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=200)),
                ('available', models.IntegerField(default=1)),
                ('food_image', models.FileField(upload_to='')),
                ('price', models.IntegerField()),
                ('food_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offline.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('table_no', models.CharField(max_length=10)),
                ('amount', models.IntegerField()),
                ('food', models.ManyToManyField(related_name='orderd_food', to='offline.Food')),
            ],
        ),
    ]
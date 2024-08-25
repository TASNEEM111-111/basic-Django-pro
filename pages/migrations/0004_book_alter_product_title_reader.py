# Generated by Django 5.0.7 on 2024-08-20 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_user_delete_users_rename_products_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reader', models.CharField(max_length=100, null=True)),
                ('books', models.ManyToManyField(to='pages.book')),
            ],
        ),
    ]

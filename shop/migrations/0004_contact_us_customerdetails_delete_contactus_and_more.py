# Generated by Django 4.0.2 on 2022-03-03 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_delete_retailer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('message', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=40)),
                ('lname', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=20)),
                ('Address', models.TextField(max_length=200)),
                ('city', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('Pincode', models.IntegerField()),
                ('pswd', models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Contactus',
        ),
        migrations.AlterField(
            model_name='shopping_cart',
            name='c_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.customerdetails', verbose_name='customer_id'),
        ),
        migrations.DeleteModel(
            name='Customer_Details',
        ),
    ]

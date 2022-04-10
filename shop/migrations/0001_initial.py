# Generated by Django 4.0.2 on 2022-02-23 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('comment', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Customer_Details',
            fields=[
                ('c_id', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=20)),
                ('adress', models.TextField(max_length=200)),
                ('city', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('pincode', models.IntegerField(max_length=10)),
                ('c_password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('Order_Id', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('Delivery_Date', models.DateTimeField()),
                ('Delivery_Address', models.TextField(max_length=200)),
                ('Total_Bill', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('images', models.ImageField(upload_to='img')),
                ('price', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=200)),
                ('color', models.CharField(max_length=20)),
                ('numberofstock', models.IntegerField()),
                ('fabric_type', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Shopping_Cart',
            fields=[
                ('Cart_id', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('Quantity', models.IntegerField(max_length=10)),
                ('Total_Bill', models.IntegerField(max_length=10)),
                ('c_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.customer_details', verbose_name='customer_id')),
                ('product_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='product_id')),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cart_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.shopping_cart', verbose_name='cart_id')),
                ('product_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='product_id')),
            ],
        ),
        migrations.CreateModel(
            name='Retailer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firm_name', models.CharField(max_length=50)),
                ('c_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.customer_details', verbose_name='Retailer_id')),
            ],
        ),
        migrations.CreateModel(
            name='Payment_Gateway',
            fields=[
                ('Transaction_Id', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('Payment_Method', models.CharField(max_length=10)),
                ('Phone_Number', models.CharField(max_length=10)),
                ('Order_Id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.orders', verbose_name='order_id')),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='Cart_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.shopping_cart', verbose_name='cart_id'),
        ),
    ]
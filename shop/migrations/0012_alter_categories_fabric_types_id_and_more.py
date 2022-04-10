# Generated by Django 4.0.2 on 2022-03-13 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_remove_payment_gateway_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='fabric_types_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='color',
            name='color_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orders',
            name='Order_Id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='payment_gateway',
            name='Transaction_Id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='Cart_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='Wishlist_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

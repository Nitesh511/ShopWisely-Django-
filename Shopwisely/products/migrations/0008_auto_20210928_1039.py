# Generated by Django 3.2.6 on 2021-09-28 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20210925_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Cash On Delivery', 'Cash On Delivery'), ('Esewa', 'Esewa'), ('Khalti', 'Khalti')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]

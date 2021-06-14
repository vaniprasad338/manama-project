# Generated by Django 3.1.7 on 2021-03-28 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210328_2044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discounted_price', models.IntegerField(blank=True, null=True)),
                ('Offerproduct_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.offerproducts')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.customer_details')),
                ('offer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.offer')),
            ],
        ),
        migrations.DeleteModel(
            name='purchase_detail',
        ),
    ]

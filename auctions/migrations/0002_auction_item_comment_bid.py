# Generated by Django 4.1.5 on 2023-01-24 04:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True)),
                ('start_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('category', models.CharField(choices=[('VHE', 'Vehicles'), ('FAS', 'Fashion'), ('ELE', 'Electronics'), ('ART', 'Collectibles & Art'), ('HGA', 'Home & Garden'), ('SPO', 'Sporting Goods'), ('TOY', 'Toys'), ('BUS', 'Business & Industrial'), ('MUS', 'Music'), ('OTH', 'Others')], default='OTH', max_length=3)),
                ('image_url', models.URLField(blank=True)),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
                ('is_open', models.BooleanField(default=True)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'auction_item',
                'verbose_name_plural': 'auction_items',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('auction_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.auction_item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_date', models.DateTimeField(auto_now_add=True)),
                ('bid_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('auction_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.auction_item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'bid',
                'verbose_name_plural': 'bids',
            },
        ),
    ]

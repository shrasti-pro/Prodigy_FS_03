from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('mobile', 'Mobile Phone'), ('watche', 'Watches'), ('shirt', 'Shirts'), ('shoes', 'Shoes'), ('others', 'Others')], default='others', max_length=120),
            preserve_default=False,
        ),
    ]

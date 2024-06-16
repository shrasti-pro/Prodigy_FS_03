from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200116_2116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='BillingProfile',
            new_name='billing_profile',
        ),
    ]

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='objectviewed',
            options={'ordering': ['-timestamp']},
        ),
    ]

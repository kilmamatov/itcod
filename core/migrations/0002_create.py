from django.db import migrations, models


def fill_service(apps, schema):
    service = apps.get_model('core', 'Service')
    service.objects.create(name='Полиция', cod='102', phone='102102')
    service.objects.create(name='Скорая', cod='101', phone='101101')
    service.objects.create(name='Пожарная', cod='103', phone='103103')


def clear_service(apps, schema):
    service = apps.get_model('core', 'Service')
    service.objects.filter(name='Полиция').delete()
    service.objects.filter(name='Скорая').delete()
    service.objects.filter(name='Пожарная').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            code=fill_service,
            reverse_code=clear_service
        )
    ]

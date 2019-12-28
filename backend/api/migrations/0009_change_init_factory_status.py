import sys
import csv
from datetime import datetime

from django.db import migrations


def forward_func(apps, schema_editor):
    Factory = apps.get_model("api", "Factory")
    factories = Factory.objects.only("id").all().order_by("created_at")[:53918]
    init_factory_ids = [f.id for f in factories]
    Factory.objects.filter(id__in=init_factory_ids).update(status="IO")


def backward_func(apps, schema_editor):
    Factory = apps.get_model("api", "Factory")
    factories = Factory.objects.only("id").all().order_by("created_at")[:53918]
    init_factory_ids = [f.id for f in factories]
    Factory.objects.filter(id__in=init_factory_ids).update(status="A")


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0008_change_factory_types"),
    ]

    operations = [
        migrations.RunPython(
            code=forward_func,
            reverse_code=None,
        ),
    ]

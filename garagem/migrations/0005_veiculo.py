# Generated by Django 4.2.3 on 2023-07-07 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("garagem", "0004_cor"),
    ]

    operations = [
        migrations.CreateModel(
            name="Veiculo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ano", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "preco",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0,
                        max_digits=10,
                        null=True,
                    ),
                ),
                (
                    "acessorios",
                    models.ManyToManyField(blank=True, to="garagem.acessorio"),
                ),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="garagem.categoria",
                    ),
                ),
                (
                    "cor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="garagem.cor"
                    ),
                ),
                (
                    "marca",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="garagem.marca"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Veículos",
            },
        ),
    ]

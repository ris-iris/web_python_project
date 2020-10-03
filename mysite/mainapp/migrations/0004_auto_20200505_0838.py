# Generated by Django 3.0.5 on 2020-05-05 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_character_armor_class'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='weapons',
        ),
        migrations.AddField(
            model_name='character',
            name='damage1',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AddField(
            model_name='character',
            name='damage2',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AddField(
            model_name='character',
            name='damage3',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AddField(
            model_name='character',
            name='damagetype1',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='character',
            name='damagetype2',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='character',
            name='damagetype3',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='character',
            name='weapon1',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='character',
            name='weapon2',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='character',
            name='weapon3',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='character',
            name='additional',
            field=models.CharField(blank=True, max_length=3000),
        ),
        migrations.AlterField(
            model_name='character',
            name='backstory',
            field=models.CharField(blank=True, max_length=3000),
        ),
        migrations.AlterField(
            model_name='character',
            name='bonds',
            field=models.CharField(blank=True, max_length=3000),
        ),
        migrations.AlterField(
            model_name='character',
            name='flaws',
            field=models.CharField(blank=True, max_length=3000),
        ),
        migrations.AlterField(
            model_name='character',
            name='ideals',
            field=models.CharField(blank=True, max_length=3000),
        ),
        migrations.AlterField(
            model_name='character',
            name='organizations',
            field=models.CharField(blank=True, max_length=3000),
        ),
        migrations.AlterField(
            model_name='character',
            name='traits',
            field=models.CharField(blank=True, max_length=3000),
        ),
        migrations.AlterField(
            model_name='character',
            name='treasure',
            field=models.CharField(blank=True, max_length=3000),
        ),
    ]

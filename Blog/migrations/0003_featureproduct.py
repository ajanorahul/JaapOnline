# Generated by Django 2.2.10 on 2020-04-21 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_category_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('img', models.ImageField(upload_to='pics2')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.Category')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.SubCategory')),
            ],
        ),
    ]
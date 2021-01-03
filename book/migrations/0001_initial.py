# Generated by Django 3.1.3 on 2021-01-02 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('author', models.CharField(default='佚名', max_length=50)),
                ('press', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=30)),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('labels', models.CharField(default='此书籍暂无标签', max_length=200)),
                ('cover_url', models.CharField(max_length=200)),
                ('publish_date', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]

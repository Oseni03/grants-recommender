# Generated by Django 4.2.2 on 2023-10-11 23:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('opportunity_no', models.CharField(max_length=15, unique=True)),
                ('expected_award_no', models.IntegerField()),
                ('eligibility_info', models.TextField()),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('estimated_total_funding', models.DecimalField(decimal_places=2, max_digits=15)),
                ('posted_date', models.DateField()),
                ('last_updated_date', models.DateField()),
                ('closing_date', models.DateField()),
                ('slug', models.SlugField(null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='funds', to='funds.agency')),
            ],
        ),
        migrations.CreateModel(
            name='FundCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FundEligibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FundProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('location', models.CharField(help_text='Your geographic scope', max_length=255)),
                ('objectives', models.TextField(help_text='Your mission and goals')),
                ('estimated_budget', models.DecimalField(decimal_places=2, max_digits=15)),
                ('background', models.TextField(help_text='Little about your history')),
                ('project_summary', models.TextField(help_text='Describe the problem to be solved')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('eligibility', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='funds.fundeligibility')),
                ('fund_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='funds.fundcategory')),
            ],
        ),
        migrations.CreateModel(
            name='FundType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('fund', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funds.fund')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funds.fundprofile')),
            ],
        ),
        migrations.AddField(
            model_name='fundprofile',
            name='fund_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='funds.fundtype'),
        ),
        migrations.AddField(
            model_name='fundprofile',
            name='matches',
            field=models.ManyToManyField(related_name='profiles', through='funds.Recommendation', to='funds.fund'),
        ),
        migrations.AddField(
            model_name='fundprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fund',
            name='eligibility',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='funds', to='funds.fundeligibility'),
        ),
        migrations.AddField(
            model_name='fund',
            name='fund_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='funds', to='funds.fundcategory'),
        ),
        migrations.AddField(
            model_name='fund',
            name='fund_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='funds', to='funds.fundtype'),
        ),
        migrations.AddConstraint(
            model_name='recommendation',
            constraint=models.UniqueConstraint(fields=('profile', 'fund'), name='unique_profile_fund'),
        ),
    ]

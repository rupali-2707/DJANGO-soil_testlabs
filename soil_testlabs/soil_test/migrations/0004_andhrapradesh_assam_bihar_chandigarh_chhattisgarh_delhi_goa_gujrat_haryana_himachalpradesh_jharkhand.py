# Generated by Django 3.0.6 on 2020-08-23 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soil_test', '0003_auto_20200823_0501'),
    ]

    operations = [
        migrations.CreateModel(
            name='andhrapradesh',
            fields=[
                ('state_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soil_test.state')),
            ],
            bases=('soil_test.state',),
        ),
        migrations.CreateModel(
            name='assam',
            fields=[
                ('state_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soil_test.state')),
            ],
            bases=('soil_test.state',),
        ),
        migrations.CreateModel(
            name='bihar',
            fields=[
                ('state_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soil_test.state')),
            ],
            bases=('soil_test.state',),
        ),
        migrations.CreateModel(
            name='chandigarh',
            fields=[
                ('state_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soil_test.state')),
            ],
            bases=('soil_test.state',),
        ),
        migrations.CreateModel(
            name='Chhattisgarh',
            fields=[
                ('state_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soil_test.state')),
            ],
            bases=('soil_test.state',),
        ),
        migrations.CreateModel(
            name='delhi',
            fields=[
                ('state_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soil_test.state')),
            ],
            bases=('soil_test.state',),
        ),
        migrations.CreateModel(
            name='goa',
            fields=[
                ('state_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soil_test.state')),
            ],
            bases=('soil_test.state',),
        ),
        migrations.CreateModel(
            name='gujrat',
            fields=[
                ('state_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soil_test.state')),
            ],
            bases=('soil_test.state',),
        ),
        migrations.CreateModel(
            name='haryana',
            fields=[
                ('state_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soil_test.state')),
            ],
            bases=('soil_test.state',),
        ),
        migrations.CreateModel(
            name='himachalpradesh',
            fields=[
                ('state_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soil_test.state')),
            ],
            bases=('soil_test.state',),
        ),
        migrations.CreateModel(
            name='jharkhand',
            fields=[
                ('state_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soil_test.state')),
            ],
            bases=('soil_test.state',),
        ),
        migrations.CreateModel(
            name='karnataka',
            fields=[
                ('state_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soil_test.state')),
            ],
            bases=('soil_test.state',),
        ),
        migrations.CreateModel(
            name='kerala',
            fields=[
                ('state_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soil_test.state')),
            ],
            bases=('soil_test.state',),
        ),
        migrations.CreateModel(
            name='madhyapradesh',
            fields=[
                ('state_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soil_test.state')),
            ],
            bases=('soil_test.state',),
        ),
        migrations.CreateModel(
            name='maharashtra',
            fields=[
                ('state_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soil_test.state')),
            ],
            bases=('soil_test.state',),
        ),
        migrations.CreateModel(
            name='meghalaya',
            fields=[
                ('state_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soil_test.state')),
            ],
            bases=('soil_test.state',),
        ),
        migrations.CreateModel(
            name='mizoram',
            fields=[
                ('state_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soil_test.state')),
            ],
            bases=('soil_test.state',),
        ),
        migrations.CreateModel(
            name='odisha',
            fields=[
                ('state_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soil_test.state')),
            ],
            bases=('soil_test.state',),
        ),
        migrations.CreateModel(
            name='punjab',
            fields=[
                ('state_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soil_test.state')),
            ],
            bases=('soil_test.state',),
        ),
        migrations.CreateModel(
            name='rajasthan',
            fields=[
                ('state_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soil_test.state')),
            ],
            bases=('soil_test.state',),
        ),
        migrations.CreateModel(
            name='sikkim',
            fields=[
                ('state_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soil_test.state')),
            ],
            bases=('soil_test.state',),
        ),
        migrations.CreateModel(
            name='tamilnadu',
            fields=[
                ('state_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soil_test.state')),
            ],
            bases=('soil_test.state',),
        ),
        migrations.CreateModel(
            name='telangana',
            fields=[
                ('state_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soil_test.state')),
            ],
            bases=('soil_test.state',),
        ),
        migrations.CreateModel(
            name='tripura',
            fields=[
                ('state_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soil_test.state')),
            ],
            bases=('soil_test.state',),
        ),
        migrations.CreateModel(
            name='uttarakhand',
            fields=[
                ('state_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soil_test.state')),
            ],
            bases=('soil_test.state',),
        ),
        migrations.CreateModel(
            name='uttarpradesh',
            fields=[
                ('state_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soil_test.state')),
            ],
            bases=('soil_test.state',),
        ),
    ]

# Generated by Django 3.2.16 on 2023-02-05 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('course', '0004_auto_20230204_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('subject', models.CharField(max_length=150, verbose_name='订单标题')),
                ('total_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='订单总价')),
                ('out_trade_no', models.CharField(max_length=64, unique=True, verbose_name='订单号')),
                ('trade_no', models.CharField(max_length=64, null=True, verbose_name='流水号')),
                ('order_status', models.SmallIntegerField(choices=[(0, '待支付'), (1, '已支付'), (2, '已取消'), (3, '超时取消')], default=0, verbose_name='订单状态')),
                ('pay_type', models.SmallIntegerField(choices=[(1, '支付宝'), (2, '微信支付')], default=1, verbose_name='支付方式')),
                ('pay_time', models.DateTimeField(null=True, verbose_name='支付时间')),
                ('user', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_user', to='user.userinfo', verbose_name='下单用户')),
            ],
            options={
                'verbose_name': '订单记录',
                'verbose_name_plural': '订单记录',
                'db_table': 'luffy_order',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='课程原价')),
                ('real_price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='课程实价')),
                ('course', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_orders', to='course.course', verbose_name='课程')),
                ('order', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='order_courses', to='order.order', verbose_name='订单')),
            ],
            options={
                'verbose_name': '订单详情',
                'verbose_name_plural': '订单详情',
                'db_table': 'luffy_order_detail',
            },
        ),
    ]

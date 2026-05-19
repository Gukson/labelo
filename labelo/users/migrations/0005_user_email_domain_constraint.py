from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210914_0109'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='user',
            constraint=models.CheckConstraint(
                check=models.Q(email__iendswith='@pwr.edu.pl'),
                name='htx_user_email_allowed_domain',
            ),
        ),
    ]

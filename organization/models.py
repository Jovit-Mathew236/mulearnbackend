from django.db import models

# Create your models here.
from user.models import User


class Country(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=75)
    updated_by = models.ForeignKey(User, models.DO_NOTHING, db_column='updated_by', related_name='updated_by')
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey(User, models.DO_NOTHING, db_column='created_by', related_name='created_by')
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'country'


class State(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=75)
    country = models.ForeignKey(Country, models.DO_NOTHING)
    updated_by = models.ForeignKey(User, models.DO_NOTHING, db_column='updated_by', related_name='updated_by')
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey(User, models.DO_NOTHING, db_column='created_by', related_name='created_by')
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'state'


class Zone(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=75)
    state = models.ForeignKey(State, models.DO_NOTHING)
    updated_by = models.ForeignKey(User, models.DO_NOTHING, db_column='updated_by', related_name='updated_by')
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey(User, models.DO_NOTHING, db_column='created_by', related_name='created_by')
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'zone'


class District(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=75)
    zone = models.ForeignKey(Zone, models.DO_NOTHING)
    updated_by = models.ForeignKey(User, models.DO_NOTHING, db_column='updated_by', related_name='updated_by')
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey(User, models.DO_NOTHING, db_column='created_by', related_name='created_by')
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'district'


class OrgAffiliation(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    title = models.CharField(max_length=75)
    updated_by = models.ForeignKey(User, models.DO_NOTHING, db_column='updated_by', related_name='updated_by')
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey(User, models.DO_NOTHING, db_column='created_by', related_name='created_by')
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'org_affiliation'


class Organization(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    title = models.CharField(max_length=100)
    code = models.CharField(unique=True, max_length=12)
    org_type = models.CharField(max_length=25)
    affiliation = models.ForeignKey(OrgAffiliation, models.DO_NOTHING, blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING)
    updated_by = models.ForeignKey(User, models.DO_NOTHING, db_column='updated_by', related_name='updated_by')
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey(User, models.DO_NOTHING, db_column='created_by', related_name='created_by')
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'organization'


class UserOrganizationLink(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    user = models.ForeignKey(User, models.DO_NOTHING)
    org = models.ForeignKey(Organization, models.DO_NOTHING)
    verified = models.IntegerField()
    created_by = models.ForeignKey(User, models.DO_NOTHING, db_column='created_by', related_name='created_by')
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_organization_link'

#
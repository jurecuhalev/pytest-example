import pytest


@pytest.mark.django_db
def test_ambassador_permission(db):
	from django.contrib.auth.models import Group

	assert Group.objects.get(name='ambassadors')
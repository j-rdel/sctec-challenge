import pytest
from datetime import timedelta
from django.utils import timezone
from rest_framework.test import APIClient

from core.enums import StatusEnum
from enterprises.enums import BusinessSegmentEnum
from enterprises.models import Enterprise
from enterprises.tests.factories import EnterpriseFactory


@pytest.mark.django_db
class TestEnterpriseAPI:

    def setup_method(self):
        self.client = APIClient()

    def test_should_list_enterprises(self):
        # GIVEN
        EnterpriseFactory.create_batch(3)

        # WHEN
        response = self.client.get("/api/v1/enterprises/")

        # THEN
        assert response.status_code == 200
        assert len(response.data["results"]) == 3

    def test_should_list_filtered_by_name(self):
        # GIVEN
        EnterpriseFactory(name="Tech Corp")
        EnterpriseFactory(name="Food Company")

        # WHEN
        response = self.client.get("/api/v1/enterprises/?name=tech")

        # THEN
        assert response.status_code == 200
        assert len(response.data["results"]) == 1

    def test_should_list_filtered_by_entrepreneur_name(self):
        # GIVEN
        EnterpriseFactory(entrepreneur_name="John Doe")
        EnterpriseFactory(entrepreneur_name="Maria Silva")

        # WHEN
        response = self.client.get("/api/v1/enterprises/?entrepreneur_name=john")

        # THEN
        assert response.status_code == 200
        assert len(response.data["results"]) == 1

    def test_should_list_filtered_by_municipality(self):
        # GIVEN
        EnterpriseFactory(municipality="Florianopolis")
        EnterpriseFactory(municipality="Joinville")

        # WHEN
        response = self.client.get("/api/v1/enterprises/?municipality=florianopolis")

        # THEN
        assert response.status_code == 200
        assert len(response.data["results"]) == 1

    def test_should_list_filtered_by_segment(self):
        # GIVEN
        EnterpriseFactory(segment=BusinessSegmentEnum.TECHNOLOGY.value)
        EnterpriseFactory(segment=BusinessSegmentEnum.INDUSTRY.value)

        # WHEN
        response = self.client.get(f"/api/v1/enterprises/?segment={BusinessSegmentEnum.TECHNOLOGY.value}")

        # THEN
        assert response.status_code == 200
        assert len(response.data["results"]) == 1

    def test_should_list_filtered_by_contact_email(self):
        # GIVEN
        EnterpriseFactory(contact_email="tech@test.com")
        EnterpriseFactory(contact_email="food@test.com")

        # WHEN
        response = self.client.get("/api/v1/enterprises/?contact_email=tech")

        # THEN
        assert response.status_code == 200
        assert len(response.data["results"]) == 1

    def test_should_list_filtered_by_status(self):
        # GIVEN
        EnterpriseFactory(status=StatusEnum.ACTIVE.value)
        EnterpriseFactory(status=StatusEnum.INACTIVE.value)

        # WHEN
        response = self.client.get(f"/api/v1/enterprises/?status={StatusEnum.ACTIVE.value}")

        # THEN
        assert response.status_code == 200
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["status"]["value"] == StatusEnum.ACTIVE.value
        assert response.data["results"][0]["status"]["label"] == "Ativo"

    def test_should_list_filtered_by_created_after(self):
        # GIVEN
        EnterpriseFactory()

        old = EnterpriseFactory()
        old.created_at = timezone.now() - timedelta(days=10)
        old.save()

        formatted_date = (timezone.now() - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%S")

        # WHEN
        response = self.client.get(f"/api/v1/enterprises/?created_after={formatted_date}")

        # THEN
        assert response.status_code == 200
        assert len(response.data["results"]) == 1

    def test_should_list_filtered_by_created_before(self):
        # GIVEN
        EnterpriseFactory()

        old = EnterpriseFactory()
        old.created_at = timezone.now() - timedelta(days=10)
        old.save()

        formatted_date = (timezone.now() - timedelta(days=5)).strftime("%Y-%m-%dT%H:%M:%S")

        # WHEN
        response = self.client.get(f"/api/v1/enterprises/?created_before={formatted_date}")

        # THEN
        assert response.status_code == 200
        assert len(response.data["results"]) == 1

    def test_should_list_filtered_by_updated_after(self):
        # GIVEN
        EnterpriseFactory()
        old = EnterpriseFactory()
        Enterprise.objects.filter(id=old.id).update(
            updated_at=timezone.now() - timedelta(days=10)
        )

        formatted_date = (timezone.now() - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%S")

        # WHEN
        response = self.client.get(f"/api/v1/enterprises/?updated_after={formatted_date}")

        # THEN
        assert response.status_code == 200
        assert len(response.data["results"]) == 1

    def test_should_list_filtered_by_updated_before(self):
        # GIVEN
        EnterpriseFactory()
        old = EnterpriseFactory()
        Enterprise.objects.filter(id=old.id).update(
            updated_at=timezone.now() - timedelta(days=10)
        )

        formated_date = (timezone.now() - timedelta(days=5)).strftime("%Y-%m-%dT%H:%M:%S")

        # WHEN
        response = self.client.get(f"/api/v1/enterprises/?updated_before={formated_date}")

        # THEN
        assert response.status_code == 200
        assert len(response.data["results"]) == 1

    def test_should_create_enterprise(self):
        # GIVEN
        payload = {
            "name": "Tech Company",
            "entrepreneur_name": "John Doe",
            "municipality": "Florianopolis",
            "segment": BusinessSegmentEnum.COMMERCE.value,
            "contact_email": "contact@test.com",
            "status": StatusEnum.ACTIVE.value
        }

        # WHEN
        response = self.client.post("/api/v1/enterprises/", payload)

        # THEN
        assert response.status_code == 201

        enterprises = Enterprise.objects.filter(id=response.data["id"])
        assert len(enterprises) == 1
        assert enterprises[0].name == "Tech Company"
        assert enterprises[0].entrepreneur_name == "John Doe"
        assert enterprises[0].municipality == "Florianopolis"
        assert enterprises[0].segment == BusinessSegmentEnum.COMMERCE.value
        assert enterprises[0].status == StatusEnum.ACTIVE.value
        assert enterprises[0].created_at is not None
        assert enterprises[0].updated_at is not None


    def test_should_retrieve_enterprise(self):
        # GIVEN
        enterprise = EnterpriseFactory()

        # WHEN
        response = self.client.get(f"/api/v1/enterprises/{enterprise.id}/")

        # THEN
        assert response.status_code == 200
        assert response.data["id"] == str(enterprise.id)

    def test_should_update_enterprise(self):
        # GIVEN
        enterprise = EnterpriseFactory()

        payload = {
            "name": "Updated Enterprise",
            "entrepreneur_name": enterprise.entrepreneur_name,
            "municipality": enterprise.municipality,
            "segment": enterprise.segment,
            "contact_email": enterprise.contact_email,
            "status": enterprise.status
        }

        # WHEN
        response = self.client.put(f"/api/v1/enterprises/{enterprise.id}/", payload)

        # THEN
        assert response.status_code == 200
        assert response.data["name"] == "Updated Enterprise"

    def test_should_delete_enterprise(self):
        # GIVEN
        enterprise = EnterpriseFactory()

        # WHEN
        response = self.client.delete(f"/api/v1/enterprises/{enterprise.id}/")

        # THEN
        assert response.status_code == 204
        assert Enterprise.objects.count() == 0

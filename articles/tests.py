from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Document
from .serializers import DocumentsSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_document(title=""):
        if title != "":
            Document.objects.create(title=title)

    def setUp(self):
        # add test data
        self.create_document("like glue")
        self.create_document("simple document")
        self.create_document("love is wicked")
        self.create_document("jam rock")


class GetAllDocumentsTest(BaseViewTest):

    def get_documents(self):
        """
        This test ensures that all documents added in the setUp method
        exist when we make a GET request to the documents/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("articles-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Document.objects.all()
        serialized = DocumentsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
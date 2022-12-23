
import pytest
from django.urls import reverse_lazy

from home.models import Category


@pytest.mark.django_db
class TestCategoryView:

    @pytest.fixture()
    def categories(self):
        Category.objects.create(name='Texnikalar', parent='telefonlar')
        Category.objects.create(name='Oziq-ovqat', parent='ichimlik-suvlari')

    def test_category_list_api(self, client, categories):
        url = reverse_lazy('category-list')
        response = client.get(url)
        assert response.status_code == 200
        assert len(response.data) == 2

    def test_category_update_api(self, client, categories):
        category = Category.objects.first()
        url = reverse_lazy('category-detail', args=(category.pk,))
        data = {
            'name':'Avtotransport',
            'parent':'velosiped'
        }
        response = client.get(url, data, content_type='application/json')
        assert response.status_code == 200
        assert response.data['name'] == data['name']
        assert response.data['parent'] == data['parent']
        assert response.data['id'] == str(category.pk)


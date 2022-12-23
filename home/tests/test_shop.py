import pytest
from django.urls import reverse_lazy

from home.models import Shop


@pytest.mark.django_db
class TestShopView:

    @pytest.fixture()
    def shops(self):
        Shop.objects.create(name='eco-bazar')
        Shop.objects.create(name='Charsu')

    def test_category_list_api(self, client, shops):
        url = reverse_lazy('shop-list')
        response = client.get(url)
        assert response.status_code == 200
        assert len(response.data) == 2

    def test_shop_update_api(self, client, shops):
        shop = Shop.objects.first()
        url = reverse_lazy('shop-detail', args=(shop.pk,))
        data = {
            'name': 'Malika',
        }
        response = client.get(url, data, content_type='application/json')
        assert response.status_code == 200
        assert response.data['name'] == data['name']
        assert response.data['id'] == str(shop.pk)

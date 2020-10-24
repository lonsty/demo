# @FILENAME : test_api
# @AUTHOR : lonsty
# @DATE : 10/24/20 10:15 PM
import requests

from fastapi_demo.schemas import Item


def test_get_index():
    response = requests.get("http://localhost:8000/")
    assert response.status_code == 200
    assert response.json().get('Hello') == 'World'


def test_get_item_by_id():
    response = requests.get("http://localhost:8000/items/1?q=kw")
    assert response.status_code == 200
    body = response.json()
    assert body.get('item_id') == 1
    assert body.get('q') == 'kw'


def test_put_item():
    item = Item(name='apple', price=12, is_offer=True)
    response = requests.put("http://localhost:8000/items/2", json=item.dict())
    assert response.status_code == 200
    body = response.json()
    assert body.get('item_name') == 'apple'
    assert body.get('item_id') == 2

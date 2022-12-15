from app import app
import json

# def test_get_api_posts():
#
#     resp = app.test_client().get('/api/posts')
#     data = json.loads(resp.data)
#     # print(type(data))
#     # print(data[0])
#     assert resp.status_code == 200
#     assert isinstance(data, list), "Возвращен не список"
#     assert 'poster_name' in data[0], "Нет нужного ключа"  # можно проверить на остальные, но смысла нет
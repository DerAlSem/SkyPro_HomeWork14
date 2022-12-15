from dao.movie import MovieDAO
import json

# Нам пригодится экземпляр DAO, так что мы создадим его в фикстуре
# Но пригодится только один раз, поэтому выносить в conftest не будем
# @pytest.fixture()
# def movie_dao():
#     movie_dao_instance = MovieDAO()
#     return movie_dao_instance


class TestMovieDao:

    def test_get_by_title(self):
        keys_should_be = {"title", "country", "release_year", "genre", "description"}
        movie_dao = MovieDAO()
        movies = movie_dao.get_by_title('4L')
        movie_dict = json.loads(movies)
        assert json.loads(movies), "не валидный JSON"
        assert len(movie_dict) > 0, "возвращается пустой список"
        assert set(movie_dict[0].keys()) == keys_should_be, "неверный список ключей"

    def test_get_by_year_period(self):
        keys_should_be = {"title", "release_year"}
        movie_dao = MovieDAO()
        movies = movie_dao.get_by_year_period(2002, 2005)
        movie_dict = json.loads(movies)
        assert json.loads(movies), "не валидный JSON"
        assert len(movie_dict) > 0, "возвращается пустой список"
        assert set(movie_dict[0].keys()) == keys_should_be, "неверный список ключей"

    def test_get_by_rating(self):
        keys_should_be = {"title", "rating", "description"}
        movie_dao = MovieDAO()
        for rate in ['children', 'family', 'adult']:
            movies = movie_dao.get_by_rating(rate)
            movie_dict = json.loads(movies)
            # print(rate)
            assert json.loads(movies), "не валидный JSON"
            assert len(movie_dict) > 0, "возвращается пустой список"
            assert set(movie_dict[0].keys()) == keys_should_be, "неверный список ключей"

    def test_get_by_genre(self):
        keys_should_be = {"title", "description"}
        movie_dao = MovieDAO()
        for genre in ['Horror', 'Thriller', 'Comedy']:
            movies = movie_dao.get_by_genre(genre)
            movie_dict = json.loads(movies)
            # print(rate)
            assert json.loads(movies), "не валидный JSON"
            assert len(movie_dict) > 0, "возвращается пустой список"
            assert set(movie_dict[0].keys()) == keys_should_be, "неверный список ключей"

    def test_get_two_actors(self):
        movie_dao = MovieDAO()
        actors_list = movie_dao.get_two_actors('Jack Black', 'Dustin Hoffman')
        assert len(actors_list) == 0, "с этими снимаются только 2 раза максимум, поэтому не должно быть результата"
        actors_list = movie_dao.get_two_actors('Rose McIver', 'Ben Lamb')
        assert len(actors_list) > 0, "пустой список, а на этих актерах должно работать"
        actors_list = movie_dao.get_two_actors('Archan Trivedi', 'Rajiv Pathak')
        assert len(actors_list) == 0, "непустой список - на этих должен быть пустой"

    def test_get_by_type_year_genre(self):
        movie_dao = MovieDAO()
        keys_should_be = {"title", "description"}
        movies = movie_dao.get_by_type_year_genre('Movie', 2010, 'Comedie')
        movie_dict = json.loads(movies)
        assert json.loads(movies), "не валидный JSON"
        assert len(movie_dict) > 0, "возвращается пустой список"
        assert set(movie_dict[0].keys()) == keys_should_be, "неверный список ключей"
import sqlite3
import json
from collections import Counter


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        # col[0] is the column name
        d[col[0]] = row[idx]
    return d


class MovieDAO:

    def get_query_result(self, query, to_json = True):
        """
        :return:
        json с результатом запроса
        """
        try:
            with sqlite3.connect("netflix.db") as dbcon:
                if to_json:
                    dbcon.row_factory = dict_factory
                cur = dbcon.cursor()
                cur.execute(query)
                rows = cur.fetchall()
                if to_json:
                    output = json.dumps([dict(ix) for ix in rows])
                else:
                    output = rows
                #print(json_output[0][0])
                #print(query)
                #r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
                #result_dict = (r[0] if r else None) if one else r
                # print(result_dict)
                return output

        except Exception as e:
            print("Exception occurred ", repr(e))
            print(query)


    def get_by_title(self, movie_title):
        query = f"SELECT title, country, release_year, listed_in as genre, description FROM netflix WHERE title LIKE '%{movie_title}%' AND type = 'Movie' ORDER BY release_year LIMIT 1"
        return self.get_query_result(query)

    def get_by_year_period(self, start, end):
        query = f"SELECT title, release_year FROM netflix WHERE release_year BETWEEN {start} AND {end} AND type = 'Movie' ORDER BY title LIMIT 100"
        return self.get_query_result(query)

    def get_by_rating(self, rating):
        ratings_list = "'G', 'PG', 'PG-13', 'R', 'NC-17'"
        if rating == 'children':
            ratings_list = "'G'"
            pass
        if rating == 'family':
            ratings_list = "'G', 'PG', 'PG-13'"
            pass
        if rating == 'adult':
            ratings_list = "'R', 'NC-17'"
        query = f"SELECT title, rating, description FROM netflix WHERE rating IN ({ratings_list}) AND type = 'Movie' ORDER BY title LIMIT 100"
        return self.get_query_result(query)

    def get_by_genre(self, genre):
        query = f"SELECT title, description FROM netflix WHERE listed_in LIKE '%{genre}%' AND type = 'Movie' ORDER BY title LIMIT 100"
        return self.get_query_result(query)

    def get_two_actors(self, actor1, actor2):
        query = f"SELECT `cast` FROM netflix WHERE type = 'Movie' AND `cast` LIKE '%{actor1}%' AND `cast` LIKE '%{actor2}%'"
        all_cast = self.get_query_result(query, False) # из-за особенностей БД тут мы получаем корявый список, его надо переформатировать
        played_two_times = []
        all_actors = [] # а вот сюда мы соберем нормальный список всех актеров
        for actors in all_cast:
            for actor in actors[0].split(', '):
                all_actors.append(actor)
        actors_appearing = Counter(all_actors)
        for actor in actors_appearing:
            if actors_appearing[actor] > 2:
                if actor != actor1 and actor != 2:
                    played_two_times.append(actor)
        return played_two_times

    def get_by_type_year_genre(self, type, year, genre):
        query = f"SELECT title, description FROM netflix WHERE type = '{type}' AND release_year = {year} AND listed_in LIKE '%{genre}%'"
        return self.get_query_result(query)
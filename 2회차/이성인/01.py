import requests
from dotenv import load_dotenv
import os
load_dotenv()


def popular_count():
    movies_condition = "popular"
    BASE_url = "https://api.themoviedb.org/3"
    path = f'/movie/{movies_condition}'
    params = {
        'api_key':os.environ.get("API"),
        'language': 'ko-KR'
    }
    response = requests.get(BASE_url + path, params=params).json()
    movies = response.get('results') # [1].get('title')
    n = len(movies)
    cnt = 0
    for i in range(n):
        cnt += 1

    return (cnt)
    # for i in len(movies):
    #     print(movies[i].get("title"))

    




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20

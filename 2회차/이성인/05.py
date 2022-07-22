import requests
from pprint import pprint
from dotenv import load_dotenv
import os
os.environ.get("API")
load_dotenv()



def credits(title):
    BASE_url = "https://api.themoviedb.org/3"
    path = f'/search/movie'
    params = {
        'api_key': os.environ.get("API") , 
        'language': 'ko-KR',
        'query' : f"{title}"
    } 
    dict_people = {}
    response = requests.get(BASE_url + path, params=params).json()
    movies = response.get('results')
    if movies != []:
        id_ = movies[0].get ('id')
        path = f'/movie/{id_}/credits'
        response2 = requests.get(BASE_url + path, params=params).json()
        list1 = []
        list2 = []
        casts = response2.get('cast')
        for cast in casts:
            if cast.get('cast_id') < 10:
                list1.append(cast.get('name'))

        crews = response2.get('crew')
        for crew in crews:
            if crew.get('department') == "Directing" :
                list2.append(crew.get('name'))
        dict_people["cast"] = list1
        dict_people["crew"] = list2

    return dict_people

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None

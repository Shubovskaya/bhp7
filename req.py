from requests import Session

# ?player_type[0]=hifiplayer&player_type[operation]=union&group=1
def get_response():
    with Session() as session:
        session.headers.update({'Accept-Language': 'ru'})
        response = session.get(
            url='https://catalog.onliner.by/sdapi/catalog.api/search/player',
            params={
                'player_type[0]':'hifiplayer',
                'player_type[operation]': 'union',
                'group': 1
            }
        )
        print(response.status_code)
        print(response.headers)
        print(response.text)
        print(response.json())
get_response()
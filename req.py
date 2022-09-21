from aiohttp import ClientSession
import asyncio

async def get_wss():
    async with ClientSession() as session:
        async with session.ws_connect(
            url='wss://demo.piesocket.com/v3/channel_1?api_key=VCXCEuvhGcBDP7XhiJJUDvR1e1D3eiVjgZ9VRiaV&notify_self'
        ) as wss:
            async for message in wss:
                print(message.data)
                await wss.send_str('in')


asyncio.run(get_wss())

#
# async def get_response():
#     async with ClientSession(
#         base_url='https://catalog.onliner.by'
#     ) as session:
#         async with session.get(
#             url='/sdapi/catalog.api/search/player',
#             params={
#                 'player_type[0]':'hifiplayer',
#                 'player_type[operation]': 'union',
#                 'group': 1
#             }
#         ) as response:
#             print(response.status)
#             print(response.headers)
#             print(response.url)
#             print(await response.text())
#             print(await response.json())
#
# import asyncio
# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# asyncio.run(get_response())


















# from requests import Session
#
#
# # ?player_type[0]=hifiplayer&player_type[operation]=union&group=1
# def get_response():
#     with Session() as session:
#         session.headers.update({'Accept-Language': 'ru'})
#         response = session.get(
#             url='https://catalog.onliner.by/sdapi/catalog.api/search/player',
#             params={
#                 'player_type[0]':'hifiplayer',
#                 'player_type[operation]': 'union',
#                 'group': 1
#             }
#         )
#         print(response.status_code)
#         print(response.headers)
#         print(response.text)
#         print(response.json())
#
#
# for i in range
# get_response()
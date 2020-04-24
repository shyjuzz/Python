import aiohttp
import asyncio
from types import SimpleNamespace
import json
def recursive_vars(dic):
    items = {}
    for key in dic:
        if type(dic[key]) is SimpleNamespace:
            items [key] = recursive_vars(vars(dic[key]))
        else:
            items [key] = dic[key]
    return items


async def test():
    discourse_ctx = SimpleNamespace(dialog_state=0)
    req = SimpleNamespace(text='account management', discourse_ctx=discourse_ctx,job="mvc", targets=['pil','conv'], debug=False )

    # async with aiohttp.ClientSession() as session:
    #     async with session.get('http://3.14.98.212:8085/reset') as resp:
    #         print(resp.status)
    #         print(await resp.text())
    host = '127.0.0.1'
    port=3030
    async with aiohttp.ClientSession() as session:
        async with session.post(f'http://{host}:{port}', json = json.dumps(recursive_vars(vars(req)))) as rest_resp:
            recv = await rest_resp.json()
            return make_obj(recv)


loop = asyncio.get_event_loop()
res = loop.run_until_complete(test())
print('Response : ',resp)
loop.close()

import asyncio,aiohttp
print(1)
@asyncio.coroutine
def handle_url_xxx(request):
	url_param=request.match_info['key']
	query_params=parse_qs(request.query_string)
	text=render('template',data)
	return web.Response(text.encode('utf8'))
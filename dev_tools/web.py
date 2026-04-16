from ddgs import DDGS
'''
results = DDGS().text("youtube",safesearch='off',backend="auto", max_results=3)
print(results)

results = DDGS().images(
    query="",
    region="us-en",
    safesearch="off",
    timelimit =None,
    page=1,
    backend="auto",
    size=None,
    color="Monochrome",
    type_image=None,
    layout=None,
    license_image=any,
    max_results =5
)
print(results)

results = DDGS().videos(
    query="",
    region="us-en",
    safesearch="off",
    timelimit=None,
    page=1,
    backend="auto",
    resolution="high",
    duration="medium",
    license_videos =None,
    max_results=3
)
print(results)

result = DDGS().extract("https://lmstudio.ai/danielsig/duckduckgo")
print(result)
'''
results = DDGS().news(query="sun", region="us-en", safesearch="off", timelimit="m", page=1, backend="auto",max_results=1)
print(results)
results = DDGS().books(query="sea wolf jack london", page=1, backend="auto",max_results=1)
print(results)
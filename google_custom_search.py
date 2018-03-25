from googleapiclient.discovery import build


#Google custom search engine id and api key
my_api_key = "yourkey";
my_cse_id = "your cse id";


#performs the google search
def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

results = google_search('python', my_api_key, my_cse_id, num=10);
for res in results:
    print(res['formattedUrl'])
    #print(res['link'])

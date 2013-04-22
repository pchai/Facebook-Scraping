import requests
import os
import simplejson as json
import sys

def make_request(url, params):
    try:
        r = requests.get(url, params=params)
        print r.url
        resp = json.dumps(r.json(), sort_keys=True,
                        indent=4, separators=(',', ': '))
    except:
        print sys.exc_info()[0]
        resp = '{"Error":"Error detected by my scirpt"}'
        raise
    data = json.loads(resp)
    return data

def get_data(url):
    try:
        r = requests.get(url)
        if r.json():
            resp = json.dumps(r.json(), sort_keys=True,
                    indent=4, separators=(',', ': '))
    except:
        print sys.exc_info()[0]
        resp = '{"Error":"Error detected by my scirpt"}'
        raise
    data = json.loads(resp)
    return data

if __name__ == "__main__":
    access_token = "174501439374420|wSEWGTm0qQG-Dr5DUlOTmTL2WOA"
    header = "https://graph.facebook.com/"
    query = "?fields=comments.limit(50000).fields(created_time,id,message,from,comments.limit(5000).fields(created_time,id,message,from)),likes.limit(50000).fields(name,id)"
    payload1 = {"access_token" : access_token, "fields":"posts", }
    payload_token = {"access_token" : access_token}
    data = make_request(header + "415541435185463_471052996300973" + query, payload_token)

    # if "posts" in data:
    #         posts = data["posts"]
    #         for post in posts["data"]:
    #             data =  make_request(header + post["id"] + query, params=payload_token)
    #             print json.dumps(data, sort_keys=True,
    #                         indent=4, separators=(',', ': '))
    #             break
    #print get_data("https://graph.facebook.com/471052976300975_1384737/comments?fields=created_time,id,message,from&limit=25&after=MjY=")




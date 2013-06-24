import requests
import os
import simplejson as json
import sys

def pretty_write(var, f):
	f.write(json.dumps(var, sort_keys=True,
						indent=4, separators=(',', ': ')))
def write_post(post, f):
	res = {}
	try:
		if "id" in post:
			res["id"] = post["id"]
		if "likes" in post and "count" in post["likes"]:
			res["likes"] = {"count": post["likes"]["count"]}

		if "comments" in post and "count" in post["comments"]:
			res["comments"] = {"count": post["comments"]["count"]}

		if "shares" in post and "count" in post["shares"]:
			res["shares"] = {"count": post["shares"]["count"]}
		if "message" in post:
			res["message"] = post["message"]
		if "type" in post:
			res["type"] = post["type"]
		if "created_time" in post:
			res["created_time"] = post["created_time"]
		if "description" in post:
			res["description"] = post["description"]
		if "picture" in post:
			res["picture"] = post["picture"]
		if "updated_time" in post:
			res["updated_time"] = post["updated_time"]
	except KeyError:
		print "KeyError writing post"
	f.write(json.dumps(res, sort_keys=True,
						indent=4, separators=(',', ': ')))

def make_request(url, params):
	try:
		r = requests.get(url, params=params)
		resp = json.dumps(r.json(), sort_keys=True,
						indent=4, separators=(',', ': '))
	except:
		print sys.exc_info()[0]
		resp = '{"Error":"Error detected by scraping scirpt"}'
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
		resp = '{"Error":"Error detected by scraping scirpt"}'
	data = json.loads(resp)
	return data

if __name__ == "__main__":
	access_token = "174501439374420|wSEWGTm0qQG-Dr5DUlOTmTL2WOA"
	header = "https://graph.facebook.com/"
	query = "?fields=comments.limit(50000).fields(created_time,id,message,from,comments.limit(5000).fields(created_time,id,message,from)),likes.limit(50000).fields(name,id)"
	fu = open('users.txt', 'r')
	users = fu.readlines()
	for user in users:
		user = user.strip("\n")
		print "Processing " + user
		payload1 = {"access_token" : access_token, "fields":"posts", }
		payload_token = {"access_token" : access_token}
		data = make_request(header + user, params=payload1)

		if not os.path.exists(user):
			os.makedirs(user)
		if "posts" in data:
			posts = data["posts"]
			while True:
				for post in posts["data"]:
					print post[""]
					break
					filename = user + "/" + post["created_time"]
					if not os.path.exists(filename):
						fw = open(filename, "w+")
						fw.write("{")
						fw.write('"post":')
						write_post(post, fw)
						fw.write(",")
						data =  make_request(header + post["id"] + query, params=payload_token)
						if "comments" in data:
							fw.write('"comments":')
							pretty_write(data["comments"], fw)

						if "likes" in data:
							fw.write('"likes":')
							pretty_write(data["likes"],fw)
							fw.write("}")

				if "paging" in posts and "next" in posts["paging"]:
					print "Goint to next page of posts"
					posts = get_data(posts["paging"]["next"])
				else:
					break






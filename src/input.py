import requests
import json

from typing import List, Dict, Tuple


class Input(object):
    def __init__(self, subreddit :str, start_date :int, end_date :int, size :int=1000) -> None:
        self.subreddit = subreddit
        self.start_date = start_date
        self.end_date = end_date
        self.size = size

    def make_url(self, start_date = None) -> str:
        if start_date is None:
            start_date = self.start_date
        return f"https://api.pushshift.io/reddit/search/comment/?subreddit={self.subreddit}&after={start_date}&before={self.end_date}&fields=author,created_utc&size={self.size}"

    # this function is adapted from Medium article @ https://medium.com/@RareLoot/using-pushshifts-api-to-extract-reddit-submissions-fb517b286563
    def getPushshiftData(self, url: str) -> List[Dict]:
        print(url)
        r = requests.get(url)  # sends a HTTP request and gets a response object
        data = json.loads(r.text)
        print(len(data["data"]))  # gives the number of JSON objects from URL
        return data["data"]  # data["data"] is a list of dicts

    def getAuthorCount(self, JSONobject: List[Dict], author_count_dict = {}) -> Dict[str, int]:
        author_list = []
        count = 0
        latest_date = None
        for dict in JSONobject:
            author = dict["author"]
            if not author in author_list:
                author_list.append(author)
            if author in author_count_dict:
                author_count_dict[author] += 1
            else:
                author_count_dict[author] = 1
            count += 1
        if count == 1000:
            latest_date = dict["created_utc"]
            print(latest_date)
            return self.getAuthorCount(self.getPushshiftData(self.make_url(start_date=latest_date)), author_count_dict)
        # print(author_list)
        # print(author_count_dict)
        return self.clean_dict(author_count_dict, author_list)

    def clean_dict(self, author_count_dict, author_list) -> None:
        cleaned_count_dict = {}
        cleaned_author_list = []
        for author in author_list:  # removes entries that have less than 5 and count for [deleted]
            if author_count_dict[author] >= 5 and author != "[deleted]":
                new_entry = {str(author): author_count_dict[author]}
                cleaned_count_dict.update(new_entry)
                cleaned_author_list.append(author)
        print(cleaned_author_list) # will give a list of usernames that have posted at least 5 times
        print(cleaned_count_dict)
        print(f"with5 measure: {len(cleaned_count_dict)}")
        return cleaned_count_dict


if __name__ == "__main__":
    input1 = Input("UCDavis", 1592438400, 1593043200) # users who posted in r/UCDavis between Thursday, June 18, 2020 12:00:00 AM (GMT) and Thursday, June 25, 2020 12:00:00 AM (GMT)
    url1 = input1.make_url()
    JSONobject1 = input1.getPushshiftData(url1)
    input1.getAuthorCount(JSONobject1)

    input2 = Input("UCDavis", 1590364800, 1593043200) # users who posted in r/UCDavis between Monday, May 25, 2020 12:00:00 AM (GMT) and Thursday, June 25, 2020 12:00:00 AM (GMT)
    url2 = input2.make_url()
    JSONobject2 = input2.getPushshiftData(url2)
    input2.getAuthorCount(JSONobject2)

    input3 = Input("BROCKHAMPTON", 1590364800, 1593043200) # users who posted in r/BROCKHAMPTON between Monday, May 25, 2020 12:00:00 AM (GMT) and Thursday, June 25, 2020 12:00:00 AM (GMT)
    url3 = input3.make_url()
    JSONobject3 = input3.getPushshiftData(url3)
    input3.getAuthorCount(JSONobject3)

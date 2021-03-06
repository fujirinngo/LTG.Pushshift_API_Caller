import requests
import json
import time

from typing import List, Dict


class Input(object):
    def __init__(self, subreddit :str, start_date :int, end_date :int, size :int=100) -> None:
        self.subreddit = subreddit
        self.start_date = start_date
        self.end_date = end_date
        self.size = size
        self.ratelimit = 0
        self.author_list = []
        self.author_count_dict = {}
        self.obj_processed_count = 0
        self.with5_measure = 0

    def get_ratelimit(self):
        r = requests.get("https://api.pushshift.io/meta")
        metadata = json.loads(r.text)
        print(metadata["server_ratelimit_per_minute"])
        self.ratelimit = metadata["server_ratelimit_per_minute"]

    def make_url_for_submissions(self, start_date = None) -> str:
        if start_date is None:
            start_date = self.start_date
        return f"https://api.pushshift.io/reddit/search/submission/?subreddit={self.subreddit}&after={start_date}&before={self.end_date}&fields=author,created_utc&size={self.size}"

    def make_url_for_comments(self, start_date = None) -> str:
        if start_date is None:
            start_date = self.start_date
        return f"https://api.pushshift.io/reddit/search/comment/?subreddit={self.subreddit}&after={start_date}&before={self.end_date}&fields=author,created_utc&size={self.size}"

    # this function is adapted from Medium article @ https://medium.com/@RareLoot/using-pushshifts-api-to-extract-reddit-submissions-fb517b286563
    def getPushshiftData(self, url: str) -> List[Dict]:
        try_count = 1
        while try_count < 5:
            try:
                time.sleep(60/self.ratelimit)
                r = requests.get(url)  # sends a HTTP request and gets a response object
                data = json.loads(r.text)
                print("Processing", len(data["data"]), "items")  # gives the number of JSON objects from URL
                return data["data"]  # data["data"] is a list of dicts
            except:
                print("Pausing and trying again...")
                time.sleep(30)
                try_count += 1

    def get_author_count_for_submissions(self, JSONobject: List[Dict]) -> None:
        count = 0
        for dict in JSONobject:
            author = dict["author"]
            if not author in self.author_list:
                self.author_list.append(author)
            if author in self.author_count_dict:
                self.author_count_dict[author] += 1
            else:
                self.author_count_dict[author] = 1
            count += 1
            self.obj_processed_count += 1
        if count == self.size:
            latest_date = dict["created_utc"]
            return self.get_author_count_for_submissions(self.getPushshiftData(self.make_url_for_submissions(start_date=latest_date)))
        return self.author_count_dict

    def get_author_count_for_comments(self, JSONobject: List[Dict]) -> None:
        count = 0
        for dict in JSONobject:
            author = dict["author"]
            if not author in self.author_list:
                self.author_list.append(author)
            if author in self.author_count_dict:
                self.author_count_dict[author] += 1
            else:
                self.author_count_dict[author] = 1
            count += 1
            self.obj_processed_count += 1
        if count == self.size:
            latest_date = dict["created_utc"]
            return self.get_author_count_for_comments(self.getPushshiftData(self.make_url_for_comments(start_date=latest_date)))
        return self.author_count_dict

    def clean_dict(self) -> Dict[str, int]:
        cleaned_count_dict = {}
        cleaned_author_list = []
        for author in self.author_list:  # removes entries that have less than 5 and count for [deleted]
            if self.author_count_dict[author] >= 5 and author != "[deleted]":
                new_entry = {str(author): self.author_count_dict[author]}
                cleaned_count_dict.update(new_entry)
                cleaned_author_list.append(author)
        self.with5_measure = len(cleaned_count_dict)
        print(cleaned_count_dict) # will give a list of usernames that have posted at least 5 times and corresponding counts
        print(f"with5 measure for r/{self.subreddit}: {self.with5_measure}")
        print("Total objects processed: ", self.obj_processed_count)
        return cleaned_count_dict


if __name__ == "__main__":
    #Example 1:
    input1 = Input("UCDavis", 1592438400, 1593043200) # users who posted in r/UCDavis between Thursday, June 18, 2020 12:00:00 AM (GMT) and Thursday, June 25, 2020 12:00:00 AM (GMT)
    url1_for_submissions = input1.make_url_for_submissions()
    JSONobject_for_submissions = input1.getPushshiftData(url1_for_submissions)
    input1.get_author_count_for_submissions(JSONobject_for_submissions)

    url1_for_comments = input1.make_url_for_comments()
    JSONobject_for_comments = input1.getPushshiftData(url1_for_comments)
    input1.get_author_count_for_comments(JSONobject_for_comments)
    input1.clean_dict()

    # RESULT: with5 measure for r/UCDavis: 81
    #         Total objects processed:  1708

    # Example 1.1:
    input1_1 = Input("UCDavis", 1592438400, 1593043200)  # users who posted in r/UCDavis between Thursday, June 18, 2020 12:00:00 AM (GMT) and Thursday, June 25, 2020 12:00:00 AM (GMT)
    url1_1_for_submissions = input1_1.make_url_for_submissions()
    JSONobject_for_submissions = input1_1.getPushshiftData(url1_for_submissions)
    input1_1.get_author_count_for_submissions(JSONobject_for_submissions)
    input1_1.clean_dict()

    # RESULT: with5 measure for r/UCDavis: 1
    #         Total objects processed:  231

    # Example 1.2:
    input1_2 = Input("UCDavis", 1592438400, 1593043200)  # users who commented in r/UCDavis between Thursday, June 18, 2020 12:00:00 AM (GMT) and Thursday, June 25, 2020 12:00:00 AM (GMT)
    url1_2_for_comments = input1_2.make_url_for_comments()
    JSONobject_for_submissions = input1_2.getPushshiftData(url1_for_comments)
    input1_2.get_author_count_for_comments(JSONobject_for_comments)
    input1_2.clean_dict()


    # Example 2:
    input2 = Input("UCDavis", 1590364800, 1593043200) # users who posted and/or commented in r/UCDavis between Monday, May 25, 2020 12:00:00 AM (GMT) and Thursday, June 25, 2020 12:00:00 AM (GMT)
    url2s = input2.make_url_for_submissions()
    JSONobject2s = input2.getPushshiftData(url2s)
    input2.get_author_count_for_submissions(JSONobject2s)

    url2c = input2.make_url_for_comments()
    JSONobject2c = input2.getPushshiftData(url2c)
    input2.get_author_count_for_comments(JSONobject2c)
    input2.clean_dict()

    # RESULTS: with5 measure: 409
    #          Total objects processed: 7550

    # Example 3:
    input3 = Input("malefashionadvice", 1590364800, 1593043200) # users who posted and/or commented in r/malefashionadvice between Monday, May 25, 2020 12:00:00 AM (GMT) and Thursday, June 25, 2020 12:00:00 AM (GMT)
    url3s = input3.make_url_for_submissions()
    JSONobject3s = input3.getPushshiftData(url3s)
    input3.get_author_count_for_submissions(JSONobject3s)

    url3c = input3.make_url_for_comments()
    JSONobject3c = input3.getPushshiftData(url3c)
    input3.get_author_count_for_comments(JSONobject3c)
    input3.clean_dict()

    # RESULT: with5 measure for r/malefashionadvice: 991
    #         Total objects processed:  33806
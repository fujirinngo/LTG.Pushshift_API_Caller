import unittest

from src.input import Input
import json

class TestInput(unittest.TestCase):
    def test_make_url(self): # tests if make_url() works
        input = Input("UCDavis", 1234567890, 9876543210)
        self.assertEqual(input.make_url_for_submissions(), "https://api.pushshift.io/reddit/search/submission/?subreddit=UCDavis&after=1234567890&before=9876543210&fields=author,created_utc&size=500")

    def test_get_author_count_v1(self):
        input = Input("FakeSubreddit", 1592438400, 1593043200)
        with open("./sample_json/simple_only5.json") as f:
            JSONobject = json.load(f)
            input.get_author_count_for_submissions(JSONobject['data'])
            author_count_dict = input.author_count_dict
        self.assertEqual(author_count_dict, {'JoeSchmoe': 5})

    def test_get_author_count_v2(self):
        input = Input("FakeSubreddit", 1592438400, 1593043200)
        with open("./sample_json/mix.json") as f:
            JSONobject = json.load(f)
            input.get_author_count_for_submissions(JSONobject['data'])
            author_count_dict = input.author_count_dict
        self.assertEqual(author_count_dict, {'JoeSchmoe': 5, 'ChickenTenderFan': 5,'reddit_user123': 3})

    def test_clean_dict(self):
        Input.subreddit = "FakeSubreddit"
        Input.author_count_dict = {'JoeSchmoe': 3, 'RedditUser123': 5, '[deleted]': 8, 'OfficialUCDavis': 12}
        Input.author_list = ['JoeSchmoe', 'RedditUser123', '[deleted]', 'OfficialUCDavis']
        cleaned_dict = Input.clean_dict(Input)
        self.assertEqual(cleaned_dict, {'RedditUser123': 5, 'OfficialUCDavis': 12})

    def test_clean_dict_all_below5(self):
        Input.subreddit = "FakeSubreddit"
        Input.author_count_dict = {'JoeSchmoe': 3, 'ChickenTenderLover': 1, '[deleted]': 20, 'AbacusWizard': 4}
        Input.author_list = ['JoeSchmoe', 'ChickenTenderLover', '[deleted]', 'AbacusWizard']
        cleaned_dict = Input.clean_dict(Input)
        self.assertEqual(cleaned_dict, {})



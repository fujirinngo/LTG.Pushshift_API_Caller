import unittest

from src.input import Input

class TestInput(unittest.TestCase):
    def test_make_url(self): # tests if make_url() works
        input = Input("UCDavis", 1234567890, 9876543210)
        self.assertEqual(input.make_url(), "https://api.pushshift.io/reddit/search/comment/?subreddit=UCDavis&after=1234567890&before=9876543210&fields=author,created_utc&size=1000")

    def test_getAuthorCount_v2(self):
        input2 = Input("UCDavis", 1592438400, 1593043200, size=50)
        url2 = input2.make_url()
        JSONobject2 = input2.getPushshiftData(url2)
        author_count_dict2 = input2.getAuthorCount(JSONobject2)
        self.assertEqual(author_count_dict2, {'daintyelephanttbh': 5})

    # def test_getAuthorCount_size_over1000(self):
    #     input3 = Input("UCDavis", CHANGE, 1593043200, size=1000) # put like 2 weeks or something

    def test_clean_dict(self):
        cleaned_dict = Input.clean_dict(Input, {'JoeSchmoe': 3, 'RedditUser123': 5, '[deleted]': 8, 'OfficialUCDavis': 12},
                                        ['JoeSchmoe', 'RedditUser123', '[deleted]', 'OfficialUCDavis'])
        self.assertEqual(cleaned_dict, {'RedditUser123': 5, 'OfficialUCDavis': 12})

    def test_clean_dict_all_below5(self):
        cleaned_dict = Input.clean_dict(Input, {'JoeSchmoe': 3, 'ChickenTenderLover': 1, '[deleted]': 20, 'AbacusWizard': 4},
                                        ['JoeSchmoe', 'ChickenTenderLover', '[deleted]', 'AbacusWizard'])
        self.assertEqual(cleaned_dict, {})

if __name__ == '__main__':
    unittest.main()

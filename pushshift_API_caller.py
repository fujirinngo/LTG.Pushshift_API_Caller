import sys
from src.input import Input
from src.date_converter import convert2unix

if __name__ == "__main__":
    subreddit_list = ["UCDavis", "BROCKHAMPTON", "MachineLearning"] # should this be a parameter for a function instead?
    start_datetime = convert2unix("06/01/2020 00:00:00")
    end_datetime = convert2unix("06/08/2020 00:00:00")
    for subreddit in subreddit_list:
        print(f'Currently processing "r/{subreddit}"')
        input = Input(subreddit, start_datetime, end_datetime)
        url_for_submissions = input.make_url_for_submissions()
        JSONobject_for_submissions = input.getPushshiftData(url_for_submissions)
        input.get_author_count_for_submissions(JSONobject_for_submissions)

        url_for_comments = input.make_url_for_comments()
        JSONobject_for_comments = input.getPushshiftData(url_for_comments)
        input.get_author_count_for_comments(JSONobject_for_comments)

        input.clean_dict()




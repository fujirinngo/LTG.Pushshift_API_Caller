import json
from src.input import Input
from src.date_converter import convert2unix

if __name__ == "__main__":
    subreddit_list = ["UCDavis"] # should this be a parameter for a function instead?
    start_datetime = convert2unix("06/01/2020 00:00:00") # edit this for desired start date & time
    end_datetime = convert2unix("06/08/2020 00:00:00") # edit this for desired end date & time
    jsonl_list = []
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

        jsonl_info4subreddit = {"subreddit": subreddit, "with5 measure": input.with5_measure,
                                "author count dict": input.author_count_dict,
                                "author count": len(input.author_list), "gross post count": input.obj_processed_count,
                                "start date": input.start_date, "end date": input.end_date}
        jsonl_list.append(jsonl_info4subreddit)

    print(jsonl_list)

    with open(f'output_from{start_datetime}_to{end_datetime}.jsonl', 'w') as outfile:
        for entry in jsonl_list:
            json.dump(entry, outfile)
            outfile.write('\n')




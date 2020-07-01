from datetime import datetime
import pytz

from typing import List

def convert2unix(dt_str :str) -> int:
    dt_parsed = parse_date(dt_str)
    dt = datetime(dt_parsed[2], dt_parsed[0], dt_parsed[1], dt_parsed[3], dt_parsed[4], dt_parsed[5], tzinfo=pytz.utc)
    print(int(dt.timestamp()))
    return int(dt.timestamp())

def parse_date(dt_str :str) -> List[int]:
    dt_obj = datetime.strptime(dt_str, '%m/%d/%Y %H:%M:%S')
    month = int(dt_obj.date().month)
    day = int(dt_obj.date().day)
    year = int(dt_obj.date().year)
    hour = int(dt_obj.time().hour)
    minute = int(dt_obj.time().minute)
    second = int(dt_obj.time().second)

    return [month, day, year, hour, minute, second]

if __name__ == "__main__":
    convert2unix("06/24/2020 00:00:00") # remember midnight is 00:00:00
    convert2unix("06/25/2020 00:00:00")


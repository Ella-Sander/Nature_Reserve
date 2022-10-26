import pandas
import datetime
import map

import pandas as pd

import consts
import numpy as n

Nature_reserves = pandas.read_csv(consts.NATURE_RESERVES_FILE)


def start_Nature_reserves():
    Nature_reserves["Last_clean_date"] = n.nan
    Nature_reserves["Last_clean_date"] = pd.to_datetime(Nature_reserves["Last_clean_date"])
    Nature_reserves.to_csv(consts.NATURE_RESERVES_FILE)
    print(Nature_reserves)


def update_last_clean_date(date, place_name):
    for index, location_info in Nature_reserves.iterrows():
        if location_info["Name"] == place_name:
            Nature_reserves.at[index, "Last_clean_date"] = date
    Nature_reserves.to_csv(consts.NATURE_RESERVES_FILE, index=False, na_rep='Unknown')


def is_time_out(place_name):
    now = datetime.datetime.now()
    for index, location_info in Nature_reserves.iterrows():
        if location_info["Name"] == place_name and location_info["Last_clean_date"] != n.nan:
            print(location_info["Last_clean_date"])
            if now - pd.to_datetime(location_info["Last_clean_date"]) >= consts.CLEAN_FREQUENCY:
                return True
            else:
                return False
    return False


def update_status():
    for index, location_info in Nature_reserves.iterrows():
        if not location_info["Status"]:
            if location_info["Reports"] == consts.MAX_REPORTS:
                Nature_reserves.at[index, "Status"] = True

        if location_info["Status"]:
            if is_time_out(location_info["Name"]):
                Nature_reserves.at[index, "Status"] = False
                Nature_reserves.at[index, "Last_clean_date"] = n.nan
                Nature_reserves.at[index, "Reports"] = 0
    Nature_reserves.to_csv(consts.NATURE_RESERVES_FILE, index=False, na_rep='Unknown')


def report(place_name):
    for index, location_info in Nature_reserves.iterrows():
        if location_info["Name"] == place_name and not location_info["Status"]:
            if location_info["Reports"] < consts.MAX_REPORTS:
                Nature_reserves.at[index, "Reports"] = 1 + location_info["Reports"]
                Nature_reserves.to_csv(consts.NATURE_RESERVES_FILE, index=False, na_rep='Unknown')
                print("Report completed")
                break


def get_dirty_places_lst():
    dirty_places_lst = []
    for index, location_info in Nature_reserves.iterrows():
        if not location_info["Status"]:
            dirty_places_lst.append(location_info["Name"])

    return dirty_places_lst


def main():
    update_status()
    start_Nature_reserves()
    map.run_map()
    input1 = input("Enter place to clean:")

    while input1 != "Stop":
        print(report(input1))
        now = datetime.datetime.now()
        update_last_clean_date(now, input1)
        print(Nature_reserves["Reports"])
        input1 = input("Enter place to clean:")

    update_status()
    print(Nature_reserves["Status"])
    map.run_map()


main()

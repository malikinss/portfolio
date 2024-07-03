'''
TODO:
        Timur plans to go to the pool.

        Of all the pools, those that are open on Monday from 10:00 to 12:00
        are suitable for him.

        He also likes to swim in long lanes, so of all the pools that are open
        at this time, you need to choose the pool with the longest lane, and
        with equal values ​​- with the widest one.

        You can access the pools.json file, which contains a list of JSON
        objects that represent data on indoor swimming pools:
            [
                {
                    "ObjectName": "Physical Culture and Health Complex with a Swimming Pool 'State Budgetary Institution 'Sports School No. 82' of the Moscow Sports Committee'",
                    "AdmArea": ​​"North-Eastern Administrative Okrug",
                    "District": "Altufevsky District",
                    "Address": "Inzhenernaya Street, Building 5, Building 1",
                    "WorkingHoursSummer": {
                        "Monday": "10:00-11:00",
                        "Tuesday": "10:00-11:00",
                        "Wednesday": "10:00-11:00",
                        "Thursday": "10:00-11:00",
                        "Friday": "10:00-11:00",
                        "Saturday": "10:00-11:00",
                        "Sunday": "09:00-15:00",
                    },
                    "DimensionsSummer": {
                        "Square": 350,
                        "Length": 25,
                        "Width": 14,
                        "Depth": 1.8
                    }
                },
                ...
            ]

        By "pool" we mean one JSON object from this list.

        The pool has the following attributes:
            ObjectName — name, whether it is a fitness club or a sports complex
            AdmArea — administrative district
            District — name of the district
            Address — address
            WorkingHoursSummer — working hours, start and close times are
            specified in the HH:MM format
            DimensionsSummer — dimensions of the pool, where Square is the
            area, Length is the length, Width is the width, Depth is the depth

        Write a program that determines the pool that is suitable for Timur.
        The program should output its dimensions and address in
        the following format:
            <length>x<width>
            <address>

NOTE:
        Example output:
            25x16
            Pistcovaya street, house 12, building 1

        The pool must be open during the entire period from 10:00 to 12:00.

        For example, if the pool is open at 10:00, but not at 11:30,
        it is not suitable.
'''
import json
from typing import Dict, List, Any
from datetime import datetime


def read_json_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Read JSON data from a file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        List[Dict[str, Any]]: List of dictionaries containing JSON data.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def find_max_dimension(pools: List[Dict[str, Any]], dimension: str) -> int:
    """
    Find the maximum value of a given dimension in a list of pools.

    Args:
        pools (List[Dict[str, Any]]): List of pool dictionaries.
        dimension (str): The dimension to find the maximum value for ('Length'
        or 'Width')

    Returns:
        int: The maximum value of the specified dimension.
    """
    return max(pool['DimensionsSummer'][dimension] for pool in pools)


def get_pools_with_max_dimension(pools: List[Dict[str, Any]],
                                 dimension: str) -> List[Dict[str, Any]]:
    """
    Get pools with the maximum value of a given dimension.

    Args:
        pools (List[Dict[str, Any]]): List of pool dictionaries.
        dimension (str): The dimension to filter pools by ('Length' or 'Width')

    Returns:
        List[Dict[str, Any]]: List of pools with the maximum value of the
        specified dimension.
    """
    max_value = find_max_dimension(pools, dimension)

    return [pool for pool in pools if pool['DimensionsSummer'][dimension] == max_value]


def get_working_hours(pool: Dict[str, Any], day: str) -> List[str]:
    """
    Get the working hours of a pool on a specific day.

    Args:
        pool (Dict[str, Any]): The pool dictionary.
        day (str): The day to get the working hours for.

    Returns:
        List[str]: The start and end times as a list of strings.
    """
    return pool['WorkingHoursSummer'][day].split('-')


def is_time_in_range(start_time: str,
                     end_time: str,
                     requiring_time: str) -> bool:
    """
    Check if a time is within a given range.

    Args:
        start_time (str): The start time in HH:MM format.
        end_time (str): The end time in HH:MM format.
        requiring_time (str): The time to check in HH:MM format.

    Returns:
        bool: True if the time is within the range, False otherwise.
    """
    time_format = '%H:%M'

    start = datetime.strptime(start_time, time_format).time()
    end = datetime.strptime(end_time, time_format).time()
    required = datetime.strptime(requiring_time, time_format).time()

    return start <= required <= end


def get_pools_open_at(pools: List[Dict[str, Any]],
                      day: str,
                      start_time: str,
                      end_time: str) -> List[Dict[str, Any]]:
    """
    Get pools that are open during a specific time range on a specific day.

    Args:
        pools (List[Dict[str, Any]]): List of pool dictionaries.
        day (str): The day to check.
        start_time (str): The start time in HH:MM format.
        end_time (str): The end time in HH:MM format.

    Returns:
        List[Dict[str, Any]]: List of pools open during the specified
        time range.
    """
    required_pools = []

    for pool in pools:
        cur_start_time, cur_end_time = get_working_hours(pool, day)

        if is_time_in_range(cur_start_time, cur_end_time, start_time) and is_time_in_range(cur_start_time, cur_end_time, end_time):
            required_pools.append(pool)

    return required_pools


def print_pool_info(pool: Dict[str, Any]) -> None:
    """
    Print the size and address of a pool.

    Args:
        pool (Dict[str, Any]): The pool dictionary.
    """
    length = pool['DimensionsSummer']['Length']
    width = pool['DimensionsSummer']['Width']
    address = pool['Address']

    print(f"{length}x{width}")
    print(address)


def find_suitable_pool(pools: List[Dict[str, Any]],
                       day: str,
                       start: str,
                       end: str) -> Dict[str, Any]:
    """
    Find the most suitable pool for swimming based on given criteria.

    Args:
        pools (List[Dict[str, Any]]): List of pool dictionaries.
        day (str): The day to check.
        start (str): The start time in HH:MM format.
        end (str): The end time in HH:MM format.

    Returns:
        Dict[str, Any]: The most suitable pool dictionary.
    """
    open_pools = get_pools_open_at(pools, day, start, end)
    longest_pools = get_pools_with_max_dimension(open_pools, 'Length')

    if len(longest_pools) > 1:
        longest_pools = get_pools_with_max_dimension(longest_pools, 'Width')

    return longest_pools[0]


if __name__ == "__main__":
    data = read_json_file('pools.json')
    suitable_pool = find_suitable_pool(data, 'Понедельник', '10:00', '12:00')
    print_pool_info(suitable_pool)

import time
from typing import List

class UnavailableChannelException(Exception):
    pass

def _add_front(channels_sequence: List[int], channel: int) -> List[int]:
    return [channel] + channels_sequence

def _get_previous_index(viewed: List[int], channel: int) -> int:
    try:
        return viewed.index(channel)
    except ValueError:
        return -1

def minimum_clicks(lowest: int, highest: int, blocked: List[int], channels_sequence: List[int]) -> int:
    # Preconditions
    if lowest < 0 or highest < 0:
        raise ValueError("Lowest and Highest channels must be positive")
    if lowest > highest:
        raise ValueError("Lowest channel must be less than or equal to Highest channel")
    if highest > 10000:
        raise ValueError("Highest channel must be less than or equal to 10000")

    counter: int = 0
    # viewed are the channels that are viewed
    # new channels are added to the front of the list
    # e.g. last viewed channel is viewed[0]
    viewed: List[int] = []
    available_channels: List[int] = [i for i in range(lowest, highest + 1) if i not in blocked]

    for channel in channels_sequence:
        # Get channel's index
        try:
            channel_index: int = available_channels.index(channel)
        except ValueError:
            raise UnavailableChannelException(f"Channel {channel} is out of range or blocked")
        # print(f"Viewed: {viewed}")
        if counter == 0:
            channel_str = str(channel)
            counter += len(channel_str)
            viewed = _add_front(viewed, channel)
            continue
        
        last_viewed: int = viewed[0]
        # If same channel then no need to click any buttons
        if channel == last_viewed:
            viewed = _add_front(viewed, channel)
            continue
        
        min_click = 0
        # Get absolute difference -> can click up or down
        diff: int = abs(channel_index - available_channels.index(last_viewed))
        # print(f"diff: {diff}")
        # Get how many number buttons to click to the channel
        channel_str: str = str(channel)
        number_clicks: int = len(channel_str)
        # print(f"number_clicks: {number_clicks}")
        # Find min
        min_click = min(diff, number_clicks)
        # print(f"min_click: {min_click}")
        
        # Check if channel is viewed previously
        previous_index: int = _get_previous_index(viewed, channel)
        # print(f"previous_index: {previous_index}")
        # print("Previous Index: ", previous_index)
        if previous_index > -1 and previous_index < min_click:
            min_click = previous_index
        
        # Add to counter
        viewed = _add_front(viewed, channel)
        counter += min_click

    # Summary
    print(f"Lowest Channel: {lowest} | Highest Channel: {highest}")
    print(f"Blocked Channels: {blocked}")
    print(f"Channels Sequence: {channels_sequence}")
    print(f"--> ANSWER: Minimum Clicks: {counter}")
    return counter


class TestCase:
    def __init__(self, lowest: int, highest: int, blocked: List[int], sequence: List[int]):
        self.lowest: int = lowest
        self.highest: int = highest
        self.blocked: List[int] = blocked
        self.sequence: List[int] = sequence

# Write your test cases here
cases: List[TestCase] = [
    TestCase(1, 10, [2, 5], [3, 1, 4, 7, 1, 10]),
    TestCase(103, 108, [104], [105, 106, 107, 103, 105]),
    TestCase(1, 100, [78, 79, 80], [10, 13, 13, 100, 99, 98, 77, 81]),
    TestCase(1000, 2000, [1500], [1000, 1003, 1000])
]

# Run test cases
for i, case in enumerate(cases):
    print(f"\n----- Case #{i + 1} -------")
    _start = time.time()
    minimum_clicks(case.lowest, case.highest, case.blocked, case.sequence)
    print(f"Time: {round((time.time() - _start) * 1000, 2)} ms")

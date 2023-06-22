# Task 1
Alice is a 12 year old student who fractured her leg and lower back in a bicycle accident and is on bed rest for the next 2 months. She keeps herself busy by watching television on her GalacticDTH. While watching the television, one day she decided to play a small game, where she has to identify the minimum number of clicks required to surf a given set of channels in a sequence. She quickly decided that it makes for an interesting problem to solve using a software program, (oh, forgot to tell you that she likes to code when she is not busy with her school work).

Your task is to write the software program (using any of the programming language choices given), before Alice can do it herself, we think she is going to take 2 hours, so you think you can beat the 12 year old in solving this, we think so! Your time starts now!

Obviously the program has to take the following instructions and constraints into account.

## Instructions

The remote consists of 13 buttons including 10 buttons for the numbers (0-9), a "↓ Channel" button, an "↑ Channel" button and a ← button:

* The number buttons will allow you to jump directly to a specific channel. (Ex: to go to channel 24 by typing “2”, “4”.)
* The "↑ Channel" button increments the current channel to the next higher viewable channel, unless the current channel is the highest viewable channel, in which case it rolls over to the lowest viewable channel.
* The "↓ Channel" button decrements to the next lower viewable channel, unless the current channel is the lowest viewable channel, in which case it rolls over to the highest viewable channel.
* The ← button reverts to whatever channel was on the television before the current channel. (Ex: If channel 1 is viewed, then channel 100, then when ← is pressed, the television will go to channel 1.)
  Also, Alice can get from one channel to the next in one of the two ways:
* Clicking any combination of "↑ Channel", "↓ Channel", and ← buttons.
* Keying in the numbers to the channel on the remote. Alice will never combine ← and number buttons when moving from one channel to the next.

Alice's parents have set up some parental controls involving some channels on her television. These channels are not viewable, so they are skipped by the "↑ Channel" and "↓ Channel" buttons.

Given a list of channels to view, the lowest channel and highest channel, and a list of blocked channels, your program should return the minimum number of clicks necessary to get through all the shows that Alice would like to watch.

**Input Format**

* Lowest_Channel Highest_Channel
* List of blocked Channels
* List containing sequence of Channels to view

**Constraints**

* The lowest channel on the television will be greater than 0, and less than or equal to 10,000.
* The highest channel on the television will be greater than or equal to lowest channel, and less than or equal to 10,000.
* The list of channels that are blocked on Alice's television. All the channels in this list will be valid channels (greater than or equal to lowest channel, less than or equal to highest channel). Duplicates may be ignored. The blocked list can be maximum of 40 channels.
* The sequence that Alice must view contains between 1 and 50 elements, inclusive. All channels in this sequence are not in the blocked list and are between lowest channel and highest channel, inclusive.

**Output Format**

* Minimum number of clicks

**Sample Input 0**

```
1 20
18 19
15 14 17 1 17
```

**Sample Output 0**

```
7
```

**Sample Input 1**

```
103 108
104
105 106 107 103 105
```

**Sample Output 1**

```
8
```

**Sample Input 2**

```
1 100
78 79 80 3
10 13 13 100 99 98 77 81
```

**Sample Output 2**

```
12
```

**Sample Input 3**

```
1000 2000
1500
1000 1003 1000
```

**Sample Output 3**

```
8
```

```
Sample python3 code
```

```py
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3
    pass

```

# Task 2

You are given two tables, `lecturer_history` and `master_term`, with the following structure:
```sql
CREATE TABLE lecturer_history (
  lecturer_name VARCHAR(10),
  term VARCHAR(20),
  activity VARCHAR(10)
);

CREATE TABLE master_term(
  term VARCHAR(20)
);
```

Each record in `lecturer_history` represents activity of certain lecturer on certain term. The colum `lecturer_name` contains the name of each lecturer. The column `term` contains on what term the activity occurs. The column `activity` contains activity taken by lecturer on that `term`. The column `activity` has value from following list (`Active`, `Leave`, `Resigned`). You may assume that each lecturer have a unique name, so that two similar name only refer to one lecturer.

It is not necessary that `lecturer_history` table will have all the term on `master_term` table. We will only record activity of the lecturer on the term that activity occur to reduce cardinality of the table. For example, 'Yanuar' has been `Active` lecturer on `2018 Semester 1` and take a `Leave` on `2019 Semester 2`, then `lecturer_history` table may only consist of two rows as follows:

| lecturer_name | term            | activity |
|---------------|-----------------|----------|
| Yanuar        | 2018 Semester 1 | Active   |
| Yanuar        | 2019 Semester 2 | Leave    |

Each record in `master_term` represents on all possibilities of `term` on this institute. You may assume that the `term` is combination of `year` and one of following list (`Semester 1`, `Semester 2`)

Write an SQL query that returns a table containing all status of lecturer at all terms available on the institute. Each record should contain the name of the lecturer, the term of the status, and the status of that lecturer. If the term is lower than earliest activity of the lecturer, you may fill the status as `-` to indicate N/A on the record. Records should be orderd by increasing lecturer name following by increasing term.

You may fill lecturer's status with `-` if the lecturer has been resigned on previous semester. It's a plus point if you can **take out** resigned lecturer from the result list after last activity recorded on the `lecturer_history`. Please consider that the resigned lecturer can be an active lecturer again someday!

For example, given:

`lecturer_history` :

| lecturer_name | term            | activity |
|---------------|-----------------|----------|
| Yanuar        | 2018 Semester 1 | Active   |
| Yanuar        | 2019 Semester 2 | Leave    |
| Yanuar        | 2020 Semester 1 | Active   |
| Singgih       | 2018 Semester 2 | Active   |
| Singgih       | 2019 Semester 2 | Resigned |

`master_term` :

| term            |
|-----------------|
| 2017 Semester 1 |
| 2017 Semester 2 |
| 2018 Semester 1 |
| 2018 Semester 2 |
| 2019 Semester 1 |
| 2019 Semester 2 |
| 2020 Semester 1 |
| 2020 Semester 2 |
| 2021 Semester 1 |

your query should return :

| lecturer_name | term            | status   |
|---------------|-----------------|----------|
| Yanuar        | 2017 Semester 1 | -        |
| Yanuar        | 2017 Semester 2 | -        |
| Yanuar        | 2018 Semester 1 | Active   |
| Yanuar        | 2018 Semester 2 | Active   |
| Yanuar        | 2019 Semester 1 | Active   |
| Yanuar        | 2019 Semester 2 | Leave    |
| Yanuar        | 2020 Semester 1 | Active   |
| Yanuar        | 2020 Semester 2 | Active   |
| Yanuar        | 2021 Semester 1 | Active   |
| Singgih       | 2017 Semester 1 | -        |
| Singgih       | 2017 Semester 2 | -        |
| Singgih       | 2018 Semester 1 | -        |
| Singgih       | 2018 Semester 2 | Active   |
| Singgih       | 2019 Semester 1 | Active   |
| Singgih       | 2019 Semester 2 | Resigned |
| Singgih       | 2020 Semester 1 | -        |
| Singgih       | 2020 Semester 2 | -        |
| Singgih       | 2021 Semester 1 | -        |

For lecturer Yanuar, the status from 2018 Semester 1 - 2019 Semester 1 is Active and Leave on 2019 Semester 2 derived from table `lecturer_history`. For lecturer Singgih, the status from 2018 Semester 2 - 2019 Semester 1 is Active and Resigned on 2019 Semester 2 derived from table `lecturer_history`.

## Code Template
```sql
-- write your code here
SELECT ...
```

## Test Data
```sql
INSERT INTO lecturer_history VALUES
('Yanuar', '2018 Semester 1', 'Active'),
('Yanuar', '2019 Semester 2', 'Leave'),
('Yanuar', '2020 Semester 1', 'Active'),
('Singgih', '2018 Semester 2', 'Active'),
('Singgih', '2019 Semester 2', 'Resigned');

INSERT INTO master_term VALUES
('2017 Semester 1'),
('2017 Semester 2'),
('2018 Semester 1'),
('2018 Semester 2'),
('2019 Semester 1'),
('2019 Semester 2'),
('2020 Semester 1'),
('2020 Semester 2'),
('2021 Semester 1');
```
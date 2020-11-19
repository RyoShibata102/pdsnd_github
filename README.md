### Date created
Project: 15.06.2020    
Readme: 19.11.2020

### Project Title
Bikeshare Evaluation Tool

###Requirements

Python (version 3.8 or higher)

Additional Packages:
 - numpy
 - pandas

### Description
The "Bikeshare Evaluation Tool" is for evaluating bikesharing data of the U.S. provided by Motivate.
The program compares the data of the following cities: Chicago, NYC and Washington, DC.
It can be used to analyze the given data for one specific city. You can filter the data by month(January to June) and/or day(monday to sunday) to get more detailed information.
The program displays Statistics about:

1. Popular times of travel (i.e., occurs most often in the start time)

    * most common month
    * most common day of week
    * most common hour of day

2. Popular stations and trip

    * most common start station
    * most common end station
    * most common trip from start to end (i.e., most frequent combination of start station and end station)

3. Trip duration

    * total travel time
    * average travel time

4. User info

    * counts of each user type
    * counts of each gender (only available for NYC and Chicago)
    * earliest, most recent, most common year of birth (only available for NYC and Chicago)


### Files used
Data provided by Motivate:

* chicago.csv
* new_york_city.csv
* washington.csv

### Datasets
Datasets needs to contain following 6 columns:

* Start Time (e.g., 2017-01-01 00:07:57)
* End Time (e.g., 2017-01-01 00:20:53)
* Trip Duration (in seconds - e.g., 776)
* Start Station (e.g., Broadway & Barry Ave)
* End Station (e.g., Sedgwick St & North Ave)
* User Type (Subscriber or Customer)


### Credits
Thanks a lot Udacity Team <3

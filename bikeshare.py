import time
import pandas as pd
import numpy as np
import datetime

pd.set_option('display.max_columns', 12)

CITY_DATA = {'chicago': 'bikeshare_data/chicago.csv',
             'new york city': 'bikeshare_data/new_york_city.csv',
             'washington': 'bikeshare_data/washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which City do you like to check? Chicago, New York City or Washington?\n").lower()
        if city == 'chicago' or city == 'washington' or city == 'new york city':
            print(f"Ok, let's check the Data of {city.title()}!\n")
            break
        else:
            print("Whoops! Please select the right City. Chicago, New York City or Washington?\n")
            continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month do you want to check? Choose between January to June or all for no filter\n").lower()
        # TODO: Don't like the if statement, another solution?
        if month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june':
            print(f"Ok, let's check the data of {month.title()}!\n")
            break
        elif month == 'all':
            print("No filter. Ok, let's check for all months\n")
            break
        else:
            print("Whoops! Please select a valid month.\n")
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day do you wanna check? Choose between monday to sunday or write all if you don't want to filter a specific day\n").lower()
        # TODO: the if statement is really long, another solution?
        if day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday':
            print(f"Ok, let's set the dayfilter to {day}s!\n")
            break
        elif day == 'all':
            print("No filter. Ok, let's check for all days\n")
            break
        else:
            print("Whoops! Please select a valid day.\n")
            continue

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df, day, month):
    """Displays statistics on the most frequent times of travel."""
    month_dic = {1: 'January',
                 2: 'February',
                 3: 'March',
                 4: 'April',
                 5: 'May',
                 6: 'June'}

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month == 'all':
        month_counter = df['month'].value_counts()
        max_month_counter = max(month_counter)
        common_month = month_counter.idxmax()
        print(f'The most common month: {month_dic[common_month]} Counter: {max_month_counter}')
    else:
        max_month_counter = max(df['month'].value_counts())
        print(f'You choosed a month filter.\nThe month you choosed: {month.title()} Counter: {max_month_counter}')

        # TO DO: display the most common day of week
    if day == 'all':
        day_counter = df['day_of_week'].value_counts()
        max_day_counter = max(day_counter)
        common_day = day_counter.idxmax()
        print(f'The most common day: {common_day} Counter: {max_day_counter}')
    else:
        max_day_counter = max(df['day_of_week'].value_counts())
        print(f'You choosed a day filter.\nThe day you choosed: {day.title()} Counter: {max_day_counter}')

    # TO DO: display the most common start hour
    hours = df['Start Time'].dt.hour.value_counts()
    max_hour_counter = max(hours)
    common_hour = hours.idxmax()

    print(f"The most common start hour: {common_hour}:00 Counter: {max_hour_counter}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station_counter = df['Start Station'].value_counts()
    common_station_counter = max(start_station_counter)
    common_start_station = start_station_counter.idxmax()

    print(f'The most commonly used start station: {common_start_station} Counter: {common_station_counter}')

    # TO DO: display most commonly used end station
    end_station_counter = df['End Station'].value_counts()
    common_end_counter = max(end_station_counter)
    common_end_station = end_station_counter.idxmax()

    print(f'The most commonly used end station: {common_end_station} Counter: {common_end_counter}')

    # TO DO: display most frequent combination of start station and end station trip
    combi_counter_all = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).nlargest(n=1)
    max_combi_counter = combi_counter_all[0]
    max_start_station = combi_counter_all.index.get_level_values('Start Station')[0]
    max_end_station = combi_counter_all.index.get_level_values('End Station')[0]

    print(f'The most frequent combination: {max_start_station} to {max_end_station} Counter: {max_combi_counter}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    total_duration = str(datetime.timedelta(seconds=int(total_duration)))
    print(f'The total travel: {total_duration:}')

    # TO DO: display mean travel time
    mean_duration = round(df['Trip Duration'].mean())
    mean_duration = str(datetime.timedelta(seconds=mean_duration))
    mean_duration_format = ':'.join(mean_duration.split(':')[1:])

    print(f'The mean travel time: {mean_duration_format}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_counter = df['User Type'].value_counts()
    subscriber_counter = user_types_counter['Subscriber']
    customer_counter = user_types_counter['Customer']

    print(f"The total subscriber counter: {subscriber_counter}")
    print(f"The total customer counter: {customer_counter}")

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counter = df['Gender'].value_counts()
        male_counter = gender_counter['Male']
        female_counter = gender_counter['Female']

        print(f"\nThe total male counter: {male_counter}")
        print(f"The total female counter: {female_counter}")
    else:
        print('\nThere are no gender information for this city!')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        most_common_birth_year = df['Birth Year'].value_counts().idxmax()
        common_by_counter = df['Birth Year'].value_counts().max()
        ealiest_birth_year = min(df['Birth Year'])
        recent_birth_year = max(df['Birth Year'])

        print(f'\nThe most recent Birth Year: {recent_birth_year}')
        print(f'The earliest Birth Year: {ealiest_birth_year}')
        print(f'The most common Birth Year: {most_common_birth_year} Counter: {common_by_counter}')
    else:
        print('\nThere are no information about the birth year!')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def raw_data(df):
    output_max = 5
    n = 0
    check_raw_data = input('\nWould you like to check some specific individual Data? Enter yes or no.\n')
    while True:
        if check_raw_data.lower() != 'yes':
            break

        while n < output_max:
            print(f'{df.iloc[n]}\n')
            n += 1
        output_max += 5
        check_raw_data = input('\nWould you like to check more specific individual Data? Enter yes or no.\n')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, day, month)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

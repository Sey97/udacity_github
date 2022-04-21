import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    username = input('Please enter your first name\n').title()
    print('\nHello, {}! Let\'s explore some US bikeshare data!'.format(username))
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to view data for Chicago, New York City, or Washington?\n').lower()
        if city not in CITY_DATA:
            print('Request not found! Please select a city from Chicago, New York or Washington.')
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nWould you like to filter the data by month? If yes, enter month name between January and June.' \
                      '\nYou can enter "all" if you do not want to filter by month name\n').lower()
        months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        if month not in months:
            print('Invalid selection! Please enter a month name as specified.')
        else:
            break      
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nWould you like to filter the data by day? If yes, enter name of day or enter "all" if you wish not to.\n').lower()
        days = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']          
        if day not in days:
            print('Invalid selection! Please enter a valid day.')
        else:
            break      
    
    print('\nYou have selected data for city: {}, month: {}, day: {}.'.format(city, month, day).title())             
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Parameters:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # We load the data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # First we convert the start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # We create new columns by extracting the month and day of week from Start Time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # We filter the data by month if applicable
    if month != 'all':
        # We use the index of the months list to get the corresponding integer
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        # We filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    # We filter by day of week if applicable
    if day != 'all':
        # Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # We use the mode method on the month column to find the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month is', most_common_month)

    # TO DO: display the most common day of week
    # We use the mode method on the day of the week column to find the most common day
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common day of the week is', most_common_day)

    # TO DO: display the most common start hour
    
    # First we extract the hour from the Start Time column to create the hour column
    # We then use mode to return the most common hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common start hour is', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    # We apply the mode method to the Start Staton column 
    most_used_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is', most_used_start_station)



    # TO DO: display most commonly used end station
    # We apply the mode method to the End Station column
    most_used_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is', most_used_end_station)
    


    # TO DO: display most frequent combination of start station and end station trip
    # We concate the Start and End Station columns and apply mode method
    df['Combination of Start and End Station'] = df['Start Station'] + ' ' + '-' + ' ' + df['End Station'] 
    most_frequent_combination = df['Combination of Start and End Station'].mode()[0]
    print('The most frequent combination of start and end station trip is', most_frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # We use sum to calculate the total travel time 
    total_time = df['Trip Duration'].sum()
    print('The total time travel is {} seconds.'.format(total_time))

    # TO DO: display mean travel time
    # We use mean to return the mean travel time
    average_time = df['Trip Duration'].mean()
    print('The mean travel time is {} seconds.' .format(average_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print('The value counts for each user type\n', count_user_type)

    # TO DO: Display counts of gender
    if city != 'washington':
        gender_counts = df['Gender'].value_counts()
        print('The counts of each gender\n', gender_counts)

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_yob = df['Birth Year'].min()
        most_recent_yob = df['Birth Year'].max()
        most_common_yob = df['Birth Year'].mode()[0]
        print('The earliest year of birth is', earliest_yob)
        print('The most recent year of birth is', most_recent_yob)
        print('The most common year of birth is', most_common_yob)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """
    Displays rows of raw data based on user's request.
          
    Parameters:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    y = 0
    
    while True:
        # We ask the user whether to display 5 rows of data
        raw_data = input('Would you like to see 5 more rows of raw data? Please enter yes or no.\n').lower()
        if raw_data == 'yes':
            print(df[y:y+5])
            y +=5  
        else:  
            break  
          
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

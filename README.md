
### Date created
21-04-2022

### Project Title
Explore US Bikeshare Data

### Description
In this project, Python is used to understand and explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. I wrote code to import the data and answered interesting questions about it by computing descriptive statistics. I also wrote a script that takes in raw input to build an interactive experience in the terminal to present these statistics. The user is able to choose data and filter for a dataset to analyze.

#### **Software Requirements**
- Python 3, Numpy, and pandas installed using [Anaconda](https://www.anaconda.com/products/distribution#windows)
- A text editor, like Visual Studio Code, [Sublime](https://www.sublimetext.com/) or [Atom](https://atom.io/).
- A terminal application (Terminal on Mac and Linux or Cygwin on Windows)

### Project and code details
The bikeshare.py file is set up as a script that takes in raw input to create an interactive experience in the terminal that answers questions about the dataset. There are four questions that will change the answers depending on the user's input:

1. Would you like to see data for Chicago, New York, or Washington?
2. Would you like to filter the data by month, day, or not at all?
3. (If they chose month) Which month - January, February, March, April, May, or June?
4. (If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?

The answers to the questions above will determine the city and timeframe on which data analysis will be done. After filtering the dataset, users will see the statistical result of the data, and choose to start again or exit. 

In addition, the code has been written to handle unexpected user input well without failing. 

The script prompts the user whether they would like want to see the raw data. If the user answers 'yes', then the script prints 5 rows of the data at a time, then asks the user if they would like to see 5 more rows of the data. The script continues prompting and printing the next 5 rows at a time until the user chooses 'no,' they do not want any more raw data to be displayed.

#### **Datasets**
The data for all the three cities were randomly selected for the first six months of 2017. All three of the data files contain the same core **six (6)** columns:
* Start Time (e.g., 2017-01-01 00:07:57)
* End Time (e.g., 2017-01-01 00:20:53)
* Trip Duration (in seconds - e.g., 776)
* Start Station (e.g., Broadway & Barry Ave)
* End Station (e.g., Sedgwick St & North Ave)
* User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
- Gender
- Birth Year

The original files for the three cities can be accessed here:
- [Chicago](https://ride.divvybikes.com/system-data)
- [New_York_City](https://ride.citibikenyc.com/system-data)
- [Washington](https://ride.capitalbikeshare.com/system-data)

#### **Statistics Computed**
1. ***Popular times of travel (i.e., occurs most often in the start time)***
- most common month
- most common day of week
- most common hour of day

2. ***Popular stations and trip***
- most common start station
- most common end station
- most common trip from start to end (i.e., most frequent combination of start station and end station)

3. ***Trip duration***
- total travel time
- average travel time

4. ***User info***
* counts of each user type
* counts of each gender (only available for NYC and Chicago)
* earliest, most recent, most common year of birth (only available for NYC and Chicago)

### Files used
- chicago.csv
- washington.csv
- new_york_city.csv
- bikeshare.py

#### ***Link to file data***
- [City data](https://drive.google.com/drive/folders/1ILlUFEz2GKN4EUwjSueCuR7OhRaRrUOf?usp=sharing)

### Credits
- https://stackoverflow.com/questions/19377969/combine-two-columns-of-text-in-dataframe-in-pandas-python
- https://www.programiz.com/python-programming/datetime
- https://www.programiz.com/python-programming/exception-handling
- https://stackoverflow.com/questions/920645/when-to-use-while-or-for-in-python
- https://docs.python.org/3/tutorial/errors.html
- https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response


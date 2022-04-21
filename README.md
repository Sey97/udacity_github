
### Date created
21-04-2022

### Project Title
Explore US Bikeshare Data

### Description
In this project, Python is used to understand and explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. I wrote code to import the data and answered interesting questions about it by computing descriptive statistics. I also wrote a script that takes in raw input to build an interactive experience in the terminal to present these statistics. The user is able to choose data and filter for a dataset to analyze.

### Project and code details
The bikeshare.py file is set up as a script that takes in raw input to create an interactive experience in the terminal that answers questions about the dataset. There are four questions that will change the answers depending on the user's input:

1. Would you like to see data for Chicago, New York, or Washington?
2. Would you like to filter the data by month, day, or not at all?
3. (If they chose month) Which month - January, February, March, April, May, or June?
4. (If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?

The answers to the questions above will determine the city and timeframe on which data analysis will be done. After filtering the dataset, users will see the statistical result of the data, and choose to start again or exit. 

In addition, the code has been written to handle unexpected user input well without failing. 

The script prompts the user whether they would like want to see the raw data. If the user answers 'yes', then the script prints 5 rows of the data at a time, then asks the user if they would like to see 5 more rows of the data. The script continues prompting and printing the next 5 rows at a time until the user chooses 'no,' they do not want any more raw data to be displayed.

### Files used
- chicago.csv
- washington.csv
- new_york_city.csv
- bikeshare.py

### Credits
It's important to give proper credit. Add links to any repo that inspired you or blogposts you consulted.


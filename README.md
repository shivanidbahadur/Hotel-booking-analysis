# Hotel-booking-analysis
Overview

This project focuses on analyzing hotel booking data to understand booking patterns, cancellation patterns and customer behavior. The dataset was cleaned and explored using Python and insights were visualised using charts.

Tools Used: 
Python
Pandas 
Matplotlib

Dataset:
 The project uses the hotel_booking.csv dataset, which contains information about 119,300+ hotel bookings.
Each record represents a single hotel booking and includes details such as:
Hotel type (City Hotel or Resort Hotel)
Booking status (canceled or not)
Arrival date
Number of adults, children, and babies
Country of origin
Customer type
Meal preferences
Market segment and booking channel
Special requests and pricing information

Data Cleaning Steps
Removed the company column due to a high number of missing values
Filled missing values in agent with 0
Filled missing values in country with the most frequent value (mode)
Removed duplicate records
Handled missing values in children column by replacing them with 0
Removed an unusual outlier where children = 10
This value was rare and not meaningful for analysis
Removed invalid bookings where adults, children, and babies were all 0
Created a new feature arrival_date by combining year, month, and day

Key Insights
A major portion of bookings were found to be cancellations, which shows that cancellation behavior is an important factor in hotel performance analysis.
When cancellation rates of city hotels and resort hotels were compared, it was noted that city hotels generally experienced higher cancellation rates compared to resort hotels.
Certain months showed higher booking activity, with clear seasonal trends in travel demand across the year.
Customers from some countries canceled more bookings than others, showing that cancellation behavior varies by location.
Meal preferences were mostly within  a few categories, with “Undefined” or less common meal types appearing occasionally in the dataset.
Most bookings came through a small number of market segments, showing that only a few channels dominate hotel reservations.

Analysis performed:
Data cleaning and exploration
Meal preference analysis
Monthly booking analysis 
Overall cancellation rate 
Cancellation analysis by month
Cancellation analysis by hotel type
Cancellation analysis by country
Cancellation analysis by customer type
Booking distribution by market segment

Output:
Cleaned dataset: hotel_booking_cleaned.csv
Multiple saved charts for reporting and visualization
 
Files included:
hotel_booking_analysis : Python code for the analysis 
hotel_booking.csv: Dataset used for the project
Chart images : Visualizations generated during the project
hotel_booking_cleaned.csv: cleaned dataset



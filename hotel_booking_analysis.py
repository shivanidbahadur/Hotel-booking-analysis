#==============================================================
# Import libraries
#==============================================================
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#==============================================================
# Load datasets
#==============================================================
df=pd.read_csv("hotel_booking.csv")
#==============================================================
# Data exploration and cleaning
#==============================================================
print(df.head(5))
print(df.columns)
print(df.isnull().sum())

print(df["company"].isnull().sum())
print(df["company"].notnull().sum()-df["company"].isnull().sum())

#nullvalues > non nul values

df.drop("company",axis =1, inplace= True) #Dropped ‘company’ due to extremely high missing values
print(df.columns)
print(df.shape)

print(df["agent"].isnull().sum())
print(df["agent"].notnull().sum())

#nullvalues<non null values

df["agent"]=df["agent"].fillna(0)
df["agent"]=df["agent"].astype(int)
print(df["agent"].head(10))

print(df["country"].isnull().sum())
df["country"]=df["country"].fillna(df["country"].mode()[0])
print(df["country"].head(20))
print(df["country"].isnull().sum())

print(df.isnull().sum())
print(df.info())
print(df.describe())
print(df.shape)
print(df.head(5))
df=df.drop_duplicates()
print(df.duplicated().sum())
print((df["children"]==0.0))
print(df["children"].unique())
print(df["children"].isnull().sum())
df["children"]=df["children"].fillna(0)
print(df["children"].isnull().sum())
df["children"]=df["children"].astype(int)
print(df["children"].unique())

print(df[df["children"]==10][["children","adults","babies"]])

print(df.loc[df["children"]==10,['hotel', 'is_canceled', 'lead_time', 'arrival_date_year',
       'arrival_date_month', 'arrival_date_week_number']])
print(df.loc[df["children"]==10,['arrival_date_day_of_month', 'stays_in_weekend_nights',
       'stays_in_week_nights', 'adults', 'children', 'babies', 'meal',
       'country', 'market_segment', 'distribution_channel',
       ]])
print(df.loc[df["children"]==10,['deposit_type', 'agent',
       'days_in_waiting_list', 'customer_type', 'adr',
       'required_car_parking_spaces', 'total_of_special_requests',
       'reservation_status',
       ]])
print(df.loc[df["children"]==10,['reservation_status_date', 'name', 'email',
       'phone-number', 'credit_card'
       ]])

#The distribution confirms that 10 is a rare isolated value with no meaningful frequency
df= df[df["children"]!=10]
print(df["children"].unique())
print(df.info())
print(df["name"].head(20))

print(df.loc[
    (df["adults"] == 0) & 
    (df["children"] == 0) & 
    (df["babies"] == 0),
    ["adults", "children", "babies"]
])

df=df[(df["adults"] != 0) |
    (df["children"] != 0) |
    (df["babies"] != 0)]
# #Removed invalid bookings with no guests
print(df.shape)
print(df.isnull().sum())

print(df["arrival_date_day_of_month"].unique())
df["arrival_date"]=pd.to_datetime(df["arrival_date_year"].astype(str)+"-"+ df["arrival_date_month"]+"-"+df["arrival_date_day_of_month"].astype(str))
print(df[["arrival_date_year","arrival_date_month","arrival_date_day_of_month","arrival_date"]].head())

print(df.shape)
print(df.isnull().sum().sort_values(ascending=False))


# Save cleaned dataset
df.to_csv("hotel_booking_cleaned.csv", index=False)

# Meal preference analysis

print((df.loc[df["meal"]=="Undefined"]["meal"]))
(df["meal"].value_counts(normalize=True)*100).plot(kind="pie",
                                                   colors=plt.cm.Pastel1.colors,
                                                   startangle=0,shadow=True,autopct="%1.1f%%",
                                                   pctdistance=0.77)
plt.title("Meal preference analysis",fontsize=20)
plt.ylabel("")
plt.savefig("mealpreferences.png")
plt.show()

# Monthly booking analysis

monthly_booking=df["arrival_date_month"].value_counts(normalize=True)
order=["January","February","March","April","May","June","July","August","September","October","November","December"]
monthly_booking=monthly_booking.reindex(order)
((monthly_booking)*100).plot(kind="bar",color="seagreen")
plt.title("Monthly booking analysis",fontsize=20)
plt.xlabel("Month")
plt.ylabel("Percentage of booking(%)")
plt.xticks(rotation=0)
plt.grid(axis="y")
plt.savefig("monthlybookinganalysis.png")
plt.show()

# Booking distribution by market segment

print(df["market_segment"].head(10))
print(df["market_segment"].unique())

marketsegment=df["market_segment"].value_counts(normalize=True)*100
marketsegment.plot(kind="bar",color="orchid")
plt.title("Booking Distribution by Market Segment", fontsize=20)
plt.xlabel("Market Segment")
plt.ylabel("Percentage of Bookings (%)")
plt.xticks(rotation=45)
plt.grid(axis="y")

plt.savefig("market_segment_distribution.png")
plt.show()

# Overall cancellation analysis

print((df["is_canceled"].value_counts(normalize=True)*100).round(1))
overall_cancelled=(df["is_canceled"].value_counts(normalize=True)*100).round(1)
overall_cancelled.plot(kind="pie",labels=["Not cancelled","Cancelled"], autopct="%1.1f%%",colors=["green","orange"],shadow=True,startangle=90)
plt.title("Overall cancellation analysis",fontsize=20)
plt.ylabel("")
plt.savefig("overallcancellation.png")
plt.show()

# Cancellation analysis by hotel

cancellation_by_hotel=df.groupby("hotel")["is_canceled"].mean()*100
cancellation_by_hotel.plot(kind="bar",color=["orange","green"])
plt.xticks(rotation=0)
plt.xlabel("Hotel Type")
plt.ylabel("Cancellation Rate (%)")
plt.grid(axis="y")
plt.title("Cancellation Rate by Hotel Type",fontsize=20)
plt.savefig("cancellation_rate_by_hoteltype.png")
plt.show()

# Cancellation analysis by month

print(df.columns)
cancellation_by_month=df.groupby("arrival_date_month")["is_canceled"].mean()*100
order=["January","February","March","April","May","June","July","August","September","October","November","December"]
cancellation_by_month=cancellation_by_month.reindex(order)
cancellation_by_month.plot(kind="bar",color="steelblue")
plt.title("Cancellation analysis by month",fontsize=20)
plt.xlabel("Month")
plt.ylabel("Cancellation rate(%)")
plt.xticks(rotation=0)
plt.grid(axis="y")
plt.savefig("cancellation_rate_by_month.png")
plt.show()

# Cancellation analysis by country 

print(df["country"].unique())
top_countries=df["country"].value_counts().head(10).index
print(top_countries)
cancellation_by_country=df[df["country"].isin(top_countries)].groupby("country")["is_canceled"].mean()*100
cancellation_by_country.plot(kind="bar",color="teal")
plt.title("Cancellation analysis by country",fontsize=20)
plt.xlabel("Countries")
plt.ylabel("Cancellation rate(%)")
plt.xticks(rotation=0)
plt.grid(axis="y")
plt.savefig("cancellation_rate_by_country.png")
plt.show()

# Cancellation analysis by customer type

print(df.columns)

print(df["customer_type"].unique())
cancellation_by_customertype=df.groupby("customer_type")["is_canceled"].mean()*100
cancellation_by_customertype.plot(kind="bar",color="lightgreen")
plt.title("Cancellation analysis by customer type",fontsize=20)
plt.xlabel("Customer type")
plt.ylabel("Cancellation rate(%)")
plt.xticks(rotation=0)
plt.grid(axis="y")
plt.savefig("cancellation_rate_by_customertype.png")
plt.show()

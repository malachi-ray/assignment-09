# Module 9 Assignment: Introduction to Data Analysis with Pandas
# GlobalTech Sales Analysis

# Import required libraries
import pandas as pd
import numpy as np

# Welcome message
print("=" * 60)
print("GLOBALTECH QUARTERLY SALES ANALYSIS")
print("=" * 60)

# TODO 1: Load and Explore the Dataset
# The sales_data.csv file contains data with the following structure:
# - Date: Date of sale (YYYY-MM-DD format)
# - Region: Sales region (North America, Europe, Asia, Latin America)
# - Store: Store identifier
# - Category: Product category (Smartphones, Computers, Audio, Accessories, Wearables)
# - Product: Specific product name
# - Units: Number of units sold
# - Unit_Price: Price per unit in USD
# - Total_Sales: Total sales amount in USD
# - Promotion: Whether the product was on promotion (Yes/No)
# Some entries contain missing values marked as NaN

# REQUIRED VARIABLE NAMES FOR AUTOGRADING:
# - sales_df: Main DataFrame loaded from CSV
# - total_units: Total units sold across all records
# - total_revenue: Total sales amount across all records
# - avg_unit_price: Average unit price across all products
# - na_sales: DataFrame containing only North America sales
# - high_volume_sales: DataFrame with sales where Units > 20
# - phonex_promo: DataFrame with PhoneX products on promotion
# - feb_sales: DataFrame containing February 2024 sales
# - best_product: Product name with highest total sales
# - sales_by_region: Series with total sales by region (sorted descending)
# - avg_units_by_category: Series with average units sold per category
# - promo_comparison: Dictionary with promotion effectiveness metrics
# - missing_counts: Series with count of missing values per column
# - missing_percentages: Series with percentage of missing values per column

# ----- USE THE FOLLOWING CODE TO SIMULATE A CSV FILE (DO NOT MODIFY) -----
from io import StringIO

# Simulated CSV content
csv_content = """Date,Region,Store,Category,Product,Units,Unit_Price,Total_Sales,Promotion
2024-01-15,North America,NA001,Smartphones,PhoneX,12,899.99,10799.88,No
2024-01-18,Europe,EU002,Computers,LaptopPro,8,1299.99,10399.92,Yes
2024-01-20,Asia,AS001,Audio,WirelessEarbuds,25,149.99,3749.75,No
2024-01-22,North America,NA002,Wearables,SmartWatch,15,249.99,3749.85,No
2024-01-25,Latin America,LA001,Smartphones,PhoneX,7,899.99,6299.93,Yes
2024-01-27,Europe,EU001,Accessories,PhoneCase,35,24.99,874.65,No
2024-01-30,Asia,AS002,Smartphones,PhoneSE,18,499.99,8999.82,No
2024-02-02,North America,NA001,Computers,LaptopPro,6,1299.99,7799.94,No
2024-02-05,Europe,EU002,Wearables,SmartWatch,20,249.99,4999.80,Yes
2024-02-08,North America,NA003,Audio,WirelessEarbuds,30,149.99,4499.70,Yes
2024-02-10,Asia,AS001,Accessories,ChargingCable,45,19.99,899.55,No
2024-02-12,Latin America,LA001,Computers,TabletBasic,12,399.99,4799.88,No
2024-02-15,North America,NA002,Smartphones,PhoneSE,14,499.99,6999.86,No
2024-02-18,Europe,EU001,Audio,BlueSpeaker,22,79.99,1759.78,Yes
2024-02-20,Asia,AS002,Wearables,FitnessTracker,28,129.99,3639.72,No
2024-02-22,North America,NA001,Accessories,PhoneCase,50,24.99,1249.50,Yes
2024-02-25,Latin America,LA002,Smartphones,PhoneX,9,,8099.91,No
2024-02-28,Europe,EU002,Computers,LaptopBasic,10,899.99,8999.90,No
2024-03-02,North America,NA003,Wearables,FitnessTracker,,129.99,2599.80,Yes
2024-03-05,Asia,AS001,Smartphones,PhoneSE,15,499.99,7499.85,No
2024-03-08,Europe,EU001,Accessories,ChargingCable,60,19.99,1199.40,Yes
2024-03-10,North America,NA002,Computers,TabletPro,7,599.99,4199.93,No
2024-03-12,Latin America,LA001,Audio,WirelessEarbuds,18,149.99,2699.82,No
2024-03-15,North America,NA001,Wearables,SmartWatch,12,249.99,2999.88,No
2024-03-18,Europe,EU002,Smartphones,PhoneX,11,899.99,9899.89,Yes
2024-03-20,Asia,AS002,Computers,LaptopPro,6,1299.99,7799.94,No
2024-03-22,North America,NA001,Audio,BlueSpeaker,25,79.99,1999.75,No
2024-03-25,Latin America,LA002,Accessories,PhoneCase,40,,999.60,No
"""

# Create a StringIO object (simulates a file)
sales_data_csv = StringIO(csv_content)

# Now you can load this as if it was a CSV file:
# sales_df = pd.read_csv(sales_data_csv)
# ----- END OF SIMULATION CODE -----


# 1.1 Load the dataset and store it in a DataFrame called 'sales_df'
# REQUIRED: Variable name must be 'sales_df'
# Your code here
sales_df = pd.read_csv(sales_data_csv)
# 1.2 Display the first 5 rows of the dataset
# Your code here
print(sales_df.head())

# 1.3 Display basic information about the DataFrame (info() method)
# Your code here
sales_df.info()

# 1.4 Get the dimensions of the DataFrame (number of rows and columns)
# Your code here
print(sales_df.shape)

# 1.5 Display summary statistics for numerical columns using describe()
# Your code here
sales_df.describe()

# TODO 2: Column Selection and Basic Analysis
# 2.1 Select and display only the 'Product', 'Units', and 'Total_Sales' columns
# Your code here
print(sales_df[['Product', 'Units', 'Total_Sales']])

# 2.2 Calculate the total units sold across all records
# REQUIRED: Store result in variable 'total_units'
# Your code here
total_units = sales_df["Units"].sum()
print(total_units)

# 2.3 Calculate the total sales amount across all records
# REQUIRED: Store result in variable 'total_revenue'
# Your code here
total_revenue = sales_df["Total_Sales"].sum()

# 2.4 Calculate the average unit price per product
# REQUIRED: Store result in variable 'avg_unit_price'
# Your code here
avg_unit_price = sales_df["Unit_Price"].mean()

# TODO 3: Row Selection and Filtering
# 3.1 Select sales from North America region only
# REQUIRED: Store result in variable 'na_sales'
# Your code here
na_sales = sales_df[sales_df["Region"] == "North America"]
# 3.2 Select sales where Units sold is greater than 20
# REQUIRED: Store result in variable 'high_volume_sales'
# Your code here
high_volume_sales = sales_df[sales_df["Units"] > 20]
# 3.3 Select sales of the 'PhoneX' product that were on promotion
# REQUIRED: Store result in variable 'phonex_promo'
# Your code here
phonex_promo = sales_df[(sales_df["Product"]=="PhoneX") & (sales_df["Promotion"]=="Yes")]
# 3.4 Select sales from February 2024 (hint: use string methods with the Date column)
# REQUIRED: Store result in variable 'feb_sales'
# Your code here
feb_sales = sales_df[sales_df["Date"].str.contains("-02-")]
print(feb_sales)

# TODO 4: Advanced Filtering and Analysis
# 4.1 Find the product with the highest total sales
# REQUIRED: Store product name in variable 'best_product'
# Your code here
top_sales = 0
best_product = ""
products = sales_df["Product"]
products_list = []
for i in products:
    if i not in products_list:
        products_list.append(i)
        
for i in products_list:
    prod_data = sales_df[sales_df["Product"] == i]
    prod_sales = prod_data["Total_Sales"].sum()
    if prod_sales > top_sales:
        top_sales = prod_sales
        best_product = i

# 4.2 Calculate total sales by region and sort in descending order
# REQUIRED: Store result in variable 'sales_by_region' (pandas Series)
# Your code here
regions = sales_df["Region"]
regions_list = []
for i in regions:
    if i not in regions_list:
        regions_list.append(i)

sales_list = []
for i in regions_list:
    region_frame = sales_df[sales_df["Region"] == i]
    sales = region_frame["Total_Sales"].sum()
    sales_list.append(sales)

sales_by_region = pd.Series(sales_list, index=regions_list)
sales_by_region = sales_by_region.sort_values(ascending=False)

    
# 4.3 Calculate average units sold per category
# REQUIRED: Store result in variable 'avg_units_by_category' (pandas Series)
# Your code here

categories = sales_df["Category"]
cat_list = []
for i in categories:
    if i not in cat_list:
        cat_list.append(i)

avg_list = []
for i in cat_list:
    cat_frame = sales_df[sales_df["Category"] == i]
    avg = cat_frame["Total_Sales"].mean()
    avg_list.append(avg)

avg_units_by_category = pd.Series(avg_list, index=cat_list)
# 4.4 Compare sales performance of items on promotion vs. not on promotion
# REQUIRED: Store result in dictionary 'promo_comparison' with keys:
# - 'promo_avg_sales': average sale amount for promoted items
# - 'no_promo_avg_sales': average sale amount for non-promoted items
# - 'promo_total_revenue': total revenue from promoted items
# - 'no_promo_total_revenue': total revenue from non-promoted items
# Your code here
promo_frame = sales_df[sales_df["Promotion"]== "Yes"]
no_promo_frame = sales_df[sales_df["Promotion"]== "No"]

promo_comparison= {"promo_avg_sales":promo_frame["Total_Sales"].mean(),
                   "no_promo_avg_sales":no_promo_frame["Total_Sales"].mean(),
                   "promo_total_revenue":promo_frame["Total_Sales"].sum(),
                   "no_promo_total_revenue":no_promo_frame["Total_Sales"].sum()
}

# TODO 5: Missing Value Detection and Reporting
# 5.1 Identify columns with missing values and count them
# REQUIRED: Store result in variable 'missing_counts' (pandas Series)
# Your code here
missing_counts = sales_df.isnull().sum()
# 5.2 Calculate what percentage of the data is missing in each column
# REQUIRED: Store result in variable 'missing_percentages' (pandas Series)
# Your code here
missing_percentages = missing_counts/len(sales_df)*100
# TODO 6: Insights and Business Analysis
# 6.1 Create a summary of the top-performing category in each region
# REQUIRED: Store result in variable 'top_categories_by_region' (pandas Series or dict)
# Your code here
top_categories_by_region = {}
for i in regions_list:
    top_sales = 0
    top_cat = ""
    for j in cat_list:
        sub_frame = sales_df[(sales_df["Region"] == i) & (sales_df["Category"]==j)]
        sub_sales = sub_frame["Total_Sales"].sum()
        if sub_sales > top_sales:
            top_sales = sub_sales
            top_cat = j
    top_categories_by_region[i] = top_cat
# 6.2 Calculate the average unit price for each product category
# REQUIRED: Store result in variable 'avg_price_by_category' (pandas Series)
# Your code here
avg_dict = {}
for i in cat_list:
    sub_frame = sales_df[sales_df["Category"] == i]
    sub_avg = sub_frame["Unit_Price"].mean()
    avg_dict[i] = sub_avg
avg_price_by_category = pd.Series(avg_dict)

# 6.3 For each product, calculate the total revenue and percentage of overall sales
# REQUIRED: Store result in variable 'product_revenue_analysis' (DataFrame with columns: 'total_revenue', 'percentage')
# Your code here
total_rev_list = []
pct_sales_list = []
for i in products_list:
    sub_frame = sales_df[sales_df["Product"]==i]
    total_rev = sub_frame["Total_Sales"].sum()
    total_rev_list.append(total_rev)
    pct_sales = (total_rev/sales_df["Total_Sales"].sum())*100
    pct_sales_list.append(pct_sales)
product_revenue_analysis = pd.DataFrame({
    "total_revenue":total_rev_list,
    "percentage":pct_sales_list
    },index=products_list)
# TODO 7: Generate Analysis Report
print("\n" + "=" * 60)
print("GLOBALTECH Q1 2024 SALES ANALYSIS REPORT")
print("=" * 60)

# 7.1 Display overall sales performance
# REQUIRED OUTPUT FORMAT:
# Overall Performance:
# - Total Revenue: $XXX,XXX.XX
# - Total Units Sold: XXX
# - Average Sale Value: $XXX.XX
# Your code here
print(f"""Overall Performance:
- Total Revenue: ${sales_df["Total_Sales"].sum():,.2f}
- Total Units Sold: {sales_df["Units"].sum():.0f}
- Average Sale Value: ${sales_df["Total_Sales"].mean():,.2f}
""")

# 7.2 Display regional performance summary
# REQUIRED OUTPUT FORMAT:
# Regional Performance:
# [Region]: $XXX,XXX.XX
# ...
# Your code here
print("Regional Performance:")
for i in sales_by_region.index:
    print(f"{i}: ${sales_by_region[i]:,.2f}")
print("")

# 7.3 Display product category performance
# REQUIRED OUTPUT FORMAT:
# Category Performance:
# [Category]: Avg Units: XX.X, Avg Price: $XXX.XX
# ...
# Your code here
print("Category Performance:")
for i in cat_list:
    print(f"{i}: Avg Units: {sales_df[sales_df['Category']==i]['Units'].mean():.1f}, Avg Price: ${sales_df[sales_df['Category']==i]['Unit_Price'].mean():.2f}")
print('')
# 7.4 Display promotion effectiveness
# REQUIRED OUTPUT FORMAT:
# Promotion Effectiveness:
# - Promoted Items Avg Sale: $XXX.XX
# - Non-Promoted Items Avg Sale: $XXX.XX
# - Revenue from Promotions: $XXX,XXX.XX
# Your code here
print(f"""Promotion Effectiveness:
- Promoted Items Avg Sale: ${promo_comparison['promo_avg_sales']:,.2f}
- Non-Promoted Items Avg Sale: ${promo_comparison['no_promo_avg_sales']:,.2f}
- Revenue from Promotions: ${promo_comparison['promo_total_revenue']:,.2f}
""")

# 7.5 Report on data quality issues
# REQUIRED OUTPUT FORMAT:
# Data Quality Report:
# - Missing Values Found: [list columns]
# - Total Missing Entries: XXX
# Your code here
print(f"""Data Quality Report:
- Missing Values Found: {missing_counts[missing_counts>0].index.tolist()}
- Total Missing Entries: {missing_counts.sum():.0f}
""")

# 7.6 Provide three key business recommendations based on your analysis
print("\nKEY BUSINESS RECOMMENDATIONS:")
# Your code and recommendations here
print("The Latin American market is underperforming compared to the others, investment in marketing could help tap into the potential there.")
print("Make further efforts to avoid missing values, as the current missing fields would become difficult to fill in larger quantities.")
print("Promotions seem to be extremely popular, as they compose nearly 30% of our sales. Perhaps reducing the discout amounts on these promotions could lead to higher revenue while still maintaining sales figures.")
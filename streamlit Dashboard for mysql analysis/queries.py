ALL_DATA = """
SELECT * FROM walmart_sales;
"""

TOTAL_SALES_PER_STORE = """
SELECT Store, SUM(Weekly_Sales) as 'Number of Sales'
FROM walmart_sales.walmart_sales
group by Store
order by sum(Weekly_Sales) DESC;
"""

BEST_SALES = """select Store as 'top five Stores', avg(Weekly_Sales) as 'avg sales', variance(Weekly_Sales) as 'fluctuations'
from walmart_sales.walmart_sales
group by Store
order by variance(Weekly_Sales) ASC
limit 5;
"""

AVG_WEEKLY_SALES_PER_STORE = """select Store, avg(Weekly_Sales) as 'average weekly sales '
from walmart_sales.walmart_sales
group by Store;
"""

HOLIDAY_EFFECTS = """SELECT Holiday_Flag, avg(Weekly_Sales) as 'average sales'

from walmart_sales.walmart_sales
group by Holiday_Flag;"""

FUEL_EFF = """select Fuel_Price, avg(Weekly_Sales) as "WEEKLY AVG SALES"
from walmart_sales.walmart_sales
group by Fuel_Price;"""

TEMP_EFF = """select Temperature, avg(Weekly_Sales) AS " WEEKLY AVG SALES"
from walmart_sales.walmart_sales
group by Temperature;"""

unemp_rate_eff = """select   avg(Weekly_Sales) as "WEEKLY AVG SALES", Unemployment 
from walmart_sales.walmart_sales
group by Unemployment;
"""

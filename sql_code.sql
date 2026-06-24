create database Walmart_Sales;

-- Which store has the highest total sales? 

SELECT Store, SUM(Weekly_Sales) as 'Number of Sales'
FROM walmart_sales.walmart_sales
group by Store
order by sum(Weekly_Sales) DESC;

-- Which weeks had the highest and lowest sales? 

(SELECT Date,Store, Weekly_Sales, 'highest sale' AS SALE_TYPE
from walmart_sales.walmart_sales
ORDER BY Weekly_Sales ASC
LIMIT 1)
UNION
(SELECT Date,Store, Weekly_Sales , 'lowest sales' AS SALE_TYPE
from walmart_sales.walmart_sales
order by Weekly_Sales DESC
LIMIT 1);

-- How do holiday weeks affect sales? 

SELECT Holiday_Flag, avg(Weekly_Sales) as 'average sales', 
sum(Weekly_Sales) as 'total sales',
count(Weekly_Sales) as 'number of records'
from walmart_sales.walmart_sales
group by Holiday_Flag;

-- Which stores perform consistently well? 

select Store as 'top five Stores', avg(Weekly_Sales) as 'avg sales', variance(Weekly_Sales) as 'fluctuations'
from walmart_sales.walmart_sales
group by Store
order by variance(Weekly_Sales) ASC
limit 5;

-- What is the average weekly sales per store? 

select Store, avg(Weekly_Sales) as 'average weekly sales '
from walmart_sales.walmart_sales
group by Store;

-- Does unemployment affect sales?

(select   avg(Weekly_Sales), Unemployment, 'min rate of unemp' as unemp_rate
from walmart_sales.walmart_sales
group by Unemployment
order by Unemployment ASC
limit 1)
union
(select   avg(Weekly_Sales), Unemployment, 'max rate of unemp' as unemp_rate
from walmart_sales.walmart_sales
group by Unemployment
order by Unemployment DESC
limit 1);

-- Does fuel price affect sales? 

(select Fuel_Price, avg(Weekly_Sales), 'min fuel price' as fuelprice_rate
from walmart_sales.walmart_sales
group by Fuel_Price
order by Fuel_Price ASC
limit 1)
union
(select Fuel_Price, avg(Weekly_Sales), 'max fuel price' as fuelprice_rate
from walmart_sales.walmart_sales
group by Fuel_Price
order by Fuel_Price DESC
limit 1);

-- Does temperature affect sales? 

(select Temperature, avg(Weekly_Sales), 'min temperature' as tem_type
from walmart_sales.walmart_sales
group by Temperature 
order by Temperature ASC
LIMIT 1)
UNION
(select Temperature, avg(Weekly_Sales), 'max temperature' as tem_type
from walmart_sales.walmart_sales
group by Temperature 
order by Temperature DESC
LIMIT 1);

-- Which month has the highest sales?
SET SQL_SAFE_UPDATES = 0;
ALTER TABLE walmart_sales.walmart_sales
ADD COLUMN New_Date DATE;

UPDATE walmart_sales.walmart_sales
SET New_Date = STR_TO_DATE(Date, '%d-%m-%Y');

SELECT month(New_Date) as 'month' , avg(Weekly_Sales)
from walmart_sales.walmart_sales
group by month(New_Date)
order by avg(Weekly_Sales) DESC;













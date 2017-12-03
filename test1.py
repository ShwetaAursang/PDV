import pandas as pd
from scipy import stats

data=pd.read_csv('set 1.csv')

#print data
print "Total number of products",data.shape[0]
def product():
	print "List all products"
	print data[['Product line','Product type','Product']]
def country():
	print "List all country names"
	print data[['Retailer country']]
def order():
	print "List all order methods"
	print data[['Order method type']]
def MaxProdctInUS():
	print "List the product which is able to sell maximum numbers in United States"
	discipline=data[['Retailer country','Product']]
	demo=discipline[discipline['Retailer country'].str.match('United States')].max()
	print demo
def MaxOrderTypeInGermany():
	print "Find the order method type which is able to sell more number of products in Germany"
	discipline=data[['Order method type','Retailer country','Product']]
	demo=discipline[(discipline['Retailer country']=='Germany')].max()
	print demo

def  topFive():
	print "List the top 5 products which has more gross profit in Australia"
	discipline=data[['Product','Retailer country','Gross profit']]
	demo=discipline[(discipline['Retailer country']=='Australia')].nlargest(5, "Gross profit")
	print demo
def basedOnQuant():
	print "Which order method is more popular (based on Quantity) world wide?"
	sr=data[['Quantity','Order method type']].max()
	print sr
def PercentOrder():
	print "Show the percentage of order methods for Flicker Lantern in Denmark"
	discipline=data[['Order method type','Product','Retailer country']]
	demo3=discipline.groupby([(discipline['Product']=='Flicker Lantern') & (discipline['Retailer country']=='Denmark')]).agg({'Order method type':'count'})
	print demo3/100

def GrossPrftUS():
	print "Show the Gross Profit for BugShield Spray in United States by all order methods from 2004 to 2007"
	discipline=data[['Gross profit','Retailer country','Product','Order method type']]
	demo3=discipline[(discipline['Retailer country']=='United States') & (discipline['Product']=='BugShield Spray') & (discipline['Gross profit'])]
	print demo3
def TopANDBottomProduct():
	print "List the top and bottom three products sold in Canada in year 2006"
	discipline=data[['Product','Retailer country','Year']]
	demo5=discipline[(discipline['Retailer country']=='Canada') & (discipline['Year']==2006)].head(3)
	print demo5
	demo6=discipline[(discipline['Retailer country']=='Canada') & (discipline['Year']==2006)].tail(3)
	print demo6

product()
country()
order()
MaxProdctInUS()
MaxOrderTypeInGermany()
topFive()
basedOnQuant()
PercentOrder()
TopANDBottomProduct()
GrossPrftUS()


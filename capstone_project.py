import pandas as pd
import matplotlib.pyplot as plt

class RetailSalesAnalyzer:
    def __init__(self):
        print('Instance Created')
        self.df = None

    def fileload(self,file_path):
        self.df = pd.read_csv(file_path)
        print('file read successfully')

    #'/Users/lpg/GE_Code/Retails_sales_data.csv'

    def filestats(self):
    #Removing rows with NULL values#
        df_nonnull = self.df.dropna()
        print(df_nonnull)
    #Finding total sales per product#
        tot_sales = df_nonnull.groupby('Product')['Sales'].sum().reset_index()
        self.tot_sales = tot_sales
        print("Total Sales: " ,tot_sales)
    #Identifying the best selling product#
    # Sort by sales in descending order
        sales_by_product = tot_sales.sort_values(by='Sales',ascending=False)
    # Get the best-selling product (top row)
    #best_seller = sales_by_product
        print(sales_by_product.iloc[[0]])
    #Avg daily sales
        avg_sales = df_nonnull.groupby('Product')['Sales'].mean().reset_index()
        print(avg_sales)

    def filemap(self):
    #Sales trend over time
        df_nonnull = self.df.dropna()
        #trend = df_nonnull.groupby('Date')['Sales'].sum().reset_index()
        df_nonnull.groupby('Date')['Sales'].sum().plot(x = 'Date' , y = 'Sales' , kind = 'line')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.show()

    #Sales per product
        df_nonnull.plot(x='Product' , y = 'Sales' , kind = 'bar')
        plt.xlabel('Product')
        plt.ylabel('Sales')
        plt.show()


RetailSalesAnalyzer1 = RetailSalesAnalyzer()
RetailSalesAnalyzer1.fileload('/Users/lpg/GE_Code/Retails_sales_data.csv')
RetailSalesAnalyzer1.filestats()
print(RetailSalesAnalyzer1.tot_sales)
RetailSalesAnalyzer1.filemap()

import os
import sqlite3

db_pass = os.path.join(os.getcwd(), 'chinook.db')
connection = sqlite3.connect(db_pass)
cur = connection.cursor()

unit_price = '''
      SELECT 
      SUM(UnitPrice * Quantity)
      FROM invoice_items;
'''


rows = cur.execute(unit_price).fetchall()
print(rows)

print("-"*50)

First_Name = '''

SELECT [FirstName], COUNT(FirstName) as 'Количество'
FROM [customers]
GROUP BY [FirstName]

      

'''
rows = cur.execute(First_Name).fetchall()
print(rows)

connection.close()


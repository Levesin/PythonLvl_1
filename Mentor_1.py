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
SELECT id, info, COUNT(*) as count 
    FROM customers
    GROUP BY FirstName
    HAVING count(*) > 2
           and count(*) < 5
ORDER BY count DESC;
      

'''
rows = cur.execute(First_Name).fetchall()
print(First_Name)

connection.close()


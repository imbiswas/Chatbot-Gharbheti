import pyodbc

conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=BIJAY\SQLSERVER;'
    r'DATABASE=Gharbheti;'
    r'UID=sa;'
    r'PWD=1234')

cursor = conn.cursor()

datas = cursor.execute("select * from Chatfiles")
print(datas)
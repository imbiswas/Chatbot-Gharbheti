import pyodbc

conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=BIJAY\SQLSERVER;'
    r'DATABASE=Gharbheti;'
    r'UID=sa;'
    r'PWD=1234')

cursor = conn.cursor()

datas = cursor.execute("select * from Chatfiles")
# datas=cursor.execute(" SELECT * FROM ChatKeywords WHERE MATCH (token) AGAINST ('anam nagar' IN NATURAL LANGUAGE MODE);")
typlelist=[]
for lines in datas:
    typlelist.append(lines)

if typlelist==[]:
    print("empty ")
else:
    print(typlelist)



conn.close()
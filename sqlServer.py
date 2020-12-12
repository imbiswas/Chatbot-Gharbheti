import pyodbc

class connectionDatabse(object):
    def dbConn(self):
        conn = pyodbc.connect(
            r'DRIVER={ODBC Driver 17 for SQL Server};'
            r'SERVER=BIJAY\SQLSERVER;'
            r'DATABASE=Gharbheti;'
            r'UID=sa;'
            r'PWD=1234')
        return  conn

class sqlserver(object):
    def __init__(self,userid,name,email,contact,message,date,time):
        self.userid=userid
        self.name=name
        self.email=email
        self.contact=contact
        self.message=message
        self.date=date
        self.time=time
        self.dbentry()

    def dbentry(self):
        #connection string
        conn=connectionDatabse.dbConn(self)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO CHATFILES VALUES(?,?,?,?,?,?,?)",
                           (self.userid, self.name, self.email, self.contact, self.message, self.date, self.time))
        
        cursor.commit()
        conn.close()

class sqlquery(object):
    def __init__(self,userid):
        self.propertyFor = None
        self.propertyType = None
        self.Address = None
        self.user_id=userid
        self.dbFetch()

    def dbFetch(self):
        conn = connectionDatabse.dbConn(self)
        
        cursor = conn.cursor()
        self.dbReply=cursor.execute('''SELECT MESSAGE FROM CHATFILES WHERE USER_ID=(?) ''',(self.user_id,))
        for self.data in self.dbReply:
            lines=self.data[0]

            mainfile = lines.split(',')

            if mainfile[-1]=='1':
                self.propertyFor=mainfile[0]

            if mainfile[-1]=='2':
                self.Address=mainfile[0]


            if mainfile[-1]=='3':
                self.propertyType=mainfile[0]
        conn.close()

    def result(self):
        return (self.propertyFor,self.Address,self.propertyType)

class sqlservertoken(object):
    def __init__(self,userid,message):
        self.userid=userid
        self.message=message
        self.dbentrytoken()
    def dbentrytoken(self):
        #connection string
        conn = connectionDatabse.dbConn(self)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO chatToken VALUES(?,?)",
                           (self.userid, self.message))
        cursor.commit()
        conn.close()
        

class sqlquerytoken(object):
    def __init__(self, userid):
        self.propertyFor = None
        self.propertyType = None
        self.Address = None
        self.user_id = userid
        self.dbFetchtoken()

    def dbFetchtoken(self):
        conn = connectionDatabse.dbConn(self)
        cursor = conn.cursor()
        self.dbReply = cursor.execute('''SELECT token FROM chatToken WHERE Userid=(?) ''', (self.user_id,))
        for self.data in self.dbReply:
            lines = self.data[0]
            mainfile = lines.split(',')

            if mainfile[-1][0] == '1':
                self.propertyFor = mainfile[0]

            if mainfile[-1][0] == '2':
                self.Address = mainfile[0]

            if mainfile[-1][0] == '3':
                self.propertyType = mainfile[0]
        conn.close()

    def resulttoken(self):
        # print(self.propertyFor,self.Address,self.propertyType)
        return (self.propertyFor,self.Address,self.propertyType)

class sqlKeyword(object):
    def __init__(self, keyword):
        self.propertyFor = None
        self.propertyType = None
        self.Address = None
        self.keyword = keyword
        self.dbFetchtoken()

    def dbFetchtoken(self):
        self.typelist=[]
        conn = connectionDatabse.dbConn(self)
        cursor = conn.cursor()
        self.dbReply = cursor.execute('select type from ChatKeywords where token=(?) ', (self.keyword,))
        for types in self.dbReply:
            self.type=types
            self.typelist.append(self.type)
        # print(self.typelist)
        conn.close()

    def resultkeyword(self):
        # print(self.typelist)
        return (self.typelist)


class databaseWriter(object):

    def myvalues(self):
        conn = connectionDatabse.dbConn(self)
        cursor = conn.cursor()
        datas = cursor.execute("select token from chatToken")
        values = []
        for lines in datas:
            values.append(lines[0])
        cursor.commit()
        conn.close()
        return values





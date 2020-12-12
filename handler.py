import dbFetch
import datetime
import random
import sqlServer,tokenization,get_closest


class chat(object):
  
    def __init__(self,value,user_id,name,email,contact):
        self.value=value
        self.user_id=user_id
        self.name=name
        self.email=email
        self.contact=contact
        self.store_msg()
        self.reply=None
        self.controller()

    def store_msg(self):#stores every essage in the database
        try:
            time = str(datetime.datetime.now().time())
            date = str(datetime.datetime.now().date())
            sqlServer.sqlserver(self.user_id, self.name, self.email, self.contact, self.value, date,time)
        except Exception:
            print("Error from store msg")
        # time = str(datetime.datetime.now().time())
        # date = str(datetime.datetime.now().date())
        # sqlServer.sqlserver(self.user_id, self.name, self.email, self.contact, self.value, date,time)

    def store_in_database(self):#stores token in the database
        
        try:
            # print(self.tokenvalue)
            sqlServer.sqlservertoken(self.user_id, self.tokenvalue)
        except Exception:
            print("Error from store in database")
        # sqlServer.sqlservertoken(self.user_id, self.tokenvalue)
    def sqlKeyword(self,value):#fetch keywords fro the database
        try:

            sender=sqlServer.sqlKeyword(value)
            self.receiver=sender.resultkeyword()

            if self.receiver!=[]:
                typ=self.receiver[0][0]
                # print(typ)
                self.bot(typ)
        except Exception:
            print("Error from sqlkeyword")
        # sender=sqlServer.sqlKeyword(value)
        # self.receiver=sender.resultkeyword()
        #
        # if self.receiver!=[]:
        #     typ=self.receiver[0][0]
        #     # print(typ)
        #     self.bot(typ)

    def controller(self):#determine whether to go for tokenization or structured
        self.tokenization()
        try:
            if self.receiver == []:
                self.structrued()
        except Exception:
            self.sorry()


    def tokenization(self):#create tokens for the query
        tokenRequest=tokenization.tokenization(self.value)
        returnValue=tokenRequest.token()
        for values in returnValue:
            ok = get_closest.correct_content(values)
            self.tokenvalue=ok
            self.sqlKeyword(ok)

    def property(self):#for property for

        if self.tokenvalue=='buy' or  self.tokenvalue=='sell':
            self.tokenvalue='sale'
        self.tokenvalue = self.tokenvalue + ",1"
        # print(self.tokenvalue)
        self.store_in_database()
        send = dbFetch.filehandlers(self.user_id)
        receive = send.result()
        
        self.reply = receive

    def location(self): #for handling locations
        self.tokenvalue=self.tokenvalue+",2"
        self.store_in_database()
        send = dbFetch.filehandlers(self.user_id)
        receive = send.result()
        self.reply = receive


    def type(self):#for handling type of property
        self.tokenvalue=self.tokenvalue+",3"
        self.store_in_database()
        send=dbFetch.filehandlers(self.user_id)
        receive=send.result()
        self.reply = receive



    def inquiry(self):#for request is gretting or inquiry
        self.store_in_database()
        respondMessageList=["Hello!! Are you looking for sale or rent? You can choose from the following: Sale and Rent","Hi! Would you like me to find a rent or sale","Hello! are you looking for rent or sale?","hay! I can help you for rent or sale"]
        self.reply=random.choice(respondMessageList)


    def sorry(self):#if the request doesnot match any query
        self.store_in_database()
        respondMessageList =["Sorry,I didn't understand. Can you start again? Thanks!!"]
        self.reply=random.choice(respondMessageList)




    def bot(self,typ):#main method for tokenization

        if typ =="propertyFor":

            self.property()

        elif typ =="propertyType":
            self.type()

        elif typ == 'address':
            self.location()

        elif typ =='keyword':
                self.inquiry()

    def structrued(self):#for structured queries
        if 'thanks' in self.value or 'thank you' in self.value:
            respondMessageList = ["Welcome!!!", "my pleasure", '']
            self.reply = random.choice(respondMessageList)

        elif 'hello' in self.value or 'hi' in self.value:
            self.inquiry()


        elif 'bye' in self.value:
            respondMessageList = ['Bye!!! Have a great day.', "bye bye!", "bye! see you again"]
            self.reply = random.choice(respondMessageList)

        elif 'contact' in self.value:
            respondMessageList=['you can contact us info@gharbheti.com or call us on 01-4482996/9801127346',"our contact number is 01-4482996/9801127346 and email address is info@gharbheti.com"]
            self.reply = random.choice(respondMessageList)

        elif 'help' in self.value:
            respondMessageList=['could you please start with the location where you are looking for','please enter the type of property such as flat','are you looking for rent or sale?']
            self.reply = random.choice(respondMessageList)

        elif 'ok' in self.value:
            respondMessageList=[ 'sounds great. please continue your query','please proceed']
            self.reply = random.choice(respondMessageList)

        else:

            self.sorry()


    def result(self):# returns result
        if self.reply==None:
            return ("sorry something went wrong at this moment, please try again with new query.")
        return (self.reply)


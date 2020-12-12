import sqlServer
import api
import random
class filehandlers(object):
    def __init__(self,user_id):
        self.propertyFor=None
        self.propertyType=None
        self.Address=None
        self.user_id=user_id
        self.handle()
        self.usercheker=user_id[0:18]


    def handle(self):
        connection = sqlServer.sqlquerytoken(self.user_id)
        replyFor=connection.resulttoken()
        self.propertyFor =replyFor[0]
        self.Address = replyFor[1]
        self.propertyType=replyFor[2]
      


    def result(self):
        if not(self.propertyFor is None) and not(self.Address is None) and not(self.propertyType is None):
            apicaller=api.api(self.propertyFor,self.propertyType,self.Address)
            apivalue=apicaller.process()
            self.Msglist=[]
            if not apivalue:#handling empty list
                return "No result found for "+self.propertyType+" at "+self.Address+" for "+self.propertyFor+" at this moment. Please try with another search or try again later."

            else:#if the list is not empty
                for datas in apivalue:
                    self.roomType=datas[0]
                    self.description=datas[1]
                    self.location=datas[2]
                    self.totalAmount=datas[3]
                    self.imagePath=datas[4]
                    self.masterID=datas[5]
                    self.salesOrRent=datas[6]
                    baseurl='https://www.gharbheti.com/'
                    self.url=(baseurl+"/"+self.salesOrRent+"/"+self.roomType+"/"+self.location+"/"+self.masterID)
                    self.image=baseurl+'/'+self.imagePath
                    if self.usercheker=='FBFBFBFB-0000-1111':
                        outputMsg=[self.url,self.image,self.roomType,self.Address,self.description,self.totalAmount]
                    else:
                        outputMsg= ("<br/><img src="+self.image+" width='150' height='150'><br/>"+self.roomType+"<br/>Location: "+self.location+"<br/>Amount: "+ self.totalAmount+"<br/> <a target='_blank' href='"+self.url+"' class='btn btn-info' role='button'>Get Details</a><br/> ***<br/>")
                    self.Msglist.append(outputMsg)


                if self.usercheker=='FBFBFBFB-0000-1111':
                    return self.Msglist[:3]
                
                else:
                    #if the list contains 3 or less properties
                    if len(self.Msglist)<=3:
                        self.propertyList=(" ".join(self.Msglist))
                    else:
                        #get only first three items from the list
                        self.Msglist=self.Msglist[:3]
                        self.propertyList = (" ".join(self.Msglist))
                
                return ("Here are some suggestions for you: "+self.propertyList)
                # return self.propertyList


        elif (self.propertyFor is None) and (self.Address is None):
            return ("Please provide propose( like rent or sale) the location where you want your property")

        elif (self.Address is None) and (self.propertyType is None):
            return ("Please provide Address and type of property")

        elif (self.propertyFor is None)  and (self.propertyType is None):
            return ("please provide the propose( like rent or sale) and type of property.")

        elif (self.propertyFor is None):
            respondMessageList = [
                "Are you looking for sale or rent? You can choose from the following: Sale and Rent",
                "Would you like me to find a rent or sale", " are you looking for rent or sale?",
                "I can help you for rent or sale"]
            return (random.choice(respondMessageList))

        elif (self.Address is None):
            respondMessageList = ["Please Enter the location of the property you want to sale.",
                                  "Where is your property located at?", "Could you please provide me the address.",
                                  "May I know the address where you are trying to rent the property.", ]
            return (random.choice(respondMessageList))

        elif (self.propertyType is None):
            respondMessageList = [
                "What are you looking for? You can choose from :  Building , Flat , Land ,space , Hostel , Apartment",
                " Are you looking for a Flat, Building, Land, Space, Apartment or hostel"]
            return (random.choice(respondMessageList))

        else:
            return ("Please provide all the values for the purpose of property, Address and type of property.")


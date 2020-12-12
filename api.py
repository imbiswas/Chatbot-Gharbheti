import requests
import json

class api(object):
    def __init__(self,propertyFor,propertyType,Address):
        self.propertyFor=propertyFor
        self.propertyType=propertyType
        self.Address=Address
        self.startingPrice=''
        self.endingPrice=''


    def process(self):
        parturl = 'https://www.gharbheti.com/RoomRentAPI/searchproperties?'
        url=parturl+"propertyFor="+self.propertyFor+"&propertyType="+self.propertyType+"&Address="+self.Address+"&startingPrice"+self.startingPrice+"&endingPrice"+self.endingPrice
        # print(url)
        headers = {
            'apitoken': 'C67934FC-A4DB-47A2-8C84-A6EDD6F91F63',
            'apiusername':'apiuser@softechdoundation.com'
        }
        try:
            response = requests.get(url, headers=headers)
            output = response.json()
            # print(output)
            alist=[]
            self.container=[]
            for datas in output:
                self.RoomType=datas['RoomType']
                self.Description=datas['Description']
                self.Location=datas['Location']
                self.TotalAmount=datas['TotalAmount']
                self.ImagePath=datas['ImagePath']
                self.masterID=datas['OwnerPublishMasterId']
                self.saleOrRent=datas["SaleOrRent"]
                alist=[self.RoomType,self.Description,self.Location,self.TotalAmount,self.ImagePath,self.masterID,self.saleOrRent]
                self.container.append(alist)#list of properties
            # print(self.container)
            response.close()
        except Exception as e:
            print("Error")

        return (self.container)


import pymongo


#gets you the handler on the mongo client
client = pymongo.MongoClient()

#choose the data base
db = client.Surveys

#choose the collection
collection = db.usersurveystemp

#example code
def insertRecords(username, email, color, food, vacation, valuebefore, valueafter):
    collection.insert({'username': username, 'email': email, 'color': color, 'food': food})

def display():
    return collection

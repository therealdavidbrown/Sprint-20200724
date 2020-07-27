#1. Create a Mongo Database and name it Data Tracker.
import pymongo
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://dbAdmin:1234@cluster0.fsu4j.mongodb.net/DataTracker?retryWrites=true&w=majority")
db =cluster["DataTracker"]
collection = db["products"]

results = collection.delete_many({}) #deletes all documents so it is started fresh each time

#2. Add your SPRINT 3 products file to MongoDB you just created.
#3. Create a collection for your top 3 products in MongoDB.

#cooldrinks
d0 =  {"_id":0 , "brand" : 'Fanta' , "type":'cooldrink'  , "price": 10.00    }
d1 = {"_id":1 , "brand" : "Coke", "type":"cooldrink", "price":10.00}
d2 = {"_id":2 , "brand" : 'Schweppes' , "type": 'cooldrink' , "price": 12.00    }
d3 = {"_id":3  , "brand" :'Red Bull'  , "type": 'cooldrink'  , "price":15.00     }
d4 = {"_id":4  , "brand" : 'Grey poupon' , "type":  'cooldrink', "price": 45.00  }
d5 = {"_id":5  , "brand" : 'Pepsi Free' , "type": 'cooldrink' , "price": 12.00   }
d6 = {"_id":6  , "brand" :  'Pepsi', "type": 'cooldrink' , "price":  10.00   }
d7 = {"_id":7  , "brand" : 'Pepsi Max' , "type": 'cooldrink' , "price": 10.00    }
d8 = {"_id":8  , "brand" : 'Pepsi Zero' , "type": "cooldrink"  , "price":  9.00   }

#pies
d9 = {"_id":9  , "brand" : 'Pepper Steak' , "type": 'pies' , "price": 17.99    }
d10 = {"_id":10  , "brand" :  'Chicken', "type":  'pies', "price":  17.99   }
d11 = {"_id":11  , "brand" : 'Cottage Pie'  , "type": 'pies'  , "price":  19.99    }
d12 = {"_id":12  , "brand" :  "Shepard's Pie", "type":'pies'  , "price": 19.99     }
d13 = {"_id":13, "brand" : 'Eskimo Pie' , "type": "pies" , "price":  6.99   }
d14 = {"_id":14  , "brand" : "Banoffee"  , "type": "pies" , "price":  19.99   }
d15 = {"_id":15  , "brand" : "Missisipi Mud Pie" , "type": 'pies'  , "price": 24.99    }

#chocolates
d16 = {"_id":16  , "brand" : "Cadbury" , "type": 'chocolates' , "price":  13.95   }
d17 = {"_id":17  , "brand" : "tex" , "type":  'chocolates' , "price":  8.95   }
d18 = {"_id":18  , "brand" :  "Lindt", "type": 'chocolates' , "price":  35.99   }
d19 = {"_id":19  , "brand" : "Chocolate Orange" , "type": 'chocolates' , "price": 45.00    }
d20 = {"_id":20  , "brand" :  "Crunchie", "type": 'chocolates' , "price":   8.99  }

collection.insert_many([d0, d1, d2,d3, d4, d5, d6, d7, d8, d9, d10,
                        d11, d12, d13, d14, d15, d16, d17, d18, d19, d20 ])

#4. Insert multiple documents into your collections in question (3)
d21 = {"_id":21  , "brand" :  "Chocolate Log", "type": 'chocolates' , "price":   20.99  }
d22 = {"_id":22  , "brand" :  "Lunch Bar", "type": 'chocolates' , "price":   8.99  }
d23 = {"_id":23  , "brand" :  "Wonder bar", "type": 'chocolates' , "price":   3.99  }
d24 = {"_id":24  , "brand" :  "Pieing Pie", "type": 'pies' , "price":   25.00  }
d25 = {"_id":25  , "brand" :  "M&Ms", "type": 'chocolates' , "price":   14.99  }
d26 = {"_id":26  , "brand" :  "Energade", "type": 'cooldrink' , "price":   11.99  }
d27 = {"_id":27  , "brand" :  "Kit Kat", "type": 'chocolates' , "price":   8.99  }
d28 = {"_id":28  , "brand" :  "Kit Kat: Chunky", "type": 'chocolates' , "price":   8.99  }
d29 = {"_id":29  , "brand" :  "Kit Kat: Chunky: Salted Caramel Fudge", "type": 'chocolates' , "price":   8.99  }
d30 = {"_id":30  , "brand" :  "Kit Kat: Chunky: Salted Caramel Fudge: Mediterranean Kosher Sea Salt Edition", "type": 'chocolates' , "price":   8.99  }
collection.insert_many([d21, d22, d23, d24, d25, d26, d27, d28, d29, d30])

#5. Implement a descending sort to your data in MongoDB
results = collection.find().sort("price", -1)
for result in results:
    print(result)
    
print("done")

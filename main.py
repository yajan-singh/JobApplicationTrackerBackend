import pymongo

# Connect to MongoDB
client = pymongo.MongoClient(
    "mongodb+srv://MongoDB:Pa55Word!@firstcluster.bc0ks91.mongodb.net/?retryWrites=true&w=majority")
db = client["APPLICATIONS"]

# Insert application handler
while True:
    # reset variables
    company = ""
    position = ""
    link = ""

    # wait for user input
    while company == "":
        company = input("Company Name: ").lower()
    while position == "":
        position = input("Position Title: ").lower()
    while link == "":
        link = input("Position URL: ").lower()

    for i in db.applications.find(
            {"company.name": company, "company.positions.title": position}):
        print("Application already exists!")
        continue

    # insert application
    db.applications.insert_one({
        "company": {
            "name": company,
            "positions": [{
                "title": position,
                "link": link,
            }]
        },
        "status": 0,
        "mail": "",
    })


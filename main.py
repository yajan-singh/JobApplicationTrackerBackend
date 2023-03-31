from time import sleep
import pymongo
import os


# Clear console lambda
def clear(): return os.system('clear')


# Connect to MongoDB
client = pymongo.MongoClient(
    "mongodb+srv://MongoDB:Pa55Word!@firstcluster.bc0ks91.mongodb.net/?retryWrites=true&w=majority")
db = client["APPLICATIONS"]

# Insert application handler
while True:
    # clear console
    clear()

    # reset variables
    company = ""
    position = ""
    link = ""

    print("\nTotal Applied: ", db.applications.count_documents({}) - 1, "\n")

    # wait for user input
    while company == "":
        company = input("Company Name: ").lower()
    if company == "-":
        continue
    while position == "":
        position = input("Position Title: ").lower()
    if position == "-":
        continue

    # check if application already exists
    for i in db.applications.find(
            {"company.name": company, "company.positions.title": position}):
        print("\nApplication already exists!")
        sleep(2)
        break
    else:

        # wait for user input
        while link == "":
            link = input("Position URL: ").lower()
        if link == "-":
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

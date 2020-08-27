import pymongo
from pymongo import MongoClient
import config as cfg

cluster = MongoClient(cfg.client)

db = cluster['Cedar_Lake']
collection = db['Members']
    

def status_mentor():
    x = 0
    while x == 0:
        status = input("What is their status? Interest, Disciple, or Mentor? ")
        if status == "Disciple":
            mentor = input("Who is their mentor? ")
            x += 1
        elif status == "Interest":
            mentor = input("Who is their church contact? ")
            x += 1
        elif status == "Mentor":
            mentor = "Jacob Gibbs"
            x += 1
        else:
            status = input("It appears you've mispelled their status. Please try again. Option are 'Interest', 'Disciple', or 'Mentor' ")
    return status, mentor

# if __name__ == "__main__":
#     print("==Welcome to the Cedar Lake MongDB Database==")
#     print("Please enter the following details:")
#     first = input("First Name: ")
#     last = input("Last Name: ")
    
#     print("==Now, contact information==")
#     address = input("Full Address: ")
#     phone = input("Best phone number: ")
#     location = input("Which town/suburb do they live in? ")
#     status, mentor = status_mentor()

#     print("==Review data==")
#     post = {
#             "name": {"first": first, "last": last },
#             "contact": {
#                 "address": address,
#                 "phone": phone,
#                 "location": location
#             },
#             "status": status,
#             "mentor": mentor
#         }

#     print(post)

#     ready = input("Looks good? Hit enter to add.")
#     if ready == "":
#         collection.insert_one(post)
#     else:
#         print("Restart the program to try again.")


post = {'name': {'first': 'Seth', 'last': 'Roberts'}, 'contact': {'address': '4769 Feather Trail, Cedar Lake, MI 48812', 'phone': '(509) 240-7153', 'location': 'Cedar Lake'}, 'status': 'Mentor', 'mentor': 'Jacob Gibbs'}
collection.insert_one(post)

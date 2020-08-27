import pymongo
from pymongo import MongoClient
import cfg
import church_data as cd

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


post = {"_id": 1, 'name': {'first': 'Seth', 'last': 'Roberts'}, 'contact': {'address': '4769 Feather Trail, Cedar Lake, MI 48812', 'phone': '(509) 240-7153', 'location': 'Cedar Lake'}, 'status': 'Mentor', 'mentor': 'Jacob Gibbs'}
#collection.insert_one(post)

post1 = {"_id": 2, 
'name': {'first': 'Dave', 'last': 'Ellis'}, 
'contact': 
{'address': '510 N Division Street, Carson City, MI 48811', 
'phone': '(989) 220-8277', 
'location': 'Carson City'}, 
'position': 'Disciple', 
'mentor': 'Seth Roberts',
'status': 'Meeting'}

post2 = {"_id": 3, 
'name': {'first': 'Steve', 'last': 'Williams'}, 
'contact': 
{'address': '6039 E. Lake Moncalm Road, Edmore, MI 48829', 
'phone': '(989) 565-0174',
'location': 'Cedar Lake'}, 
'position': 'Disciple', 
'mentor': 'Seth Roberts',
'status': 'Contacted'}

post3 = {"_id": 4, 
'name': {'first': 'Nancy', 'last': 'Coon'}, 
'contact': 
{'address': '11960 E. Edgar Road, Vestaburg, MI 48891', 
'phone': '(989) 268-1001',
'location': 'Vestaburg'}, 
'position': 'Disciple', 
'mentor': 'Seth Roberts',
'status': 'Contacted'}

post4 = {"_id": 5, 
'name': {'first': 'Mona', 'last': 'Nessen'}, 
'contact': 
{'address': '4163 N. Sheridan Road, Stanton, MI 48888', 
'phone': '(706) 506-7520',
'location': 'Stanton'}, 
'position': 'Disciple', 
'mentor': 'Seth Roberts',
'status': 'Contacted'}

post6 = {"_id": 6, 
'name': {'first': 'Matthew', 'last': 'Romashko'}, 
'contact': 
{'address': '125 Charlotte Street, Edmore, MI 48829', 
'phone': '(989) 560-3437',
'location': 'Edmore'}, 
'position': 'Disciple', 
'mentor': 'Seth Roberts',
'status': 'Contacted'}

post7 = {"_id": 7, 
'name': {'first': 'Jeff', 'last': 'Akenberger'}, 
'contact': 
{'address': '5417 Quarter Road, Edmore, MI', 
'phone': '(989) 385-0100',
'location': 'Edmore'}, 
'position': 'Mentor', 
'mentor': 'Jacob Gibbs',
'status': 'Contacted'}

post8 = {"_id": 8, 
'name': {'first': 'Scott', 'last': 'Smith'}, 
'contact': 
{'address': '5200 N Luce Road, Alma, MI 48801', 
'phone': '(989) 944-3494',
'location': 'Alma'}, 
'position': 'Disciple', 
'mentor': 'Seth Roberts',
'status': 'Contacted'}

post9 = {"_id": 9, 
'name': {'first': 'Dean', 'last': 'Voss'}, 
'contact': 
{'address': '7350 Vickeryville Road, Edmore, MI 48829', 
'phone': '(989) 304-1991',
'location': 'Edmore'}, 
'position': 'Disciple', 
'mentor': 'Seth Roberts',
'status': 'Contacted'}

post10 = {"_id": 10, 
'name': {'first': 'Dave', 'last': 'Carter'}, 
'contact': 
{'address': '5660 Faculty Drive, Cedar Lake, MI 48812', 
'phone': '(989) 565-0020',
'location': 'Cedar Lake'}, 
'position': 'Disciple', 
'mentor': 'Seth Roberts',
'status': 'Contacted'}

collection.insert_one(post10)

students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
    {"first_name": "Mark", "last_name": "Guilen"},
    {"first_name": "KB", "last_name": "Tonel"},
]

def namesp1():
    for i in students:
        print i["first_name"], i["last_name"]
namesp1()


users = {
    "Students": [
        {"first_name": "Michael", "last_name": "Jordan"},
        {"first_name": "John", "last_name": "Rosales"},
        {"first_name": "Mark", "last_name": "Guilen"},
        {"first_name": "KB", "last_name": "Tonel"}
    ],
    "Instructors": [
        {"first_name": "Michael", "last_name": "Choi"},
        {"first_name": "Martin", "last_name": "Puryear"},
    ]
}

def namesp2():
    for role in users:
        print role
        counter = 0
        for person in users[role]:
            counter += 1 #numbers each of the people per role
            first_name = person["first_name"].upper() #uppercase
            last_name = person["last_name"].upper()
            length = len(first_name) + len(last_name)
            print counter, "-", first_name, last_name, "-", length
namesp2()

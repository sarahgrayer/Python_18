Using the shell...

Retrieve all users:
User.objects.all()

Get the last user:
User.objects.last()

Create a few records in the users:
User.objects.create(first_name = 'Chloe', last_name = 'Dog', email_address = 'cd@gmail.com', age = 1)

Get the first user:
User.objects.first()

Get the users sorted by their first name (order by first_name DESC):
User.objects.all().order_by("last_name")

Get the record of the user whose id is 3 and UPDATE the person's last_name to something else:
user3 = User.objects.get(id=3)
user3.last_name = "Shepherd"
user3.save()

Delete a record of a user whose id is 4:
User.objects.get(id=4).delete()
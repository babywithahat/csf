#!/usr/bin/python2

daily_tasks = ["wake up", "eat", "poop", "smoke a cigarette", "sleep"]
print "name : daily_tasks"
print "type : ", type(daily_tasks)
print "contents : ", daily_tasks
print "length : ", len(daily_tasks)

print ""
unique_items = set(daily_tasks)
print "name : unique_items"
print "type : ", type(unique_items)
print "contents : ", unique_items
print "length : ", len(unique_items)

print""
coordinate = (1,2,3)
print "coordinate = (1,2,3)"
print "type : ", type(coordinate)

mental_state = ["slow", "ravenous", "relief", "focused", "sleepy"]
the_day = (daily_tasks, mental_state)

print ""
phone_contact = { "Mom":"306-123-12345", 
                  "Dad":"306-987-6543" }
print phone_contact
print type(phone_contact)
for (k,v) in phone_contact.items():
    print k + " has number " + v
print "phone_contact.items()"
print phone_contact.items()
print type(phone_contact.items())

print ""
a = [{'a':1, 'b':2},{'c':3, 'd':4}]
print "a = ", a
print "a[0] = ", a[0]
#print "a[0][0] = ", a[0][0]

print ""
rows1 = [{'dem':1.0, 'rep':1.0}]
print "rows1 =               ", rows1
print type(rows1)
print "rows1[0] =            ", rows1[0]
print type(rows1[0])
print "rows1[0].items() =    ", rows1[0].items()
print "rows1[0].values() =   ", rows1[0].values()
print "rows1[0].keys() =     ", rows1[0].keys()
print "rows1[0].items()[0] = ", rows1[0].items()[0]

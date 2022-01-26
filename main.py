import json
import sys

#Get user names to look for from argv
length = len(sys.argv)
usersToLookFor = []
for x in range(1, length):
    usersToLookFor.append(sys.argv[x])


#open users file and get the user id that matches with the user name sent with argv
with open('users.json') as f:
    data = json.load(f)

userIdList=[]
for users in usersToLookFor:
    for x in data:
        if(x['name'])== users:
            userIdList.append(x['id'])

f.close()


#open events file and get the even date related to the users that our client looking for
with open('events.json') as f:
    events = json.load(f)

eventList=[]
for users in userIdList:
    for event in events:
        if(event['user_id'])== users:
            tempEvent = {
                'start_time': event['start_time'],
                'end_time': event['end_time']
            }
            eventList.append(tempEvent)

f.close()


#sort the eventList
sortedEventList = sorted(eventList, key= lambda i: (i['start_time']))

#define starting and end point for the calender events
eventStartTime = "2021-07-05T13:00:00"
eventEndTime = "2021-07-07T21:00:00"

#find if there exists a first availability time slot between eventStartTime and the first event in sortedEventList
tempAvailabilityList = []
if(sortedEventList[0]['start_time']!=eventStartTime):
    tempEvent = {
                'start_time': eventStartTime,
                'end_time': sortedEventList[0]['start_time']
    }
    tempAvailabilityList.append(tempEvent)

#find if there exists a last availability time slot between the last event in sortedEventList and eventEndTime
if(sortedEventList[len(sortedEventList)-1]['end_time']!=eventEndTime):
    tempEvent = {
                'start_time': sortedEventList[len(sortedEventList)-1]['end_time'],
                'end_time': eventEndTime
    }
    tempAvailabilityList.append(tempEvent)

#find the free times in between the events
currentStartTime = sortedEventList[0]['start_time']

for event in sortedEventList:
    if(event['end_time'] <= currentStartTime):
        continue

    if(event['start_time'] > currentStartTime):
        tempEvent = {
                'start_time': currentStartTime,
                'end_time': event['start_time']
        }
        tempAvailabilityList.append(tempEvent)
    
    if(event['end_time'] > currentStartTime):
        currentStartTime = event['end_time']


#clear out the work day conflicts from the time slots
availabilityList = []
for event in tempAvailabilityList:
    tempTime = event['start_time'].split('T')
    startOfWorkDay = tempTime[0]+'T13:00:00'
    endOfWorkDay = tempTime[0]+'T21:00:00'

    if((event['start_time'] >= startOfWorkDay) and (event['start_time'] != endOfWorkDay)):
        if(event['end_time'] <=endOfWorkDay):
                tempEndTime = event['end_time']
        else:
                tempEndTime = endOfWorkDay
        tempEvent={
            'start_time': event['start_time'],
            'end_time': tempEndTime
        }

        availabilityList.append(tempEvent)



#Print the output results
prevTempStartTime = availabilityList[0]['start_time'].split('T')[0]
for event in availabilityList:
    tempStartTime = event['start_time'].split('T')
    tempEndTime = event['end_time'].split('T')

    if(tempStartTime[0] == prevTempStartTime):
        print(tempStartTime[0] + " " + tempStartTime[1] + " - " + tempEndTime[1])
    else:
        print()
        print(tempStartTime[0] + " " + tempStartTime[1] + " - " + tempEndTime[1])
    prevTempStartTime = tempStartTime[0]

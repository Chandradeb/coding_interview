# Background

Most calendar applications provide some kind of "meet with" feature where the user
can input a list of coworkers with whom they want to meet, and the calendar will
output a list of times where all the coworkers are available.

For example, say that we want to schedule a meeting with Jane, John, and Mary on Monday.

- Jane is busy from 9am - 10am, 12pm - 1pm, and 4pm - 5pm.
- John is busy from 9:30am - 11:00am and 3pm - 4pm
- Mary is busy from 3:30pm - 5pm.

Based on that information, our calendar app should tell us that everyone is available:
- 11:00am - 12:00pm
- 1pm - 3pm

We can then schedule a meeting during any of those available times.


# Instructions

Given the data in `events.json` and `users.json`, build a script that displays available times
for a given set of users. For example, your script might be executed like this:

```
python availability.py Maggie,Joe,Jordan
```

and would output something like this:

```
2021-07-05 13:30 - 16:00
2021-07-05 17:00 - 19:00
2021-07-05 20:00 - 21:00

2021-07-06 14:30 - 15:00
2021-07-06 16:00 - 18:00
2021-07-06 19:00 - 19:30
2021-07-06 20:00 - 20:30

2021-07-07 14:00 - 15:00
2021-07-07 16:00 - 16:15
```


For the purposes of this exercise, you should restrict your search between `2021-07-05` and `2021-07-07`,
which are the three days covered in the `events.json` file. You can also assume working hours between
`13:00` and `21:00` UTC, which is 9-5 Eastern (don't worry about any time zone conversion, just work in
UTC). Optionally, you could make your program support configured working hours, but this is not necessary.


## Data files

### `users.json`

A list of users that our system is aware of. You can assume all the names are unique (in the real world, maybe
they would be input as email addresses).

`id`: An integer unique to the user

`name`: The display name of the user - your program should accept these names as input.

### `events.json`

A dataset of all events on the calendars of all our users.

`id`: An integer unique to the event

`user_id`: A foreign key reference to a user

`start_time`: The time the event begins

`end_time`: The time the event ends


# Notes

- Feel free to use whatever language you feel most comfortable working with
- Please provide instructions for execution of your program
- Please include a description of your approach to the problem, as well as any documentation about
  key parts of your code.
- You'll notice that all our events start and end on 15 minute blocks. However, this is not a strict
  requirement. Events may start or end on any minute (for example, you may have an event from 13:26 - 13:54).


My solution:

To run the program execute following command:
python main.py Maggie, Joe, Jordan

(user name can be different depending on the requirements)

My approach to the problem:
I used the knowledge I inherited from my problem solving class in college. I basically made a flow chart for solving this problem and dealt with each problem, one at a time.
First, I decided to get the user names from the argument sent using the command and used those user names to get user id from "users.json" file and created a list called usersToLookFor. Then, I used usersToLookFor list to get start date and end date of the events related to those users from "events.json" file. I sorted the list and saved it sortedEventList.
After that, I used my logic to find free time slot in between those events. First, I started by creating a variable named currentStartTime and setting it equal to the start time of the first event. Then, I looped through sortedEventList. Inside the loop, I first compared end_time of the event and if its smaller or equal to currentStartTime, I broke the iteration and proceeded to next one. My thought process behind this approach was if the event in the iteration end_time is already smaller than or equal to the current event in question, then I don’t need to take this event into consideration. If its not smaller or equal, I compared the start_time of the event in current iteration to currentStartTime and if the start_time is bigger than currentStartTime, that means I have found the even then I created a tempEvent dictionary with key start_time which equals to currentStartTime and end_time which equals to start_time of the event in the current iteration. My thought process behind this approach was if the start time is greater than currentStartTime than the start_time of this event is the end time of free time slot. And after that I compared if the end_time of the event in the current iteration is bigger than currentStartTime and if it is, I reset the currentStartTime to the end_time of the current event as that would be the start of free time slot if there is any.
This logic was working fine until I did some testing and realized that I was missing some free time slots due to not taking two things into consideration. The first availability time slot between eventStartTime and the first event in sortedEventList and the last availability time slot between the last event in sortedEventList and eventEndTime. I checked if those two time slots exist and added them at the beginning of my logic.
Then, I discovered the new problem which is conflicting after work hour time slots. So, I filtered them out by iterating through the loop again and comparing start_time of each free time slots with start time of each workday and end time of each workday to make sure every free time slots starts between start and end of work hours. If those two conditions were met, I compared end_time of that free time slot with end of workday to make sure each free time slots ends at the end of work hours and not later than that.
After that, I simply printed out the result using simple print function in python. I used split method to make sure I group free time slots of each day into different group separated by an empty line to make it more visually pleasing.


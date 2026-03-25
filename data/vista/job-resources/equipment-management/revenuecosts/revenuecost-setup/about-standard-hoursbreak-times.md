---
title: "About Standard Hours/Break Times | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-standard-hoursbreak-times"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-standard-hoursbreak-times"
---

# About Standard Hours/Break Times

The system uses the standard hours (sum of day start and stop
 times, less break times) to calculate the total number of hours a piece of equipment is on
 the job on a normal day.
For example, if your workday begins at 08:00
 and ends at 17:00 (9 hours), and you normally break for lunch from 12:00 – 1:00 (1
 hour), the standard number of hours per day would be 8 (9–1=8).
Note: The system will allow for 24-hour bill periods, as
 long as the hours span a single day. However, since “24:00” is not a valid hour, you
 will need to enter 00:00 as both the day start and day stop times (i.e., midnight to
 midnight).
On the day you transfer equipment to a job,
 the system calculates the usage hours by subtracting the later of the start time or
 ‘transfer in’ time from the workday stop time. It then subtracts the time for any breaks
 that occurred during that period.
For example, if your workday starts at 08:00
 and stops at 17:00, and you transfer the equipment ‘in’ at 10:00, the system subtracts
 10:00 from 17:00 (7 hours) because it is later than 08:00. Then, if you have designated
 a break time of 12:00 to 13:00 (1 hour), it subtracts that from the 7 hours to get a
 total of 6 hours for that day.
When calculating the usage hours for the
 ‘transfer out’ day, a similar method is used. The system subtracts the workday start
 time from the earlier of the ‘transfer out’ time or the workday stop time. It then
 subtracts the time for any breaks that occurred during that period.
To get the total number of hours a piece of
 equipment was on a job for a billing period, the system multiplies the standard number
 of hours per day by the number of full days (the days between the transfer in/out days),
 and adds them to the number of hours calculated for the transfer in/out days.

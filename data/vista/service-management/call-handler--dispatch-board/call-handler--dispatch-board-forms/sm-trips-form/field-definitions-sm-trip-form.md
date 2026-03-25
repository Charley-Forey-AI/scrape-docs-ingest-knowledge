---
title: "Field Definitions: SM Trip Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/call-handler--dispatch-board/call-handler--dispatch-board-forms/sm-trips-form/field-definitions-sm-trip-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/call-handler--dispatch-board/call-handler--dispatch-board-forms/sm-trips-form/field-definitions-sm-trip-form"
---

# Field Definitions: SM Trip Form

The following is a list of field descriptions for the SM Trip
 form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Work Order

This field is enabled only when you access this form via SM Work Centers.
Enter the work order for which this trip is being scheduled. Initially defaults the work order selected in SM Work Center, SM Dispatch Board, or SM Work Orders.

## Trip

Enter the trip to edit or enter N, New, or
 + to add a new trip. The
 system will automatically assign the next sequential trip number.

## Assignment

Assignment field on the SM Work Orders form, Info tab of scope section.
Enter
 an assignment number, or press F4 for the SM Assignment Lookup from
 which to select an assignment number. Press F5 to connect to the [SM Assignments](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-assignments-form) form.

## Description

Enter a description of the trip. Up to 60 characters.

## Details

Use this field to enter any details pertinent to this trip or the work to be done (e.g. special considerations or instructions, information about who to contact at the specified location, etc.). Space allowance is virtually unlimited.

## Status

From the drop-down menu, select the status of this trip.

- 0-Open — All new trips default this status. You will typically leave trips at this status if you have not scheduled the trip or assigned a technician.

- 1-Notified — The technician has been notified of the scheduled trip. Trips are set to this status automatically when the technician is notified electronically (using the Notify option in SM Dispatch Board).

- 2-Accepted — The technician has accepted the trip assignment.

- 3-Rejected — The technician has rejected the trip assignment.

- 4-En Route — The technician is traveling to the service site.

- 5-Arrived — Technician has arrived at the service site, but not yet begun the scheduled work.

- 6-In Progress — Technician is at the service site; scheduled work is currently in progress.

- 7-Completed — Technician has completed the scheduled work and returned from the trip.

- Once you select a status here, the system automatically sets the status Date and Time (on the Status Detail tab) equal to the system date and time. You may override these values as needed for the selected status. For more information, see [About Status Detail](/en/vista/vista/service-management/call-handler--dispatch-board/sm-dispatch-board/about-using-the-dispatch-board/about-trips/about-the-status-detail-for-a-trip).

- You can also set the status for a trip using the trip context menu in SM Dispatch Board. See [Updating the Trip Status](/en/vista/vista/service-management/call-handler--dispatch-board/sm-dispatch-board/about-using-the-dispatch-board) in the SM Dispatch Board help for more information.

- When you close a work order, the system automatically sets the status to 7-Completed for all trips with a status greater than 0-Open. Trips with a status of 0-Open will be deleted.

## Multi-Day Trip

Select this checkbox to indicate that this trip will span multiple days. The trip will display as an all-day trip for each of the dates from the
 Scheduled Date
 to the
 Scheduled End Date
 .
Selecting this checkbox enables the
 Scheduled End Date
 field, and hides the
 Scheduled Start Time
 and
 Estimated Duration
 fields.

## Scheduled Date

Enter the date work is scheduled to be performed at the service site.
For multi-day trips (Multi-Day Trip
 checkbox is selected), if you edit the date in this field, then the date in the Scheduled End
 Date field will be updated to maintain the same trip duration.

## Scheduled Start Time

Displays only when the Multi-Day Trip
 checkbox is not selected.
Enter the start time scheduled for this trip. Initially defaults as follows:

- If you added this trip directly in SM Trips, this field defaults as blank.

- If you added this trip in SM Dispatch Board using the drag-and-drop function, defaulting is based on the time view:

- If using the Hourly view, this field defaults to the time slot selected (i.e. if you dropped the trip on 09:00 A, this field defaults as 09:00). If overridden, the trip will be moved accordingly on the dispatch board.

- If using the Day or Week views, this field defaults as blank.

Note: Changing the status of a trip to In Progress does not affect the Scheduled Start Time. This allows you to track differences between scheduled start times and actual start times.

## Estimated Duration

Displays only when the Multi-Day Trip
 checkbox is not selected.
Enter the estimated number of hours it will take to complete the work specified on this work order.
Note: If you do not specify an estimated duration, the text displayed when you hover over the trip on the dispatch board will default a Duration time of 1 hour. Once you specify an actual duration time, the hover text will display the hours you specify.

## Scheduled End Date

Displays only when the Multi-Day Trip
 checkbox is selected.
Enter the date that work is scheduled to end at the service site.
If you edit the date in the Scheduled Date
 field, then the date in this field will be automatically updated to maintain the same trip
 duration.

## Technician

The Technician field in the SM Trips form, Info tab.
Enter the technician scheduled for this trip
 or press F4 to select from list of valid technicians. Technician must be flagged as Active in PR Employees and must not be flagged as Do Not Use for the customer or service site (in SM Technician Preferences).
If you have defined work schedules for your technicians, and you enter a technician who is not scheduled to work on the specified date or who is scheduled to work but is already assigned to other work order trips, you will receive a warning; however, you will be allowed to save the record.
Note: If you did not assign a lead technician to the work order (header) and this is the first trip on the work order to which you have assigned a technician, the system will auto-assign this technician as the lead technician for the work order.

### Agreement Work Orders

If this trip was auto-added during work order generation (in SM Generate PM Work Orders), this field will default the Assigned Tech designated for the agreement service in SM Service. See [Assigned Tech](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-form/field-definitions-sm-service-form#ID-0004141b--en) for more information.

## Reason

The Reason field on the SM Trips form, Info tab.
If a return trip is needed for the specified service site/work order, enter a reason code to indicate why. Press F4 to select from a list of valid reason codes (set up in HQ Reason Codes).

## Notes

The Notes field on the SM Trips form, Info tab.
 Use this field to enter any additional information about why a return trip for this service site/work order is needed. The space allowance is virtually unlimited.

## Open: Date

Required if also entering Open Time.
This status is applied automatically once you add a trip via SM Trips or by dragging and dropping the work order on time slot or date in SM Dispatch Board, and displays the date this trip was created. May be overridden if needed.
Note: If you change the trip's Scheduled Date (Info tab) to
 a date prior to the date specified here, the system automatically sets this date equal to
 the Scheduled Date and sets the Open Time field to 00:00.

## Open: Time

This field is only enabled when the trip status is Open. The Open status is applied automatically or by dragging and dropping the work order on time slot or date in SM Dispatch Board.
Required if also entering Open Date.
Displays the time this trip was created. May be overridden if needed.
Note: If you change the trip's Scheduled Date (Info tab) to a date prior to the Open Date, the system automatically sets the Open Date equal to the Scheduled Date and sets this field to 00:00.

## Notified: Date

This field is only enabled when the trip status is Notified or greater.
Requires also entering Notified Time.
Displays the notification date for this trip. Initially defaults as follows:

- If you changed the status of this trip to Notified directly in SM Trips, this field defaults to the system date (today's date).

- If you selected the Notify...option for this trip in SM Dispatch Board (right-clicking on the trip and selecting Notify... from the context menu), once the notification is sent to the employee, this field populates with the date the notification was sent.

- If you changed the status of this trip to Notified in SM Dispatch Board (by right-clicking on the trip and selecting Notified from the context menu), this field defaults the date specified in the Date
 Notified field in the Trip Date Picker pop-up window.

You may override the date as needed to reflect the actual date the technician was notified of this trip.
Note: If you change from this status to a lesser status, the system will clear the date and time for this status.

## Notified: Time

This field is only enabled when the trip status is Notified or greater.
Requires also entering Notified Date.
Displays the notification time for this trip. Initially defaults as follows:

- If you changed the status of this trip to Notified directly in SM Trips, this field defaults to the system time (current time).

- If you selected the Notify...option for this trip in SM Dispatch Board (right-clicking on the trip and selecting Notify... from the context menu), once the notification is sent to the employee, this field populates with the time the notification was sent.

- If you changed the status of this trip to Notified in SM Dispatch Board (by right-clicking on the trip and selecting Notified from the context menu), this field defaults the time specified in the Date Notified field in the Trip Date Picker pop-up window.

You may override the time as needed to reflect the actual time the technician was notified of this trip.
Note: If you change from this status to a lesser status, the system will clear the date and time for this status.

## Accepted: Date

This field is only enabled when the trip status is Accepted or greater.
Requires also entering Accepted Time.
Enter the date this trip was accepted (typically by the technician). Initially defaults to the system date.
Note: If you change from this status to a lesser status, the system will clear the date and time for this status.

## Accepted: Time

This field is only enabled when the trip status is Accepted or greater.
Requires also entering Accepted Date.
Enter the time this trip was accepted (in 24-hour format). Initially defaults to the system time.
Note: If you change from this status to a lesser status, the system will clear the date and time for this status.

## Rejected: Date

This field is only enabled when the trip status is Rejected or greater.
Requires also entering Rejected Time.
Enter the date this trip was rejected (typically by the technician). Initially defaults to the system date.
Note: If you change from this status to a lesser status, the system will clear the date and time for this status.

## Rejected: Time

This field is only enabled when the trip status is Rejected or greater.
Requires also entering Rejected Date.
Enter the time this trip was rejected. Initially defaults to the system time.
Note: If you change from this status to a lesser status, the system will clear the date and time for this status.

## En Route: Date

This field is only enabled when the trip status is En Route or greater.
Requires also entering En Route Time.
Enter the date the technician left for the service site. Initially defaults to the system date.
Note: If you change from this status to a lesser status, the system will clear the date and time for this status.

## En Route: Time

This field is only enabled when the trip status is En Route or greater.
Requires also entering En Route Date.
Enter the time the technician left for the service site. Initially defaults to the system time.
Note: If you change from this status to a lesser status, the system will clear the date and time for this status.

## Arrived: Date

This field is only enabled when the trip status is Arrived or greater.
Requires also entering Arrived Time.
Enter the date the technician arrived at the service site. Initially defaults to the system date.
Note: If you change from this status to a lesser status, the system will clear the date and time for this status.

## Arrived: Time

This field is only enabled when the trip status is Arrived or greater.
Requires also entering Arrived Date.
Enter the time the technician arrived at the service site. Initially defaults to the system time.
Note: If you change from this status to a lesser status, the system will clear the date and time for this status.

## In Progress: Date

This field is only enabled when the trip status is In Progress or greater.
Requires also entering In Progress Time.
Displays the 'in progress' date for this trip. Initially defaults as follows:

- If you changed the status of this trip directly in SM Trips, this field defaults to the system date (today's date).

- If you changed the status of this trip in SM
 Dispatch Board (by right-clicking on the trip and selecting In Progress from the
 context menu), defaults the date entered in the Date In Progress field in the Trip
 Date Picker pop-up window.

You may override this date as needed to reflect the actual 'in progress' date for the trip.

- The date and time of this status must be less than the date and time of the Completed status.

- If you change from this status to a lesser status, the system will clear the date and time for this status.

-  Changes to the in-progress date will not affect the trip's Scheduled Date; however, it will affect the trip's placement on the SM Dispatch Board.

## In Progress: Time

This field is only enabled when the trip status is In Progress or greater.
Requires also entering In Progress Date.
Displays the 'in progress' time for this trip (in 24-hour format). Initially defaults as follows:

- If you changed the status of this trip directly in SM Trips, this field defaults to the system time (current time).

- If you changed the status of this trip in SM
 Dispatch Board (by right-clicking on the trip and selecting In Progress from the
 context menu), defaults the time entered in the Time In Progress field in the Trip
 Date Picker pop-up window.

You may override the time as needed to reflect the actual 'in progress' time for the trip.

- The date and time of this status must be less than the date and time of the Completed status.

- If you change from this status to a lesser status, the system will clear the date and time for this status.

-  Changes to the in-progress time will not affect the trip's Scheduled Start Time; however, if you are using the Hourly view in SM Dispatch Board, it will affect the trip's time slot placement.

## Completed: Date

This field is only enabled when you set the trip status to Completed (via the Info tab or using the trip context menu in SM Dispatch Board).
Required if also entering Completed Time.
Displays the completion date for this trip. Initially defaults as follows:

- If you changed the status of this trip directly in SM Trips, this field defaults to the system date (today's date).

- If you changed the status of this trip in SM
 Dispatch Board (by right-clicking on the trip and selecting Completed from the
 context menu), defaults the date entered in the Date Completed field in the Trip
 Date Picker pop-up window.

You may override this date as needed to reflect the actual completion date for the trip.

- The date and time of this status must be greater than the date and time of the In Progress status.

- If you change from this status to a lesser status, the system will clear the date and time for this status.

## Completed: Time

This field is only enabled when you set the trip status to Completed (via the Info tab or using the trip context menu in SM Dispatch Board).
Required if also entering Completed Date.
Displays the completion time for this trip (in 24-hour format). Initially defaults as follows:

- If you changed the status of this trip directly in SM Trips, this field defaults to the system time (current time).

- If you changed the status of this trip in SM
 Dispatch Board (by right-clicking on the trip and selecting Completed from the
 context menu), defaults the time entered in the Time Completed field in the Trip
 Date Picker pop-up window.

You may override the time as needed to reflect the actual completion time for the trip.

- The date and time of this status must be greater than the date and time of the In Progress status.

- If you change from this status to a lesser status, the system will clear the date and time for this status.

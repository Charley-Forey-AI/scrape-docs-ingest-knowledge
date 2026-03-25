---
title: "Set up Service Work Schedules | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/service-schedules/about-service-work-schedules/set-up-service-work-schedules"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/service-schedules/about-service-work-schedules/set-up-service-work-schedules"
---

# Set up Service Work Schedules

You will use the Schedule tab in SM Service to define the frequency at which each service on the work schedule is to be performed.
This will automatically generate and schedule preventative maintenance work orders.
For each service, you must indicate whether the customer must be contacted before scheduling, identify when the service is due, and define the schedule pattern (e.g. the 1st of every month, once a year, etc.).
Once you set up service schedules, you can run the SM Generate PM Work Orders form to generate preventative maintenance work orders for services that are due based on a set of criteria. If you are required to contact a customer before scheduling work, the system displays a message indicating contact is required before scheduling the work order.
The following steps detail how to set up a service work schedule.

1. From the main menu, select Service Management > Programs > SM Agreements. The SM Agreements form opens.

1. In the Agreement field, enter the agreement for which you are defining a service work schedule.

1. Select the Work Schedule tab and then double-click in the grid to open the SM Service form.

1. In the Service Seq field, enter the service for which to set up a service schedule.

1. Select the Schedule tab.

1. If you are required to contact the customer before scheduling the service, select Contact Before Scheduling.

1. If you want trips automatically scheduled for this service on the Dispatch Board, select the Auto Schedule Trips checkbox.Note: Auto-scheduled trips will default to the date and technician specified on the SM Service form.

1. From the Due drop-down, select when the service is due.

- 1-Due On

- 2-Due By

- 3-Due Within

 - If you selected 3-Due Within, enter the number of 'due within' days in the Days field to the right.
Note: When generating preventative maintenance work orders, the system defaults this option on the work order scope and uses this in conjunction with the schedule pattern to determine the due date for the specified service.

1. In the Recurring Pattern section, specify when the service will occur by selecting the appropriate radio button (Task Scheduled, Daily, Weekly, Monthly, or Yearly).

1. Using the recurrence options available for the frequency you selected, create the desired recurrence pattern. See the F1 help for more information about each option. For example:
If you selected the Task Scheduled option in Step 8, you will enter a frequency code (in the Frequency field) rather than a recurring pattern.
Note: The frequency code entered for Task Scheduled services is only used to identify the frequency at which the service will occur. Scheduling for these services is handled using the SM Task Scheduling form.

1. Save the record.

1. Repeat steps 4-10 for each service you have set up for the agreement.

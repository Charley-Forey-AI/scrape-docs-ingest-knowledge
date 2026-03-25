---
title: "SM Agreement Task Schedule Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-task-schedule-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-task-schedule-form"
---

# SM Agreement Task Schedule Form

Use the SM Agreement Task Schedule form to set up agreement task schedules.
Access this form by selecting Task Scheduling in SM Agreements.
Task schedules allow you to define the frequency at which maintenance tasks or other service tasks are performed for each applicable service on an agreement (those with the Task Scheduled recurring pattern selected on the Schedule tab of SM Service).
The scheduling grid automatically displays a list of agreement services that are flagged for task scheduling, along with their designated frequency. You can set up a schedule for each service by assigning a task group to each applicable month in the selected year (based on the agreement term). For more information, see [Set up an Agreement Task Schedule](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/about-tasking--task-scheduling/set-up-an-agreement-task-schedule).
Once you activate the agreement, the system then uses the task schedule to create a list of service dates.

## How the System Uses Task Groups

If you set up task schedules for an agreement, the system uses the task groups assigned to each month to determine grouping of tasks on a work order. Task groups are set up by craft/class, so if you have tasks requiring technicians of the same craft/class and you want them included on a single work order, you would assign the same task group to each applicable service for each applicable month. For example, if you have yearly, monthly, and quarterly services, all due in January, you would assign the same task group to January for each service.
In addition, each service you want grouped together on a work order must have the following criteria in common:

- same price method (and rate template if applicable)

- same call type

- same service site

- same service center and, if applicable, division

- not flagged for separate work order

When you generate preventative maintenance work orders, the system will group all services for the agreement that meet the specified criteria on a single work order/scope.
Note: If you selected the Separate Scope Per Service Item checkbox for the agreement in SM Agreements (Info tab), the work order generation process (in SM Generate PM Work Orders) creates a separate work order scope for each service item rather than grouping them on the same work order scope. If you also selected the Separate Work Order checkbox for one or more agreement services, the system generates a separate work order for each agreement service flagged for a separate work order and sets up the remaining services on one work order with separate scopes per service item.

## What do the colors mean?

When you assign a task group to a month, the system checks the labor allocation table to verify certain values between the labor allocation entries and the scheduled task. Based on this check, the system will highlight the month in one of the following colors:

- Pink – This color is applied when no hours are found in the labor allocation for the call type associated with the scheduled task/agreement service. This will occur if:

- The labor allocation call type does not match the scheduled task call type (which is the same as the agreement service call type)

- The labor allocation and scheduled task call types match, but no hours are posted to the allocation call type.

- No labor allocations have been set up

- Yellow – This color is applied when the task group has a different craft/class designation than the labor allocation entry of the same call type.

- Gray – This color occurs when the labor allocation call type matches the scheduled task call type, hours are posted to the labor allocation call type, and the craft/class for the labor allocation and schedule task match.

You can change the data as needed for tasks highlighted in pink or yellow; however, it is not required.

---
title: "Resource Scheduling Installation | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/resource-scheduling/installation-overview/resource-scheduling-installation"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/resource-scheduling/installation-overview/resource-scheduling-installation"
---

# Resource Scheduling Installation

Use this screen to establish a list of operators who will
 be able to schedule jobs and equipment from companies other than the current company.
In addition, use this screen to set some of the default values (starting times and quantity
 cost types) that will be used elsewhere in the module, and multi-company permissions.
This screen is protected by company-based security and only those operators with the required security settings can access this screen's information.
Note: When the Resource Scheduling Installation screen is
 opened for the first time, a dialog box stating "CONTROL RECORD HAS NOT BEEN CREATED-OK TO
 PROCEED" will display. Once this installation screen has been completed and the information
 saved, the message will not appear again.
Field
Description

Default start time
Type the number of hours that will
 serve as the default start time in the Schedule Employees and Equipment screen
 and the Schedule Equipment Moves screen. Hours entered here must be between 0
 and 23.  The time entered in this field is used as a
 default on the Schedule Employees & Equipment screen. Because scheduling
 is tracked by day (not by time), an assignment's start time is more a
 convenient memo field for the purposes of planning and e-mail notification.


Default assignment duration
Enter the number of days for the
 default assignment duration. Entering zero will indicate an indefinite
 assignment date.
Allow multi-company for scheduled jobs and equipment?
Select this checkbox to display the
 following:

- New, Edit, and Delete buttons that are used to
 create and manage a list of operators and their access to the Resource
 Scheduling module in this company.

- A list box (including Operator, Name, Job companies,
 and Equipment companies columns).

- The Job companies column will display No if
 multi-company jobs are not allowed for the operator.

- The Equipment companies column will display No
 if multi-company equipment is not allowed for the corresponding
 operator.

This checkbox defaults to clear/cleared,
 signaling that you cannot access any of the job and equipment codes while in
 the Resource Scheduling module.
If this checkbox
 is selected but your operator is not already set up in this screen, then you
 will not be able to access the current company from the Resource Scheduling
 module.
Lastly, if this checkbox is selected and
 your operator is set up in the list of operators, you will have access to
 the company code prompt in the Edit Operator window based on your settings
 for jobs and equipment.

New/Edit Operator window

Operator
Enter an operator code.
Multi-company jobs
Select this checkbox to give the
 operator access to jobs for the specified companies. The default is ALL
 companies, or a list of companies can be specified using the SuperSelect
 options. Clear this checkbox to deny access to jobs.
Multi-company equipment
Select this checkbox to give the
 operator access to equipment for the specified companies. The default is ALL
 companies, or a list of companies can be specified using the SuperSelect
 options. Clear this checkbox to deny access to equipment.

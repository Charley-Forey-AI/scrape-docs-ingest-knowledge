---
title: "Quantity Complete Entry - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/quantity-complete-entry/quantity-complete-entry---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/quantity-complete-entry/quantity-complete-entry---field-descriptions"
---

# Quantity Complete Entry - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields/Buttons
Descriptions

Listing
Click this button to open the [Quantity Complete Edit Listing](/en/spectrum/spectrum/accounting/payroll/data-entry/quantity-complete-entry/quantity-complete-edit-listing) screen.

Employee
Click this button to open the [Pre-Time Card Entry](/en/spectrum/spectrum/accounting/payroll/data-entry/pre-time-card-entry) screen.

By Job
Click this button to open the[Pre-Time Card Entry by Job](/en/spectrum/spectrum/accounting/payroll/data-entry/pre-time-card-entry-by-job) screen.

Company
The current company code defaults in this field.

Job
Enter the job number for which quantities will be entered. The job description will display to the right of this field.

Batch
Enter the batch or job number corresponding to the pre-time card information to be printed. Press Enter to print ALL batches and jobs entered in Pre-Time Card Entry.

Date
Enter the date (for example, for hours that the employee worked on the 14th, enter "14").
The cursor stops at the Date field for all pay types, including Miscellaneous, Special Amount, and OTHER (1,2,3) pay types. It also prompts for 'day' when entering an add-on for a job. This optional information will then be stored permanently in the time card history file upon update of the Payroll cycle.
 If the previously entered department does not allow work in process for the entered pay type, then the job, phase, and cost type fields will be skipped and no entry will be allowed. If the department code and pay type indicate that this is a work in process account, then a valid job, phase and cost type must be entered.

Phase
Enter the phase number for this line. The phase and cost type entered must be previously set up in job cost or entry will be disallowed and an error message will display. No entry is required if the phase status is Complete.
If this is a sub-job transaction set up on a master job, double-click on this field to search phases for the sub-job. This will allow you to easily select a phase set up on a master job, but not present on the sub-job. Spectrum will add a new phase to the sub job if the current job is a sub-job of a valid master job, the phase lengths of both jobs match, and the Phase + Cost type combination for the current job is valid and not 'Complete'.

Ct
Enter the cost type for this line.
Note regarding Equipment Usage and cost types:
If a new EU line is for a job, then the cost type is assigned based on the following hierarchy: first, the system checks the G/L account in the Payroll department to see if it has a cost type specified; if blank then the system checks the Equipment Control Installation for a cost type; if blank, then the import cost type is used.

Descriptions
The phase description displays in this field.

Um
The unit of measure displays from the job cost phase file. For example, Labor quantities might be "hours", Material quantities might be "each", and so forth.

Est quantity
Based on the cost type, the estimated quantity displays from the Phase Maintenance screen.

JTD quantity
The job-to-date quantity displays from the Phase Maintenance screen.

Add'l JTD quantity
Enter any additional quantities that were completed for this phase and cost type. Repeat entry until all quantities have been entered. When entry is complete, click OK until the fields clear. Enter a new job and repeat until all desired job cost quantities have been entered for all jobs.

Crew
Enter a valid crew code for this line. A crew code with a status of Not used may not be entered.
If this field is skipped based on installation settings, press the back arrow to return to this field for entry of a crew number.

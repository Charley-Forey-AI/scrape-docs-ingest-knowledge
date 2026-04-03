---
title: "Cost Type File Maintenance - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/cost-type-file-maintenance/cost-type-file-maintenance---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/cost-type-file-maintenance/cost-type-file-maintenance---field-descriptions"
---

# Cost Type File Maintenance - Field Descriptions

Use the table below for reference when completing fields on this screen.
Fields
Descriptions

Cost type
This is the Key field for the cost type file. This code is used throughout the job cost system and is not usually changed once it is set up.
Enter a unique code to define the Cost type, click the drop-down arrow, or double-click in this field to select from a list of available cost types.
Any combination of letters and digits may be defined (26 uppercase and lowercase alpha codes, plus the 10 numeric codes). Generally, contractors use alpha (L for labor, M for material, S for subcontractor) or numeric 1, 2, 3. Keep in mind that cost types sort alpha-numerically by default.

Description
The cost type description is printed throughout Spectrum on job cost screens and reports.

G/L account code
 This entry allows for validation of the correct General Ledger code during A/P Invoice/Credit Memo Entry, Time Card Entry, and other data entry screens in Spectrum.

- If no validation is needed, press Enter to leave this optional field blank.

- If validation is needed, the account code must have been defined in the chart
 of accounts through G/L Master File
 Maintenance > New > G/L account
 code. A lookup window is available for viewing valid G/L
 account codes.Note: This must be a direct job
 cost code.

It is NOT recommended that you enter a GL code here when you are operating in a departmentalized chart of accounts structure.

Summary Name
Select the summary name to assign to the cost type for grouping purposes.
The Summary Name is also used for JC Cost Type Summary Setup for Business Intelligence Reporting.

Post to job cost history in detail?
Select this checkbox to separate the job cost history entries when posting to Job Cost History for this cost type. Leave this checkbox is clear to summarize the job cost history entries.
This option is applicable to all job cost history sources: Accounts Payable, Equipment Control, Inventory Control, and Payroll. In all cases, if the cost type being posted to is set for detail posting, no summarization will occur when writing to the job cost history record.
When the cost type is selected for detail, an internal counter sequence is used as part of the key to the history file to ensure uniqueness.

> Post detail = selected
Post detail = clear

Payroll
One entry per time card line
One entry per check

Accounts Payable
One entry per line of distribution per invoice
One entry per invoice

Inventory Control
One line per line of the requisition
One line per item per requisition

Equipment Control
One line per transaction line
One line per piece of equipment

Job Cost
One line per transaction line
One line per reference

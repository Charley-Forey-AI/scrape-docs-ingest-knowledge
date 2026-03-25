---
title: "Field Definitions: WF Checklist Initialization Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/work-flow/checklists/wf-checklist-initialization/field-definitions-wf-checklist-initialization-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/work-flow/checklists/wf-checklist-initialization/field-definitions-wf-checklist-initialization-form"
---

# Field Definitions: WF Checklist Initialization Form

The following is a list of field descriptions for the WF
 Checklist Initialization form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Company

 Enter the company for filtering checklists. This field defaults to the current company.

## Checklist Status

Select one or more statuses for filtering. Any checklists with a matching status type displays in the grid.

- New

- In Progress

- Final

When you access this form, the New and In Progress checkboxes default to checked.

## Search By Checklist Date

Select an option for sorting by a checklist date.

- None – The system does not filter by a checklist date

- Created – The system filters by the checklist creation date.

- Completed – The system filters by the checklist completed date.

If you select ‘Created’ or ‘Completed’, enter a date range in the Beginning Date and Ending Date fields.

## Beginning Date/Ending Date

Enter a range of dates for filtering.
Note: If you do not enter a date in either field, the system automatically enters yesterday’s date in the Beginning Date field and a date fifteen days later in the Ending Date field.

##  Init

 Select this checkbox to create a new checklist based on this template or checklist.

##  New Name

 Enter a name for the new checklist.

## Init Status

 Enter the initial status for this checklist,
 or press F4 to select from a list of available status codes.
If you see these codes: 999997, 999998, or 999999, you should not use them. Instead, set up status codes for New, In Progress, and Final in WF Checklist Status Codes.

##  Dest Co

 Enter the destination company for the new checklist. This field defaults to the current company.

##  Set Private

 Select this checkbox to keep this checklist from displaying for other users.

##  Send Notification

 Select this checkbox to allow automatic notifications for this checklist.

##  Enforce Order

 Select this checkbox if users must complete all tasks and steps in order.

##  Assign To

 Enter the name of the user this checklist is assigned to. Press F4 for a list of users.

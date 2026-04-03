---
title: "Job Notes | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/job-cost-services/job-notes"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/job-cost-services/job-notes"
---

# Job Notes

Use this service to import Job Notes information.
WSDL: JobNotes.jws
Method: JobNotes
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Job Notes information, the following file maintenance areas must be completed:

- System Administration > Installation > Job Cost

- System Administration > Installation > Job Cost > Job Maintenance

- System Administration > Installation > Job Cost > Job Note Topics Maintenance

## Assumptions and Dependencies

- If Company_Code is blank then use the Authorization ID default value.

- The Job_Number and Notes_Topic must exist in order to add the notes.

- The Job Notes web service has an option to append to the current Note Topic.

- If not defined then the Notes will be replaced.

- The formatting options available within the Notes are not supported.

- The Notes_Text can hold up to 1000 characters total in the table therefore if appending the notes and the value of the current notes plus the web service notes exceeds the limit, the web service notes will be truncated.

- If duplicate records exist to be updated, then they will all be updated as they are processed.

## Field Descriptions

Use the table below for reference when using this service.
Note: The Authorization_ID and GUID elements are not shown on the
 Spectrum Excel Office Add-in templates for data entry points.
Excel
Element Name
Description
Req
Type
Max
Format
Validation

Authorization_ID
Authorization ID to access the server
YES
Text
20
Data Exchange Installation Screen

GUID
Unique reference number created by programming
Text
36
** See GUID definition

B
Company_Code
Company Code
Text
3
Valid Company in Spectrum. Defaults from the Authorization ID if not populated.

C
Job_Number
Job Number
YES
Text
10
Valid Job and must exist for the defined Company Code.

D
Notes_Topic
Notes Topic
YES
Text
20
Job Note Topics Maintenance

E
Notes_Text
Notes
Text
1000

F
Append_Note
Append Notes?
Text
1
 (Y) to append. Blank = Replace all notes

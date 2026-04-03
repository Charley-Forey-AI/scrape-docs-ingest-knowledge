---
title: "Subcontract Notes | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-payable-services/subcontract-notes"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-payable-services/subcontract-notes"
---

# Subcontract Notes

Use this service to import Subcontract Notes information.
WSDL: SubcontractNotes.jws
Method: SubcontractNotes
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Subcontract Notes information, the following file maintenance areas must be completed:

- System Administration > Installation > Accounts Payables

- System Administration > Installation > Accounts Payables > Subcontract

- System Administration > Installation > Accounts Payables > Subcontract Note Topics
 Maintenance

## Assumptions and Dependencies

- If Company_Code is blank then use the Authorization ID default value.

- The Vendor_Code, Subcontract_Number and Notes_Topic must exist in order to add the notes.

- The Subcontract Notes web service has an option to append to the current Note Topic.

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
YES
Text
3
Valid Company in Spectrum. Defaults from the Authorization ID if not populated.

C
Vendor_Code
Vendor Code
YES
Text
10
Valid combination of Vendor_Code and Subcontract_Number
Vendor

D
Subcontract_Number
Subcontract Number
Text
10
Valid combination of Vendor_Code and Subcontract_Number
Subcontract

E
Notes_Topic
Notes Topic
YES
Text
20
Customer Note Topics Maintenance

F
Notes_Text
Notes
Text
1000

G
Append_Note
Append Notes?
Text
1
 (Y) to append. Blank = Replace all notes

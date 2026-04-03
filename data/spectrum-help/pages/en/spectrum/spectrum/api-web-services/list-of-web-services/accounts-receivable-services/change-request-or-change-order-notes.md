---
title: "Change Request or Change Order Notes | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-receivable-services/change-request-or-change-order-notes"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-receivable-services/change-request-or-change-order-notes"
---

# Change Request or Change Order Notes

Use this request to import AR Change Request or Change Order Notes information.
WSDL: ChgReqChgOrderNotes.jws
Method: ChgReqChgOrderNotes
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing AR Change Request or Change Order Notes information, the following file maintenance areas must be completed:

- System Administration > Installation > Accounts Receivable

- System Administration > Installation > Accounts Receivable > Customers

- System Administration > Installation > Accounts Receivable > Change Request

- System Administration > Installation > Accounts Receivable > Change Order

- System Administration > Installation > Job Cost > Jobs

## Assumptions and Dependencies

- If Company_Code is blank then use the Authorization ID default value.

- The Job_Number, Customer_Code, Type, and CR_CO_Number must exist in order to add the notes.

- The Change Request or Change Order Notes web service has an option to append to the current Note Topic.

- If not defined then the Notes will be replaced.

- The formatting options available within the Notes are not supported.

- The Notes_Text can hold up to 1000 characters total in the table therefore if appending the notes and the value of the current notes plus the web service notes exceeds the limit, the web service notes will be truncated.

- If duplicate records exist to be updated, then they will all be updated as they are processed.

## Field Descriptions

Use the table below for reference when using this service.
Note: The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.
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
Valid Company in Spectrum

C
Job_Number
Job
YES
Text
10
Unique combination of Job, Customer, Type and Number. * See Assumption and Dependencies.
Job

D
Customer_Code
Customer
YES
Text
10
Unique combination of Job, Customer, Type and Number. * See Assumption and Dependencies.
Customer

E
Type
Type of Note
YES
Text
2
(CR)Change Request or (CO)Change Order only.

F
CR_CO_Number
Change Request or Change Order #
YES
Text
8
Number must exist for the unique combination of Job, Customer and Type. * See Assumption and Dependencies.

G
Notes_Text
Notes
Text
1000

H
Append_Note
Append Notes?
Text
1
(Y) to append. Blank = Replace all notes

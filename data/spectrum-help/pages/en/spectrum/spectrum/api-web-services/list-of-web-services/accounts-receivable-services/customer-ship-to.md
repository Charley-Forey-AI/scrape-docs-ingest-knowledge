---
title: "Customer Ship-to | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-receivable-services/customer-ship-to"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-receivable-services/customer-ship-to"
---

# Customer Ship-to

Use this service to import Customer Ship-to information.
WSDL: CustomerShipto.jws
Method: CustomerShipto
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Customer Ship-to information, the following file maintenance areas must be completed:

- System Administration > Installation > Accounts Receivable

- System Administration > Installation > Accounts Receivable > Customer Maintenance

- System Administration > Installation > Accounts Receivable > Ship-to Code Maintenance

## Assumptions and Dependencies

- If the Company_Code is blank then use the Authorization ID default value.

- The Customer Ship-to Address web service will either create a new Ship-to code or update an existing Ship-to code.

- To add a new Ship_Code, leave this field blank and it will use the next available sequence number.

- To change information, define the unique Customer_Code and Ship_Code fields in the layout. This will update all the detail information provided.

- The service does not delete values that exist in Spectrum; it only changes data defined in the layout.

- The Ship_Code only allows up to 999 per Customer_Code to be created.

- If the Ship_Code is not defined then then next available number will be used.

- Records cannot be updated when user is locking the entry screen.

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
Text
3
Valid Company in Spectrum. Defaults from the Authorization ID if not populated.

C
Customer_Code
Customer code
YES
Text
10
Customer Maintenance

D
Ship_Code
Ship-to code
Numeric
3
Unique combination of Customer code and Ship-to code. Define code to change information; leave blank to add new code and uses next sequence available.
Customer and Ship-to Maintenance

E
Ship_Name
Ship-to name
Text
30
Required if creating a new Ship-to code.

F
Ship_Cust_Job
Customer's job
Text
10

G
Ship_Address1
Ship-to Address 1
Text
30

H
Ship_Address2
Ship-to Address 2
Text
30

I
Ship_City
Ship-to City
Text
25

J
Ship_State
Ship-to State/province
Text
2
2 character postal abbreviation

K
Ship_Zip_Code
Ship-to Postal code
Text
10

L
Ship_Contact
Ship-to Contact name
Text
20

M
Ship_Phone
Telephone
Numeric
14
Formatted for example, (206) 555-1212 or 123-123-1224 or 123-1233 or 1231231225.
Remove the dashes from format when sending to Spectrum.

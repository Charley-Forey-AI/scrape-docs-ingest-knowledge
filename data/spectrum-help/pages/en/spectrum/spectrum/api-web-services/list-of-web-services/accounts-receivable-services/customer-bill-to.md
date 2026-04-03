---
title: "Customer Bill-to | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-receivable-services/customer-bill-to"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-receivable-services/customer-bill-to"
---

# Customer Bill-to

Use this service to import Customer Bill-to information.
WSDL: CustomerBillto.jws
Method: CustomerBillto
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Customer Bill-to information, the following file maintenance areas must be completed:

- System Administration > Installation > Accounts Receivable

- System Administration > Installation > Accounts Receivable > Customer Maintenance

- System Administration > Installation > Accounts Receivable > Bill-to Code Maintenance

## Assumptions and Dependencies

- If the Company_Code is blank then use the Authorization ID default value.

- The Customer Bill-to Address web service will either create a new Bill-to code or update an existing Bill-to code.

- To add a new Billto_Code, leave this field blank and it will use the next available sequence number.

- To change information, define the unique Customer_Code and Billto_Code fields in the layout. This will update all the detail information provided.

- The service does not delete values that exist in Spectrum; it only changes data defined in the layout.

- If the Billto_Code is not defined then then next available number will be used.

- If the Status is blank and a new Bill-to code is being created it will default to be Active.

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
Billto_Code
Bill-to code
Text
4
Unique combination of Customer code and Bill-to code. If blank auto populate with next available number.
Customer and Bill-to Maintenance

E
AltName
Bill-to name
Text
30
Required if creating a new Bill-to code.

F
AltPhone
Telephone
Numeric
14
Formatted for example, (206) 555-1212 or 123-123-1224 or 123-1233 or 1231231225.
Remove the dashes from format when sending to Spectrum.

G
AltFax
Fax
Numeric
14
Formatted for example, (206) 555-1212 or 123-123-1224 or 123-1233 or 1231231225.
Remove the dashes from format when sending to Spectrum.

H
AltAddr1
Bill-to Address 1
Text
30

I
AltAddr2
Bill-to Address 2
Text
30

J
AltCity
Bill-to City
Text
25

K
AltState
Bill-to State/province
Text
2
2 character postal abbreviation

L
AltZip
Bill-to Postal code
Text
10

M
AltCountry
Bill-to Country
Text
25

N
AltContact
Bill-to Contact
Text
20

O
AltEmail
Bill-to Email
Text
80
Example: John@xxx.com
Must be the basic layout for an email address.

P
Remark
Bill-to Remarks
Text
250

Q
Status
Status
Text
1
A(ctive) or I(nactive) only. If blank then defaults to A for new billto_codes.

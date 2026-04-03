---
title: "Add Work Order Site Address | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/work-order-services/add-work-order-site-address"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/work-order-services/add-work-order-site-address"
---

# Add Work Order Site Address

Use this service to add site addresses to work orders.
WSDL: AddWOSiteAddress.jws
Method: AddWOSiteAddress
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Work Order Site information, the following file maintenance areas must be completed:

- System Administration > Installation > Work Order

- System Administration > Installation > Accounts Receivable

- System Administration > Installation > Payroll

- System Administration > Installation > Work Order > Lead Source Maintenance

- System Administration > Installation > Work Order > Technician Maintenance

- System Administration > Installation > Work Order > Type Maintenance

- System Administration > Installation > Work Order > Zone Maintenance

- System Administration > Installation > Work Order > Site Maintenance

- System Administration > Installation > Work Order > Make Maintenance

- System Administration > Installation > Work Order > Model Maintenance

- System Administration > Installation > Work Order > Equipment Type Maintenance

- System Administration > Installation > Accounts Receivable > Customer Maintenance

- System Administration > Installation > Accounts Receivable > Sales Tax Code Maintenance

- System Administration > Installation > Accounts Receivable > Bill-to Code Maintenance

- System Administration > Installation > Payroll > Tax Tables Maintenance

- System Administration > Installation > Payroll > Worker's Compensation Code Maintenance

- System Administration > Installation > Work Order > Site User-Defined Fields

- System Administration > Installation > Work Order > Site Note Topics Maintenance

- System Administration > Installation > Enterprise Management > Cost Center Maintenance

## Assumptions and Dependencies

- All work order sites are created with an 'Active' Status.

- Billing Address defaults from the Customer Code unless defined within the service.

- The Site_Contact_Person, Site_Phone1 and the Work_Site_Email fields will be used to define the Contact on the Work Order site and marked as the Primary Contact.

- Cost centers will validate against the Cost Center Maintenance Table and Customer Cost Center.

- Cost Center information will only be allowed in if Company is set to Pending or Yes status.

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
Valid Company in Spectrum

C
Site_ID
Site code
YES
Text
10
No duplicates

D
Site_Name
Site Name
YES
Text
30

E
Site_Address1
Address Line 1
Text
30

F
Site_Address2
Address Line 2
Text
30

G
Site_City
City
Text
25

H
Site_State
State
Text
2
2 digit postal code

I
Site_Zip_Code
Zip
Text
10

J
Site_Phone1
Site Phone
Text
14
Formatted for example, (206) 555-1212 or 123-123-1224 or 123-1233 or 1231231225.
 Remove the dashes from format when sending to Spectrum.

K
Telephone_Ext_1
Site Phone Ext
Text
4

L
Site_Phone2
Other Phone
Text
14
Formatted for example, (206) 555-1212 or 123-123-1224 or 123-1233 or 1231231225.
 Remove the dashes from format when sending to Spectrum.

M
Telephone_Ext_2
Other Phone Ext
Text
4

N
Site_Contact_Person
Site Contact
Text
20
No commas

O
Site_Customer_Code
Customer Code
Text
10
Customer Maintenance File

P
Lead_Source
Lead Source Code
Text
15
Lead Source Maintenance

Q
Requested_Tech
Requested Tech
Text
11
Technician Maintenance

R
WO_Type
Work Order Type
Text
5
Work Order Type Maintenance

S
Zone
Zone
Text
3
Work Order Zone Maintenance File

T
Special_Instructions
Alert Notes
Text
70

U
Show_Notes
Display Alert Notes in WO main properties?
Text
1
(Y)es or (N)o only. Blank = No

V
Sales_Tax_Code
Sales Tax Code
Text
15
Defaults from the Customer Code if blank.
A/R Sales Tax Code Maintenance File.

W
Taxable_Flag
Default site to Taxable?
Text
1
(Y)es or (N)o only. Blank = No

X
Labor_Taxable
Labor Taxable?
Text
1
(Y)es or (N)o only. Blank = No

Y
Material_Taxable
Material Taxable?
Text
1
(Y)es or (N)o only. Blank = No

Z
Work_Comp_Code
Worker's Compensation Code
Text
6
Worker's Compensation Code Maintenance File

AA
Wage_Rate_Level
Wage Rate Level
Numeric
1
numbers 1-9

AB
Work_State_Tax_Code
Work State Code
Text
10
The Work Tax codes must be unique.
Tax Table Maintenance

AC
Work_County_Tax_Code
Work County Code
Text
10
The Work Tax codes must be unique.
Tax Table Maintenance

AD
Work_Local_Tax_Code
Work Local Code
Text
10
The Work Tax codes must be unique.
Tax Table Maintenance

AE
Work_Site_Email
WO Contact Email
Text
80
Must be the basic layout for an email address. Example: John@xxx.com

AF
Site_Case_Type
Case Type
Text
10
Case Type Maintenance

AG
Customer_Job
Customer Job
Text
10
No validation

AH
Latitude
Latitude
Numeric
11
Format = -XXX.XXXXXX.

AI
Longitude
Longitude
Numeric
11
Format = -XXX.XXXXXX.

AJ
Markup_Code
Non-Stock Markup Code
Text
10
Non-stock Markup File Maintenance

AK
Alternate_Address
Print alternate address on work order/invoice?
Text
1
(Y)es or (N)o only. Blank = No

AL
Billto_Code
Bill-to code
Text
4
Required if Alternate_Address is Y. Tied to defined Customer code.
Customer Bill-to Address Maintenance

AM
Cost_Center
Site Cost Center
Text
10
Cost Center Maintenance and Customer Cost Center

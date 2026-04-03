---
title: "Update Service Contract | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/service-contract-services/update-service-contract"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/service-contract-services/update-service-contract"
---

# Update Service Contract

Use this service to import Service Contract information.
WSDL: UpdateServiceContract.jws
Method: UpdateServiceContract
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Service Contract information, the following file maintenance areas must be completed:

- System Administration > Installation > Service Contract

- System Administration > Installation > Service Contract > Service Contract

- System Administration > Installation > Service Contract > Contract Type

- System Administration > Installation > Work Order > Site

- System Administration > Installation > Work Order > Work Order Type Maintenance

- System Administration > Installation > Work Order > Material Markup Maintenance

- System Administration > Installation > Accounts Receivable > Customer Maintenance

- System Administration > Installation > Accounts Receivable > Sales Tax Code Maintenance

- System Administration > Installation > Accounts Receivable > Salesperson Code Maintenance

- System Administration > Installation > Accounts Receivable > Bill-to Code Maintenance

- System Administration > Installation > Enterprise Management > Cost Center Maintenance

## Assumptions and Dependencies

- The following fields are required to create a new Service Contract when Create_New is defined as Y -

- Site_Code

- Contract_Number

- Description

- Contract_Type

- Work Order Type

- Customer_Code

- Web service cannot create a duplicate Service Contract.

- A Valid combination of Site_ID and Contract_Number must exist to change the data.

- The Contract_Type has default options for what type of basis will be used for the billing. These defaults will override any data shown in the Basis field when creating a new Service Contract only.

- The Contract_Amount field cannot be less than the unscheduled balance when updating this field.

- The Cost_Center field is not required and is used as an override if defined within the Service Contract. The cost center validates the standard hierarchy of Site, Contract type and Customer.

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
Text
3
Valid Company in Spectrum. Defaults from the Authorization ID if not populated.

C
Site_ID
Site
YES
Text
10
Valid combination of Site_ID and Contract_Number.
Work Order Site

D
Contract_Number
Contract
YES
Text
10
Valid combination of Site_ID and Contract_Number if changing information
Service Contract

E
Create_New
Create New Service Contract?
Text
1
Y=Yes or N=No. If blank then defaults to N.

F
Description
Description
Text
30
Required for a new Service Contract

G
Contract_Type
Contract type
Text
2
**See Assumptions and Dependencies.
Service Contract Type

H
Salesman
Salesperson
Text
3
AR Salesperson

I
Begin_Date
Start date
Date
10
Enter as: MM/DD/YYYY (for example, 01/05/2010)

J
End_Date
End date
Date
10
Enter as: MM/DD/YYYY (for example, 01/05/2010). Must be within processing dates.

K
WO_Type
Work order type
Text
5
Required for a new Service Contract
Work Order Type

L
Material_Level
Material level
Numeric
1
Allows levels 0-5 to be defined. Defaults to 0 if blank.

M
Labor_Level
Labor level
Numeric
1
Allows levels 0-5 to be defined. Defaults to 0 if blank.

N
Markup_Code
Material markup
Text
10
Must be valid for the given time frame
Work Order Material Markup

O
Include_Notes
Include contract notes?
Text
1
Y=Yes or N=No. If blank then defaults to N.

P
Include_Exceptions
Include contract exceptions?
Text
1
Y=Yes or N=No. If blank then defaults to N.

Q
Proposal_Flag
Proposed service contract?
Text
1
Y=Yes or N=No. If blank then defaults to N.

R
Proposal_Date
Proposal issued date
Date
10
Enter as: MM/DD/YYYY (for example, 01/05/2010)

S
Proposal_Days_Honored
Honor Proposal for number of days
Numeric
3

T
Customer_Code
Customer
Text
10
Customer

U
Contract_Amount
Total contract amount
Numeric
13
Positive numbers only. Format = 10.2 **See Assumptions and Dependencies.

V
Taxable_Flag
Taxable?
Text
1
Y=Yes or N=No. If blank then defaults to N.

W
Sales_Tax_Code
Sales Tax
Text
15
AR Sales Tax Code

X
Bill_Date_List1
Billing start date
Date
10
Enter as: MM/DD/YYYY (for example, 01/05/2010)

Y
Number_Of_Bill_Periods
Total contract billings
Numeric
3

Z
Basis
Earned revenue basis
Text
1
B=As billed, S=Straigh line, V=Visit dates, C=Budget cost of visit and O=Other. If blank defaults to B (As billed). **See Assumptions and Dependencies.

AA
Billto_Code
Bill-to code
Text
4
Customer Bill-to Address

AB
Cost_Center
Cost center
Text
10
**See Assumptions and Dependencies.
Cost Center Maintenance. Service Contract, WO Site and Customer Cost Center.

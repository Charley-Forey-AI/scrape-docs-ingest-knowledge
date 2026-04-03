---
title: "Add Inventory Job Requisitions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/inventory-control-services/add-inventory-job-requisitions"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/inventory-control-services/add-inventory-job-requisitions"
---

# Add Inventory Job Requisitions

Use this service to import Inventory Job Requisitions information.
WSDL: AddJob_Reqs.jws
Method: AddJob_Reqs
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Inventory Job Requisitions information, the following file maintenance areas must be completed:

- System Administration > Installation > Inventory Control

- System Administration > Installation > Inventory Control > Inventory Item File Maintenance

- System Administration > Installation > Inventory Control > Inventory Item Category File Maintenance

- System Administration > Installation > Inventory Control > Warehouse File Maintenance

- System Administration > Installation > Inventory Control > G/L Department File Maintenance

- System Administration > Installation > General Ledger > G/L Master File Maintenance

- System Administration > Installation > Job Cost > Jobs

- System Administration > Installation > Job Cost > Job Phases

- System Administration > Installation > Job Cost > Cost Type File Maintenance

- System Administration > Installation > Job Cost > Job Classifications

- System Administration > Installation > Accounts Payable > Use Tax Code Maintenance

- System Administration > Installation > System Administration > Security > Operator Maintenance

## Assumptions and Dependencies

- If the Company_Code is blank then use the Authorization ID default value.

- The Instructions and Message fields will be truncated if they exceed the Max character length.

- The Status will default to O(rdered) if left blank.

- The import has a record limit of 990 records per Requisition and the service will prevent any additional detail lines to be added.

- The Job Requisition header contains the following fields which must match in order to add detail lines.

- Company_Code

- Batch_Code

- Operator

- Transaction_Reference

- Req_Company_Code

- Default_Job

- Status

- Transaction_Date

- Ship_Date

- From_Warehouse

- The Inventory Item must exist for the defined warehouse.

- Non-stock items can be created using the combination of the Item_Category and the Item_Code using the standard Spectrum logic.

- If the Non-stock item logic exceeds the character length then the defined Item_Code will be truncated.

- If the Non_Stock_Description field is not defined then the Item Category Description will be used.

- If field is populated and the Item Code is not defined as a non-stock item then this field will be ignored

- If the Transaction_Reference is blank in the web service then the following logic will apply.

- If a Transaction_Reference exists within the unposted Inventory transaction table and all header information matches then the web service will add additional records until it reaches the 990 record limits then create additional Transaction_Reference as needed.

- If a Transaction_Reference does not exist within the unposted Inventory transaction table then the web service will follow the standard Spectrum logic and create auto-assigned reference numbers.

- GL_Credit_Account field defaults from the GL_Department field if left blank and must be a non-direct cost account.

- The Standard_Cost field can be defined or is defaulted from the Item_code. The Inventory Control Installation defined how and if the Standard_Cost data is updated or not.

- The Inventory Control Installation defined whether or not multi_company requisitions can be done.

- Job Requisitions are not created when Physical Inventory is in progress.

- For Intercompany Job Requisitions

- The options and set up must be completed on the company Inventory Installation screens.

- The Use Tax code must exist in both companies.

- The transaction data being submitted using this web service are stored within the Job Requisition Entry screen; the data must be manually updated within Spectrum.

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
Batch_Code
Batch Code
YES
Text
10

D
Operator
Entered by
Text
3
If blank then defaults to Operator ID.

E
Transaction_Reference
Requisition number
Text
7
Use Auto-assign next requisition # if left blank. If defined then all Requisition Header details must match.

F
Req_Company_Code
Job (Requisition) company -header
Text
3
Used for Multi-company requisition feature. If blank or option not selected use the Company_Code field.
Inventory Control installation option for Multi-company requisition is defined. Valid Company in Spectrum.

G
Default_Job
Job number - Header
Text
10
If defined then each associated detail will use the same Job number.
Valid Job in defined Req_Company_Code otherwise valid for definedÂ Company_Code

H
Status
Status
Text
1
O(rdered) or S(hipped) only. If blank defaults to O(rdered).

I
Special_Instructions
Instructions
Text
70

J
Transaction_Date
Requisition date
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/2010). Use Current Date for Inventory module if blank.

K
Ship_Date
Ship date
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/2010). Use Current Date for Inventory module if blank.

L
Ship_Via
Ship via
Text
15

M
From_Warehouse
Default warehouse
YES
Text
10
If blank, defaults from Inventory Control Installation screen. If the Default Warehouse field is blank on the Installation screen and this field is left blank, you will get an error message.
Warehouse File Maintenance

N
Item_Code
Item code
YES
Text
15
If Item code is valid, then it must be valid for From_Warehouse, if defined. Non-stock items will be created using the Item_Category if defined and Item_Code is not valid.
Inventory Item File Maintenance

O
Item_Category
Item category
Text
4
Used to create Non-stock items only.
Inventory Item Category Maintenance

P
Warehouse
Warehouse
Text
10
Warehouse must be defined for Item_Code field. If blank, use default warehouse or it is required.
Warehouse File Maintenance

Q
Markup_Percent
Markup
Numeric
7
Example: Enter 10.55% as 10.55. Format = 3.2-
Defaults from Inventory Item if left blank. Not used for Non-stock items.

R
Transaction_Quantity
Order quantity
YES
Numeric
11
Required. Negative numbers allowed. Cannot be zero. Format = -7.2

S
Ship_Quantity
Ship Quantity
Numeric
11
Negative numbers allowed. Format = -7.2
Quantity cannot exceed the Transaction_Quantity value.

T
Reason
Message
Text
30

U
GL_Department
Department
Text
4
Defaults from Warehouse default then Item Category default
Inventory G/L Department File Maintenance

V
GL_Debit_Account
G/L Account
Numeric
10
Defaults from Department if not entered. Required for intercompany records. Must be a direct job cost G/L Account
G/L Account Master File

W
Job_Number
Job - Detail
Text
10
Required if Default_Job not defined.
Job File Maintenance for defined Company.

X
Phase_Code
Phase
Text
20
Defaults from Inventory Item if left blank.
Phase File Maintenance

Y
Cost_Type
Cost type
Text
3
Defaults from Inventory Item if left blank. Validates to the defined GL_Debit_Account for direct job cost.
Cost Type Maintenance

Z
Use_Tax_Code
Use Tax Code
Text
15
If blank- default from Job Tax Classification if used.
Use Tax Code Maintenance

AA
Standard_Cost
Standard Cost
Numeric
11
Positive number only. Defaults from Inventory Item if left blank. Format = 6.4

AB
Non_Stock_Description
Description
Text
30
 Used for non-stock items only. If not defined then defaults to the Category description

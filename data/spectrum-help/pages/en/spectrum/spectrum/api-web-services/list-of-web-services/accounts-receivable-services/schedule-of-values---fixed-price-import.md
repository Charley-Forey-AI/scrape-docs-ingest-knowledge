---
title: "Schedule of Values - Fixed Price Import | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-receivable-services/schedule-of-values---fixed-price-import"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-receivable-services/schedule-of-values---fixed-price-import"
---

# Schedule of Values - Fixed Price Import

Use this service to import Schedule of Values information for Fixed Price billings.

## Connection Information

URL: https://<SPECTRUM-SERVER>:8482/contract/scheduleofvalues
Authentication: [Basic Authentication](/en/spectrum/spectrum/api-web-services/authentication/basic-authentication),
 [Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)
Supported methods: POST
Supported formats: JSON

## Underlying File Maintenance

Prior to importing Schedule of Values information, the following file maintenance areas must be completed:

- System Administration > Installation > Accounts Receivable > Customers

- System Administration > Installation > Accounts Receivable > Contract

- System Administration > Installation > Accounts Receivable > Online Tax Code

- System Administration > Installation > Accounts Receivable > Set Up Standard Fixed Billing Items

- System Administration > Installation > General Ledger > G/L Master File Maintenance

- System Administration > Installation > Job Cost > Jobs

## Assumptions and Dependencies

- The service will sum up all 'Contract_Amount' columns and the total must tie to the 'Original contract' amount in Contract Main Properties.

- Only (A)ctive and (I)nactive Customer codes are allowed.

- Only (A)ctive and (I)nactive Job codes are allowed.

- Only (A)ctive and (I)nactive G/L codes are allowed.

- The import will error out when the contract has information defined in the G/L Distribution for Draw Request Invoices window. When such allocation is required, first import the schedule of values and then enter the allocation percentages.

- Customer must have security to entered cost enter. Only (A)ctive cost centers are allowed.

- When the bill item is found in 'Set Up Standard Fixed Billing Items' and the following fields are left blank, default the following in from the standard list:

- Billing Description

- Additional Billing Description

- G/L Account Code

- Online Tax Code

## Sample JSON Body

```
`{
 "contracts": [
 {
 "Company_Code": "2ND",
 "Customer_Code": "DF001",
 "Job_Number": "DF002",
 "Schedule_Of_Values_Fixed": [
 {
 "Billing_Item": "01",
 "Billing_Description": "MOBILIZATION",
 "Additional_Billing_Description": "& GENERAL CONDITIONS",
 "GL_Account": "104000",
 "Taxable": "Y",
 "Original_Contract": 2400,
 "Projected_Revenue": 2424,
 "Memo": "Memo Memo Memo",
 "Cost_Center": "",
 "Online_Tax_Code": ""
 },
 {
 "Billing_Item": "02",
 "Billing_Description": "Billing Item 02",
 "Additional_Billing_Description": "Add'l Description 02",
 "GL_Account": "104000",
 "Taxable": "N",
 "Original_Contract": 2012,
 "Projected_Revenue": 0,
 "Memo": "",
 "Cost_Center": "",
 "Online_Tax_Code": ""
 }
 ]
 }
 ]
}`
```

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
Customer_Code
Customer Code
YES
Text
10
** See Assumptions and Dependencies.
Customer Master File

D
Job_Number
Job Number
YES
Text
10
** See Assumptions and Dependencies.
Job Master File

E
Billing_Item
Billing Item
YES
 Text
10

F
Billing_Description
Billing Description
 Text
30
G/L Master File

G
Additional_Billing _Description
Additional Billing Description
 Text
 40

H
Taxable
Taxable?
Text
 1
(Y)es or (N)o
Defaults from Contract Master File if left Blank

I
Original_Contract
Original Contract Amount
Numeric
10.2

J
Projected_Revenue
Projected Revenue
Numeric
10.2

K
Memo
Memo
Text
25

L
GL_Account
G/L Account Code
Numeric
12
** See Assumptions and Dependencies. No dashes.
G/L Master File

M
Cost_Center
Cost Center
Text
10
 ** See Assumptions and Dependencies.

N
Online_Tax_Code
Online Tax Code
Text
15
Cost Center Maintenance; G/L Account Cost Center; Job Cost Center, Customer Cost Center

---
title: "Add AR Sales Tax | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-receivable-services/add-ar-sales-tax"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-receivable-services/add-ar-sales-tax"
---

# Add AR Sales Tax

Use this service to import Accounts Receivable Sales Tax information.
WSDL: Update_AR_Sales_Tax.jws
Method: Update_AR_Sales_Tax
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Accounts Receivable Sales Tax information, the following file maintenance areas must be completed:

- System Administration > Installation > Accounts Receivable

- System Administration > Installation > Processing Dates

- System Administration > Installation > General Ledger > G/L Master File Maintenance

- System Administration > Installation > Accounts Receivable > Sales Tax Maintenance

- System Administration > Installation > Accounts Receivable > Sales Tax Rate History Maintenance

## Assumptions and Dependencies

- If the Company_Code is blank then use the Authorization ID default value.

- The Accounts Receivable Sales Tax web service will either create a new Sales Tax code or update an existing Sales Tax code. The changes are recorded in the Rate History information.

- If the Sales_Tax_Code field does not exist then it will be added.

- The Rate History will populate using the current AR processing date and display Initial Entry in the Comments field.

- If the Effective_Date and Comments fields are populated they will be ignored since they are used for changes and defined on the Rate History information.

- If the Sales_Tax_Code field does exist then it will update all the detail information provided.

- The Effective_Date and Comments fields are used for the Rate History information.

- Duplicate Effective dates cannot exist for a given Use_Tax_Code.

- The service does not delete values that exist in Spectrum; it only changes data defined in the layout.

- Comments that exceed the Max character length will be truncated.

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
Valid Company in Spectrum. Defaults from the Authorization ID if not populated.

C
Sales_Tax_Code
Sales tax code
YES
Text
15
If it exists then update the information.
Accounts Receivable Sales Tax Maintenance

D
Description
Description
Text
20

E
GL_Account
G/L account code
YES
Numeric
12
Must be a non-direct GL Account. No dashes.
General Ledger Account Maintenance

F
Freight_Tax_Flag
Tax on freight?
Text
1
Y(es) or N(o) only. Default to N if blank.

G
Sales_Tax_Percent
Tax rate
Numeric
7
Positive number only. Format = xx.xxxx

H
Effective_Date
Effective as of
Date
10
If left blank then use current processing date. Enter as: MM/DD/CCYY (for example, 01/05/2010). ** See Assumptions and Dependencies
Must be current or future date for AP Processing date. Rate change cannot exist for the defined date.

I
Comments
Comments
Text
40
** See Assumptions and Dependencies

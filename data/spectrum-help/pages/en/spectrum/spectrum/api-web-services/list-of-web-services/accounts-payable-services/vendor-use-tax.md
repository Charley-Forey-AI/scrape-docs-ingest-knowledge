---
title: "Vendor Use Tax | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-payable-services/vendor-use-tax"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-payable-services/vendor-use-tax"
---

# Vendor Use Tax

Use this service to import Accounts Payable Vendor Use Tax information.
WSDL: Update_AP_Use_Tax.jws
Method: Update_AP_Use_Tax
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Accounts Payable Use Tax information, the following file maintenance areas must be completed:

- System Administration > Installation > Accounts Payables

- System Administration > Installation > Processing Dates

- System Administration > Installation > General Ledger > G/L Account Master File
 Maintenance

- System Administration > Installation > Accounts Payable > Use Tax Maintenance

- System Administration > Installation > Accounts Payable > Use Tax Rate History
 Maintenance

## Assumptions and Dependencies

- If the Company_Code is blank then use the Authorization ID default value.

- The Accounts Payable Use Tax web service will either create a new Use Tax code or update an existing Use Tax code. The changes are recorded in the Rate History information.

- If the Use_Tax_Code combination field does not exist then it will be added.

- The Rate History will populate using the current AP processing date and display Initial Entry in the Comments field.

- If the Effective_Date and Comments fields are populated they will be ignored since they are used changes and defined on the Rate History information only.

- If the Use_Tax_Code combination field does exist, then it will update all the detail information provided.

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
Use_Tax_Code
Use tax code
YES
Text
15
If it exists then update the information.
Accounts Payable Use Tax Maintenance

D
Use_Tax_Description
Description
Text
20

E
Tax_GL_Account
G/L account code
YES
Text
12
Must be a non-direct GL Account. No dashes.
General Ledger Account Maintenance

F
Tax_Type
Tax Type
Text
1
S(ales) or U(se) only. Defaults to U(se) if blank.

G
Tax_Percent
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

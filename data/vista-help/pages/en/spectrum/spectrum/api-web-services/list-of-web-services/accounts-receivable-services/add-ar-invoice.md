---
title: "Add AR Invoice | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-receivable-services/add-ar-invoice"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-receivable-services/add-ar-invoice"
---

# Add AR Invoice

Use this service to import Accounts Receivable Customer Invoices information.
WSDL: AddARInvoice.jws
Method: AddARInvoice
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Customer Invoices information, the following file maintenance areas must be completed:

- System Administration > Installation > Accounts Receivable

- System Administration > Installation > General Ledger > G/L Master File Maintenance

- System Administration > Installation > General Ledger > Value Added Tax Code Maintenance

- System Administration > Installation > Accounts Receivable > Customers

- System Administration > Installation > Accounts Receivable > Contracts

- System Administration > Installation > Accounts Receivable > Terms Code File Maintenance

- System Administration > Installation > Accounts Receivable > Sales Tax Code Maintenance

- System Administration > Installation > Job Cost > Jobs

- System Administration > Installation > Accounts Receivable > Salesperson Code Maintenance

- System Administration > Installation > Multi-Currency > Currency Codes

- System Administration > Installation > Enterprise Management > Cost Center Maintenance

## Assumptions and Dependencies

- The import file contains one detail line per header record.

- The General Ledger date and Invoice date must be within the Accounts Receivable processing date. Based on the Accounts Receivable Installation option, the General Ledger date and Invoice date may need to be in the same GL period.

- The import requires that Line_Extension, Sales_Tax_Amount, and Retention_Amount contain a positive number. If a negative retention is needed, then the Transaction_Type needs to be defined as a C(redit Memo) to provide a negative retention number.

- The import allows the user to import retention-only records which will require the Line_Extension and Retention_Amount to have the same defined value.

- Sales tax code and Invoice date will be used to define the percentage for the header. Sales tax codes must be set up; if the rates are different than the rates defined in the Historical table, Spectrum will use the closest date.

- When creating a new contract request invoice, the Customer_PO field defaults from the Contract Defaults page. This field can be edited.

- Value Added Tax (VAT)

- GL Installation option that allows the user to add functionality to use Value Added Tax logic.

- If selected then the Invoice header contains additional fields appear for the VAT code and amount and the Sales Tax field name changes to PST and the Retention name changes to Holdback.

- The VAT is calculated on the total Invoice amount.

- If selected then the VAT_Code and Total_VAT_Amt can be defined on the Invoice header.

- VAT_Code default hierarchy

- The Job Classification File Maintenance provides an option to override the default VAT on the Customer invoice. If defined, then use this code.

- If the Job Classification is not selected, then default from the GL Installation screen, otherwise use the defined code contained in the service.

- Total_VAT_Amt can be either calculated based on the defined VAT_Code or overwritten by the defined value in the layout.

- This web service supports the Multi-Currency module.

- Cost center information will only be allowed if the Company is set to a 'Yes' status.

The transaction data being submitted using this web service are stored within the Customer Invoice Entry screen; the data must manually be updated within Spectrum.

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
GL_Date
General Ledger Date
YES
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/2011)
Within AR processing date range.

D
Batch_Code
Batch Code
YES
Text
10

E
Customer_Code
Customer Code
YES
Text
10
Customer File Maintenance

F
Job_Number
Job Number / AR Contract
Text
10
Job File Maintenance and Contract File Maintenance

G
Invoice_Or_Transaction
Invoice Number
YES
Text
10
Unique invoice number - no duplicates

H
Transaction_Type
(I)nvoice or (C)redit Memo
YES
Text
1
(I)nvoice or (C)redit memo only

I
Invoice_Date
Invoice Date
YES
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/2011)
Within AR processing date range. AR Installation option forces Invoice date to match the GL period.

J
Terms_Code
Payment Terms Code
Text
1
Defaults from the Customer Master if left blank.
Terms Code File Maintenance

K
Salesperson_Code
Salesperson Code
Text
3
Defaults from the Contract then the Customer Master if left blank.
Salesperson Code Maintenance

L
Sales_Tax_Code
Invoice Sales Tax Code
Text
15
Defaults from the Contract, then the Job's Tax Class code and then the Customer Master if left blank. If set to 'No Default' then field is required.
Sales Tax Code Maintenance

M
Taxable_Flag
Invoice Taxable?
Text
1
(Y)es or (N)o only. Defaults from the Contract, then the Customer if left blank. If set to 'No Default' then field is required.

N
Retention_Percent
Retention (Holdback) %
Numeric
6
Example: Enter 10.5% as 10.5. Positive Amounts only.
If Retention invoice only then % = 100 and the entry is required. If Retention % is blank then default the % from the contract master.

O
Print_Job_Address_Flag
Print Job Address?
Text
1
(Y)es or (N)o only.
If left blank it will default to Y.

P
Remarks
Invoice Remarks
Text
65

Q
Customer_PO
Customer PO #
Text
25
See Assumptions and Dependencies

R
AR_GL_Account
A/R G/L Code
Text
12
AR G/L Account code must be a non-direct cost account. Defaults from the Installation Screen if left blank. No dashes.
G/L Master File Maintenance

S
Detail_Description
Line Item Description
Text
30

T
Line_Extension
Line Item Extension
YES
Numeric
13
Positive Amounts only.
Total Invoice Amount including retention portion.(If record is the retention only value then Line_Extension field and Rentention_Amount field will be the same value).

U
GL_Account
Line Item G/L Code
Text
12
G/L Account code must be a non-direct cost account. Defaults from GL installation screen or Job Contract. If defined as 'No Default' then it will be required. No dashes.
G/L Master File Maintenance

V
Sales_Tax_Amount
Invoice Tax Amount
Numeric
13
Positive Amounts only.

W
Retention_Amount
Invoice Retention (Holdback)
Numeric
13
Positive Amounts only.
Retention Amount only. (If record is the retention only value then Line_Extension field and Rentention_Amount field will be the same value).

X
VAT_Code
VAT Code
Text
10
Defaults from Job Classification File Maintenance, or the GL Installation option if defined. Can override both default locations.
Value Added Tax Maintenance

Y
Total_VAT_Amount
VAT tax amount
Numeric
12
Positive Amounts only. If defined then overrides calculated value.

Z
Asset_Cost_Center
Asset Cost Center
Text
10
Will tie to the AR_GL_Account field. Defaults from the Contract if left blank. If set to 'No Default' then field is required.
Cost Center Maintenance; Customer Cost Center; Job Contract Cost Center and AR_GL_Account Cost Center, Sales Tax Code GL Account CC

AA
Income_Cost_Center
Income Cost Center
Text
10
Will tie to the GL_Account field.
Cost Center Maint, Customer CC, G/L Account Cost Center

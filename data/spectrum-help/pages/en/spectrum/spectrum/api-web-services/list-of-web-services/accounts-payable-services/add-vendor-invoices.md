---
title: "Add Vendor Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-payable-services/add-vendor-invoices"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-payable-services/add-vendor-invoices"
---

# Add Vendor Invoices

Use this service to import Vendor Invoice information.
WSDL: AddAPInvoice.jws
Method: AddAPInvoice
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Vendor Invoice information, the following file maintenance areas must be completed:

- System Administration > Installation > Accounts Payable

- System Administration > Installation > General Ledger > G/L Master File Maintenance

- System Administration > Installation > General Ledger > Value Added Tax Code Maintenance

- System Administration > Installation > Accounts Payable > Vendors

- System Administration > Installation > Accounts Payable > Subcontracts

- System Administration > Installation > Accounts Payable > Use Tax Code Maintenance

- System Administration > Installation > Job Cost > Jobs

- System Administration > Installation > Job Cost > Job Phases

- System Administration > Installation > Job Cost > Cost Type File Maintenance

- System Administration > Installation > Equipment Control > Equipment

- System Administration > Installation > Equipment Control > Cost Category File Maintenance

- System Administration > Installation > Work Order > Site File Maintenance

- System Administration > Installation > Work Order > Work Order Entry

- System Administration > Installation > Work Order > Material Item Code File Maintenance

- System Administration > Installation > Inventory Control > Inventory Items

- System Administration > Installation > Service Contracts > Service Contract File Maintenance

- System Administration > Installation > Accounts Payable > Invoice User-Defined Fields Maintenance

- System Administration > Installation > Enterprise Management > Cost Center Maintenance

## Assumptions and Dependencies

- The import file contains one detail line per header record.

- The Distribution_GL_Account controls the logic based on the type of direct cost options selected for the G/L Code.

- If the General Ledger Code is set to Direct Cost = N (Non-direct):

- Then any data defined in the Job Cost, Equipment, or Work Order fields will be ignored and not populated.

- If the General Ledger Code is set to Direct Cost = Y (Job Cost):

- The Job number, Phase code, and Cost type are mandatory and validated.

- If the General Ledger Code is set to Direct Cost = E (Equipment):

- The Equipment Code and Equipment Cost Category are both mandatory and validated.

- The Equipment_Work_Order is required optional or not allowed (none) based on the defined Equipment Cost Category data entry rule.

- The Equipment Cost Category Code contains General Ledger Overrides.

- If field is blank then will default from the Cost Category Code.

- If defined it will validate to the GL Overrides and the Cost Category Code.

- If the General Ledger Code is set to Direct Cost = W (Work Order):

- The Work Order Number and Item Code are required.

- The Item Code must be set up when the Inventory Control module is turned on.

- If the Inventory Control module is not on, then the Item Code is validated to the W/O Item file maintenance.

- If the code exists, populate the Item Description, Unit Cost, and WO Unit Price using standard Spectrum logic.

- If the code is not a WO Item, allow it to be entered as a 'generic' code using Spectrum standard logic (Item_Desc and Unit_Cost are not populated).

- Non-stock items are not supported and will be considered as 'generic' codes when the IC module is not present.

- The Quantity, WO Service Contract, and WO Unit Price are NOT required. However the W/O Service Contract will be validated if populated. If the quantity field is populated, it updates only when the General Ledger Code is set to Direct Cost = W.

- The W/O Equipment and W/O Component are required and validated when the W/O Installation 'Require equipment code for work order transactions?' and the 'Require component code for work order transactions?' boxes are selected.

- Sales_Tax_Amount works in conjunction with the Tax_Code field and follows the logic defined with regards to the Distribution_GL_Account defined.

- For non-direct, Equipment or Work Order direct cost records:

- If the Sales_Tax_Amount is left blank then:

- When the Tax_Code is populated or it defaults from the Vendor's Sales/Use Tax code it must have a tax type defined as use tax.

- When the Tax_Code is not populated and defaults blank because the Vendor's Sales/Use Tax code is blank, the invoice is considered non-taxable.

- If the Sales_Tax_Amount is populated then

- The Tax_Code entered or if blank and defaults from the Vendor's Sales/Use Tax code, it must have a tax type of sales tax.

- The Sales_Tax_Amount will be allocated to the detail lines when it doesn't equal the detail's total tax calculation.

- For Job Cost direct cost records:

- If the Job Tax Classification features are not used then it follows the Vendor's Tax code hierarchy.

- If the Job Tax Classification features are used:

- When the Tax_Code is populated, the Job Tax Classification setup is ignored.

- If the Tax Class defaults by Vendor and the Vendor's Sales/Use Tax code is populated then it follows the Vendor's hierarchy. If the Vendor's Sales/Use Tax code is blank it uses the Job's Tax Classification code; if it is defined as blank, then the invoice is considered non-taxable.

- When the Tax Class defaults by Job and the Job has a Tax Classification code, then if follows the Tax Classification code hierarchy:

- If an A/P Override exists then it will follow standard Spectrum logic.

- If the Job's Tax Classification code is blank, it uses the Vendor's Sales/Use Tax code, unless it is blank, then the invoice is considered non-taxable.

- If the Sales_Tax_Amount is blank then

- The Tax code defaulted must have a tax type defined as use tax, or if an A/P Override exists it must be set as tax exempt.

- If the Sales_Tax_Amount is populated then

- The Tax code defaulted must have a tax type of sales tax or if an A/P Override exists it must be set as taxable.

- The Sales_Tax_Amount will be allocated to the detail lines when it doesn't equal the detail's total tax calculation.

- Value Added Tax (VAT)

- The Company Installation allows the user to add functionality to use Value Added Tax logic and to define a default code.

- If selected then the Invoice header contains additional fields appear for the VAT code and amount and the Sales Tax field name changes to PST and the Retention name changes to Holdback.

- The VAT is calculated on the total Invoice amount.

- If selected then the VAT_Code and Total_VAT_Amt can be defined on the Invoice header.

- VAT_Code can be defaulted from the GL Installation screen or defined on the Invoice. If it is not valid then both the VAT_Code and Total_VAT_Amt information defined in the record.

- Total_VAT_Amt can be either calculated based on the defined VAT_Code or overwritten by the defined value in the record.

- Follows standard Spectrum logic to define the 'Pay when Paid' setting.

- PO_Number is no longer used. Leave this field blank. If defined then it will be stored in the Remarks field if it is blank, otherwise it will cause an error.

- Cost Center information will only be allowed in if the Company is set to a Yes status.

- Cost Center Logic:

- The Liability_Cost_Center (Header Cost Center) is required if a cost center company is specified, it must be active, valid for the AP GL Account and Vendor Code.

- The Expense_Cost_Center (Detail Cost Center) field name is required, however it can be defaulted if left blank and will use the following logic:

- For a non-direct Distribution_GL_Account:

- If the Expense_Cost_Center is defined then the cost center must be active, a valid cost center for the Distribution_GL_Account and the Vendor_Code.

- If the Expense_Cost_Center is not entered, it will attempt to use the Liability_Cost_Center as long as it is valid for the Distribution_GL_Account and the Vendor_Code.

- When a direct Distribution_GL_Account is defined in the layout, then the Expense_Cost_Center (if entered) must be a valid and active cost center. However, it could be overwritten based on the following standard Spectrum logic:

- For a direct Job cost distribution G/L code it will attempt to use the Phase cost center; if the field is blank then it will use the Job cost center.

- For a direct Equipment cost distribution G/L code it will attempt to use the Equipment cost category's cost center; if the field is blank then it will use the Equipment cost center.

- For a direct Work Order cost distribution G/L code it will attempt to use the Work Order's cost center.

- Once the Expense_Cost_Center is determined for direct cost records, it is then validated against the Distribution G/L code's cost centers.

- The standard Spectrum logic will be used to define the Pay when Paid option.

- This web service supports the Multi-Currency module.

- The transaction data being submitted using this web service are stored within the Vendor Invoice Entry screen; the data must be manually updated within Spectrum.

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
GL_Date
G/L Date
YES
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/2010)
Within A/P processing date range.

D
Batch_Code
Batch
YES
Text
10

E
Vendor_Code
Vendor
YES
Text
10
Vendor File Maintenance

F
Contract_Number
Subcontract
Text
10
Subcontract File Maintenance

G
Invoice_Number
Invoice Number
YES
Text
20
Unique invoice number within each vendor code.

H
Invoice_Type_Code
Invoice Type
YES
Text
1
(I)nvoice or (C)redit only

I
Invoice_Date
Invoice Date
YES
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/2010)
Cannot exceed A/P maximum processing date if A/P installation option selected.

J
Invoice_Amount
Invoice Amount before tax
YES
Numeric
12
Positive Amounts only. Must be greater than Discount amount
Total Invoice including retention portion. (If record is the retention only value then Invoice_Amount field and Retention_Amount field will be the same value)

K
Sales_Tax_Amount
Sales (PST) Tax Amount
Numeric
12
Positive Amounts only.

L
Retention_Amount
Retention (Holdback) Amount
Numeric
12
Positive Amounts only. Must be greater than Discount amount
This is the retention portion only of the invoice

M
PO_Number
***LEAVE BLANK***
Text
10
Vendor's P. O. number. Reference only. ** See Assumptions and Dependencies.
 If defined will be stored in the 'Remarks' field if blank. Otherwise user must define.

N
Payment_Due_Date
Payment Due Date
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/2010)

O
Status
On hold?
Text
1
(H)old or (O) only. If left blank defaults to O status.

P
Discount_Due_Date
Discount Due Date
Date
10
Enter as: MM/DD/CCYY (for example, 01/05/2010)

Q
Discount_Amount
Discount Amount
Numeric
12
Positive Amounts only. Must be greater than zero and less than the Invoice Amount.

R
Remarks
Invoice Remarks
Text
30

S
AP_GL_Account
A/P G/L Code
Text
12
GL account must be active and a non-direct account. No dashes.
G/L Master File Maintenance

T
Distribution_GL_Account
Distribution G/L Account
Text
12
*See Assumptions for Rules. No dashes.
G/L Master File Maintenance

U
Job_Number
Job Number
Text
10
Job's status cannot be Complete.
Job File Maintenance

V
Phase_Code
Phase Code
Text
20
No dashes.
Phase File Maintenance

W
Cost_Type
Cost Type
Text
3
Cost Type File Maintenance

X
Equipment_Code
Equipment Code
Text
10
Equipment's status type cannot be Retired.
Equipment File Maintenance

Y
Equipment_Category
Equipment Cost Category
Text
4
Equipment Cost Category Maintenance

Z
Equipment_Work_Order
Equipment Work Order
Text
10
Equipment Work Order is required, optional or none based on Equipment Cost Category data entry rule.
Equipment Item must exist on the Equipment Work Order for required or optional settings.

AA
WO_Number
Work Order #
Text
10
Work Order status cannot be (C)omplete. Cannot be a job WO.
Work Order Maintenance

AB
Item_Code
Item Code
Text
15
Inventory Item File Maintenance when Inventory Control is installed; Work Order Item File Maintenance when Inventory Control is not installed

AC
Quantity
Quantity
Numeric
11

AD
WO_Equipment
WO Site Equipment
Text
8
Required if Work Order installation flag is selected.
Work Order Site Master File/Equipment Tab

AE
WO_Component
WO Component
Text
2
Required if Work Order installation flag is selected.
Work Order Site Master File/Equipment Tab /Component Tab (old systems)

AF
WO_SC_Contract
WO Service Contract
Text
10
Work Order Site Master File/Service Contract Tab

AG
WO_Unit_Price
Unit billing price
Numeric
13

AH
Tax_Code
Tax code
Text
15
Dependent on the Sales_Tax_Amount field and the Tax Type defined. ** See Assumptions for Rules
Use Tax Code Maintenance

AI
VAT_Code
VAT code
Text
10
Defaults from GL Installation option if defined. Can override.
Use Tax Code Maintenance

AJ
Total_VAT_Amt
VAT tax amount
Numeric
13
Positive Amounts only. If defined then overrides calculated value.
Value Added Tax Maintenance

AK
UDF1
User Defined Alpha/Numeric/Date 1
+
20
Web Service Authorization ID Service UDF defined.

AL
UDF2
User Defined Alpha/Numeric/Date 2
+
20
Web Service Authorization ID Service UDF defined.

AM
UDF3
User Defined Alpha/Numeric/Date 3
+
20
Web Service Authorization ID Service UDF defined.

AN
UDF4
User Defined Alpha/Numeric/Date 4
+
20
Web Service Authorization ID Service UDF defined.

AO
UDF5
User Defined Alpha/Numeric/Date 5
+
20
Web Service Authorization ID Service UDF defined.

AP
UDF6
User Defined Alpha/Numeric/Date 6
+
20
Web Service Authorization ID Service UDF defined.

AQ
UDF7
User Defined Alpha/Numeric/Date 7
+
20
Web Service Authorization ID Service UDF defined.

AR
UDF8
User Defined Alpha/Numeric/Date 8
+
20
Web Service Authorization ID Service UDF defined.

AS
UDF9
User Defined Alpha/Numeric/Date 9
+
20
Web Service Authorization ID Service UDF defined.

AT
UDF10
User Defined Alpha/Numeric/Date 10
+
20
Web Service Authorization ID Service UDF defined.

AU
UDF11
User Defined Alpha/Numeric/Date 11
+
20
Web Service Authorization ID Service UDF defined.

AV
UDF12
User Defined Alpha/Numeric/Date 12
+
20
Web Service Authorization ID Service UDF defined.

AW
UDF13
User Defined Alpha/Numeric/Date 13
+
20
Web Service Authorization ID Service UDF defined.

AX
UDF14
User Defined Alpha/Numeric/Date 14
+
20
Web Service Authorization ID Service UDF defined.

AY
UDF15
User Defined Alpha/Numeric/Date 15
+
20
Web Service Authorization ID Service UDF defined.

AZ
UDF16
User Defined Alpha/Numeric/Date 16
+
20
Web Service Authorization ID Service UDF defined.

BA
UDF17
User Defined Alpha/Numeric/Date 17
+
20
Web Service Authorization ID Service UDF defined.

BB
UDF18
User Defined Alpha/Numeric/Date 18
+
20
Web Service Authorization ID Service UDF defined.

BC
UDF19
User Defined Alpha/Numeric/Date 19
+
20
Web Service Authorization ID Service UDF defined.

BD
UDF20
User Defined Alpha/Numeric/Date 20
+
20
Web Service Authorization ID Service UDF defined.

BE
Liablility_Cost_Center
Liability Cost Center
Text
10
Must be valid for the AP_GL_Account field.
Cost Center Maintenance, Vendor Code

BF
Expense_Cost_Center
Expense Cost Center
Text
10
Must be valid for the Distribution_GL_Account field.
Cost Center Maintenance; Vendor Cost Center; Job Cost Center; Phase Cost Center; Equipment Cost Center; Equipment Category Cost Center and Work Order Cost Center

+ NOTE = the UDF (1-20) elements can be Numeric, Date or Text depending on how they are created within Spectrum.

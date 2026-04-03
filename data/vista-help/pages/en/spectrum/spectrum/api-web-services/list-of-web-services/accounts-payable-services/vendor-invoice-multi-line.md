---
title: "Vendor Invoice Multi-Line | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-payable-services/vendor-invoice-multi-line"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-payable-services/vendor-invoice-multi-line"
---

# Vendor Invoice Multi-Line

Use this service to add unposted invoice header and detail information.

## Connection Information

URL: https://<SPECTRUM-SERVER>:8482/vendor/invoice
Authentication: [Basic Authentication](/en/spectrum/spectrum/api-web-services/authentication/basic-authentication), [Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)
Supported methods: POST
Supported formats: JSON

## Sample JSON Body

```
`{
 "APInvoices": [{
 "Company_Code": "SP1",
 "Vendor_Code": "AAAIND",
 "Invoice_Number": "AP00000001",
 "Invoice_Type_Code": "I",
 "Approval_Status": "A",
 "Routing_Code": "JOB125",
 "GL_Date": "05/15/2017",
 "Invoice_Date": "05/15/2017",
 "Invoice_Amount": 5000.54,
 "Sales_Tax_Amount": 50.01,
 "VAT_Code": "",
 "Total_VAT_Amount": 0,
 "Contract_Number": "",
 "Retention_Amount": 500,
 "Batch_Code": "ABATCH",
 "Payment_Due_Date": "05/30/2017",
 "Discount_Due_Date": "05/20/2017",
 "Discount_Amount": 250,
 "Status": "O",
 "Payment_Status": "U",
 "Bank_Account_Code": "",
 "Check_Number": "",
 "Check_Date": "",
 "Card_Number": "",
 "AP_GL_Account": "012400",
 "Cost_Center": "",
 "Remarks": "JSON Sample for AP Multi-line import",
 "Images": [{
 "Image_Type": "PDF",
 "Image_Description": "Image file should be base 64 encoded",
 "Document_ID": "",
 "Image_File": "**base 64 file encoding**"
 }],
 "APInvoiceDetails": [{
 "Distribution": {
 "Company_Code": "SP2",
 "GL_Account": "012450",
 "Cost_Center": ""
 },
 "Item_Code": "",
 "Item_Description": "",
 "Unit_Of_Measure": "",
 "Quantity": 15,
 "Amount": 4450,
 "Tax_Code": "1500",
 "Job": {
 "Job_Number": "",
 "Phase_Code": "",
 "Cost_Type": ""
 },
 "Equipment": {
 "Equipment_Work_Order": "",
 "Equipment_Code": "",
 "Equipment_Category": ""
 },
 "Work_Order": {
 "WO_Number": "",
 "Unit_Price": 0,
 "Equipment": "",
 "Component": "",
 "Service_Contract": ""
 },
 "Remark": "This is a sample detail for an AP Multi-line import"
 }]
 }]
}`
```

## Underlying File Maintenance

Prior to importing information for a particular vendor invoice, the following file maintenance areas must be completed:

- System Administration > Installation > Accounts Payables

- System Administration > Installation > Accounts Payables > Vendors

- System Administration > Installation > Accounts Payables > Vendor Defaults

- System Administration > Installation > Accounts Payables > Invoice Approval Routing Maintenance

- System Administration > Installation > Accounts Payables > Subcontracts

- System Administration > Installation > Accounts Payables > Use Tax Code Maintenance

- System Administration > Installation > Accounts Payables > Vendor Locations

- System Administration > Installation > Cash Management > Account File Maintenance

- System Administration > Installation > Document Imaging

- System Administration > Installation > Document Imaging > Cabinet Maintenance

- System Administration > Installation > General Ledger

- System Administration > Installation > General Ledger > G/L Master File Maintenance

- System Administration > Installation > General Ledger > Value Added Tax Code Maintenance

- System Administration > Installation > Job Cost

- System Administration > Installation > Job Cost > Jobs

- System Administration > Installation > Job Cost > Job Phases

- System Administration > Installation > Job Cost > Cost Type File Maintenance

- System Administration > Installation > Job Cost > Tax Classification Maintenance

- System Administration > Installation > Equipment Control > Equipment File Maintenance

- System Administration > Installation > Equipment Control > Cost Category File Maintenance

- System Administration > Installation > Preventive Maintenance > Equipment Work Order Entry

- System Administration > Installation > Work Order > Work Order Main Properties

- System Administration > Installation > Work Order > Site Main Properties

- System Administration > Installation > Work Order > Site Equipment

- System Administration > Installation > Inventory Control > Inventory Item File Maintenance

- System Administration > Installation > Service Contracts > Service Contract Main Properties

- System Administration > Installation > Enterprise Management > Cost Center Maintenance

- System Administration > Installation > Multi-Currency > Currency Code Maintenance

## Assumptions and Dependencies

- The Add Vendor Invoice Web Service adds unposted invoice header and detail information.

- The Vendor Invoice Web Service adds invoice images when the package contains a new invoice

- Updating or adding images to an existing invoice is not currently supported.

- The Web Service will not support the following logic:

- If any of these conditions are encountered (or if any field-level validation fails), the Web Service will reject the particular invoice in its entirety and return summary error messages indicating problem found (in the Header, in the Detail or both). Please note that in the case where there are multiple invoices in the batch, the Web Service will import the ones with no errors while rejecting those with problems.

- Invoice already exists (unapproved, unposted, open items, payment history or rejected)

- Invoice Header with No Detail record

- Vendor with a 'Not used' status

- Subcontract with a 'Completed' status

- Job with a 'Completed' status

- Equipment with a 'Retired' status

- Work order with a 'Completed' status

- G/L Account with a 'Not used' status

- The Web Service follows the majority of the same logic as manually entering a new vendor invoice, with the exceptions of the data defined here.

- The Web Service does not support Purchase Order invoice receiving, Subcontract progress billings or Subcontract back charges.

- Sales/Use Tax

- When the Tax Code field is left blank in the Vendor Invoice Detail, the Web Service will determine the default Tax Code using the hierarchy (Job or Vendor) specified in Job Cost Installation if Tax Classification is enabled, and settings in Tax Classification Maintenance and Vendor Defaults, using same rules as in Vendor Invoice Entry, including phase-specific tax rules from Tax Classification Maintenance, if applicable.

- When the Sales Tax Amount field is left blank in the Vendor Invoice Header, calculate the amount from the Detail applying the same rules as in Vendor Invoice Entry.

- When the Sales Tax Amount field is non-zero in the Vendor Invoice Header, calculate the amount from the Detail and then allocate any differences among Detail records, applying the same rules as in Vendor Invoice Entry. In the case where there are no Detail records configured for sales tax, the Web Service will not import the invoice.

- Please note that the tax code field in the Detail record may be either Sales Tax or Use Tax (based on the flag in Use Tax Code Maintenance), and will be stored separately in the Spectrum Detail Table. Use tax is not applicable when computing the Sales Tax Amount for the Invoice Header.

- VAT Code will be set from Company Installation if left blank. (VAT Code is typically used by non-US companies, and the VAT code will automatically be set to blank in the Invoice if Company Installation option to utilize VAT is not enabled).

- The 'Amount' in the Detail record is usually entered as a positive value for both invoices and credit memos (but negative amounts can be submitted when applicable.)

- For Invoices, positive amounts in the Detail record will Debit the Distribution G/L account (and negative amounts will be Credits) when the transaction is later updated to G/L.

- For credit memos, positive amounts in the Detail record will Credit the Distribution G/L account (and negative amounts will be Debits) when the transaction is later updated to G/L.

- The 'Amount' in the Detail record does not include Sales or Use tax amount.

- The sum of amounts in the Detail record must equal the Invoice_Amount in the Header, if defined.

- Amounts containing partial pennies will be rounded to nearest whole penny when necessary.

- Currency Code will be assigned from Vendor setup, if applicable.

- The new invoice will be configured by the Web Service for "Pay-When-Paid" based on Job and Subcontract setup, if applicable, using the same rules for flagging a transaction as in Vendor Invoice Entry.

- Pay Location Code will be auto-assigned by the Web Service like in Vendor Invoice Entry, based on Vendor setup (if defined).

- The Approval Status serves as an indicator when importing invoices that need to be routed for approval. If the routing code is left blank in the import file, it will be auto-assigned by the Web Service like in Vendor Invoice Entry, based on Job and Vendor setup (if defined).

- The Payment Status serves as an indicator when the invoice has already been paid by check or credit card. If paid with manual check, the Bank Account and Check# are required. If paid with credit card, the Credit Card account code is required (plus Card #, if applicable). Cash G/L account and net payment amount will be set automatically by the Web Service. Cash Management must be present to utilize this feature.

- All Detail records must be for the subcontract job when Invoice references a defined Subcontract# in the Header record. Subcontract job must be in the defined company (that is, job and invoice in same company).

- Distribution G/L Account:

- If a G/L account is defined in the Detail record, it must be Active or Inactive in the Distribution Company

- If not defined in the Detail record, the Web Service will first attempt to auto-assign it from settings in Accounts Payable Installation in the Distribution Company when 'Automate G/L defaults' is set to Yes.:

- If a valid Job Code is defined in the Detail record, then auto-assign from Cost Type File Maintenance, if defined, or the 'J'ob G/L account from that installation screen, if found. G/L account must be 'direct job cost'.

- If a valid Equipment Code is defined in the Detail record, then auto-assign the 'E'quipment G/L account from that installation screen, if found. G/L account must be 'direct equipment cost'.

- If a valid Work Order number is defined in the Detail record, then auto-assign the 'W'ork order G/L account from that installation screen, if found. G/L account must be 'direct work order cost'.

- If not defined in the Detail record and the Web Service could not assign it from Installation settings, then the Web Service will assign the G/L account from Vendor Defaults.

- The Distribution G/L Account is required, either from the import file or from settings in Spectrum, and the assigned account must be valid in the Distribution Company, with a status of Active or Inactive.

- Cost Centers:

- Liability Cost Center (Header Cost Center)

- Cost Center is required when Cost Centers are set to Yes in the defined Company

- Cost center information is ignored when Cost Centers are set No or Pending.

- Cost Center must be Active in the defined company

- Cost Center must be valid for the A/P G/L Account and valid for the Vendor Code

- Distribution Cost Center (Detail Cost Center):

- If a direct cost Distribution G/L code is defined in the Detail record, the Distribution Cost Center will be assigned by the Web Service (and import data will be ignored):

- For a Direct Job Cost Distribution G/L code, the Web Service will assign the Phase then Job Cost Center.

- If it is a Direct Equipment Cost Distribution G/L code, the Web Service will assign the Equipment Category then Equipment CC

- For a Direct Work Order Cost Distribution G/L Code, the Web Service will assign the Work Order Cost Center.

- The assigned Distribution Cost Center for a direct cost record must be allowed for the Distribution G/L code.

- If a non-direct Distribution G/L code is defined in the Detail record, the Distribution Cost Center is optional:

- If the Distribution Cost Center is blank, the Web Service will assign the Liability Cost Center if valid for the Distribution G/L Code and Vendor Code.

- If the Distribution Cost Center is defined in the import file, the Web Service will verify the Distribution Cost Center is Active in the distribution company, and is valid for the Distribution G/L Account and the Vendor Code.

- Cost Center import data is ignored if Cost centers are not set to Yes in the Distribution Company

- Document Imaging

- The Web Service will determine the applicable Cabinet and Drawer, as follows:

- The Web Service will determine the applicable DI Folder for the incoming Image File

- The Web Service will determine the applicable Path for the Image File by reading for the company-wide default "Path" variable specified in Document Imaging Installation

- Note to Reader: Document Imaging offers an option to store images by Year and Period. The Web Service will automatically store imported invoice images as if the DIPathByYearAndPeriod value variable is <blank>.

- A/P Invoice Image-Specific Detail Information:

- The Web Service will insert a record for the incoming invoice image into DI_IMAGE_MASTER, as follows:

- Document_ID = Use text string from Import File, if specified

- However, if no Document ID is imported, the Web Service will generate unique Document ID.

- In the case where the Web Service generates the Document ID, the value will be returned to a 3rd party calling the web service.

- Image_Path = Path determined above

- Image_Filename = Unique file name devised by Web Service

- Create_Operator = Set to 3-character Spectrum Operator Code associated with the Authorization ID in Data Exchange Installation

- Create_Date = Set to current system date

- Create_Time = Set to current system time

- Change_Operator = <leave blank>

- Change_Date = <leave blank>

- Change_Time = <leave blank>

- Image_Description = Use text string from Import File, if specified

- A/P Invoice <invoice#> (<#>)

- A/P Invoice 123 (2)

- Image Cross-Reference Table:

- The Web Service will insert a record into the DI_IMAGE_XREF Table, linking the Invoice Image-Specific Detail with the detail and the Invoice Image Header record, as follows:

- Transaction_ID = same as field in DI_MASTER_MC

- Document_ID = same as KEY field in DI_IMAGE_MASTER

- The Web Service follows the majority of the same logic as manually attaching an image to the invoice, with the exceptions of the data defined here.

## Header Fields

Use the table below for reference when using this service.
Element NameDescriptionReq?TypeMaxFormatValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation screen
GUIDUnique reference number created by programmingText36** See GUID definition
Company_CodeCompany codeYESText3Valid company in Spectrum
Vendor_CodeVendor CodeYESText10Valid vendor code must exist in the defined company
Status = Active or Inactive

Invoice_NumberInvoice NumberYESText20Unique invoice number within each vendor code (including unapproved, unposted, open items, payment history or rejected).
Invoice_Type_CodeInvoice TypeText1If left blank, assign as InvoiceI=Invoice
C=Credit memo

Approval_StatusApproval StatusText1If left blank, invoice will be treated as A (Approved Entry)U=Unapproved
A=Approved

Routing_CodeRouting CodeText10If left blank, routing code will be auto-assigned by the Web Service based on Job and Vendor setup (if defined).Valid routing code must exist in the defined company.
GL_DateG/L DateDate10Enter as: MM/DD/CCYY
Data in this field is ignored when importing an Unapproved item
Must be within A/P processing date range when importing an Approved invoice
Invoice_DateInvoice DateDate10Enter as MM/DD/CCYY
If left blank, assign current A/P processing date
Cannot exceed A/P maximum processing date if A/P installation option selected.
Invoice_AmountInvoice Amount Before TaxNum14Enter total Invoice amount before tax, including retention.
If left blank, set equal to the sum of Amounts in the Detail records.
Must be Positive Amount only.
Must be greater than Discount amount
No partial pennies.
Maximum allowable amount = 999,999,999.99 (commas optional)

Sales_Tax_AmountSales Tax Amount (Canada PST)Num12*** See Assumptions and DependenciesNegative value not allowed
No partial pennies.

VAT_CodeVAT CodeText10*** See Assumptions and DependenciesValid VAT code must exist in the defined company
Total_VAT_AmtVAT Tax AmountNum13If left blank, value will be calculated when VAT Code defined.
Entered VAT amount will override calculated value, if non-zero.
Negative value not allowed
No partial pennies.

Contract_NumberSubcontract #Text10 *** See Assumptions and DependenciesValid subcontract # for defined vendor must exist in the defined company
Vendor Status = Active or Inactive

Retention_AmountRetention Amount (Canada Holdback)Num12This is the retention portion only of the invoice
If Header record is entirely retention, then Invoice Amount field and this amount will be the same value
Positive Amounts only.
No partial pennies.

Batch_CodeBatchText10If left blank, assign Operator code (from Authorization_ID)
Payment_Due_DatePayment Due DateDate10Enter as MM/DD/CCYY
If left blank, then date will be calculated from subcontract or vendor defaults

Discount_Due_DateDiscount Due DateDate10Enter as MM/DD/CCYY
If left blank, then date will be calculated from subcontract or vendor defaults

Discount_AmountDiscount AmountNum12If left blank, then date will be calculated from subcontract or vendor defaultsNegative value not allowed.
Must be less than the Invoice Amount.
No partial pennies.

StatusOn Hold?Text1If left blank, invoice will be set to OpenH=Hold
O=Open

Payment StatusPayment StatusText1If left blank, invoice will be treated as Unpaid
*** See Assumptions and Dependencies
U=Unpaid
M=Manual Check
C=Credit Card
Payment Status must be Unpaid if retention is non-zero.
Payment Status cannot be set to Manual Check if invoice is Unapproved.

Bank_Account_CodeCredit Card or Bank Account CodeText10Ignored unless Payment Status = Manual Check or Credit Card
Account type must be Bank for Payment Status=M
Account must be Credit Card for Payment Status=C
Valid Account Code must exist in defined company
Check_NumberManual Check #Text6Required if paid with Manual CheckMust be un-used check # for Bank Account
Card_NumberCard #Text10Required if defined Account tracks Card NumbersValid card number must exist in defined Credit Card Account Code
Check_DatePayment DateDateEnter as MM/DD/CCYY Ignore unless Payment Status = Manual Check or Credit CardMust be within A/P processing date range, and within the same Fiscal Year and Period as the G/L Date
AP_GL_AccountLiability G/L CodeText12No dashes.
If left blank, assign 'Default A/P Trade G/L account' from Accounts Payable Installation
Valid G/L code must exist in the defined company.
Account Status = Active or Inactive
G/L account must be 'Non-direct cost'.

Cost_CenterLiability Cost CenterText10*** See Assumptions and DependenciesValid Cost Center code must exist in the defined company if Cost Centers = Yes
RemarksInvoice RemarksText30

## Image Fields

Use the table below for reference when using this service.
Element NameDescriptionReq?TypeMaxFormatValidation
Image_FileImage FileYESBase64
Image_TypeFile ExtensionYESText
Document_IDDocument IDText19*** See Assumptions and DependenciesMust be unique in Spectrum
Image_DescriptionImage DescriptionText40*** See Assumptions and Dependencies

## Detail Fields

Use the table below for reference when using this service.
Element NameDescriptionReq?TypeMaxFormatValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation screen
GUIDUnique reference number created by programmingText36** See GUID definition
Company_Code_2Distribution CompanyText3If left blank, then the defined company will be assignedA/P Installation must be set in the defined company to allow multi-company transactions
Distribution_GL_AccountDistribution G/L AccountText12*** See Assumptions and Dependencies
No dashes.
If a cost type is assigned to the G/L Account, it must match the Cost Type Code in the Detail record (below).
Valid G/L code must exist in the distribution company.
Account Status = Active or Inactive

Cost_CenterDistribution Cost CenterText10*** See Assumptions and DependenciesValid Cost Center code must exist in the distribution company, if Cost Centers = Yes
AmountAmount Before TaxNum14*** See Assumptions and Dependencies
Amount may be negative, but sum of all lines must result in positive value
No partial pennies.
Maximum allowable unit price = 999,999,999.99 (commas optional)

Job_NumberJob NumberText10Data in this field is ignored if the G/L account is not 'Direct job cost'Required when Distribution G/L account is 'Direct job cost'.
Valid job code must exist in the Distribution company
Status = Active or Inactive

Phase_CodePhase CodeText20No dashes.
Data in this field is ignored if the G/L account is not 'Direct job cost'
Required when Distribution G/L account is 'Direct job cost'
Cost_TypeCost TypeText3If a G/L Account is assigned to the Cost Type Code, it must match the G/L Account in the Detail record (above).
Data in this field is ignored if the G/L account is not 'Direct job cost'
Required when Distribution G/L account is 'Direct job cost'.
Valid Phase Code + Cost Type Code combination for the Job Code must exist in the distribution company
Phase Code + Cost Type Code cannot be 'Completed'

Equipment_CodeEquipment CodeText10Data in this field is ignored if the G/L account is not 'Direct equipment cost'Required when Distribution G/L account is 'Direct equipment cost'.
Valid equipment code must exist in the Distribution company
Status = Active or Inactive

Equipment_CategoryEquipment Cost CategoryText4Data in this field is ignored if the G/L account is not 'Direct equipment cost'Required when Distribution G/L account is 'Direct equipment cost'.
Valid equipment cost category code must exist in the Distribution company

PM_Work_OrderEquipment Work OrderText10If the Cost Category File Maintenance 'Data entry' radio group is set to 'Require equipment work order' in the Distribution company, then entry in this field is required. WO# is ignored if radio group set to 'None'.
Data in this field is ignored if the G/L account is not 'Direct equipment cost'
PM Work Order must be valid in the Distribution company, if assigned.
WO_NumberWork Order #Text10Work Order status cannot be 'C'omplete.
Work Order cannot be a job Work Order.
Data in this field is ignored if the G/L account is not 'Direct work order cost'
Required when Distribution G/L account is 'Direct work order cost'.
Valid Work Order # must exist in the defined company

Item_CodeItem CodeText15When the first character of the code is '!' it will be treated a non-stock item.
Data in this field is ignored if the G/L account is not 'Direct work order cost'
Valid item code must exist in the defined company, unless it is a non-stock item.
Item Code cannot have status = 'Not used'.

Item_DescNon-Stock Item DescriptionText35Data in this field is ignored if the Item Code is valid.
Data in this field is ignored if the G/L account is not 'Direct work order cost'

Unit_Of_MeasureNon-Stock Unit of MeasureText3Data in this field is ignored if the Item Code is valid.
Data in this field is ignored if the G/L account is not 'Direct work order cost'

QuantityQuantityNum12Data in this field is ignored if the G/L account is not 'Direct work order cost'Maximum allowable quantity = 9,999,999.99 (commas optional)
WO_Unit_PriceWork Order Billing PriceNum13Data in this field is ignored if the G/L account is not 'Direct work order cost'Maximum allowable unit price = 99,999,999.99 (commas optional)
WO_EquipmentWork Order Site EquipmentText8Required if Work Order installation flag is selected.
Data in this field is ignored if the G/L account is not 'Direct work order cost'
Valid site equipment code must exist for the Site assigned to the defined Work Order # in the defined company.
WO_ComponentWork Order Site ComponentText2Required if Work Order installation flag is selected.
Data in this field is ignored if the G/L account is not 'Direct work order cost'
Valid site equipment component must exist for the Site assigned to the defined Work Order # in the defined company.
WO_SC_ContractWork Order Service ContractText10Data in this field is ignored if the G/L account is not 'Direct work order cost'
Data in this field will be ignored if Service Contract is not present in the defined company.
Valid service contract must exist for the Site assigned to the defined Work Order # in the defined company.
Tax_CodeTax CodeText15*** See Assumptions and DependenciesValid Sales/Use Tax code must exist in the defined company
RemarkRemarkText30If left blank, assign Invoice Remarks text string from Header

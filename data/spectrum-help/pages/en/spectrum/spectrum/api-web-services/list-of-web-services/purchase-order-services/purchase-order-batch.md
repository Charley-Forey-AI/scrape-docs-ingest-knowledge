---
title: "Purchase Order Batch | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/purchase-order-services/purchase-order-batch"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/purchase-order-services/purchase-order-batch"
---

# Purchase Order Batch

Use this service to add purchase order header and detail information for job-specific purchases and warehouse purchases.

## Connection Information

URL: https://<SPECTRUM-SERVER>:8482/purchaseOrders
Authentication: [Basic Authentication](/en/spectrum/spectrum/api-web-services/authentication/basic-authentication), [Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)
Supported methods: POST
Supported formats: JSON

## Sample JSON Body

```
`{
 "purchaseOrders": [{
 "Company_Code": "KM2",
 "PO_Number": "",
 "Vendor_Code": "KM_117",
 "Warehouse_Code": "",
 "Job_Number": "KM101",
 "WO_Number": "",
 "Vat_Code": "",
 "Status_Flag": "O",
 "Create_Revision": "",
 "Cost_Center": "101",
 "Remarks": "",
 "Special_Instructions": "",
 "Ship_To_Code": "",
 "Ship_Name": "",
 "Ship_Address_1": "",
 "Ship_Address_2": "",
 "Ship_City": "",
 "Ship_State": "",
 "Ship_Zip_Code": "",
 "Ship_Via": "",
 "Ship_Terms": "",
 "FOB": "",
 "Ordered_By": "",
 "Confirmed_By": "",
 "PO_Order_Date": "",
 "Batch_Code": "100218",
 "Terms_Code": "",
 "Payment_Days": 0,
 "Discount_From_Code": "",
 "Discount_Days": 0,
 "Terms_Percent": 0,
 "Terms_Description": "",
 "Resale_Flag": "",
 "Tax_Code": "",
 "Routing_Code": "",
 "PO_Delivery_Date": "10/02/2018",
 "PO_Method": "1",
 "PO_Type": "U",
 "Bank_Account_Code": "",
 "Card_Number": "",
 "Comment": "",
 "poDetails": [{
 "Detail_Entry_Type": "D",
 "PO_Quantity": 100,
 "Item_ID": "101",
 "Item_Description": "",
 "Unit_Of_Measure": "EA",
 "Item_Price": 0,
 "Item_Discount_Percent": 0.0,
 "GL_Account": "000666",
 "Phase_Code": "000100",
 "Cost_Type": "M",
 "Tax_Code": "",
 "Delivery_Date": "",
 "Message": "",
 "Warehouse": "",
 "Equipment_Code": "",
 "Equipment_Category": "",
 "PM_Work_Order": "",
 "WO_Number": "",
 "System_ID": "",
 "Component_Number": "",
 "WO_Item_Price": 0,
 "SC_Contract": "",
 "Cost_Center": "101"
 },
 {
 "Detail_Entry_Type": "M",
 "PO_Quantity": 0,
 "Item_ID": "",
 "Item_Description": "",
 "Unit_Of_Measure": "",
 "Item_Price": 0,
 "Item_Discount_Percent": 0.0,
 "GL_Account": "",
 "Phase_Code": "",
 "Cost_Type": "",
 "Tax_Code": "",
 "Delivery_Date": "",
 "Message": "Test Message",
 "Warehouse": "1",
 "Equipment_Code": "",
 "Equipment_Category": "",
 "PM_Work_Order": "",
 "WO_Number": "",
 "System_ID": "",
 "Component_Number": "",
 "WO_Item_Price": 0,
 "SC_Contract": "",
 "Cost_Center": "101"
 }]
 }]
}`
```

## Underlying File Maintenance

Prior to importing information for a particular Purchase Order, the following file maintenance areas must be completed:

- System Administration > Installation > Purchase Order

- System Administration > Installation > Purchase Order > P.O. Remarks Maintenance

- System Administration > Installation > Purchase Order > Special Instructions Maintenance

- System Administration > Installation > Purchase Order > Ship Via Maintenance

- System Administration > Installation > Purchase Order > Shipping Terms Maintenance

- System Administration > Installation > Purchase Order > Vendor Special Cost Maintenance

- System Administration > Installation > Purchase Order > Job Special Cost Maintenance

- System Administration > Installation > Accounts Payable

- System Administration > Installation > Accounts Payable > Use Tax Code Maintenance

- System Administration > Installation > Accounts Payable > Invoice Approval Routing Maintenance

- System Administration > Installation > Accounts Payable > Vendor

- System Administration > Installation > Accounts Payable > Vendor Defaults

- System Administration > Installation > Accounts Payable > Vendor Locations

- System Administration > Installation > Cash Management > Accounts (Credit card type)

- System Administration > Installation > Cash Management > Accounts (Credit card - multiple card numbers)

- System Administration > Installation > General Ledger > Value Added Tax Code Maintenance

- System Administration > Installation > Job Cost

- System Administration > Installation > Job Cost > Cost Type File Maintenance

- System Administration > Installation > Job Cost > Tax Classification Maintenance

- System Administration > Installation > Job Cost > Jobs

- System Administration > Installation > Job Cost > Phases

- System Administration > Installation > Job Cost > Tax Classification Maintenance

- System Administration > Installation > Inventory Control > Inventory Item Maintenance

- System Administration > Installation > Inventory Control > Warehouse Maintenance

- System Administration > Installation > Enterprise Management > Cost Center Maintenance

## Assumptions and Dependencies

- The Purchase Order Web Service will support inclusion of multiple new and/or existing purchase orders ('batch' processing) when submitted in the following sequence:
```
`<First PO – Header record>
 <Detail record 1>
 <Detail record 2>
 <Detail record 3> . . . .
<Second PO – Header record>
 <Detail record 1>
 <Detail record 2>
 <Detail record 3> . . . .
<Third PO – Header record>
<Fourth PO – Header record>
 <Detail record 1> . . . .`
```

- The Purchase Order Web Service ADDS purchase order header and detail information for job-specific purchases and warehouse purchases.

- The Purchase Order Web Service UPDATES purchase order header and detail information for purchases with Status = Proposed, essentially replacing all data on the existing P.O. with latest information.

- The Web Service will not support the following logic: If any of these conditions are encountered (or if any field-level validation fails), the Web Service will reject the particular P.O. in its entirety and return summary error messages indicating problem found (in the Header, in the Detail or both). Please note that in the case where there are multiple POs in the batch, the Web Service will import the ones with no errors while rejecting those with problems.

- Add Purchase Order for a Job with a 'Completed' status

- Add Purchase Order for a Vendor with a 'Not used' status

- Update to Purchase Order for a Job with a 'Completed' status

- Update to Purchase Order for a Vendor with a 'Not used' status

- Update to Purchase Order with an 'Open' status

- Update to Purchase Order with a 'Closed' status

- Add Purchase Order containing direct equipment cost purchase line

- Add Purchase Order containing direct work order cost purchase line

- Update Purchase Order containing direct equipment cost purchase line

- Update Purchase Order containing direct work order cost purchase line

- The Web Service follows the majority of the same logic as manually entering a P.O., with the exceptions of the data defined here.

- The System Administration > Installation > Purchase Order > Defaults Tab will populate the following fields if the field in the record is left blank:

- Ship_To_Code

- Ship_Address_1

- Ship_Address_2

- Ship_City (Please note that this column is expanded from 15 to 25 characters as part of this project)

- Ship_State

- Ship_Zip_Code

- Ship_Via

- Ship_Terms

- FOB

- Confirmed_By

- Ship-to code field:

- Options include: D=Default address, J=Job address or I=Input. If field is blank, Ship-to code will be set to D

- If the Ship-to code is defined as "I" (Input), then all the Ship-to fields must be defined except for Ship_Address_2

- Remarks, Special Instructions, Ship Via and Shipping Terms may have pre-defined data; however, the field can be over-written with other text

- Terms Description text will be constructed automatically by the Web Service when this field is left blank. Like in Purchase Order Entry, it will read the Payment basis and number of days ('NET 10 Days' or 'NET 10TH') PLUS Discount basis, days and percentage ('2% 10' or '2% 10TH')

- Sales/Use Tax Code

- When the Tax Code field is left blank in the Purchase Order Header, determine the default Tax Code using the hierarchy (Job or Vendor) specified in Job Cost Installation if Tax Classification is enabled, and settings in Tax Classification Maintenance and Vendor Defaults, using same rules as in Purchase Order Entry.

- When the Tax Code field is left blank in the Purchase Order Detail, apply same rules as in Purchase Order Entry, including phase-specific tax rules from Tax Classification Maintenance, if applicable.

- VAT Code will be set from Company Installation if left blank. (VAT Code is typically used by non-US companies, and the VAT code will automatically be set to blank in the P.O. if Company Installation option to utilize VAT is not enabled).

- When the Resale Flag is left blank, this field will be set to 'Y'es if vendor's sales/use tax code is a 'Use' type code or 'No' (blank) if vendor's sales/use tax code is 'Sales' type.

- Purchase Location Code and Pay Location Code will be auto-assigned by the Web Service like in Purchase Order Entry, based on Vendor setup (if defined).

- P.O. receiving method (1-step or 2-step) will be auto-assigned by the Web Service like in Purchase Order Entry, based on Vendor setup, if defined (and otherwise from Purchase Order Installation). Currency Code will also be assigned from Vendor setup, if applicable.

- Currency Code will be assigned from Vendor setup, if applicable.

- Line_Number is auto-assigned to Detail lines by the Web Service in the same sequence as the Detail records are submitted (001-999). Detail records are automatically assigned to the same Company and P.O. number as referenced in the Header.

- The Detail Entry Type field will be used to indicate what data is contained in the particular detail record. There are three basic types of detail line: Stock item, Non-stock item or Message-only text.

- Stock item: Set Detail Entry Type = D when importing a stock item and specify the Item_Code in the 'Item ID' field

- Item_Code must be valid in the defined company and cannot have a status of 'Not Used'

- If an Item_Code (with an authorized status) is not found, an error will be generated

- If the Data Entry Type field is left blank, then treat the record as if Detail Entry Type =D

- Non-stock item: Set Detail Entry Type =N and specify the Item_Code in the 'Item ID' field. Non-stock items must begin with an exclamation mark (!). The Web Service will add it automatically if not present in the import data. The Item_Code, including the exclamation mark, must not exceed 15 characters.

- If the PO_Type in the Header is set to (L)ump sum, then all items in the P.O. must be non-stock

- Message-only: Set Detail Entry Type =M and specify up to 250 characters in the 'Comment' field. Data in all other fields in the record will be ignored for message-only lines.

- Item Description

- For non-stock items, the imported data will be assigned to the detail line in the P.O.

- For stock items, the item description will be assigned from Inventory Item Master (and imported data ignored)

- Unit of Measure

- For non-stock items, the imported data will be assigned to the detail line in the purchase order. Like in Purchase Order Entry, special calculations are provided for 'C' and 'M' units of measure. When the unit of measure is 'C', the Item Price will be interpreted as a price-per-100 and when the unit of measure is 'M', the Item Price will be interpreted as a price-per-1000

- For stock items, the unit of measure will be assigned from Inventory Item Master (and imported data ignored)

- If the Item Price is left blank, the Web Service will assign the price to the detail line using the same rules as the Default price when adding the item directly in Purchase Order Entry, including any Vendor Special Cost or Job Special Cost settings

- Tax amounts and detail line extensions will be calculated automatically by the Web Service, based on quantity, unit price, line-item discounts and other settings, like in Purchase Order Entry. P.O. totals in the Header Table will also be set automatically by the Web Service.

- Cost Centers

- Job Purchase Order:

- If left blank, the Cost Center Code in the Purchase Order Header will be assigned from Job Master when cost centers are set to 'Yes' in the defined company.

- If defined, the Cost Center Code in the Purchase Order Detail will be auto-assigned from Phase Maintenance, (and otherwise from Job Master) when cost centers are set to 'Yes' in the defined company.

- Warehouse Purchase Order

- If left blank, the Cost Center Code in the Purchase Order Header will be assigned from Warehouse Maintenance when cost centers are set to 'Yes' in the defined company.

- The Cost Center in the Purchase Order Detail will be assigned from Warehouse Maintenance or the P.O. Header (as in Purchase Order Entry) if left blank when cost centers are set to 'Yes' in the defined company.

- Workflow

- When a new purchase order is ADDED with a status of 'Proposed', the Web Service will automatically initiate the Workflow for the new P.O. if the 'Proposed Purchase Order' Workflow is Active in the defined company.

- When an existing purchase order with a Workflow is UPDATED, that Workflow will remain 'as is' and will not be altered or reassigned.

- When an existing purchase order with No Workflow is UPDATED, the Web Service will automatically initiate the Workflow for that existing P.O. if its status is 'Proposed' and the 'Proposed Purchase Order' Workflow is Active in the defined company.

- Fields in the Header and Detail labeled 'Reserved' are included for future development. Any information contained in these fields will be ignored by the Web Service.

## Header Fields

Use this table for reference when using this service.
Element NameDescriptionReq?TypeMaxFormatValidation
Company_CodeCompany codeYESText3A valid company
PO_NumberPO NumberYESText10If left blank, auto-assign the next P.O. numberNo duplicates
Vendor_Code
Vendor Code
YES
Text
10
Valid vendor code must exist in the defined company
Status = Active or Inactive

Warehouse_Code
Warehouse
Text
10
Required unless there are no non-direct cost records in Detail
Valid warehouse code must exist in defined company

Job_Number
Job #
Text
10
Required unless valid Warehouse_Code is defined in Header AND there are no Direct Job Cost records in Detail
Valid job code must exist in the defined company
Status = Active or Inactive

WO_Number
Reserved
Text
10
Reserved for future use
Ignore any data in this field

VAT_Code
VAT Code
Text
10
*** See Assumptions and Dependencies
Valid VAT code must exist in the defined company

Status_Flag
Status
Text
1
If left blank, P.O. will be set to Proposed
P=Proposed, O=Open, C=Closed.

Create_Revision
Reserved
Text
1
Reserved for future use
Ignore any data in this field

Cost_Center
Cost Center
Text
10
*** See Assumptions and Dependencies
Valid Cost Center code must exist in the defined company, if cost centers = Yes

Remarks
Remarks
Text
29
If text matches valid Remarks Code in defined company, then assign its description to PO
Allow Remarks Code, blank or any text string

Special_Instructions
Special Instructions
Text
29
If text matches valid Special Instructions Code in defined company, then assign its description to PO
Allow Special Instructions Code, blank or any text string

Ship_To_Code
Ship-to Code
Text
1
If left blank, assign (D)efault
*** See Assumptions and Dependencies
D=Default
J=Job
I=Input

Ship_Name
Ship-to Name
Text
30
Must be defined if Ship-to code =I

Ship_Address_1
Ship-to Address1
Text
30
Must be defined if Ship-to code =I

Ship_Address_2
Ship-to Address2
Text
30

Ship_City
Ship-to City
Text
25
Must be defined if Ship-to code =I

Ship_State
Ship-to State
Text
2
Must be defined if Ship-to code =I

Ship_Zip_Code
Ship-to Postal Code
Text
10
Must be defined if Ship-to code =I

Ship_Via
Ship Via
Text
15
If text matches valid Ship Via Code in defined company, then assign its description in PO.
If left blank, assign from Purchase Order Installation
Allow Ship Via Code, blank or any text string

Ship_Terms
Shipping Terms
Text
15
If text matches valid Ship Terms Code in defined company, then assign its description in PO
If left blank, assign from Purchase Order Installation
Allow Ship Terms Code, blank or any text string

FOB
FOB
Text
15
If left blank, assign from Purchase Order Installation

Ordered_By
Ordered By
Text
20

Confirmed_By
Confirmed By
Text
20
If left blank, assign from Purchase Order Installation

PO_Order_Date
Order Date
Date
10
Format = MM/DD/CCYY.
If left blank, assign current P.O. processing date
Must be within P.O. minimum/maximum date range

Batch_Code
Batch Code
Text
10
If left blank, assign Operator code (from Authorization_ID)

Terms_Code
Payment Terms Basis
Text
1
If left blank, assign from Vendor
A=Based on Invoice date
B=Based on First of next month

Payment_Days
Payment Number of Days
Num
3
If left blank, assign from Vendor
Must be non-negative

Discount_From_Code
Discount Due Basis
Text
1
If left blank, assign from Vendor
A=Based on Invoice date
B=Based on First of next month

Discount_Days
Discount Number of Days
Num
3
If left blank, assign from Vendor
Must be non-negative

Terms_Percent
Discount %
Num
6
Enter 12.34 for 12.34%.
If left blank, assign from Vendor
Must be non-negative

Terms_Description
Terms Description
Text
20
*** See Assumptions and Dependencies

Resale_Flag
â€˜For Resaleâ€™ Flag on PO Form
Text
1
*** See Assumptions and Dependencies
Y=For resale
N= Not for resale

Tax_Code
Default Sales/Use Tax Code
Text
15
*** See Assumptions and Dependencies
Valid Sales/Use Tax code must exist in the defined company

Routing_Code
Routing Code
Text
10
*** See Assumptions and Dependencies
Valid Routing code must exist in the defined company

PO_Delivery_Date
Delivery Date
Date
10
Format = MM/DD/CCYY

PO_Method
Receiving Method
Text
1
*** See Assumptions and Dependencies
Must be '1' or '2' if non-blank

PO_Type
Pricing Type
Text
1
If left blank, assign from Purchase Order Installation
U=Unit price
L=Lump sum

Bank_Account_Code
Credit Card Account
Text
15
Must be a 'Credit Card' type account
Valid Account Code must exist in the defined company

Card_Number
Card #
Text
10
Required if defined Account tracks Card Numbers
Valid card number must exist in the defined company

Comment
Comment
Text
250

## Detail Fields

Use this table for reference when using this service.
Element Name
Description
Req?
Type
Max
Format
Validation

Authorization_ID
Authorization ID to access the server
YES
Text
20
Data Exchange Installation screen

GUID
Unique reference number created by programming
Text
36
** See GUID definition

Detail_Entry_Type
Detail Entry Type
Text
1
*** See Assumptions and Dependencies
D=Defined item code
N=Non-stock item
M=Message-only

PO_Quantity
Quantity
Num
12
Map to PO_Quantity_List1
Required to be non-zero unless this is a Message-only line
Maximum allowable quantity = 9,999,999.99 (commas optional)

Item_ID
Item ID
Text
15
*** See Assumptions and Dependencies
Required unless this is a Message-only line

Item_Description
Item Description
Text
35
*** See Assumptions and Dependencies

Unit_Of_Measure
Unit of Measure
Text
3
*** See Assumptions and Dependencies

Item_Price
Item Price
Num
14
*** See Assumptions and Dependencies
Maximum allowable price = 9,999,999.9999 (commas optional)

Item_Discount_Percent
Discount %
Num
6
Enter 12.34 for 12.34%
Must be non-negative

GL_Account
G/L Account
Text
12
For Job P.O.: Must be 'Direct job cost' account
If a cost type is assigned to the G/L Account, it must match the Cost Type Code in the detail record (below).
If this field is left blank, default from Cost Type Maintenance (or from Accounts Payable Installation 'Automatic Default' setup for job if defined)
For Warehouse P.O.: Must be non-direct cost G/L account
Required unless this is a Message-only line
Valid G/L Account code must exist in the defined company
Status = 'Active' or 'Inactive'

Phase_Code
Phase
Text
20
No dashes
Required unless this is a Message-only line or a non-job purchase

Cost_Type
Cost Type
Text
3
If a G/L Account is assigned to the Cost Type Code, it must match the G/L Account in the detail record (above)
Required unless this is a Message-only line or a non-job purchase
Valid Phase Code + Cost Type Code combination for the Job Code in the Header must exist in the defined company
Phase Code + Cost Type Code cannot be 'Completed'

Tax_Code
Sales/Use Tax Code
Text
15
*** See Assumptions and Dependencies
Valid Sales/Use Tax code must exist in the defined company

Delivery_Date
Delivery Date
Date
10
Format = MM/DD/CCYY

Message
Message
Text
250
Required if this is a 'message-only' line

Warehouse
Reserved
Text
10
Reserved for future use
Ignore any data in this field

Equipment_Code
Reserved
Text
10
Reserved for future use
Ignore any data in this field

Equipment_Category
Reserved
Text
4
Reserved for future use
Ignore any data in this field

PM_Work_Order
Reserved
Text
10
Reserved for future use
Ignore any data in this field

WO_Number
Reserved
Text
10
Reserved for future use
Ignore any data in this field

System_ID
Reserved
Text
8
Reserved for future use
Ignore any data in this field

Component_Number
Reserved
Text
2
Reserved for future use
Ignore any data in this field

WO_Item_Price
Reserved
Num
12
Reserved for future use
Ignore any data in this field

SC_Contract
Reserved
Text
10
Reserved for future use
Ignore any data in this field

Cost_Center
Cost Center
Text
10
*** See Assumptions and Dependencies
Valid Cost Center code must exist in the defined company, if cost centers = Yes

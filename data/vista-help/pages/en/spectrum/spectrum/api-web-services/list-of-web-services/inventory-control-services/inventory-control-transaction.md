---
title: "Inventory Control Transaction | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/inventory-control-services/inventory-control-transaction"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/inventory-control-services/inventory-control-transaction"
---

# Inventory Control Transaction

Use this service to add unposted inventory transactions.

## Connection Information

URL: https://<SPECTRUM-SERVER>:8482/inventory/transaction
Authentication: [Basic Authentication](/en/spectrum/spectrum/api-web-services/authentication/basic-authentication),
 [Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)
Supported methods: POST
Supported formats: JSON

## Sample JSON Body

```
`{
 "inventoryTransactions": [
 {
 "Company_Code": "ABC",
 "Transaction_Reference": "474",
 "Batch_Code": "WS-01",
 "transactionDetails": [{
 "Item_Code": "101",
 "Transfer_Type": "A",
 "Message": "WS Testing",
 "Warehouse": "01",
 "Transaction_Date": "09/13/2017",
 "Quantity": 100,
 "Unit_Cost": 800,
 "GL_Account": "7515",
 "Department": "MAT"
 },
 {
 "Item_Code": "101",
 "Transfer_Type": "M",
 "Message": "WS Testing",
 "Warehouse":"01",
 "Transaction_Date": "09/13/2017",
 "GL_Account": "7515",
 "Department": "MAT",
 "Cost_Adjustment": -50,
 "Source_Code": "1"
 },
 {
 "Item_Code": "101",
 "Transfer_Type": "T",
 "Message": "WS Testing",
 "Warehouse": "01",
 "To_Warehouse": "02",
 "Transaction_Date": "09/13/2017",
 "Quantity": 100
 },
 {
 "Item_Code": "101",
 "Transfer_Type": "R",
 "Message": "WS Testing",
 "Warehouse": "01",
 "Transaction_Date": "09/13/2017",
 "Quantity": 100,
 "Unit_Cost": 800,
 "GL_Account": "7515",
 "Department": "MAT"
 }
 ],
 "receiptCharges": {
 "Freight_Cost": 100,
 "Freight_Department": "MAT",
 "Misc_Charge": 100,
 "Misc_Department": "MAT"
 },
 "transferCharges": {
 "Freight_Cost": 100,
 "Freight_Department": "MAT",
 "Misc_Charge": 100,
 "Misc_Department": "MAT"
 }
 }]
}`
```

## Underlying File Maintenance

Prior to importing information for a particular vendor invoice, the following file maintenance areas must be completed:

- System Administration > Installation > Inventory Control

- System Administration > Installation > Inventory Control > Inventory Items

- System Administration > Installation > Inventory Control > Warehouse

- System Administration > Installation > Inventory Control > Category

- System Administration > Installation > Inventory Control > Cost Adjustment Source

- System Administration > Installation > Inventory Control > G/L Department

- System Administration > Installation > General Ledger

- System Administration > Installation > General Ledger > G/L Master File Maintenance

## Assumptions and Dependencies

- The Inventory Transaction Web Service adds unposted inventory transaction.

- The Web Service will not support the following logic:

- If any of these conditions are encountered (or if any field-level validation fails), the Web Service will reject the particular transaction in its entirety and return summary error messages indicating problem found (in the Header, in the Detail or both). Please note that in the case where there are multiple invoices in the batch, the Web Service will import the ones with no errors while rejecting those with problems.

- Transaction reference already exists historically or is used for entry type not covered within this service.

- Item code with a 'Not used' status

- G/L Account with a 'Not used' status

- The Web Service follows the majority of the same logic as manually entering a
 new inventory transaction, with the exceptions of the data defined here. The
 Spectrum Help Files can be used for troubleshooting errors along with the details
 defined here. Error message may vary however the validations within the web
 service should not allow data to enter Spectrum that cannot be provided via the
 Inventory Transaction Entry. Any fields that do not have a natural home within
 Spectrum will be ignored; for example, Cost Adjustment
 field on a (T)ransfer line if populated will be
 ignored.

- Transaction_Reference allows the user to define what type of detail lines there are. The current valid options are:

- A = Adjustment

- T = Transfer

- M = Cost adj.

- R = Receipt

- Warehouse –We will not allow a warehouse to have a transaction posted against it while the a count is in process. (See ticket IC0126, project IC-10783)

- Charges - transferCharges and recieptCharges can be defined as objects on the transaction. These will be ignored if the detail line does have it's corresponding transfer type. This should mimic the logic of the buttons in the upper right hand of the inventory transaction screen.

- Unit_cost of 0 (zero) is subject to defaults.

## Header Fields

Element Name
Description
Req?
Type
Max
Format
Validation

Company_Code
Company code
YES
Text
3
Valid company in Spectrum

Batch_Code
Batch code
Text
10
If left blank, assign Operator code (from Authorization_ID)

Transaction_Reference
Transaction reference
Text
7
 If left blank defaults from installation screen.

## Detail Fields

Element Name
Description
Req?
Type
Max
Format
Validation

Item_Code
Item code
Yes
Text
15

Transfer_Type
Transfer Type
Yes
Text
1
A = Adjustment
T = Transfer
M = Cost adj.
R = Receipt

Warehouse
Warehouse

Text
10
If left blank, defaults from installation screen.

To_Warehouse
To warehouse
Text
10
Required if Transfer_Type = "T"

Transaction_Date
Transaction date
Yes
Date
10
MM/DD/CCYY

Quantity
Quantity
Num
9
Six characters, decimal and two characters after decimal.
Ignored for Transfer_Type = "M"

Unit_Cost
Unit cost
Num
12
Ignored for Transfer_Type = "M","T"

Message
Message
Text
30

Department
GL Department
Text
4
Ignored for Transfer_Type = "T"

GL_Account
GL Account
Text
10
Ignored for Transfer_Type = "T"

Cost_Adjustment
Cost adjustment
Num
12
Ignored for Transferable = "A","T","R"

Source_Code
Source code
Text
2
Ignored for Transferable = "A","T","R"

## Charges (Transfer & Receipt) Fields

Element Name
Description
Req?
Type
Max
Format
Validation

Freight_Cost
Freight cost
Num
12

Freight_Department
Freight department
Text
4
Department must exist, required if freight cost populated

Misc_Charge
Miscellaneous charge
Num
12

Miscellaneous_Department
Miscellaneous department
Text
4
Department must exist, required if freight cost populated

---
title: "Purchase Order Header (POHB) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/purchase-order-header-pohb"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/purchase-order-header-pohb"
---

#  Purchase Order Header (POHB)

[Purchase Order
 Sample Text File](/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/purchase-order---sample-text-file)

Purchase Order Header - Table bPOHB

 Columns that are typically used for importing are in yellow

Column Name
Type
Importable
Default Available
Length & Scale
Required
Comments

Co
bCompany
Yes
Yes
### - 0 to 999
yes
AP Company number.Must exist in HQCO.

Mth
bMonth
Yes
Yes
MM/YY
yes
Can use the Invoice date to derive the Month of the transaction.

BatchId
bBatchID
No
Yes
##########
yes
Viewpoint Import will create next BatchId.

BatchSeq
int
No
Yes
##########
yes
Viewpoint Import will always generate the next Batch Sequence.

BatchTransType
char
No
Yes
1 Character
yes
Viewpoint Import Default will always set this value to "A" for additions.

VendorGroup
tinyint
No
Yes
###
yes
Vendor Group used to qualify the vendor number.Pulled from bHQCO based on AP Co#.

Vendor
tinyint
Yes
No
######
yes
Unique number identifying this vendor.

APRef
bAPReference
Yes
No
15 Characters
yes
AP reference number for this invoice. Typically, this is the invoice number supplied by the vendor.

Description
bDesc
Yes
No
30 Characters
no
Description of this invoice.

InvDate
bDate
Yes
Yes
MM/DD/YY
yes
Invoice date of this invoice.

DiscDate
bDate
Yes
Yes
MM/DD/YY
no
Discount date of this invoice.

DueDate
bDate
Yes
Yes
MM/DD/YY
yes
Due date of this invoice.

InvTotal
bDollar
Yes
No
##########.##
yes
Invoice Total.

HoldCode
bHoldCode
Yes
No
10 Characters
no
Hold code (from HQ Hold Codes) for this transaction, if applicable. This will prevent the invoice from being paid until the hold code is released.

PayControl
varchar
Yes
No
10 Characters
no
The pay control code is used to group invoices together for payment.

PayMethod
char
Yes
Yes
1 Character
yes
Payment methods are "C" for Check and "E" for EFT.

CMCo
bCompany
Yes
Yes
### - 0 to 999
yes
Viewpoint Cash Management company used for validating CM Accounts, and to which payment information from this AP company will be posted.

CMAcct
bCMAcct
Yes
Yes
####
no
Viewpoint CM Account from which this transaction will be paid.

PrePaidYN
char
Yes
Yes
1 Character
yes
"Y" if this transaction has already been paid else "N".

PrePaidMth
bMonth
Yes
No
MM/YY
no
if prepaid the month in which the payment will be posted.

PrePaidDate
bDate
Yes
No
MM/DD/YY
no
If prepaid, the date the payment was made on this transaction.

PrePaidChk
bCMRef
Yes
No
10 Characters
no
if prepaid, the check number on which this transction will be posted.

V1099YN
char
Yes
Yes
1 Character
yes
"Y" if this invoice’s amounts are to be included in the specified vendor’s 1099 totals else "N".

V1099Type
varchar
Yes
Yes
10 Characters
no
Specify a 1099 type of“MISC” (Miscellaneous Income), “INT” (Interest Income), or “DIV” (Dividends/Distributions).

V1099Box
tinyint
Yes
Yes
###
no
Specify the Vista Box # that will be used to accumulate and
 print 1099 amounts. Refer to the F4 lookup on the Box
 # field in AP Vendors, Add'l Info tab.

PayOverrideYN
char
Yes
Yes
1 Character
no
"Y" to override the name and/or address specified for this vendor in the
 AP Vendors.

PayName
varchar
Yes
No
60 Characters
no
If override payment address is "Y" you may enter an override to the vendor name.

PayAddress
varchar
Yes
No
60 Characters
no
If override payment address is "Y" you may enter an override to the vendor address.

PayCity
varchar
Yes
No
30 Characters
no
If override payment address is "Y" you may enter an override to the vendor city.

PayState
varchar
Yes
No
2 Characters
no
If override payment address is "Y" you may enter an override to the vendor state.

PayZip
varchar
Yes
No
12 Characters
no
If override payment address is "Y" you may enter an override to the vendor zip.

PayAddInfo
varchar
Yes
No
60 Characters
no
If override payment address is "Y" you may enter an override to the vendor additional information.

Notes

Yes
No

no
Notes

Table Guidelines
The definition of each of the table’s columns is outlined below.

- Column Name – The name of the column/field in the database table.

- Type – The column’s SQL data type. Types starting with a “b” are Viewpoint defined data types.

- Importable – The field is available for import.

- Default Available – Indicated if a programmatic default value is available for this field. Defaults use the same logic as a posting program to determine a value.

- Length and Scale – Indicates the format of the field.

- Required – Indicates if the data is required.
A hard coded default value can be specified in IM Template; when importing files this value overwrites the imported value.
Note:Use the Template Detail tab in the IM Template form to add any additional fields for importing.

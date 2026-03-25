---
title: "JC Contract Items (JCCI) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/jc-contract-items-jcci"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/jc-contract-items-jcci"
---

#  JC Contract Items (JCCI)

[JC Contract Items Sample Text File](/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/jc-contract-items---sample-text-file)

JC Contract Items - JCCI

* Columns are not necessarily in this order

Column Name
Type
Importable
Default Available
Length & Scale
Required
Comments

JCCo
bCompany
Yes
Y
integer 0-255
Yes
Company number

Contract
bContract
Yes
N
10 characters
Yes
Contract number

Item
bContractItem
Yes
N
16 characters
Yes
Item "number", up to 16 characters, not required to be sequential

Description
bItemDesc
Yes
Y
60 characters
No
Defaults to description of SICode if provided, otherwise "Item " + Item number

Department
bDept
Yes
Y
10 characters
Yes
Defaults to contract department

TaxGroup
bGroup
Yes
Y
integer 0-255
No
Tax group

TaxCode
bTaxCode
Yes
Y
10 characters
No
Tax code that will be used as a default when posting Accounts Receivable (AR) and Job Billing (JB) transactions to this contract item

UM
bUM
Yes
Y
3 characters
Yes
Unit of measure by which the contract units will be tracked.

SIRegion
varchar
Yes
Y
6 characters
No
All rights reserved. Any reproduction of this document without Viewpoint's written permission is strictly prohibited.

SICode
varchar
Yes
Y
16 characters
No
Standard Item code for the specified region

RetainPCT
bPct
Yes
Y
numeric; 5,4
Yes
Retainage percent

OrigContractAmt
bDollar
Yes
Y
numeric; 9,2
Yes
Contract item's original dollar value - updates contract's total amount

OrigContractUnits
bUnits
Yes
Y
numeric; 9,3
Yes
Contract item's original units (unless UM is lump sum)

OrigUnitPrice
bUnitCost
Yes
Y
numeric; 9,5
Yes
If SICode given, defaults to that UnitPrice (unless UM is lump sum)

BillType
bBillType
Yes
Y
1 character
No
(P)rogress, (T) & M, (B)oth, (N)one

BillGroup
bBillingGroup
Yes
Y
20 characters
No
Bill group for this item (used by Job Billing)

BillDescription
bItemDesc
Yes
Y
60 characters
No
Defaults to item description, may be overridden.Displayed on JB invoices.

Notes
bNotes
Yes
N
2^31 characters
No
Any notes for this item (currently 60 character limit).

InitSubs
bYN
Yes
Y
1 char (Y or N)
Yes
Y if % complete for subs should be same as for item.

StartMonth
bMonth
Yes
Y
valid month
No
Start month for this item, defaults to contract start month.

MarkUpRate
bRate
Yes
Y
numeric; 5,6
Yes
Markup rate for this item, in decimal (not %) form.

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

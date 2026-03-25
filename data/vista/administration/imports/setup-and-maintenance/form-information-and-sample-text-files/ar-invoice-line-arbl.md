---
title: "AR Invoice Line (ARBL) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/ar-invoice-line-arbl"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/ar-invoice-line-arbl"
---

#  AR Invoice Line (ARBL)

[AR Invoice Sample Text File](/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/ar-invoice---sample-text-file)

AR Invoice Line - Table bARBL

 Columns that are typically used for importing are in yellow

Column Name
Type
Importable
Default Available
Length & Scale
Required
Comments

Co
company
Yes
Yes
### - 0 to 999
yes
AR Company number.Must exist in HQCO.

Mth
bMonth
No
Yes
MM/YY
yes
Viewpoint import will set the month to be the same as the header.

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

ARLine
smallint
Yes
No
###
yes
Unique number identifying the line for this invoice.

TransType
char
No
Yes
1 Character
yes
Viewpoint Import Default will always set this value to "A" for additions.

RecType
tinyint
Yes
Yes
###
yes
Receivable types define various GL accounts that will automatically be updated when transactions are posted in AR.  deductions and liabilities.

LineType
char
Yes
Yes
1 Character
yes
M" for Material – For non-contract invoices, this type is used to enter information about materials you have sold.  "O" for Other – This type is used to enter detail for all other non-contract type invoices.  "C" for Contract – This type is used to enter detail for all other contract type invoices.

Description
bDesc
Yes
No
30 Characters
no
Description of this invoice line.

GLCo
bCompany
Yes
Yes
###
no
General Ledger company to use for this transaction.

GLAcct
bGLAcct
Yes
Yes
20 Characters
no
GL account to credit or debit for this transaction

TaxGroup
tinyint
Yes
Yes
###
yes
Tax Group used to qualify the Tax Code on this transaction.Pulled from HQCO based on the current ARCo or JCCo for contracts.

TaxCode
bTaxCode
Yes
Yes
10 Characters
no
Tax Code applied to this transaction.

Amount
bDollar
Yes
No
##########.##
no
Total charge for this line. This amount includes tax.

TaxBasis
bDollar
Yes
Yes
##########.##
no
Amount subject to tax.

TaxAmount
bDollar
Yes
Yes
##########.##
no
Amount subject to tax.

RetgPct
bUnitCost
Yes
Yes
##########.#####
no
Retainage percent by which retainage amount will be calculated for this transaction.

Retainage
bDollar
Yes
Yes
##########.##
no
Retainage amount for this transaction.

DiscOffered
bDollar
Yes
Yes
##########.##
no
Discount offered for this transaction.

TaxDisc
bDollar
Yes
Yes
##########.##
no
The amount of the Discount Offered that is Tax.

JCCo
bCompany
Yes
Yes
### - 0 to 999
no
Job Cost company to use for contract information.

Contract
bContract
Yes
Yes
10 Characters
no
Contract to which this invoice line is being applied. This must be the same as the contract as the one in the header record for this transaction.This column only applies to LineTypes that equal "C" for Contract.

Item
bContractItem
Yes
No
16 Characters
no
Contract item to which this invoice line is being appiled. This column only applies to LineTypes that equal "C" for Contract.

ContractUnits
bUnitCost
Yes
No
#####.#####
no
Contract Units for Invoice line being appiled. This column only applies to LineTypes that equal "C" for Contract.

UM
bUM
Yes
Yes
3 Characters
no
Material unit of measure. This column only applies to LineTypes that equal "M" for Material.

MatlGroup
tinyint
Yes
Yes
###
yes
Material Group is used to qualify the material on this transaction.Pulled from HQCO based on the current MS Co#. This column only applies to LineTypes that equal "M" for Material.

Material
bMatl
Yes
No
20 Characters
no
Material sold on this transaction. This column only applies to LineTypes that equal "M" for Material.

MatlUnits
bUnits
Yes
No
##########.###
no
Units of material sold on this transaction. This column only applies to LineTypes that equal "M" for Material.

UnitPrice
bUnitCost
Yes
Yes
##########.#####
no
Price per unit of material sold.This column only applies to LineTypes that equal "M" for Material.

ECM
bECM
Yes
Yes
1 Character
no
Qualifies the unit price. This column only applies to LineTypes that equal "M" for Material.  "E" =per each  "C" = per hundred  "M" = per thousand.

Notes
bNotes
Yes
No
Text
no
Note column

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

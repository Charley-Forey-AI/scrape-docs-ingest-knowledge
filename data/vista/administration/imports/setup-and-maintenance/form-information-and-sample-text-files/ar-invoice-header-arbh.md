---
title: "AR Invoice Header (ARBH) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/ar-invoice-header-arbh"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/ar-invoice-header-arbh"
---

#  AR Invoice Header (ARBH)

[AR Invoice Sample Text File](/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/ar-invoice---sample-text-file)

AR Invoice Header - Table bARBH

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
Yes
No
MM/YY
yes
Can use the Actual date to derive the Month of the transaction.

BatchId
bBatchID
No
No
##########
yes
Viewpoint Import will create next BatchId.

BatchSeq
int
No
No
##########
yes
Viewpoint Import will always generate the next Batch Sequence.

TransType
char
No
Yes
1 Character
yes
Viewpoint Import Default will always set this value to "A" for additions.

Source
bSource
No
Yes
10 Characters
yes
Viewpoint Import Default will always set this value to "AR Invoice".

ARTransType
char
No
Yes
1 Character
yes
Viewpoint Import Default will always set this value to "I" for Invoice.

CustGroup
char
Yes
No
1 Character
yes
Customer Group used to qualify the customer number.Pulled from bHQCO based on AR Co#.

Customer
tinyint
Yes
No
###
yes
Unique number identifying this customer.

RecType
tinyint
Yes
Yes
###
yes
Receivable types define various GL accounts that will automatically be updated when transactions are posted in AR.  deductions and liabilities.

JCCo
bCompany
Yes
Yes
###
no
Job Cost company to use for contract information, and to which this transaction will be updated.

Contract
bContract
Yes
No
10 Characters
no
Contract to which this invoice is being applied.

CustRef
char
Yes
No
20 Characters
no
Customer reference for this invoice.

Invoice
char
Yes
Yes
10 Characters
yes
Invoice number.

Description
bDesc
Yes
No
30 Characters
no
Description of this invoice.

PayTerms
bLocalCode
Yes
Yes
10 Characters
no
Viewpoint Import Default will always set this value to the pay term define for the customer.

TransDate
bDate
Yes
No
MM/DD/YY
yes
Invoice date of this invoice.

DueDate
bDate
Yes
Yes
MM/DD/YY
yes
Due date of this invoice.

DiscDate
bDate
Yes
Yes
MM/DD/YY
no
Discount date of this invoice.

ReasonCode
bState
Yes
Yes
2 Characters
no
Reason code (from HQ Reason Codes) that identifies why this invoice is being entered.

Notes
bNote
Yes
No
Text column
no
Note column

AppliedMth
bMonth
No
Yes
MM/YY
no
Not used for importing invoices.

AppliedTrans
bTrans
No
Yes
##########
no
Not used for importing invoices.

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

---
title: "AR Customers | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/ar-customers"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/ar-customers"
---

#  AR Customers

[ AR Customers - Sample Text File](/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/ar-customers---sample-text-file)

Table 1. AR Customers - bARCMColumn NameTypeImportableDefault AvailableLength & ScaleRequiredComments
CustGroup
bGroup
Yes
Y
1-255
Yes

Customer
bCustomer
Yes
N
integer
Yes

Name
varchar
Yes
N
30
Yes

SortName
bSortName
Yes
N
15
Yes

TempYN
bYN
Yes
Y
1
Yes

Phone
bPhone
Yes
N
20
No

Fax
bPhone
Yes
N
20
No

EMail
varchar
Yes
N
60
No

URL
varchar
Yes
N
60
No

Contact
varchar
Yes
N
30
No

ContactExt
varchar
Yes
N
10
No

Address
varchar
Yes
N
60
No

City
varchar
Yes
N
30
No

State
bState
Yes
N
2
No

Zip
bZip
Yes
N
12
No

Country
Char
Yes
N
2
No

Address2
varchar
Yes
N
60
No

BillAddress
varchar
Yes
N
60
No

BillCity
varchar
Yes
N
30
No

BillState
bState
Yes
N
2
No

BillZip
bZip
Yes
N
12
No

BillAddress2
varchar
Yes
N
60
No

Status
char
Yes
Y
1
Yes

RecType
tinyint
Yes
Y
1-255
No

PayTerms
bPayTerms
Yes
N
10
No

TaxGroup
bGroup
Yes
Y
tinyint
No

TaxCode
bTaxCode
Yes
N
10
No

CreditLimit
bDollar
Yes
Y
numeric
Yes

SelPurge
bYN
Yes
Y
1
Yes

StmntPrint
bYN
Yes
Y
1
Yes

StmtType
char
Yes
Y
1
Yes

FCType
char
Yes
Y
1
Yes

FCPct
bPct
Yes
Y
numeric
Yes

MarkupDiscPct
bRate
Yes
Y
numeric
Yes

DateOpened
bDate
Yes
Y

No

MiscDistCode
char
Yes
N
10
No

Notes
bNotes
Yes
N
text
No

PriceTemplate
smallint
Yes
N
smallint
No

DiscTemplate
smallint
Yes
N
smallint
No

HaulTaxOpt
tinyint
Yes
Y
tinyint
Yes

InvLvl
tinyint
Yes
Y
tinyint
Yes

BillFreq
bFreq
Yes
N
10
No

MiscOnInv
bYN
Yes
Y
1
Yes

MiscOnPay
bYN
Yes
Y
1
Yes

PrintLvl
tinyint
Yes
Y
tinyint
Yes

SubtotalLvl
tinyint
Yes
Y
tinyint
Yes

SepHaul
bYN
Yes
Y
1
Yes

ExclContFromFC
bYN
Yes
Y
1
Yes

UniqueAttchID
uniqueidentifier
No
N

No

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

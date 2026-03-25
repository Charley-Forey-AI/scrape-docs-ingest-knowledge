---
title: "AP Vendors | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/ap-vendors"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/ap-vendors"
---

#  AP Vendors

[AP Vendors
 Sample Text File](/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/ap-vendors---sample-text-file)

AP Vendors import - bAPVM

Columns that are typically used for importing are in yellow

Column Name
Type
Importable
Default Available
Length & Scale
Required
Comments

VendorGroup
bGroup
Yes
Y
1-255
Yes

Vendor
bVendor
Yes
N
integer
Yes

SortName
bSortName
Yes
Y
15
Yes

Name
varchar
Yes
N
60
No

Type
char
Yes
Y
1
Yes

TempYN
bYN
Yes
Y
1
Yes

Contact
varchar
Yes
N
30
No

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
30
No

URL
varchar
Yes
N
60
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

POAddress
varchar
Yes
N
60
No

POCity
varchar
Yes
N
30
No

POState
bState
Yes
N
2
No

POZip
bZip
Yes
N
12
No

POAddress2
varchar
Yes
N
60
No

Purge
bYN
Yes
Y
1
Yes

CustGroup
bGroup
Yes
Y
1-255
No

Customer
bCustomer
Yes
N
integer
No

TaxGroup
bGroup
Yes
Y
1-255
No

TaxCode
bTaxCode
Yes
N
10
No

PayTerms
bPayTerms
Yes
N
10
No

GLCo
bCompany
Yes
Y
1-255
Yes

GLAcct
bGLAcct
Yes
N
20
No

V1099YN
bYN
Yes
Y
1
Yes

V1099Type
varchar
Yes
Y
10
No

V1099Box
tinyint
Yes
Y
1-255
No

TaxId
varchar
Yes
N
12
No

Prop
varchar
Yes
N
30
No

ActiveYN
bYN
Yes
Y
1
Yes

EFT
char
Yes
Y
1
Yes

RoutingId
varchar
Yes
N
10
No

BankAcct
varchar
Yes
N
20
No

AcctType
varchar
Yes
Y
1
No

LastInvDate
bDate
Yes
N

No

AuditYN
bYN
Yes
Y
1
Yes

Notes
bNotes
Yes
N
text
No

AddnlInfo
varchar
Yes
N
60
No

AddendaTypeId
tinyint
Yes
N
1-255
No

Reviewer
varchar
Yes
N
3
No

SeparatePayInvYN
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

OverrideMinAmtYN
bYN
Yes
Y
1
Yes

MasterVendor
bVendor
Yes
N
integer
No

APRefUnqOvr
tinyint
Yes
Y
1-255
Yes

ICFirstName
varchar
Yes
N
28
No

ICMInitial
varchar
Yes
N
1
No

ICLastName
varchar
Yes
N
40
No

ICSocSecNbr
varchar
Yes
N
9
No

ICStreetNbr
varchar
Yes
N
5
No

ICStreetName
varchar
Yes
N
40
No

ICAptNbr
varchar
Yes
N
4
No

ICCity
varchar
Yes
N
40
No

ICState
bState
Yes
N
2
No

ICZip
bZip
Yes
N
12
No

ICLastRptDate
bDate
Yes
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

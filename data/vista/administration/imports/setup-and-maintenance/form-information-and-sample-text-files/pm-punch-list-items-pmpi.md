---
title: "PM Punch List Items (PMPI) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/pm-punch-list-items-pmpi"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/pm-punch-list-items-pmpi"
---

# PM Punch List Items (PMPI)

[PM Punch List Items Sample Text File](/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/pm-punch-list-items---sample-text-file)

PM Punch List Items - PMPI

 Columns that are typically used for importing are in yellow

Column Name
Type
Importable
Default Available
Length & Scale
Required
Comments

PMCo
bCompany
Yes
Y
1-255
Yes

Project
bJob
Yes
N
10
Yes

PunchList
bDocument
Yes
N
10
Yes

Item
smallint
Yes
N
smallint
Yes

Description
char
Yes
N
255
No

VendorGroup
bGroup
Yes
Y
1-255
No

ResponsibleFirm
bFirm
Yes
N
integer
No

Location
varchar
Yes
N
10
No

DueDate
bDate
Yes
N

No

FinDate
bDate
Yes
N

No

BillableYN
bYN
Yes
Y
1
Yes

BillableFirm
bFirm
Yes
N
integer
No

Issue
bIssue
Yes
N
integer
No

Notes
bNotes
Yes
N
text
No

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

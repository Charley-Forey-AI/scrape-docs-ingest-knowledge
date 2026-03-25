---
title: "IN Material Order Header (INMB) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/in-material-order-header-inmb"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/in-material-order-header-inmb"
---

#  IN Material Order Header (INMB)

[IN Material Order Sample Text File](/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/in-materials---sample-text-file)

IN Material Order - bINMB

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
Y
Y

Yes

Mth
bMonth
Y
Y

Yes

BatchId
bBatchID
N
N

Yes

BatchSeq
int
N
N

Yes

BatchTransType
char
Y
Y

Yes

MO
varchar
Y
Y

Yes

Description
bDesc
Y
N

No

JCCo
bCompany
Y
Y

Yes

Job
bJob
Y
Y

Yes

OrderDate
bDate
Y
N

No

OrderedBy
varchar
Y
N

No

Status
tinyint
Y
Y

Yes

Notes
bNotes
Y
N

No

OldDesc
bDesc
Y
N

No

OldJCCo
bCompany
Y
N

No

OldJob
bJob
Y
N

No

OldOrderDate
bDate
Y
N

No

OldOrderedBy
varchar
Y
N

No

OldStatus
tinyint
Y
N

No

UniqueAttchID
uniqueidentifier
N
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

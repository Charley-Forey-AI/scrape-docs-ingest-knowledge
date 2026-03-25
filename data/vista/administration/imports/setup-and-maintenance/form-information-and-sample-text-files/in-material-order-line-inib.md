---
title: "IN Material Order Line (INIB) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/in-material-order-line-inib"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/in-material-order-line-inib"
---

#  IN Material Order Line (INIB)

[IN Material Order Sample Text File](/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/in-materials---sample-text-file)

IN Material Order - bINIB

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

MOItem
bItem
Y
Y

Yes

BatchTransType
char
Y
Y

Yes

Loc
bLoc
Y
N

Yes

MatlGroup
bGroup
Y
Y

Yes

Material
bMatl
Y
N

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

PhaseGroup
bGroup
Y
Y

Yes

Phase
bPhase
Y
Y

Yes

JCCType
bJCCType
Y
Y

Yes

GLCo
bCompany
Y
Y

Yes

GLAcct
bGLAcct
Y
Y

Yes

ReqDate
bDate
Y
N

No

UM
char
Y
Y

Yes

OrderedUnits
bUnits
Y
N

Yes

UnitPrice
bUnitCost
Y
Y

Yes

ECM
bECM
Y
Y

Yes

TotalPrice
bDollar
Y
Y

Yes

TaxGroup
bGroup
Y
Y

No

TaxCode
bTaxCode
Y
Y

No

TaxAmt
bDollar
Y
Y

Yes

RemainUnits
bUnits
Y
Y

Yes

Notes
bNotes
Y
N

No

OldLoc
bLoc
N
N

No

OldMatlGroup
bGroup
N
N

No

OldMaterial
bMatl
N
N

No

OldDesc
bDesc
N
N

No

OldJCCo
bCompany
N
N

No

OldJob
bJob
N
N

No

OldPhaseGroup
bGroup
N
N

No

OldPhase
bPhase
N
N

No

OldJCCType
bJCCType
N
N

No

OldGLCo
bCompany
N
N

No

OldGLAcct
bGLAcct
N
N

No

OldReqDate
bDate
N
N

No

OldUM
char
N
N

No

OldOrderedUnits
bUnits
N
N

No

OldUnitPrice
bUnitCost
N
N

No

OldECM
bECM
N
N

No

OldTotalPrice
bDollar
N
N

No

OldTaxGroup
bGroup
N
N

No

OldTaxCode
bTaxCode
N
N

No

OldTaxAmt
bDollar
N
N

No

OldRemainUnits
bUnits
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

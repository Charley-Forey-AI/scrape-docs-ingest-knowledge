---
title: "JC Jobs (JCJM) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/jc-jobs-jcjm"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/jc-jobs-jcjm"
---

#  JC Jobs (JCJM)

[JC Jobs Sample
 Text File](/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/jc-jobs---sample-text-file)

JC Jobs - JCJM

 Columns that are typically used for importing are in yellow

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
1-255
Yes

Job
bJob
Yes
N
10
Yes

Description
bDesc
Yes
N
30
No

Contract
bContract
Yes
Y
10
Yes

JobStatus
tinyint
Yes
Y
1-255
Yes

BidNumber
varchar
Yes
N
10
No

LockPhases
bYN
Yes
Y
1
Yes

ProjectMgr
int
Yes
N
integer
No

JobPhone
bPhone
Yes
N
20
No

JobFax
bPhone
Yes
N
20
No

MailAddress
varchar
Yes
N
60
No

MailCity
varchar
Yes
N
30
No

MailState
bState
Yes
N
2
No

MailZip
bZip
Yes
N
12
No

MailAddress2
varchar
Yes
N
60
No

ShipAddress
varchar
Yes
Y
60
No

ShipCity
varchar
Yes
Y
30
No

ShipState
bState
Yes
Y
2
No

ShipZip
bZip
Yes
Y
12
No

ShipAddress2
varchar
Yes
Y
60
No

LiabTemplate
smallint
Yes
N
smallint
No

TaxGroup
bGroup
Yes
Y
1-255
Yes

TaxCode
bTaxCode
Yes
N
10
No

InsTemplate
smallint
Yes
N
smallint
No

MarkUpDiscRate
bRate
Yes
Y
numeric
Yes

PRLocalCode
bLocalCode
Yes
N
10
No

PRStateCode
bState
Yes
Y
2
No

Certified
bYN
Yes
Y
1
Yes

OverTimeFlag
char
Yes
N
1
No

EEORegion
char
Yes
N
8
No

SMSACode
char
Yes
N
10
No

CraftTemplate
smallint
Yes
N
smallint
No

ProjMinPct
bPct
Yes
Y
numeric
Yes

Reviewer
varchar
Yes
N
3
No

Notes
bNotes
Yes
N
text
No

ComGroup
varchar
Yes
N
10
No

SLCompGroup
varchar
Yes
N
10
No

POCompGroup
varchar
Yes
N
10
No

VendorGroup
bGroup
Yes
N
1-255
No

ArchEngFirm
bFirm
Yes
N
integer
No

OTSched
tinyint
Yes
N
1-255
No

PriceTemplate
smallint
Yes
N
smallint
No

HaulTaxOpt
tinyint
Yes
Y
1-255
Yes

GeoCode
varchar
Yes
N
10
No

BaseTaxOn
varchar
Yes
Y
1
Yes

UpdatePlugs
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

ContactCode
bEmployee
Yes
N
integer
No

ClosePurgeFlag
bYN
Yes
N
1
No

OurFirm
bFirm
Yes
N
integer
No

AutoAddItemYN
bYN
Yes
N
1
Yes

OverProjNotes
varchar
Yes
N
8000
No

WghtAvgOT
bYN
Yes
Y
1
Yes

HrsPerManDay
bUnits
Yes
Y
numeric
Yes

AutoGenSubNo
varchar
Yes
N
1
Yes

SecurityGroup
smallint
Yes
Y
smallint
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

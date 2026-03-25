---
title: "PM Submittal (PMSM) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/pm-submittal-pmsm"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/pm-submittal-pmsm"
---

#  PM Submittal (PMSM)

[PM Submittal Sample Text File](/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/pm-submittal---sample-text-file)

PM Submittal - bPMSM

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
Y
Y

Yes

Project
bJob
Y
N

Yes

Submittal
bDocument
Y
Y

Yes

SubmittalType
bDocType
Y
N

Yes

Rev
tinyint
Y
N

Yes

Description
bItemDesc
Y
Y

No

PhaseGroup
bGroup
Y
Y

No

Phase
bPhase
Y
Y

No

Issue
bIssue
Y
Y

No

Status
bStatus
Y
Y

No

VendorGroup
bGroup
Y
Y

No

ResponsibleFirm
bFirm
Y
Y

No

ResponsiblePerson
bEmployee
Y
Y

No

SubFirm
bFirm
Y
Y

No

SubContact
bEmployee
Y
Y

No

ArchEngFirm
bFirm
Y
Y

No

ArchEngContact
bEmployee
Y
Y

No

DateReqd
bDate
Y
N

No

DateRecd
bDate
Y
N

No

ToArchEng
bDate
Y
N

No

DueBackArch
bDate
Y
N

No

RecdBackArch
bDate
Y
N

No

DateRetd
bDate
Y
N

No

ActivityDate
bDate
Y
Y

No

CopiesRecd
tinyint
Y
N

No

CopiesSent
tinyint
Y
N

No

Notes
bNotes
Y
N

No

CopiesReqd
tinyint
Y
Y

No

CopiesRecdArch
tinyint
Y
N

No

CopiesSentArch
tinyint
Y
N

No

UniqueAttchID
uniqueidentifier
N
N

No

SpecNumber
varchar
Y
Y

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

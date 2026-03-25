---
title: "PR Employees (PREH) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/pr-employees-preh"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/pr-employees-preh"
---

#  PR Employees (PREH)

[PR
 Employees Sample Text File](/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/pr-employees---sample-text-file)

Table 1. PR Employees - PREHColumn NameTypeImportableDefault AvailableLength & ScaleRequiredComments
PRCo
bCompany
Yes
Y
1-255
Yes

Employee
bEmployee
Yes
N
integer
Yes

LastName
varchar
Yes
N
30
Yes

FirstName
varchar
Yes
N
30
No

MidName
varchar
Yes
N
15
No

SortName
bSortName
Yes
Y
15
Yes

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

Address2
varchar
Yes
N
60
No

Phone
bPhone
Yes
N
20
No

SSN
char
Yes
N
11
Yes

Race
char
Yes
N
2
Yes

Sex
char
Yes
Y
1
Yes

BirthDate
smalldatetime
Yes
N

No

HireDate
bDate
Yes
N

No

TermDate
bDate
Yes
N

No

PRGroup
bGroup
Yes
N
1-255
Yes

PRDept
bDept
Yes
N
10
Yes

Craft
bCraft
Yes
N
10
No

Class
bClass
Yes
N
10
No

InsCode
bInsCode
Yes
N
10
Yes

TaxState
bState
Yes
N
2
No

UnempState
bState
Yes
Y
2
Yes

InsState
bState
Yes
Y
2
Yes

LocalCode
bLocalCode
Yes
N
10
No

GLCo
bCompany
Yes
Y
1-255
No

UseState
bYN
Yes
Y
1
Yes

UseLocal
bYN
Yes
Y
1
Yes

UseIns
bYN
Yes
Y
1
Yes

JCCo
bCompany
Yes
N
1-255
No

Job
bJob
Yes
N
10
No

Crew
varchar
Yes
N
10
No

LastUpdated
bDate
Yes
Y

No

EarnCode
bEDLCode
Yes
N
smallint
Yes

HrlyRate
bUnitCost
Yes
Y
numeric
Yes

SalaryAmt
bDollar
Yes
Y
numeric
Yes

OTOpt
char
Yes
Y
1
Yes

OTSched
tinyint
Yes
N
1-255
No

JCFixedRate
bUnitCost
Yes
Y
numeric
Yes

EMFixedRate
bUnitCost
Yes
Y
numeric
Yes

YTDSUI
bDollar
Yes
Y
numeric
Yes

OccupCat
varchar
Yes
N
10
No

CatStatus
char
Yes
N
1
No

DirDeposit
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
char
Yes
N
1
No

ActiveYN
bYN
Yes
Y
1
Yes

PensionYN
bYN
Yes
Y
1
Yes

PostToAll
bYN
Yes
Y
1
Yes

CertYN
bYN
Yes
Y
1
Yes

ChkSort
varchar
Yes
N
10
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

UniqueAttchID
uniqueidentifier
No
N
uniqueidentifier
No

Email
varchar
Yes
N
50
No

DefaultPaySeq
bYN
Yes
Y
1
Yes

DDPaySeq
tinyint
Yes
N
1-255
No

Suffix
varchar
Yes
N
4
No

TradeSeq
tinyint
Yes
N
1-255
No

CSLimit
bPct
Yes
N
numeric
No

CSGarnGroup
bGroup
Yes
N
1-255
No

CSAllocMethod
char
Yes
Y
1
Yes

Shift
tinyint
Yes
N
1-255
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

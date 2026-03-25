---
title: "GL Journal Entries (GLDB) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/gl-journal-entries-gldb"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/gl-journal-entries-gldb"
---

#  GL Journal Entries (GLDB)

GL Journal Entries - Table bGLDB

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
Yes
Yes
### - 0 to 999
yes
General Ledger number.Must exist in HQCO.

Mth
bMonth
Yes
No
MM/YY
yes
Can use the Actual date to derive the Month of the Journal entry.

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

BatchTransType
char
No
No
1 Character
no
Viewpoint Import will always set this value to "A" for additions.

ActDate
bDate
Yes
Yes
MM/DD/YY
yes
Date of the journal entries.

InterCo
bCompany
Yes
Yes
### - 0 to 999
yes
Company that will be updated with this journal entry. For intercompany journal entries, this company must be the same as the posting company for at least one entry. Offsetting entries must be posted to a different company.

Jrnl
bJrnl
Yes
No
2 Characters
yes
Journal (set up in Viewpoint GL Journals) to which this entry will be posted.  For intercompany journal entries, this journal must be the same in all specified companies.

GLRef
bGLRef
Yes
No
10 Characters
yes
References allow you to group related journal entries together. All entries sharing the same reference within a journal and month must balance.

Description
bTransDesc
Yes
No
60 Characters
yes
Description of the journal entry.

GLAcct
bGLAcct
Yes
No
20 Characters
yes
GL account (set up in GL Chart of Accounts) that this entry will be posted.

Amount
bDollar
Yes
No
##########.##
yes
Amount of this entry. Positive values will be recorded as debits and negative values as credits.

Source
bSource
No
No
10 Characters
no
Viewpoint Import will always set this value to 'GL Jrnl'.

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

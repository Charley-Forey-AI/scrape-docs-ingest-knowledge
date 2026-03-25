---
title: "JC Contracts (JCCM) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/jc-contracts-jccm"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/jc-contracts-jccm"
---

#  JC Contracts (JCCM)

[JC Contracts
 Sample Text File](/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/jc-contracts---sample-text-file)

JC Contracts - JCCM

* Columns are not necessarily in this order

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
integer 0-255
No
JC Company number

Contract
bContract
Yes
N
10 characters
Yes
Contract code

Description
bDesc
Yes
N
30 characters
No
Contract description

Department
bDept
Yes
N
10 characters
Yes
Department used for default item department

ContractStatus
tinyint
Yes
Y
integer 0-255
Yes
0=pending, 1=open, 2=soft close, 3=hard close

OriginalDays
smallint
Yes
Y
integer -+ 32767
Yes
Targeted number of days contract will take to complete.

CurrentDays
smallint
Yes
Y
integer -+ 32767
Yes
Days since start of contract.

StartMonth
bMonth
Yes
Y
valid month
Yes
Starting month for this contract (used for storing original estimates)

MonthClosed
bMonth
Yes
N
valid month
No
Month the contract was closed (can be projected or actual)

ProjCloseDate
bDate
Yes
N
valid date
No
Target completion date for this contract.

ActualCloseDate
bDate
Yes
N
valid date
No
No value needed for imports - used by JC Contract Close.

CustGroup
bGroup
Yes
Y
integer 0-255
No
Customer Group used to qualify Customer.Pulled from bHQCO based on JC Co#.Not editable.

Customer
bCustomer
Yes
N
integer
No
AR customer to whom billing invoices for this contract will be posted.

PayTerms
bPayTerms
Yes
N
10 characters
No
Payment terms used as default for AR Transaction Entry (blank if using terms from AR Customers)

TaxInterface
bYN
Yes
Y
1 char (Y or N)
Yes
Y=include in revenue interfaced to Job Cost, N=not interfaced to JC.

TaxGroup
bGroup
Yes
Y
integer 0-255
No
Tax Group used to qualify Tax code.Pulled from bHQCO based on JC Co#.Not editable.

TaxCode
bTaxCode
Yes
N
10 characters
No
Tax code that will be used as the default when posting to this contract in Accounts Receivable (AR) or Job Billing (JB)

RetainagePCT
bPct
Yes
Y
num; 5,4
Yes
Retainage percent (in decimal form, not %)

DefaultBillType
bBillType
Yes
Y
1 character
Yes
(P)rogress, (T) & M, (B)oth, (N)one

Notes
bNotes
Yes
N
2^31 characters
No
Notes for this contract (currently limited to 60 characters)

SIRegion
varchar
Yes
N
6 characters
No
Location or region of the standard item code.

SIMetric
bYN
Yes
Y
1 char (Y or N)
No
Y=use metric

BillDayOfMth
varchar
Yes
N
10 characters
No
Day(s) of the month billings are to be processed for this contract in JB.

JBTemplate
varchar
Yes
Y
10 characters
No
T&M template used by Job Billing to determine accumulated job cost detail.

SecurityGroup
smallint
Yes
Y
integer -+ 32767
No
Defaults to security setting for bContract datatype if In Use flag set for JCCM.

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

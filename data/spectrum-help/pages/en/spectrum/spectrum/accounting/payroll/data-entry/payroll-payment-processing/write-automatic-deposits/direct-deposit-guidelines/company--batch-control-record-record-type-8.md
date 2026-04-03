---
title: "Company / Batch Control Record (Record Type 8) | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/direct-deposit-guidelines/company--batch-control-record-record-type-8"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/direct-deposit-guidelines/company--batch-control-record-record-type-8"
---

# Company / Batch Control Record (Record Type 8)

The Company/Batch Control Record contains the counts, hash totals, and total dollar controls for the preceding detail entries within the indicated batch.
Because prenotification records are non-dollar specific, they are excluded from the total dollar control amounts. Prenotifications are hashed and are included in the entry/addenda counts; Batch Header and Batch Control Records are not included.
Col
Position
Size
Fir
Field Name
Contents

1
01-01
 1
M
RECORD TYPE
'8'

2
02-04
 3
M
SERVICE CLASS CODE
'200'

3
05-10
 6
M
ENTRY/ADDENDA COUNT
Numeric

4
11-20
10
M
ENTRY HASH
Numeric

5
21-32
12
M
TOTAL DEBIT ENTRY DOLLAR AMT
$$$$$$$$$$cc

6
33-44
12
M
TOTAL CREDIT ENTRY DOLLAR AMT
$$$$$$$$$$cc

7
45-54
10
R
COMPANY ID
Alphanumeric

8
55-73
19
O
MESSAGE AUTHENTICATION CODE
Alphanumeric

9
74-79
 6
N/A
RESERVED (LEAVE BLANK)
Numeric

10
80-87
 8
M
ORIGINATING DFI
TTTTAAAA

11
88-94
 7
R
BATCH NUMBER
Numeric

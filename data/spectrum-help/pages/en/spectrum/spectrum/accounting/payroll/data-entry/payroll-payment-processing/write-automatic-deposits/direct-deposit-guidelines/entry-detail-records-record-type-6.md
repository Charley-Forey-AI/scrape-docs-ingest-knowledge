---
title: "Entry Detail Records (Record Type 6) | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/direct-deposit-guidelines/entry-detail-records-record-type-6"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/direct-deposit-guidelines/entry-detail-records-record-type-6"
---

# Entry Detail Records (Record Type 6)

 Entry Detail Records contain the information sufficient to
 relate the entry to the individual; for example, individual account number; identification
 number; name and the debit or credit amount as indicated by the transaction code.
The information in the Company/Batch Header Record must be incorporated with the Entry
 Detail Records to describe fully that entry and all participants to the transaction.
Prenotifications are non-dollar entries, identical to the basic entry format, but with appropriate transaction codes and zeros in the amount field. Pre-notifications can be batched with other dollar entries or batched separately.
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
'6'

2
02-03
 2
M
TRANSACTION CODE
Numeric

3
04-11
 8
M
RECEIVING DFI IDENTIFICATION
TTTTAAAA

4
12-12
 1
M
RDFI TRANSIT ROUTING CK DIGIT
Numeric

5
13-29
17
R
RDFI ACCOUNT NUMBER
Alphanumeric

6
30-39
10
M
TRANSACTION AMOUNT
$$$$$$$$cc

7
40-54
15
O
INDIVIDUAL ID
Alphanumeric

8
55-76
22
R
INDIVIDUAL NAME
Alphanumeric

9
77-78
 2
O
DISCRETIONARY DATA
Alphanumeric

10
79-79
 1
M
ADDENDA INDICATOR
Numeric

11
80-94
15
M
TRACE NUMBER
Numeric

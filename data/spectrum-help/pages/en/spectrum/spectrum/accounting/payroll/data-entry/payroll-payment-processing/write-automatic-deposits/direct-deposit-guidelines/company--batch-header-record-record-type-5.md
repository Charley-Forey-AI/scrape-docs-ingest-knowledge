---
title: "Company / Batch Header Record (Record Type 5) | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/direct-deposit-guidelines/company--batch-header-record-record-type-5"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/direct-deposit-guidelines/company--batch-header-record-record-type-5"
---

# Company / Batch Header Record (Record Type 5)

The Company/Batch Header Record identifies the company and
 briefly describes the prearranged paperless debit or credit; for example; "REG SALARY"
 indicates the reason for the transaction originated by the company.
The Company/Batch Header Record contains the Transit Routing/ABA number of the Originating
 Depository Financial Institution (ODFI) for settlement, routing of returns, and other
 control purposes. In addition, the Company/Batch Header Record indicates the intended
 effective date of all transactions within the batch. The information contained in the
 Company/Batch Header Record applies uniformly to all subsequent Entry Detail Records in the
 batch.
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
'5'

2
02-04
 3
M
SERVICE CLASS CODE
Numeric

3
05-20
16
M
COMPANY NAME
Alphanumeric

4
21-40
20
O
COMPANY DISCRETIONARY DATA
Alphanumeric

5
41-50
10
R
COMPANY ID
Alphanumeric

6
51-53
 3
M
STANDARD ENTRY CLASS CODE
'PPD'

7
54-63
10
M
COMPANY ENTRY DESCRIPTION
Alphanumeric

8
64-69
 6
O
COMPANY DESCRIPTIVE DATA
Alphanumeric

9
70-75
 6
R
EFFECTIVE ENTRY DATE
YYMMDD

10
76-78
 3
N/A
RESERVED (LEAVE BLANK)
Numeric

11
79-79
 1
M
ORIGINATOR STATUS CODE
'1'

12
80-87
 8
M
ORIGINATOR DFI
TTTTAAAA

13
88-94
 7
R
BATCH NUMBER
Numeric

---
title: "File Header Record (Record Type 1) | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/direct-deposit-guidelines/file-header-record-record-type-1"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/direct-deposit-guidelines/file-header-record-record-type-1"
---

# File Header Record (Record Type 1)

The File Header Record designates physical file
 characteristics and identifies the immediate origin (Sending Point or Company) and destination
 (Receiving Point or Blank) of the entries contained with the file or within the transmitted
 batched area.
In addition, this record includes date, time and file identification fields, which can then
 be used to uniquely identify the file.
Batch #1

Company/Batch Header Record (Record Type 5)

Entry Detail Records (Record Type 6)

Company/Batch Control Record (Record Type 8)

Batch #n

Company/Batch Header Record (Record Type 5)

Entry Detail Records (Record Type 6)

Company/Batch Control Record (Record Type 8)

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
'1'

2
02-03
 2
R
PRIORITY CODE
'01'

3
04-13
10
M
IMMEDIATE DESTINATION
bTTTTAAAAC

4
14-23
10
M
IMMEDIATE ORIGIN
bTTTTAAAAC

5
24-29
 6
M
TRANSMISSION DATE
YYMMDD

6
30-33
 4
O
TRANSMISSION TIME
HHMM

7
34-34
 1
M
FILE ID MODIFIER
'A'

8
35-37
 3
M
RECORD SIZE
'094'

9
38-39
 2
M
BLOCKING FACTOR
'10'

10
40-40
 1
M
FORMAT CODE
'1'

11
41-63
23
M
IMMEDIATE DESTINATION NAME
Alphanumeric

12
64-86
23
M
IMMEDIATE ORIGIN NAME
Alphanumeric

13
87-94
 8
O
REFERENCE CODE
Alphanumeric

*Field Inclusion Requirement (Mandatory, Required or Optional): Please refer to the end of this chapter for complete descriptions.

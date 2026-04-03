---
title: "File Control Record (Record Type 9) | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/direct-deposit-guidelines/file-control-record-record-type-9"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/direct-deposit-guidelines/file-control-record-record-type-9"
---

# File Control Record (Record Type 9)

The File Control Record contains the dollar, entry and hash
 total accumulations from the Company/Batch Control Records in the file.
This record also contains counts of the number of blocks and the number of batches within
 the file.
The majority of the fields in these records are calculated fields or can be filled by information already available in the Employees screen. The fields which must be entered in Spectrum in order to begin direct deposit processing are as follows:
The Payroll Installation screen includes a field for automatic deposit liability General Ledger code. This account will be credited during the payroll update in the amount of the automatic deposit. In some versions, there is also a prompt for pausing after the computer checks are generated, to change paper for your direct deposit stubs. The Print Checks function will print void checks for those employees enrolled in the direct deposit program.
Click the Auto Deposit button in the Employees screen to display the Auto Deposit window. Enter the account code, type of account, and aba number. These are required input fields for employees participating in the direct deposit program.
The remaining fields in creating the PPD file not available from existing information will need to be entered on the starting screen for Write Auto Deposits. Two formats may be created through Write Automatic Deposits, the NACHA format and the ACH Manager format. The NACHA format will create one file titled "PAYROLL," which will contain the File Header Record, Batch Header Record, Entry Detail Records, Batch Control Record and the File Control Record. The ACH Manager format will create multiple files designed to be merged into external ACH software (generally provided by your bank).
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
RECORD TYPE CODE
'9'

2
02-07
 6
M
BATCH COUNT
Numeric

3
08-13
 6
M
BLOCK COUNT
Numeric

4
14-21
 8
M
ENTRY/ADDENDA COUNT
Numeric

5
22-31
10
M
ENTRY HASH
Numeric

6
32-43
12
M
TOTAL DEBIT ENTRY DOLLAR AMT
$$$$$$$$$$cc

7
44-55
12
M
TOTAL CREDIT ENTRY DOLLAR AMT
$$$$$$$$$$cc

8
56-94
39
N/A
RESERVED (LEAVE BLANK)
Blank

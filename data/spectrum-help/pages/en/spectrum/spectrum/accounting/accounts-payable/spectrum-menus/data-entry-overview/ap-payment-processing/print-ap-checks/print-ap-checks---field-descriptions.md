---
title: "Print A/P Checks - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/print-ap-checks/print-ap-checks---field-descriptions"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/print-ap-checks/print-ap-checks---field-descriptions"
---

# Print A/P Checks - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields
Descriptions

Include file copy?
Select this checkbox to run a copy of the check for historical purposes.

From/to vendor
The first time a group of checks is run, press Enter to
 use the defaults for these fields. Checks are printed for all vendors
 appearing on the Pre-Payment Register. If you are reprinting checks, a
 starting and ending vendor code must be entered.

Check number
The number of the next check, as recorded on the Accounts Payable
 Installation screen, is displayed.
Note: In order to prevent Accounts Payable and Payroll Check
 Prints from printing at the same time if they are using the same check
 stock, the software will first verify if the starting default check number
 has been changed by another check print. If it has, you will be notified
 before printing.
Bank account
If the Cash Management module is installed, the bank
 account code entered during the Pre-Payment Register
 print displays. To use a different account, exit this screen
 then reprint the Pre-Payment Register using another bank account code.

G/L cash account
The cash account entered during the Pre-Payment Register
 print displays. To use a different account, exit this screen
 then reprint the Pre-Payment Register using another G/L account. If the Cash
 Management module is installed, the G/L cash account associated with the
 bank account is shown.

Check date
The check date defaults, and you must have security authority to make changes in this field.
If a different date appears on these checks, exit this screen then change the
 processing date using either the Processing Date
 Change or A/P Processing Date Change
 screen.

Processing group
Enter a batch code to identify the group of subcontractor invoices being entered at this time. The default is the operator's logon ID.

Spoiled checks?
Select this option to manually enter check numbers for checks spoiled during the printing process. For example, the numbers of any check stock used for the alignment mask should be entered here.
It is not necessary to enter the numbers of checks that are reprinted. Whenever a check reprint is run, the software automatically voids the appropriate checks; the checks should not be entered as "spoiled."
If this checkbox is selected, the Spoiled Check Entry
 window appears after the checks have printed. Use this window to record the
 check numbers for spoiled checks; for example, those that were used for
 alignment purposes, jammed in the printer, voided before printing, or
 otherwise spoiled.

Reprint options
Select Checks to print checks only, Remittance advice to print remittance advice information. This radio group is only available after the original checks have been previewed. An [About Electronic Payment Remittance Advices](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/about-electronic-payment-remittance-advices) form is also available.

Sort checks by
Select whether to sort checks by the default vendor code or vendor alpha characters.

Add-on options
If applicable, select the correct Add-on option and click Preview to review the checks and the Auto-Signature setup to find a signature location for the operator and company and to see if an AP check limit is defined. If the signature file is not found a warning message will appear and the signature will not be printed.
[Click this link for more information on the Auto Signature product.](https://trimble.deploy.heretto.com/v4/deployments/mVyHSMAo9PbkfqcxUBWF/object/c5ffac40-8ea8-11ec-9179-02420ae60f1a?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJodHRwczovL2pvcnNlay5jb20vZXpkX29yZ2FuaXphdGlvbiI6InZpZXdwb2ludCIsImh0dHBzOi8vam9yc2VrLmNvbS9lemQvb2JqZWN0X3V1aWQiOiJjNWZmYWM0MC04ZWE4LTExZWMtOTE3OS0wMjQyMGFlNjBmMWEiLCJleHAiOjE3NzUzMzMxNDcsImp0aSI6IjNlMDA1MjQyNzBjYTQzMzFhNWZhZDdkOGFmN2UwOWUxIiwiaHR0cHM6Ly9qb3JzZWsuY29tL2V6ZF9maWxlc2V0IjoiOE1GRmpJZEw3ZEZLQmJiVGwxTXMifQ.mW-Av-HyOMrq4qc8ThjMAMOOW7oiBToeVa6pliQZlg4&response-content-disposition=filename%3D%22Auto-Signature_Procedures_v1422.pdf%22)
[Click this link for more information on the MICR product.](https://trimble.deploy.heretto.com/v4/deployments/mVyHSMAo9PbkfqcxUBWF/object/c1b5f4a0-8ea8-11ec-9179-02420ae60f1a?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJodHRwczovL2pvcnNlay5jb20vZXpkX29yZ2FuaXphdGlvbiI6InZpZXdwb2ludCIsImh0dHBzOi8vam9yc2VrLmNvbS9lemQvb2JqZWN0X3V1aWQiOiJjMWI1ZjRhMC04ZWE4LTExZWMtOTE3OS0wMjQyMGFlNjBmMWEiLCJleHAiOjE3NzUzMzMxNDcsImp0aSI6IjQ5ZjhlZGMyOGMyMjRjMzNhN2ZkODE5NGQ5YTBhNjM0IiwiaHR0cHM6Ly9qb3JzZWsuY29tL2V6ZF9maWxlc2V0IjoiOE1GRmpJZEw3ZEZLQmJiVGwxTXMifQ.LbuLVu_IvFBw3VMCFKfJJszCI0Qn_wQdeVk5O7lZh40&response-content-disposition=filename%3D%22MICR_Checks_Procedures_v1423_1.pdf%22)

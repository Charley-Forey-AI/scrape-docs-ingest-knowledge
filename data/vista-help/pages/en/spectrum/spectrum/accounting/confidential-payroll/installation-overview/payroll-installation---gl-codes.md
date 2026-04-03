---
title: "Payroll Installation - G/L Codes | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/confidential-payroll/installation-overview/payroll-installation---gl-codes"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/confidential-payroll/installation-overview/payroll-installation---gl-codes"
---

# Payroll Installation - G/L Codes

Use this tab to select the default G/L code settings for
 the Payroll module. Be sure to include the G/L account numbers entered on this screen when you
 enter your chart of accounts. Enter your these G/L accounts even if you do not have the
 General Ledger module installed on your computer. These settings can be changed as needed at
 any time.
Note: The software will use the cash in bank G/L account
 code during the payroll update if the Cash Management module is not present in the main
 company, unless this account is not set up in the main company's Payroll Installation
 screen. If this is the case, the software will use the cash account specified on this tab
 for the main company.
If cost centers are being used and multi-company processing is NOT being used in this company, the Inter-company G/L account code field on this tab is replaced with a Cost center inter-posting G/L account code field.
Fields/Buttons
Descriptions

Cash in bank G/L account code
Enter the G/L account code you plan to title "cash in bank" (or similar name) in your Spectrum chart of accounts. .
When the Payroll Update is performed in a Confidential Payroll company, it will use the cash account of the confidential company if it is set up in the Chart of Accounts of the main company. If a valid G/L code is not specified in the Payroll Installation of the confidential company, then the update will use the G/L cash account specified in the main company Payroll Installation screen.

Accrued payroll G/L account code
Enter the G/L account code you plan to title "accrued payroll payable" (or similar name) in your Spectrum chart of accounts.
The software will use this G/L account code during Payroll Update if the Accrue expense to field is set to Period-end date or Work date. If accrual posting is used, this G/L account code will be credited on the period-end date of the payroll cycle, and debited in the same amount on the check date. If Work date is selected, it will post to job cost history using the work date. For G/L, it is similar to the Period-end date option: liabilities and cash outlay post to the G/L check date, and expenses post to the period ending date. However, if the work cycle goes over a month end, then the Payroll Update will split and post expenses in two postings – one on the last day of the previous month and one on the period ending date.

Automatic deposit liability G/L account code
Enter the General Ledger account code you plan to title "payroll automatic deposit payable" (or similar name) in your Spectrum chart of accounts.
The software will utilize this G/L account code during Payroll Update only if your office has designated employees participating in this program. If the automatic deposit feature is used, this G/L account code will be credited in the amount of net checks to be directly deposited to the bank on the employees' behalf.

Inter-company G/L account code
Enter the G/L account code you plan to title "inter-company receivable" (or similar name) in your Spectrum chart of accounts. The software will automatically update inter-company transactions to this G/L account code when you designate alternate company code(s) during Payroll Update. This G/L account code is the default account, unless another account code is specified in the Inter-company G/L Code portion of this screen.
This field will be skipped if the Multi-company payroll checkbox is not selected.

Inter-company G/L Account Code button
Enter the company and G/L account codes to track inter-company relationships with multiple account numbers. Entry in this field is optional and any companies listed may override the default G/L account code in the Inter-company G/L account code field.

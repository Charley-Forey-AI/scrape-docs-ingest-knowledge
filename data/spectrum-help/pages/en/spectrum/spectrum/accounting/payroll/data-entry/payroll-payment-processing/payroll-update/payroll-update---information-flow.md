---
title: "Payroll Update - Information Flow | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/payroll-update/payroll-update---information-flow"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/payroll-update/payroll-update---information-flow"
---

# Payroll Update - Information Flow

Use the information following for the flow of payroll
 update information.

- Job Cost and Equipment Control records are also updated during this process,
 and G/L entries are created. If a check number has been used more than once during
 this check cycle, a report with the check number and both employee names will print
 and the software will exit without updating. If there are no duplicate check numbers,
 the start screen for the Payroll Update will appear and
 processing can continue as usual.When Equipment Usage 'meter transactions' are
 updated, the software adjusts all usage records with a later transaction date so that
 the new transaction is included in the life-to-date 'usage' total.

- A Payroll add-on or deduction creates an invoice to which the routing hierarchy is applied.

- Hours Taken and Hours Earned totals will be stored in the Payroll Time Off Bank Log Table.

- JX pay type transactions recorded in Time Card Entry will result in unposted Job Cost transaction entries recorded in Job Cost Transaction Entry as part of this update. It is recommended that those transactions be updated using the Job Cost Transaction Report and Update, then the Job Cost G/L Detail Report and Update.

- If the Job Cost Installation  >  Properties - Set add-on G/L account from Payroll department checkbox is selected, Spectrum will automatically change the G/L accounts of add-ons based on the payroll department file when the Update is run. [Example - Payroll Update](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/example---payroll-update).The software will also verify that the resulting G/L account is valid in the chart of accounts. For multi-company entries, the department of the destination company is used and the resulting account is validated against the destination company's chart of accounts. If an invalid or blank account exists, the record will be flagged in the G/L summary file as an error.

- If an add-on has been set up to use the '% of gross by time card line' calculation method, then the software will add 'vacation pay' to employee checks during the Check Calculation update, and the amount will appear on the paycheck (based on settings in Deduction / Add-on Code Maintenance). The Payroll Update will store the amount in Employee records and General Ledger (in the specified 'direct cost' G/L accounts). Applicable amounts will also be stored in Job Cost, Equipment Control and Work Order cost history.

- During the Payroll update Spectrum updates G/L expense accounts specified in Payroll > Department Expense Maintenance screen to General Ledger tables. If this department is not set up as a
 'Direct work order cost' department, then the update will not store the time card
 detail line in the cost history table.

- If the Cash Management module is installed and a bank account has been
 designated for the pay cycle, the Payroll update will transfer transaction data to
 the Cash Management > Bank Reconciliation table. At most, a single record is added across all Auto Deposits for all
 employees processed during the Payroll Update, and if no auto deposit checks were
 paid, then no record is added for the auto deposit total.

- If the Cash Management module is installed in both the confidential and main
 companies and you post payroll from the confidential company, then the G/L account
 for the auto deposit for the Confidential Payroll employees is the auto deposit
 account number in the main company. If the Cash Management Module is not installed,
 then the G/L account for the Confidential Payroll employees is the auto deposit
 account number in the confidential company. If no account is specified in the
 confidential company, or if the specified account is invalid, then the G/L account is
 the auto deposit account number in the main company.

- Payroll Image links are established during the Payroll Update as each new Job Cost History record is created. The Update stores the job time card image links, if present. If there are no job time card image files, then the Payroll Update will store the employee time card image.

Note Regarding Transaction Dates:
If the Work date option is selected in the Payroll Installation Accrue expense to field:

- For a Direct Job Cost time card entry, the software stores the work date of the time card line as the Transaction date in Job Cost History. The date assigned to this transaction in G/L is dependent upon whether or not the transaction date is in a period earlier than the Pay cycle period end date:

- If the transaction date is in the same period as the Pay cycle period end date, the Payroll Update will assign the transaction date to the G/L entry.

- If the transaction date is in a period earlier than the Pay cycle period end date, the Payroll Update will assign the G/L period end date of the period containing the transaction to the G/L entry.

- For a Direct Work Order Cost time card entry, the software stores the work date of the time card line as the Transaction date in Work Order Actual Cost History. The date assigned to this transaction in G/L is dependent upon whether or not the transaction date is in a period earlier than the Pay cycle period end date:

- If the transaction date is in a period earlier than the Pay cycle period end date, the Payroll Update will assign the G/L period end date of the period containing the transaction to the G/L entry.

- If the transaction date is in the same period as the Pay cycle period end date, the Payroll Update will assign the transaction date to the G/L entry.

- For quantity complete transactions, the software will always update based on work date. In the unusual case where the transaction date is blank in the quantity record, the software will assign the period end date.

Note Regarding Payroll Update Validation:
In order to prevent cost center adjustments and to incorporate
 additional balancing verification by period, the Payroll Update
 screen has G/L Error Correction that disallows cost center editing and does not see blank
 cost centers as errors during the update process.
Each time you exit the G/L Error Correction
 screen, the software will perform a test to confirm that the sum of the debits equals the
 sum of the credits within the same fiscal period. If an out-of-balance period is found, the
 software will not proceed with the update. Instead, all transactions previously shown will
 redisplay in the G/L Error Correction screen, allowing you to make
 any necessary changes.

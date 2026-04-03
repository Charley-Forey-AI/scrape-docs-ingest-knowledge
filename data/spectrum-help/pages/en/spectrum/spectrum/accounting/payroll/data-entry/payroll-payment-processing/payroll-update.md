---
title: "Payroll Update | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/payroll-update"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/payroll-update"
---

# Payroll Update

This function will update the employee master records and history files with payroll information from this cycle and will create General Ledger transaction entries.
Cash Management, Equipment Control, Work Order and Time + Material billing files will be updated, if applicable. It will also store time card quantity information into the Job Cost phase and history files.

- This screen updates the employee earnings, retro pay records, and check information into the employee earnings history file and Employees. Note that the burden % specified in the Phase Rate Override window will be used if the rate is a non-zero figure. The amounts for all pay types now post to Job Cost, using the Job Cost History file as a "catch-all." All pay types may be generated, including job labor markup information.

- Regarding Labor Markups: If the bill rate of the transaction is zero, the markup is calculated based on the cost; if the bill rate of the transaction is a non-zero number, the markup is calculated using that bill rate. (if applicable). This update does not generate a report.

- Payroll burden will be recorded in the same Work Order Cost History record as the employee earnings if the 'Post actual payroll burden to work order cost history' option is selected in Work Order Installation. If this checkbox is not selected, the burden will be computed by multiplying the percentage specified in Work Order Installation by the extension of the time card record.

- This update can store additional information for the employee check, including the period start date and the Cash Management bank account code in the check history files. The payroll auto deposit amount is automatically added to the Cash Management > Bank Reconciliation Entry screen as a withdrawal transaction, and it displays as a Computer check. When the cycle includes auto deposit Void Check for an employee, the software will use the employee's auto deposit check number to determine which transaction in the Bank Reconciliation 'Checks' list includes the void item. The software will then reduce the 'Amount' of that payment accordingly.

- This update sets the certified date in the job file to the time card work date for certified jobs whenever the work date is earlier than the certified date or the certified date is blank. This date is used to calculate the 'week number' when the Certified Payroll Report is printed.

- This update automatically applies portions of the worker's compensation liability to different accounts if G/L codes are recorded in the Component Rate Detail window of the [Worker's Compensation Code Maintenance](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/workers-compensation-code-maintenance) screen. Each component applied to a different G/L account will be calculated to the nearest penny (and will be made on the check totals). If the G/L account on the Worker's Compensation Code Maintenance screen is different from all of the component G/L accounts, the rounding difference is applied to the last component G/L account.

- If Payroll overhead is specified for the work order type (or a company-wide overhead setting), calculate the actual labor cost for each time card and then increase this amount by the percentage or rate/hour previously specified. Payroll overhead will always be stored in the same Work Order Cost History record as the employee earnings and burden.

- The update can conditionally post to Job Cost and Equipment Control cost history in summary on an employee-by-employee basis, based on settings in the Employee Pay Rates screen. This optional security measure allows you to prevent unauthorized Job Cost or Equipment Control users from inferring payroll rates of confidential employees.

- The update generates G/L transaction for 'direct equipment earnings' (specifically, the extension of Time Cards referencing a pay type and a 'direct equipment' Payroll department). Employer burden/overhead expenses (FICA, FUTA, SUTA, worker's compensation, union benefits and add-ons) are posted to both Equipment Control cost history and General Ledger. When burden cost totals are updated to General Ledger, expense is distributed among the various 'Employer Expense' General Ledger account codes (that is, component taxes/burden by department). When burden cost totals are updated to Equipment Control cost history, expense is distributed among equipment codes and either bundled with the earnings (cost category on the time card), or segregated in the 'Burden' cost category defined in Equipment Control Installation.

- If this is a sub-job billed from a master job, the software will read for job-specific setup rates for the master job, and if none are found use standard settings. If this is a sub-job billed at the sub-job level, the software will read for job-specific setup rates for the sub-job first, and if billing rates are not found then the master job, and if none are found there use standard settings.

- If the "Display accumulated balance on paycheck?" option is selected in the [New/Edit Deduction/Add-on Code - Properties](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/create-or-edit-a-deduction-or-add-on-code/newedit-deductionadd-on-code---properties) screen, the accumulated balance that is referenced on the pay check, Replacement Check Print, and Employee Kiosk > Earning Statement will be stored instead of the Year To Date amounts.

- When updating recurring add-on amounts allocated by Time Card, the software will use the 'Add-on allocation' G/L account code. The update will also post additional worker's compensation amounts, as well as taxes for add-ons not paid to employee on the paycheck.

- Union add-ons that are not paid to the employee on the paycheck will assign the debit G/L account assigned to the 'Union fringe' defined on the Employer Expense tab of the Department Expense Maintenance screen.

- For systems set to accrue expenses by work date: during the update, 'JX' time card records are updated to Job Cost Transaction Entry as unposted job charges. These transactions will post to Job Cost using the time card's 'Work' date if available. If the 'Work' date was not entered on the time card line, the system will post it to Job Cost using the 'Period End' date.

- If the 'Create transactions to distribute overtime among jobs on a paycheck?' checkbox is selected in [Payroll Installation - Properties](/en/spectrum/spectrum/accounting/payroll/installation-overview/payroll-installation---properties), this update will generate Job Cost transactions, backing out time card amounts charged as overtime (or double time) and then reallocating the total across all job-related time cards on the particular paycheck, based on hours worked. These entries will be assigned the 'Batch code' of the operator performing the Payroll Update. Likewise, they will be stored as 'unposted' transactions in Job Cost Transaction Entry, allowing for editing and review prior to update to Job Cost History. This feature exclusively reallocates the time card extension for Job entries (but not Hours). The Payroll Update will allocate the amount for all time cards assigned to a 'Direct job cost' payroll department where the pay type is O, EO, D or ED. These amounts will be negative transactions and the total amount of these lines will be distributed proportionally among all 'Direct job cost' payroll department time cards where the pay type is R, SR, ER, O, EO, D or ED. Specifically, the total Job Overtime amount (from time cards with pay type O, EO, D or ED) is apportioned across all Job time cards (pay types R, SR, ER, O, EO, D or ED) using the sum of all hours across these time card lines as the basis for allocation.

- If the Post to Job Cost using standard labor rates? option was selected on the Payroll Installation > Defaults screen, standard labor costs will additionally post to Job Cost History, and an adjustment journal entry will be added for standard labor costs when posting to General Ledger.

- If the Set to zero anniversary? checkbox was selected on the [Time Off Code Maintenance](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/time-off-code-maintenance) screen, the vacation, holiday and sick balances will be calculated for the current year only based on the employee's anniversary date.

Following completion of this update, the [Payroll G/L Report](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/payroll-update/payroll-gl-report) and [Payroll G/L Summary Update](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/payroll-update/payroll-gl-summary-update) should be the next steps performed. Like the Check Calculation function, this update will display a message line throughout the update describing what portion of the function is currently in progress.
Note: If you receive an "Invalid year & period" message on the [G/L Error Correction Screen](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/payroll-update/gl-error-correction-screen), check to make sure that the minimum/maximum processing dates for Payroll and General Ledger are in the fiscal calendar.
Important: If you have not completed the current payroll process, the current payroll cycle will be cleared and information about the current payroll process will be lost.

Related information

- [Payroll G/L Report](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/payroll-update/payroll-gl-report)

- [Payroll G/L Summary Update](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/payroll-update/payroll-gl-summary-update)

- [Error - Errors exist in the Payroll G/L summary file](/en/spectrum/spectrum/accounting/payroll/payroll-procedures/error---errors-exist-in-the-payroll-gl-summary-file)

- [Error - Operator or routing code is invalid...](/en/spectrum/spectrum/accounting/payroll/in-depth-overview/error---operator-or-routing-code-is-invalid...)

- [Error - Payroll Update - Create A/P Invoices Error Correction Screen](/en/spectrum/spectrum/accounting/payroll/in-depth-overview/error---payroll-update---create-ap-invoices-error-correction-screen)

- [Error - Payroll Update to General Ledger is Not Complete](/en/spectrum/spectrum/accounting/payroll/in-depth-overview/error---payroll-update-to-general-ledger-is-not-complete)

- [Job % Payroll burden vs. Actual Payroll Burden in General Ledger](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/payroll-update/job--payroll-burden-vs.-actual-payroll-burden-in-general-ledger)

- [Payroll Update - Cost Center Information](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/payroll-update/payroll-update---cost-center-information)

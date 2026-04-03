---
title: "Pre-Installation Plan | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/installation-overview/pre-installation-plan"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/installation-overview/pre-installation-plan"
---

# Pre-Installation Plan

After the appropriate companies or divisions have been
 installed through the Company Installation screen, the Payroll module may be installed.
General Ledger must be installed before Payroll. Also, make sure that the following General
 Ledger account codes have been set up; use the same account codes in Payroll as in General
 Ledger.
For purposes of preparing quarterly payroll reports, it is desirable to convert payroll at the beginning of a quarter. This is because many of the tax filings (such as FICA, FIT, and FUTA) are prepared quarterly. Alternatively, if conversion is planned for a date other than quarter-end, two conversion cycles may be performed: from January 1 through the most recent quarter-end, then a second cycle for the remaining payrolls since that quarter-end. For example: to convert at 8/31, perform two cycles: 1/1 through 6/30, then 7/1 to 8/31. This will allow the software to provide complete quarterly reports for the first live quarter. Otherwise, the first set of quarterly reports will need to be prepared manually, since the quarter-to-date information may not be accurate.
Payroll is an extremely important function. It is advisable to check the results of the first one or more computer-generated payrolls carefully for accuracy. Furthermore, every payroll should always be checked for errors.
Use the following list as a guide:

- Payroll Cash in Bank

- Accrued Payroll (if accrued payroll is planned)

- Intercompany Payroll (if multi-company payroll processing is
 planned)

- Federal Liability - Federal Income Tax
 Payable
- FICA/Medical Aid Payable
- FUTA Payable

- State Liability (each applicable state) -
 State Income Tax Payable
- SUTA Payable
- Worker's Compensation Payable

- One General Ledger code for each Deduction needed - Union Fringes and Deduction Liability (if needed)
- Expenses

- For each department to be set up, the following General Ledger
 account codes will be needed. It is acceptable to have the same General Ledger account
 code for multiple payroll expense types. Salaries and WagesOther earnings 1*
Other earnings 2*Other earnings 3*
FICA expenseFUI expense
Residence SUI expense*Work SUI expense*
Vacation expense*Holiday expense*
Sick leave expense*Net adjustments*
Misc. expense*Resident state Worker's
 compensation
Work state Worker's
 compensation

*(if applicable)

For each General Ledger code entered in the General Ledger module, select either Yes, Equipment, or No to indicate whether or not this General Ledger code refers to a work-in-progress account. If a Yes is selected, any employee time charged to this General Ledger account must also be charged to a job. If Equipment is selected, employee time charged to this G/L code must also be charged to an equipment piece. If No is selected, time charged to this General Ledger code may not be charged to a job or piece of equipment. This is designed to help ensure that Job Cost and Equipment Control systems balance to the General Ledger system. Accordingly, when setting up General Ledger codes, it will be necessary to decide which earning codes for which departments will be charged to jobs and equipment, and which will not.

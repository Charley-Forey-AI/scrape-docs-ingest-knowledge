---
title: "Payroll Update - Cost Center Information - G/L Account Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/payroll-update/payroll-update---cost-center-information/payroll-update---cost-center-information---gl-account-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/payroll-update/payroll-update---cost-center-information/payroll-update---cost-center-information---gl-account-information"
---

# Payroll Update - Cost Center Information - G/L Account Information

Use the table below for reference when completing the
 fields on this screen.
G/L Account
How the G/L account is posted…

Cash
If Cash Management is installed, then the bank account specified for the cycle is used to determine the cash G/L account; otherwise the Payroll Installation screen is used to determine the G/L account. The Check cost center specified in the cycle setup is used for posting the cash G/L account to General Ledger. If the Enterprise Installation setting for this cost center company is set to Allow G/L overrides by cost center then an override may also be set up on the Payroll Installation screen for the cash account. This uses the check run cost center to determine the G/L account to post to (if Cash Management is NOT installed). This posts to the current company unless a Confidential Payroll company is designated in Payroll Installation (in that case the G/L account will post into the Confidential company.)
For auto deposit checks, the liability account is assigned based on Payroll Installation G/L account settings. The cost center assigned to the auto deposit liability is the cost center for check run that was specified in Set Payroll Cycle.

Income Tax
The tax payable, unemployment payable, FICA employee payable, and FICA employer payable G/L accounts from the income tax table all post to General Ledger using the cost center assigned as the 'Check cost center' specified in the cycle setup. These post to the current company unless a Confidential Payroll company is designated in Payroll Installation; in that case the G/L account will post into the Confidential Payroll company.

Department Expense
The G/L accounts in Department Maintenance for Salary/Wages and Employer Expense all post to General Ledger using the cost center assigned to the time card line. Spectrum determines if an override G/L account is set up for that department and cost center and it posts with that G/L account or, if the override is blank, it uses the department G/L account. Department expense G/L accounts post to the company entered on the time card line.

Worker's Compensation
The G/L liability account from Worker's Compensation Maintenance will post to General Ledger with the 'Check cost center' specified in the cycle setup. These post to the current company unless a Confidential Payroll company is designated in Payroll Installation; in that case the G/L account posts to the Confidential Payroll company.
The Worker's Compensation G/L expense account from Department Expense Maintenance will post to General Ledger with the cost center assigned to the time card line. Spectrum determines if an override G/L account is set up for that department and cost center and posts with that G/L account or, if the override is blank, it uses the Department G/L account. Worker's comp G/L accounts post to the company entered on the time card line.

Deduction/Add-on
The G/L account and Non-cash G/L accounts (for add-ons not paid to employee on check) will post to General Ledger with the 'Check cost center' specified in the cycle setup for all deductions and for add-ons entered in Employee Recurring Deductions/Add-ons. These will post into the current company unless a Confidential Payroll company is designated in Payroll Installation; in that case the G/L account will posts to the Confidential Payroll company.
When A/P invoices are creating for deductions and non-cash add-ons, the check cost center assigned to the pay cycle is recorded in the header and detail of the A/P invoice.
For add-ons entered in Time Card Entry from a union or from a non-union pay group, the cost center associated with that time card line is used when posting to General Ledger.
These G/L accounts will post to the company entered on the time card line.

Union Fringe
The Fringe Payable G/L accounts set up in Union Maintenance post to General Ledger with the 'Check cost center' specified in the cycle setup. These will post to the current company unless a Confidential Payroll company is designated in Payroll Installation; in that case the G/L account will post into the Confidential Payroll company.
The Union Fringe Expense G/L accounts in Department Maintenance will post to General Ledger using the cost center assigned to the time card line. Spectrum will check if an override G/L account is set up for that department and cost center and post with that G/L account; or use the Department G/L account if the override is blank.
These G/L accounts post to the company entered on the time card line.

Department Job Expense
The % payroll burden debit and % payroll burden credit G/L accounts will post to General Ledger using the cost center assigned to the time card line. Spectrum determines if an override G/L account is set up for that department and cost center and posts with that G/L account or, if the override is blank, it uses the Department G/L account. These G/L accounts post to the company entered on the time card line.

- Burden G/L accounts are only used when the job associated with the time card line has the actual burden flag cleared and a payroll percentage entered in Job File Maintenance.

- Overhead G/L accounts are only used when the job associated with the time card line has the overhead type set to percent and a percentage entered in Job File Maintenance.

Department Equipment Expense
The % payroll burden debit and % payroll burden credit G/L accounts will post to General Ledger using the cost center assigned to the time card line. Spectrum determines if an override G/L account is set up for that department and cost center and post with that G/L account or, if the override is blank, it uses the Department G/L account. These will post into the company entered on the time card line. Burden G/L accounts are only used when the Equipment Control Installation setting for Payroll burden type is not set to Actual.

Equipment Revenue
Spectrum checks the Equipment Control Installation settings. For a direct cost (job) time card line, Spectrum uses the Job revenue credit G/L account; otherwise the Rental revenue credit G/L account is used. The cost center assigned to the equipment in Equipment File Maintenance will be used for posting these accounts to General Ledger (not the cost center assigned to the time card line).
If the Enterprise Installation setting for this cost center company is set to Allow G/L overrides by cost center then an override may also be set up for these G/L accounts. Spectrum uses the equipment cost center to determine which G/L account to post to in this case. These post to the current company unless a Confidential Payroll company is designated in Payroll Installation; in that case the G/L account posts to the Confidential Payroll company.
The Equipment usage G/L account from Department Expense Maintenance posts to General Ledger using the cost center assigned to the time card line. Spectrum checks if an override G/L account is set up for that department and cost center and posts with that G/L account or, if the override is blank, it uses the Department G/L account.
These G/L accounts post to the company entered on the time card line.

Intercompany / Inter-posting
Spectrum checks the Enterprise Installation option to use cost centers setting for each company that the update will post to. If this setting is Yes for a company, Spectrum uses the existing intercompany G/L accounts to post a matching G/L entry to balance that company.
For any cost center companies, Spectrum checks the total balance for each cost center. If the balance is not zero, then Spectrum creates a balancing G/L post using the cost center inter-posting account from Payroll Installation. If the Enterprise Installation setting for this company is set to Allow G/L overrides by cost center then an override may also be set up on the Payroll Installation screen for this G/L accounts. Spectrum use the cost center to determine which G/L account to post to in this case.

% overhead
If Payroll overhead is specified for the Work order type (or a company-wide overhead setting), calculate the actual labor cost for each time card and then increase this amount by the percentage or rate/hour previously specified.

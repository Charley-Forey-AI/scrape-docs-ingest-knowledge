---
title: "Multi-Company Setup | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/system-administration/multi-company-processing-overview/multi-company-setup"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/system-administration/multi-company-processing-overview/multi-company-setup"
---

# Multi-Company Setup

The user must select the multi-company option during Accounts Payable Installation, Payroll Installation, Inventory Control Installation, Cash Management, and/or Equipment Control Installation. Screens in each of these modules plus Materials Management and Equipment Tracking are affected by this option.
When a business decides to use the Spectrum multi-company feature, the following setup is required:

- Create the desired companies

- Complete the Company Installation page - once for each company

- Complete the installation pages for all modules present on the system; note that this will need to be done multiple times - once for each company

- The G/L account code mask and financial calendar must be identical for all companies.

- The multi-company invoices checkbox should be selected for Accounts Payable, and an inter-company A/P account code designated.

- The multi-company payroll checkbox should be selected Payroll, and an inter-company payroll account code designated.

- The multi-company checkbox should be selected for Cash Management, and an inter-company cash account code designated.

- The multi-company checkbox should be selected for Equipment Control, and an inter-company equipment account code designated.

- The multi-company checkbox should be selected for Inventory Control, and an inter-company inventory account code designated.
Following the Part I instructions provided in the Conversion section of this Help file, perform all file maintenance for the installed modules:

- Set up the chart of accounts in every company created. Be sure to include the intercompany account(s) specified on the installation pages when setting up the chart of accounts. Don't forget that it is possible to copy the chart of accounts from one company to another, easing file maintenance in the General Ledger.

- Set up vendors in the company that will be paying A/P invoices.

- Set up all tax tables and employees in the company that will be issuing payroll checks.

- Set up equipment in every company that will record the equipment as a capital item. When using the multi-company feature, it may be necessary to enter a single piece of equipment in more than one company.

- Set up inventory in each company that will be tracking stock items in warehouses.
Following the Part II instructions provided in the Conversion section of this Help file, perform all data conversion for the installed modules:
When entering A/P invoices, log on to the company that issued the checks. After the page header is complete, the cursor will be positioned in the account code column of the line transaction portion of the page. Use the Arrow key or the computer mouse to position the cursor down one line at the cc: prompt and enter the company to which this invoice should be charged, then press Enter; the G/L account code should be from the company that is incurring the expense.
When entering Multi Company A/P invoices, log on to the company that issued the checks. After the page header is complete, the cursor will be positioned in the account code column of the line transaction portion of the page. Use Shift+Tab to position the cursor on the company code field to which this invoice should be charged to then press Enter. The G/L account code should be from the company that is incurring the expense. The payroll dept must be in the company being charged. Write all financial reports, using the Design Financial Reports. Reports written in one company are accessible from all consolidated companies.

Related information

- [Multi-Company Transactions](/en/spectrum/spectrum/system-administration/multi-company-processing-overview/multi-company-transactions)

- [Multi-Company vs. Departments](/en/spectrum/spectrum/system-administration/multi-company-processing-overview/multi-company-vs.-departments)

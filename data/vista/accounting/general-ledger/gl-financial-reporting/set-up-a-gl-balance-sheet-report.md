---
title: "Set Up a GL Balance Sheet Report | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/general-ledger/gl-financial-reporting/set-up-a-gl-balance-sheet-report"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/general-ledger/gl-financial-reporting/set-up-a-gl-balance-sheet-report"
---

# Set Up a GL Balance Sheet Report

You can generate a report that represents asset and liability accounts in an order you set.
Before setting up a balance sheet report, you must first set up the GL Income Statement report. For more information, see [Set Up a GL Income Statement Report](/en/vista/vista/accounting/general-ledger/gl-financial-reporting/set-up-a-gl-income-statement-report).

The report consolidates income/expense accounts into Current Year Retained Earnings on the report. You use GL Report Categories to set up this report.

1. On the Grid tab of GL Report Categories, in the Major Category field, specify a unique number to identify this major category.

1. In the Description field, enter the text for the group labels on the report. Also, it would be useful to describe categories so that it is easy to see at a glance which categories apply to asset, liability, or income/expense accounts.

1. Specify the order that the accounts with these major categories will be represented on the report.

1. For each major category that will be assigned to liability or asset accounts:

- In the Balance Sheet Order field, enter a unique number to specify the order that the account assigned to this major category will be listed on balance sheets.

- Leave the Income Statement Order as is.

1. For each major category that will be assigned to income/expense accounts, to group these accounts together as Current Year Retained Earnings on the balance sheet:

- For for all major categories that will be assigned to income/expense accounts, in the Balance Sheet Order field, enter the same number. This number must not have been used for any liability or asset accounts.

- Leave the Income Statement Order values as they are. They will specify the order for each account within the Current Year Retained Earnings section of the balance sheet.

1. On the Minor Category tab, for each major category, set up minor categories:

1. In the Minor Category field, specify a unique number to identify this minor category.

1. In the Description field, enter the text for the sub-group labels on the report.

1. In the Balance Sheet Order field:

-  For each minor category that will be assigned to liability or asset accounts, enter a unique number to specify the order that the account with this minor category will be listed on balance sheets within its major category.

- For minor categories that will be assigned to income/expense accounts, leave this field blank.

1. Leave the Income Statement Order as is.

1. Leave the Cash Flow Statement Order fields blank.

1. In GL Account Parts, on the Instances tab, assign the major and minor categories to each instance of a GL Account Part 1 that you want to include on the report.

1. Run the GL Balance Sheet report from the Reports menu under General Ledger.  For more information, see also the F1 Help and the Report Info tab on each report launcher.

Related information

- [GL Financial Reporting](/en/vista/vista/accounting/general-ledger/gl-financial-reporting)

- [Set Up a GL Income Statement Report](/en/vista/vista/accounting/general-ledger/gl-financial-reporting/set-up-a-gl-income-statement-report)

- [Setting Up a GL Statement of Cash Flow Report](/en/vista/vista/accounting/general-ledger/gl-financial-reporting/setting-up-a-gl-statement-of-cash-flow-report)

- [About the GL Report Categories Form](/en/vista/vista/accounting/general-ledger/gl-financial-reporting/about-the-gl-report-categories-form)

---
title: "Set Up a GL Income Statement Report | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/general-ledger/gl-financial-reporting/set-up-a-gl-income-statement-report"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/general-ledger/gl-financial-reporting/set-up-a-gl-income-statement-report"
---

# Set Up a GL Income Statement Report

You can generate a report that represents GL accounts in a standard income statement using the GL Report Categories form.
The setup of this report is used also in the setup of the GL Balance Sheet and GL Statement of Cash Flow reports, so it is recommended that you complete the following steps first.
To set up a GL Income Statement report:

1. On the Grid tab of GL Report Categories, in the Major Category field, specify a unique number to identify this major category.

1. In the Description field, enter the text for the group labels on the report. Also, it would be useful to describe categories so that it is easy to see at a glance which categories apply to asset, liability, or income/expense accounts.

1. Specify the order that the accounts with these major categories will be represented on the report:

1. For each major category that will be assigned to a liability or asset account, leave the Balance Sheet Order and Income Statement Order fields blank.

1. For each major category that will be assigned to an income/expense account, in the Income Statement Order field, enter a unique number to specify the order for the account. Leave the Balance Sheet Order field blank.

1. optional On the Minor Category tab, for each major category, set up minor categories:

1. In the Minor Category field, specify a unique number to identify this minor category.

1. In the Description field, enter the text for the sub-group labels on the report.

1. Leave the Balance Sheet Order field blank.

1. In the Income Statement Order field:

-  For minor categories that will be assigned to a liability or asset accounts, leave this field blank.

- For minor categories that will be assigned to income/expense accounts, enter a unique number to specify the order for the account with this minor category to be listed on balance sheets within its major category.

1. Leave the Cash Flow Statement Order field blank.

1. In GL Account Parts, on the Instances tab, assign the major and minor categories to each instance of a GL Account Part 1 that you want to include on the report.

1. Run the GL Income Statement report from the Reports menu under General Ledger.  For more information, see also the F1 Help and the Report Info tab on each report launcher.

Related information

- [GL Financial Reporting](/en/vista/vista/accounting/general-ledger/gl-financial-reporting)

- [Set Up a GL Balance Sheet Report](/en/vista/vista/accounting/general-ledger/gl-financial-reporting/set-up-a-gl-balance-sheet-report)

- [Setting Up a GL Statement of Cash Flow Report](/en/vista/vista/accounting/general-ledger/gl-financial-reporting/setting-up-a-gl-statement-of-cash-flow-report)

- [About the GL Report Categories Form](/en/vista/vista/accounting/general-ledger/gl-financial-reporting/about-the-gl-report-categories-form)

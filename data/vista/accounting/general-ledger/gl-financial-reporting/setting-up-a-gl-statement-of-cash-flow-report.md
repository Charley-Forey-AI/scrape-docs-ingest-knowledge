---
title: "Setting Up a GL Statement of Cash Flow Report | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/general-ledger/gl-financial-reporting/setting-up-a-gl-statement-of-cash-flow-report"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/general-ledger/gl-financial-reporting/setting-up-a-gl-statement-of-cash-flow-report"
---

# Setting Up a GL Statement of Cash Flow Report

You can generate a report that that represents GL accounts in a standard cash flow statement, displayed in an order you set, and consolidating income/expense accounts into Cash Flow from Operating Activities on the report. Use the GL Report Categories form to set up this report.
The setup of this report uses much of the setup done for the GL Income Statement report, so you will want to complete those steps first. See [Set Up a GL Income Statement Report](/en/vista/vista/accounting/general-ledger/gl-financial-reporting/set-up-a-gl-income-statement-report).

To set up a GL Statement of Cash Flow report:

1. On the Grid tab of GL Report Categories, in the Major Category field, specify a unique number to identify this major category.

1. In the Description field, enter text that describes this major category of accounts. For example, it would be useful to describe categories so that it is easy to see at a glance which categories apply to asset, liability, or income/expense accounts.

1. Fill in the following three fields as noted for accounts you want represented on the report:

1. For each major category that will be assigned to a liability or asset account:

- In the Balance Sheet Order field, leave any values that may already be present from when the GL Balance Sheet report was set up.

- Leave the Income Statement Order field values as they are.

1. For all major categories that will be assigned to income/expense accounts, to group these accounts together as Cash Flow from Operating Activities on the cash flow statement:

- In the Balance Sheet Order field, leave any values that may already be present from when the GL Balance Sheet report was set up.

- Leave the Income Statement Order values as they are.

1. On the Minor Category tab, for each major category of accounts that you want represented on the Statement of Cash Flows report and that does not have a value in the Income Statement Order field in the major category, set up minor categories:

1. In the Minor Category field, specify a unique number to identify this minor category.

1. In the Description field, enter the text for the sub-group labels on the report.

1. Leave the Balance Sheet Order and the Income Statement Order fields blank.

1. In the Cash Flow Statement Order field, enter a three digit number:

-  For all minor categories that will be assigned to accounts that you want consolidated into the Cash Flow from Operating Activities section of the report, use the same three digit number with a value of 100-199.

- For all other minor categories, enter a unique number to specify the grouping of accounts within the following categories on the report, as follows:

- 200-299 — Adjustments to Reconcile to Net Income to Net Cash Flow

- 300-399 — Decrease (Increase) in Current Assets

- 400-499 — Increase (Decrease) in Current Liabilities

- 500-599 — Cash Flow from Investing Activities

- 600-699 — Cash Flow from Financing Activities

Note: Make sure that the number used in the minor category Cash Flow Statement Order field is unique, and is not used for as any other minor category under any major category.

1. In GL Account Parts, on the Instances tab, assign the major and minor categories to each instance of a GL Account Part 1 that you want to include on the report.

1. Run the GL Statement of Cash Flow report from the Reports menu under General Ledger.  For more information, see also the F1 Help and the Report Info tab on each report launcher.

Related information

- [GL Financial Reporting](/en/vista/vista/accounting/general-ledger/gl-financial-reporting)

- [Set Up a GL Income Statement Report](/en/vista/vista/accounting/general-ledger/gl-financial-reporting/set-up-a-gl-income-statement-report)

- [Set Up a GL Balance Sheet Report](/en/vista/vista/accounting/general-ledger/gl-financial-reporting/set-up-a-gl-balance-sheet-report)

- [About the GL Report Categories Form](/en/vista/vista/accounting/general-ledger/gl-financial-reporting/about-the-gl-report-categories-form)

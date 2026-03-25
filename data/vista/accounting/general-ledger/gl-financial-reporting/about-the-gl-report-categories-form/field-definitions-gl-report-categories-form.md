---
title: "Field Definitions: GL Report Categories Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/general-ledger/gl-financial-reporting/about-the-gl-report-categories-form/field-definitions-gl-report-categories-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/general-ledger/gl-financial-reporting/about-the-gl-report-categories-form/field-definitions-gl-report-categories-form"
---

# Field Definitions: GL Report Categories Form

The following is a list of field descriptions for the GL
 Report Categories form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Major Category

 Required.
Enter a unique number, up to 6 numerals, to
 identify this major category, or press F4 for a list of existing major
 categories.
After you have associated the major category with a GL account part instance, you can then use the category to sort and group sections of financial statements.

Related information

- [About the GL Report Categories Form](/en/vista/vista/accounting/general-ledger/gl-financial-reporting/about-the-gl-report-categories-form)

## Description

Enter a description or name, up to 60 characters, to describe this major category of accounts.
After you have associated the major category with a GL account, you can then use the description to help you sort and group financial statements based on the category. For example, it might be useful to describe categories so that it is easy to see at a glance which categories apply to asset, liability, or income/expense accounts.
For GL Income Statement and GL Balance Sheet reports
The descriptions will be the group labels on the report.

Related information

- [About the GL Report Categories Form](/en/vista/vista/accounting/general-ledger/gl-financial-reporting/about-the-gl-report-categories-form)

## Balance Sheet Order

Enter a unique number, up to 6 numerals, to specify the order on balance sheets for the GL accounts associated with this major category.
For GL Income Statement reports

- Leave the Balance Sheet Order field blank.

For GL Balance Sheet reports

- For each major category that will be assigned to liability or asset accounts, enter a unique number to specify the order that the account assigned to this major category will be listed on the balance sheet.

- For all major categories that will be assigned to income/expense accounts, to group these accounts together as Current Year Retained Earnings on the balance sheet, enter the same number. This number must not have been used for any liability or asset accounts.

For GL Statement of Cash Flow reports

-  Leave any values that may already be present from when the GL Balance Sheet report was set up.

Related information

- [About the GL Report Categories Form](/en/vista/vista/accounting/general-ledger/gl-financial-reporting/about-the-gl-report-categories-form)

## Income Statement Order

Enter a unique number, up to 6 numerals, to specify the order on income statements for the GL accounts associated with this major category.
For GL Income Statement reports

- For each major category that will be assigned to a liability or asset account, leave the field blank.

- For each major category that will be assigned to an income/expense account, enter a unique number to specify the order for the account.

For GL Balance Sheet reports

- For each major category that will be assigned to liability or asset accounts, leave the field as was set up for the GL Income Statement reports.

- For each major category that will be assigned to income/expense accounts, leave the field as was set up for the GL Income Statement reports. This will group these accounts together within the Current Year Retained Earnings on the balance sheet.

For GL Statement of Cash Flow reports

- For each major category that will be assigned to a liability or asset account, leave the field blank.

- For all major categories that will be assigned to income/expense accounts, leave the field as was set up for the GL Income Statement reports. This will group these accounts together as Cash Flow from Operating Activities on the cash flow statement.

Related information

- [About the GL Report Categories Form](/en/vista/vista/accounting/general-ledger/gl-financial-reporting/about-the-gl-report-categories-form)

## Minor Category

Enter a unique number, up to 6 numerals, to
 identify this minor category, or press F4 for a list of existing minor
 categories.
After you have associated the minor category with a major category, and then have associated them with a GL account part instance, you can then use the minor category to sort and group sections of financial statements.

Related information

- [About the GL Report Categories Form](/en/vista/vista/accounting/general-ledger/gl-financial-reporting/about-the-gl-report-categories-form)

## Description

Enter a description or name, up to 60 characters, for this minor category.
After you have associated the minor category with a major category, and then have associated them with a GL account, you can then use the minor category description to help you sort and group sections of financial statements.
For GL Income Statement and GL Balance Sheet reports
The descriptions will be the sub-group labels on the report.

Related information

- [About the GL Report Categories Form](/en/vista/vista/accounting/general-ledger/gl-financial-reporting/about-the-gl-report-categories-form)

## Minor Category: Balance Sheet Order

Enter a unique number, up to 6 numerals, to specify the order on balance sheets for the GL accounts associated with this minor category.
For GL Income Statement reports

- Leave this field blank.

For GL Balance Sheet reports

-  For each minor category that will be assigned to liability or asset accounts, enter a unique number to specify the order that the account with this minor category will be listed on balance sheets within its major category.

- For minor categories that will be assigned to income/expense accounts, leave this field blank.

For GL Statement of Cash Flow report

- Leave this field blank.

Related information

- [About the GL Report Categories Form](/en/vista/vista/accounting/general-ledger/gl-financial-reporting/about-the-gl-report-categories-form)

## Minor Category: Income Statement Order

Enter a unique number, up to 6 numerals, to specify the order on income statements for the GL accounts associated with this minor category.
For GL Income Statement reports

-  For minor categories that will be assigned to a liability or asset accounts, leave this field blank.

- For minor categories that will be assigned to income/expense accounts, enter a unique number to specify the order for the account with this minor category to be listed on balance sheets within its major category.

For GL Balance Sheet reports

- Leave this field as it was set up for the GL Income Statement report.

For GL Statement of Cash Flow reports

- Leave this field blank.

Related information

- [About the GL Report Categories Form](/en/vista/vista/accounting/general-ledger/gl-financial-reporting/about-the-gl-report-categories-form)

## Minor Category: Cash Flow Statement Order

Enter a unique number, up to 6 numerals, to specify the order on cash flow statements for the GL accounts associated with this minor category.
For GL Income Statement reports

- Leave this field blank.

For GL Balance Sheet reports

- Leave this field blank.

For GL Statement of Cash Flow reports
Enter a three digit number:

-  For all minor categories that will be assigned to accounts that you want consolidated into the Cash Flow from Operating Activities section of the report, use the same three digit number with a value of 100-199.

- For other minor categories, enter a unique number from 200-699 to specify the grouping of accounts within the following categories on the report, as follows:

- 200-299 — Adjustments to Reconcile to Net Income to Net Cash Flow

- 300-399 — Decrease (Increase) in Current Assets

- 400-499 — Increase (Decrease) in Current Liabilities

- 500-599 — Cash Flow from Investing Activities

- 600-699 — Cash Flow from Financing Activities

Note: Make sure that the number used in this field is unique, and is not used for as any other minor category under any major category.

Related information

- [About the GL Report Categories Form](/en/vista/vista/accounting/general-ledger/gl-financial-reporting/about-the-gl-report-categories-form)

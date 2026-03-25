---
title: "Field Definitions: AP On Cost Type Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/on-cost-invoices/ap-on-cost-invoice-forms/ap-on-cost-types-form/field-definitions-ap-on-cost-type-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/on-cost-invoices/ap-on-cost-invoice-forms/ap-on-cost-types-form/field-definitions-ap-on-cost-type-form"
---

# Field Definitions: AP On Cost Type Form

The following is a list of field descriptions for the AP On Cost Type form.Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## On-Cost ID

Enter a number for this on-cost type. You can enter a number between 1 - 255. Press F4 for a list of previously created ID numbers.

## Description

Enter a description of this on-cost type. For example, you might enter "worker's compensation" or "payroll taxes."

## On-Cost Vendor

Enter the vendor that the system will create an invoice for based on the on-cost type.

## Calculation Method

Select a calculation method: A-Amount or
 R-Rate. If you select A-Amount, the system enables the
 Amount field. If you select R-Rate, the system enables the Rate field.

## Rate

Enter the percentage rate for calculating this on-cost type.

## Amount

Enter the flat amount for calculating this on-cost type.

## Pay Type

Enter the pay type for this on-cost type.

## Job Expense Option

Select an option for determining the job expense account for this on-cost type. The following options are available:

- Use Original Invoice Expense Account - When the system generates the on-cost invoice, it will use the expense information that you specified on the original invoice that you created for the subcontractor/vendor.

- Use On-Cost Cost Type - When the system generates
 the on-cost invoice, it will use the job and phase from the original subcontractor
 invoice, but will use the cost type that you specified in the Cost Type
 field on this form. When you select this option, the system enables the Cost Type
 field.

- Use On-Cost Job Expense Account - When the system
 generates the on-cost invoice, it will not use the job from the original invoice, and
 will create an expense line for the on-cost invoice using the GL expense account that
 you specify in the Job Expense Acct field. When you
 select this option, the system enables the Job Expense Acct field.

## Cost Type

The system enables this field when you select
 Use On-Cost Cost
 Type from the Job Expense Option drop-down.
Enter a cost type or press F4 to see a
 list of cost types. The system will use this cost type to determine the job expense account
 for transactions to the on-cost vendor.
Note:If you are performing intercompany postings, the cost type that you select must exist in both companies.

## Job Expense Acct

The system enables this field when you select
 Use On-Cost Job Expense Account from the Expense Option drop-down in the Job
 Expense Options section of the form.
Enter a GL account for job expense on-cost
 invoices or press F4 to see a list of GL accounts.
Note:If you are performing intercompany postings, the GL
 account that you select must exist in both companies.

## Non-Job Expense Option

Select an option for determining the non-job
 expense account for this on-cost type. The following options are available:

- Use Original Invoice Expense Account - When the
 system generates the on-cost invoice, it will use the GL account number that you
 specified on the original invoice that you created for the subcontractor/vendor.

- Use On-Cost Expense Account - Select this option if
 you want to specify a cost expense account for this on-cost type. When you select
 this option, the system enables the Non-Job Expense Acct field.

## Non-Job Expense Acct

The system enables this field when you select
 Use On-Cost Expense Account from the Expense Option drop-down in the Non-Job
 Expense section of the form.
Enter a GL account for non-job expense,
 on-cost invoices or press F4 to see a list of GL accounts.

## ATO Category

The system enables this field when the current
 company's country is set to Australia (HQ Company Setup, Default Country
 field).
Select an ATO category from this drop-down
 when necessary: Superannuation or Superannuation-Extra. For more
 information on which option to choose, see [Setting Up Deduction and Liability Codes for
 Superannuation](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/superannuation/set-up-superannuation/setting-up-liability-codes-for-superannuation).

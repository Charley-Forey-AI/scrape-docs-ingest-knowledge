---
title: "JB Company Control Options | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-company-control-options"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-company-control-options"
---

# JB Company Control Options

There are several setup options that control processing in Job Billing, including auto-numbering, auto-update of previously billed amounts and change order amounts, certification of progress billing claims, and implementing a billing review and approval workflow.
Once defined, changes are usually rare to settings in the form. Because changing an option may affect processing or stored information, you should make changes carefully. If you want to change an option but are unsure of its effect on existing data in the system, contact Viewpoint Support.
The following sections describe each control option
 and how it functions.

## Set Auto Invoice Numbering Option

Job Billing allows you to enter invoice
 numbers manually or have the system generate them automatically. If you elect to use
 auto-numbering (i.e. Auto Sequence Invoice # option is checked), use the Last Invoice
 Option to specify whether to use Job Billing numbers or share invoice numbers with
 Accounts Receivable.

- Job Billing – System assigns invoice
 numbers sequentially based on the JB Last Invoice# field. You have the option to
 specify a beginning invoice number or leave it blank to have the system begin with
 ‘1’.

- Accounts Receivable – System assigns
 invoice numbers sequentially based on the Last Invoice # field in AR Company
 Parameters. With this option, invoice numbers are shared across AR and JB.

If you plan to enter invoice numbers
 manually, leave the Auto Sequence Invoice # option unchecked.

## Allow Changes to Previous and Contract Amounts

This option, when checked, allows manual
 changes to previous and contract amounts when entering progress invoices. Contract
 Units, Contract Amount, Previous
 Units, and Previous Amount fields are enabled for
 input, allowing changes to previous and contract amounts for existing and/or new
 invoices. Changes to ‘previous’ amounts only affect the figures that print on invoices;
 they do not update General Ledger, Accounts Receivable, or Job Cost.
Note: If using the 'auto update previous billed amounts'
 feature, it is strongly suggested that you do NOT check this option, as it may cause
 inaccuracies when previous amounts are updated for future billings. You will typically
 only check this option when setting up the Job Billing module.

## Automatic Update of Prev Billed and ChgOrder Amounts on Future Bills

This option determines whether the system
 will automatically update previous amounts on future billings whenever changes are made
 to progress or T&M billings. If checked, and a change is made to a billing, the
 system automatically updates the 'change' amount to the previous billed amounts, and the
 current contract and contract units on all subsequent (future) billings for that
 contract/customer.
For progress billings, previous change
 order additions and deductions are updated when changes are made to approved change
 order items in JB Progress Change Order. Any manual changes to previous amounts will be
 recalculated based on the previous and current amounts of the previous billing.
If this option is not checked, you must
 manually update previous amounts, current contract/contract units, and change order
 adds/deducts using the update options found in the File menus of the JB Progress Billing
 and JB T&M Bill Edit forms. When manually updating previous amounts, the system adds
 the value of the change for the current billing to the current billing's previous amount
 and recalculates the previous amounts for all subsequent billings.
Regardless of the option used, the results
 will be the same unless manual changes were made to the previous amounts of a future
 bill. In this case, each method will produce a different amount.
Note: When using this option, it is strongly suggested
 that you do NOT also select the Allow Changes to Previous and Contract Amounts check
 box. Allowing manual changes to previous amounts when this option is in use may
 potentially cause inaccuracies when previous amounts are updated automatically. If
 previous values must be changed manually, it is imperative that they are accurate and
 equal to the sum of all earlier bills to that point.

## Allow Changes to Progress Bill Data When Both Progress and T&M Exists

Checking this option allows you to make
 changes to progress billings when both progress and T&M billings are used. You can
 edit items on billings with a bill type of ‘Both’ in JB Progress Billing as long as the
 item's bill type (in JC Contract Items) is also ‘Both’. Because T&M billings are not
 updated with changes made to a progress billing, they will not provide accurate backup
 for the data. Therefore, you should only use this option if you are not concerned with
 progress and T&M billings being out of sync.

## Flag JC transactions not defined on template as billed

 This flag indicates what billing status
 will be assigned to job cost detail records that do not have a source/cost type defined
 in a template or are set up with the Bill Flag set to ‘Neither’ in JC Phase Cost Types.
 Check this box to mark detail records as
 ‘unbillable’ (status 2). Records with this billing status will not be available for
 future billing even if you define a source/cost type on a template later or the bill
 flag in JC Phase Cost Types is changed. These records will appear on an error report for
 review on this billing but will not be included in the invoice.
 Leave this box unchecked if you do not
 want detail records assigned a billing status. Records will appear on the error report
 but will not be included in the invoice. If you do not change the Bill Flag in JC Phase
 Cost Types or the template to include these records, they will continue to come up on
 future invoices as errors.
 It is recommended that all sources and
 cost types be defined in the templates, even if they are defined as non-billable
 (typically Burden). If you commonly have phase/cost types that are non-billable but
 specific to a job, checking this flag will keep them from coming up on each billing.


## Certify Progress Billing Claims

By checking this box, you enable the
 certification process for progress billings in JB Progress Billing. Certifying progress
 billings allow Australian users to comply with the requirements of the Building and
 Construction Industry Security of Payment Act (2002). For other customers, it provides a
 way to track an initial billing amount against the final amount. See [Certifying Billings ](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-certifying-billings) for more information.

## Review and Approval Workflow

If your company requires the approval of job billing invoices before they are sent to Accounts Receivable for payment, you can use the Review and Approval Workflow feature in Job Billing to track the review and approval process for progress and T&M billings.
To enable this feature, you must select the Use Review and Approval Workflow check
 box and then set a minimum review level for interfacing billings to Accounts Receivable.
 For more information about this feature, see [About the Review and Approval Workflow for Job Billings](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-the-review-and-approval-workflow-for-job-billings).

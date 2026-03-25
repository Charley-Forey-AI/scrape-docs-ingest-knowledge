---
title: "About Billing SM Job Work Orders | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/sm-invoices/about-billing-sm-job-work-orders"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/sm-invoices/about-billing-sm-job-work-orders"
---

# About Billing SM Job Work Orders

If you are creating job work orders in Service Management, you must bill for work completed using either the Job Billing (JB) or Accounts Receivable (AR) modules.
All work completed labor, equipment, miscellaneous expenses, and materials for a job work order must be billed using the Job Billing or Accounts Receivable modules. You will typically only use Accounts Receivable if you do not have the Job Billing module.
When you capture work completed for a job work order (in SM Work Orders), if you selected the JC interface checkbox in SM Company Parameters, the system sends the costs to Job Cost (via the JC Cost Detail table, JCCD). Each record is assigned a "JC Trans Type" as follows:

- EM (for work completed equipment)

- MI (for work completed miscellaneous)

- IN (for work completed inventory)

- PR (for work completed labor)

- AP (for AP transaction lines with SM Work Order type referencing a job work order)

- AP (for AP transaction lines with PO type referencing an SM job work order).

Note: The update to Job Cost is handled via batch processing. However, this process occurs at different times depending on the work completed line type:

- Equipment / Inventory - The system creates and processes a batch (behind the scenes) when you save the work completed line and move off the record.

- Labor - The update to JC occurs once you process payroll and run PR Ledger Update.

- Miscellaneous - The update to JC occurs when you create and post a batch via SM Batches.

- Purchase - The update to JC occurs when you invoice the PO in AP Transaction Entry.

If you will be using Job Billing to generate invoices for job-related work orders, there are setup requirements that you must meet before you proceed. For more information, see [Enable Billing for Work Completed in Job Billing](/en/vista/vista/service-management/sm-invoices/about-billing-sm-job-work-orders/enable-billing-for-work-completed-in-job-billing).
If you do not have the Job Billing module, you must use the Accounts Receivable module to create invoices for work completed on a job work order. However, you will need to bill offline and then enter the invoices for the customer (associated with the job's contract) in AR Invoice Entry. For more information, see [About the AR Invoice Entry Form](/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-invoice-entry-form).

Related concepts

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)

- [About Capturing Work Completed for a Work Order](/en/vista/vista/service-management/work-orders/about-capturing-work-completed-for-a-work-order)

Related information

- [JB T&M Template Setup Form](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)

- [JB Bill Initialization Form](/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/jb-bill-initialization-form)

- [JB T&M Bill Edit Form](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-edit-form)

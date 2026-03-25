---
title: "About the JC Cost Adjustments form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form"
---

# About the JC Cost Adjustments form

Use this form to create adjustments to job costs that cannot otherwise be posted in other modules (such as Payroll or Accounts Payable) and interfaced to Job Cost.
Typically, you will enter cost adjustments to…

- offset incorrect postings interfaced from another module that can no longer be corrected in that module, such as a correction needed for payroll costs posted to the wrong phase code after the payroll week is closed;

- post additional costs that cannot be entered in other modules, such as job insurance costs that you choose not to enter through Accounts Payable;

- make month-end accruals for reversal in a subsequent month;

- make changes to the system-generated cost adjustments created when you run the Cost Allocations program;

- enter job cost beginning balances during installation startup.

On occasion, you may need to make cost adjustments for sources other than Job Cost. You can do this using the JC Type field, which allows you to identify the source to which the cost adjustment applies. However, since you cannot edit the actual record for which you are adjusting costs, the system makes the adjustment by creating one entry to back out the old information and one entry to enter the correct information.
 When making cost and/or revenue adjustments, there are two dates: a transaction date and a posting date. For cost adjustments, these two dates are stored in the JC Cost Detail (JCCD) table; for revenue adjustments, they are stored in the JC Revenue Detail (JCRD) table. The transaction date is entered for each transaction line in the batch, and is the ‘actual’ date a cost was incurred. The posting date is the ‘processing’ date for the batch. This date is entered when you post the batch in JC Batch Process, and is the same for the entire batch. It may be useful for reporting changes for a week.

## Field Tickets

Field tickets enable you to link labor, material, and equipment costs related to specific work activity on a job, and facilitate owner billing. When you add a cost adjustment entry, you can assign the entry to a field ticket associated with the contract for the specified job. You can assign multiple cost adjustment entries to a single field ticket, as long as the ticket is still open (that is, it has a status of O-Open in JC Field Ticket). Once the status is set to Closed, Approved, Rejected, or Billed, you can no longer post costs to that ticket.Note: Costs associated with approved field tickets only impact T&M billings; therefore, assigning field tickets to cost adjustments is only useful if the job's contract/contract item has a bill type of T&M or Both. Additionally, once you process a cost adjustment batch, entries associated with approved field tickets appear on the Cost Detail tab in JC Field Ticket for the specified field ticket.

 For more information about field tickets, see [JC Field Ticket Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form).

Click the links below for more information about cost adjustments.
[Intercompany Cost Adjustments](/en/vista/vista/costs-and-contracts/job-cost/costs/intercompany-cost-adjustments#concept-4450--en__concept-4450)
[Transaction & Offset Accounts](/en/vista/vista/costs-and-contracts/job-cost/costs/transaction--offset-accounts)
[JC Add Transaction To Batch Form](/en/vista/vista/costs-and-contracts/job-cost/costs/jc-add-transaction-to-batch-form)
[About the JC Initialize Reversals Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-initialize-reversals-form)

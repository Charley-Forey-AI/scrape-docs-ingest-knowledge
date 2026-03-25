---
title: "JC Field Ticket Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form"
---

# JC Field Ticket Form

Use this form to create and track field tickets for contracts. You can access this form from the Job Cost Programs menu or via the JC Contracts or PM Contracts forms by clicking on the Field Tickets tab and double-clicking in the grid.
Once you create a field ticket, you can then reference that field ticket when entering timecards, equipment usage, AP invoices / unapproved invoices, material usage, and purchase orders for a job so that project costs can be linked and pre-approved for billing by the customer.Note: It is important to note that costs associated with approved field tickets only impact T&M billings; therefore, assigning field tickets to labor, equipment usage, or cost adjustment entries is only useful if the job's contract/contract item has a bill type of T&M or Both.

You can post multiple labor, equipment, and cost adjustment entries to a field ticket, as long as the ticket is open (that is, the ticket's status is set to O-Open). Once the status is set to Closed, Approved, Rejected, or Billed, you can no longer post costs to that ticket.
When you approve the field ticket for billing (that is, you set the Status field to A-Approved), the system updates the Billing Approved By and Billing Date Approved fields (these fields are display only and cannot be edited). You can then create billings that include costs associated with the approved field tickets using the JB Bill Initialization or JB T&M Bill Edit forms. Once you create a billing, the system updates the Bill Month, Bill Number, and Bill Invoice fields for the field ticket associated with the contract/job. These fields are also display only and cannot be edited.

## Field Management Field Tickets

If you are using the Field Management web application, you can use the Field Ticket Dashboard to create a field ticket, enter costs associated with the field ticket (such as timecards and equipment usage), and then approve the field ticket.
 When you create a field ticket, it is automatically updated to JC Field Ticket. When you enter and save timecard and equipment usage, it is added to a timecard batch in PR Timecard Entry. Once you approve the field ticket (via the Field Ticket Dashboard), the system updates progress entry and material usage data entered for the field ticket to JC Progress Entry batch and JC Material Use batches, respectively. In addition, the system updates the Ticket Approved By and Ticket Date Approved fields on the JC Field Ticket form (these fields are display only and are only populated via Field Management).
When you are ready to bill the field ticket (after timecards are posted), you must set the Status field (in JC Field Ticket) to Approved. You can then generate a billing for the field ticket using JB Bill Initialization.
For more information about creating, editing, and approving field tickets in Field Management, see [Field Tickets](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:FM_000044:FM:FM) in the Field Management Help.

## Cost Detail

The Cost Detail tab displays all cost detail associated with the selected Field Ticket. The system populates this grid each time you post cost entries (such as labor, equipment usage, and cost adjustments) that reference the field ticket number, or when you manually add costs from other sources to the field ticket using the JC Field Ticket Add Costs form.
In addition to the job, phase, and cost type, other information includes, but is not limited to, the actual and posting dates, source, and billing information. Sources include the following:

- AP Entry

- AR Receipt

- EMRev

- IN MatlOrd

- JC CostAdj

- JC MatUse

- MS Tickets

- PO Receipt

- PR Entry

- SM WorkOrd

For more information about adding costs to a field ticket, see [Add / Remove Costs for a Field Ticket](/en/vista/vista/costs-and-contracts/job-cost/costs/add--remove-costs-for-a-field-ticket).

Select the following link for more information about using this form.
[Create a Field Ticket](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/create-a-field-ticket)

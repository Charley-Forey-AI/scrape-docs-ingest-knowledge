---
title: "JB T&M Bill Edit Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-edit-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-edit-form"
---

# JB T&M Bill Edit Form

Use this form to edit invoices created in JB T&M Bill Initialization or to enter a new invoice manually.
From this form you can also edit header and line detail, Job Cost detail,
 miscellaneous distribution information, or delete an entire invoice.
Note: To view all bills for the current JB company,
 select Options > Show All Invoices. All invoices display on the Grid tab. This display option is not
 saved and will not be displayed the next time you access the form.

You can set up billings automatically using JB T&M Bill Initialization or add them manually.
When you initialize T&M billings, all items on a contract with a Bill Type of “T&M” are added to the billing. For more information on the initialization process, see [About Initializing T&M Billings](/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/about-initializing-tm-billings).
When you enter a bill manually, much of the information on this form defaults
 once the contract is specified. This information includes the customer, billing address,
 and payment terms. As with initialization, only contract items with a Bill Type of
 T&M are added to the billing.
Once you initialize or manually add a billing, you can then edit the billing
 information to fine-tune your invoices. The following is a list of forms you can access
 to edit billing information. See the following articles for more information:

- [JB T&M Bill Lines](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-line-sequences-form): Use to edit line and
 sequence detail, as well as to access job cost detail for each line.

- [JB T&M All JC Detail Lines](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-all-jcdetail-lines-form): Use to edit
 the billing status of JC transactions or remove them from the billing.

- [JB T&M JC Detail for Lines](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-jcdetail-by-seq-form): Use to edit
 transactions for a specific sequence line.

- [JB Miscellaneous Distributions](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-the-jb-miscellaneous-distributions-form): Use to
 create miscellaneous distributions that interface to AR.

## Bill Status Tracking

The Bill Status Tracking section allows you to assign a JB reviewer group, and then track the review and approval process for Progress billings. Once you assign a reviewer group, the Reviewers tab shows the reviewers in the specified reviewer group. The Reviewer tab is display only.
Tip: You can change the field values in the Bill Status Tracking section only when the Status drop down value is either A-Active or C-Change.

## Field Tickets

The Field Tickets tab is (display only) and shows all field
 tickets associated with the selected billing. Field tickets only display on this tab
 once they are approved and added to a billing manually, via initialization (in JB
 Bill Initialization), or using the JB T&M JC Detail Fill Grid form.
You can delete all costs for a ticket from the bill by selecting the related bill line/ticket in the grid and clicking Delete. The system prompts you to delete all bill lines associated with the field ticket. Only select Yes if you want all bill lines associated with the ticket deleted. If you select No, the delete process is canceled and the bill line/ticket remains intact.
Once you delete a bill line/ticket from this grid, the system sets
 the field ticket status back to Approved (in JC Field Tickets) and clears the
 Bill Month and Bill Number fields.

## Recipients / Delivery Tracking

The Recipients and Deliver tabs are used in conjunction with the Invoice Delivery feature and provide information about the recipients and delivery history for each invoice (respectively).
Regardless of whether you initialize billings (in JB Bill Initialization) or add them manually, the Recipients tab automatically defaults the recipients you have defined for the contract in the [JC Contract Recipients Detail](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-recipients-detail-form) form. You can edit the delivery information for existing recipients (delivery method, name, email or mailing address), add new recipients, or delete recipients.
The Delivery tab allows you to track the delivery history for invoices associated with the billing. This tab is display only, and shows you the delivery ID, the date the invoice was sent (delivered), delivery status (Delivered or Failed), and the recipient, as well as the recipient's email and/or address information (depending on the delivery method).

For more information, see the following articles:

- [About Updating Previous Billed Amounts on
 Future Bills](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/about-updating-previous-billed-amounts-on-future-bills)

- [About Changing Interfaced or Closed-Month Billings](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-changing-interfaced-or-closed-month-billings)

- [About Closed Contract Billings](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/about-closed-contract-billings)

- [Copy Associated Attachments](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/copy-associated-attachments)

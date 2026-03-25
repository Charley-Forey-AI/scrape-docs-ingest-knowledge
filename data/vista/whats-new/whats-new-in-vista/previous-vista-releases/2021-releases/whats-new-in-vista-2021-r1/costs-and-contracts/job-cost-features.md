---
title: "Job Cost Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r1/costs-and-contracts/job-cost-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r1/costs-and-contracts/job-cost-features"
---

# Job Cost Features

Vista 2021 R1 delivers on user-requested Job Cost enhancements, fixes, and other improvements.

## Associate Material Use Transactions with Job Cost Field Tickets

You can now assign field tickets to material use entries, enabling you to link related costs to specific work activity on a job, and facilitate owner billing. To enable this functionality, a new Field Ticket field was added to the JC Material Use form.
When you enter a material use transaction (Inventory or Miscellaneous type), you can associate it to a field ticket for the specified job/contract; however, the field ticket must be Open. You cannot post to field tickets with a Closed, Approved, Rejected, or Billed status.
Once you post the material use batch, the system automatically creates an entry on the Cost Detail tab of JC Field Ticket for each material use transaction, with a Source of JC MatUse.
Note: Costs associated with approved field tickets only impact T&M billings; therefore, assigning field tickets to material use entries for a job is only useful if the job's contract/contract item has a bill type of T&M or Both.

For more information about the Field Tickets feature, see [JC Field Ticket Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form).

## Allow Creating Separate T&M Bills for Customer POs with Approved Ticketed Costs

You can now create separate T&M billings for costs associated with JC Tickets that reference a customer purchase order.
A new Separate Inv checkbox was added to the Customer POs tab on the JC Contract Master form. If you select the checkbox for a customer PO, the bill initialization process (in JB Bill Initialization) creates a separate billing for that customer PO, and groups all costs for approved field tickets associated with that customer PO on the same billing.
If you do not select the Separate Inv checkbox for a customer PO, all ticketed costs for that customer PO are included on the same billing as other non-ticketed costs for the associated contract.
For related information, see the [Job Billing](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r1/costs-and-contracts/job-billing-features) release notes.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.

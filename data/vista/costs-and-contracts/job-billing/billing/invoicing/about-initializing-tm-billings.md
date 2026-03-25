---
title: "About Initializing T&M Billings | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/about-initializing-tm-billings"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/about-initializing-tm-billings"
---

# About Initializing T&M Billings

To initialize T&M billings, contract items must be set up as ‘T&M’ or ‘Both’ bill types in JC Contract Items.
You must have selected one of the following options in the Initialize Option field in JB Billing Initialization:

- B-Progress (P) and Both (B) Items – Initialize (B) Items as T&M

- T-T&M (T) Items Only

You can initialize billings by contract range or by processing group. If you initialize by contract range, you can initialize a single contract or a range of contracts. If you initialize by processing group (defined in [JB Processing Group](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-processing-group-form)), the system generates billings for all contracts assigned the specified processing group. If there are customers assigned to a processing group, initialization processes those billings first using the template assigned to the customer in JB Processing Group. Customer billings have a bill header and lines, but no Job Cost detail. (You will typically use these types of billings for monthly maintenance billings or other non-job related billings.)
If you are using the Field Tickets feature, use the T&M Field Tickets drop-down to specify whether to include or exclude cost detail associated with approved field tickets. You can also specify an Approval Cutoff Date to control which approved field tickets are included. Once initialization is complete, cost detail records associated with field tickets are displayed in the JB T&M Bill JCDetail By Seq grid.
Note: If a field ticket is associated with a customer PO that is flagged for separate billing (the Separate Inv checkbox is selected for the customer PO on the Customer POs tab in JC Contract Master), the bill initialization process creates a separate billing for that customer PO, and groups all costs for approved field tickets associated with that customer PO on the same billing.

For more information about the field ticket initialization options, see the [Ticketed Cost Option](/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/jb-bill-initialization-form/field-definitions-jb-bill-initialization-form#concept-9667--en) and [Approval Cutoff Date](/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/jb-bill-initialization-form/field-definitions-jb-bill-initialization-form#concept-4484--en) F1 help. For more information about field tickets, see [JC Field Ticket Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form).
Use the T&M Job Cost Detail Transaction Range section to specify a beginning/ending cost detail date, and a cost detail cutoff month. These dates identify the dates/month through which cost detail will be pulled from Job Cost to include on billings. You may enter date in one or all of these fields. If you make an entry in all fields, the cost detail record must meet all requirements in order to be included in the invoice generating process. If you will be using a different cutoff date for labor detail, check the Use Different Labor Cutoff Date box and then specify the labor cutoff date.
Note: When determining the costs to include based on the specified date range/cutoff month/labor cutoff date, the system uses the ‘Actual Date’ posted in JC (i.e., the date entered on the transaction).
If you are initializing both progress and T&M items (Initialize Option B), use the Progress Billing Date Range section to specify the beginning and ending bill date for the billings processed as progress. (Note: These dates are informational only and do not control the data included when initializing billings. For example, you might use these dates to identify the range this billing covers.)
Once you have entered the selection criteria, click the Initialize Bill button to begin the initialization process. During initialization, the system uses the template assigned to the contract in JB Contract Info to compile the appropriate cost data from the JC Cost Detail table (JCCD) based on the template specifications, and stores it in the JB files. This detail prints according to the invoice format you have created using Crystal Reports, or from any of the standard formats provided with Vista™.

If you are using the Invoice Delivery feature and have set up recipients for the selected contract(s) in [JC Contract Recipients Detail](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-recipients-detail-form), the initialization process automatically adds the recipients to the Recipients tab in JB T&M Bill Edit. You can then modify, add, or delete recipients as needed for each billing.
Note: The Prebill checkbox (in JB T&M Bill Edit) is used to bill AP detail before detail exists in Job Cost. If the previous billing has a setting of Prebill, the next billing in the job cost range triggers an error. Billings will still generate, but the error report provides an error message stating that the transaction was possibly pre-billed. The error report includes the month and the bill, line, and sequence numbers. To prevent billing of the transaction, use the JB T&M Bill JC Detail form (accessed by clicking the JCDetail button while focus is on the related Line Seq) to change the item’s status to ‘Non-Billable’.
The following are related topics:

- [JB T&M Bill Edit Form](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-edit-form)

- [JB Bill Groups Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-bill-groups-form)

- [About Initializing Progress Billings](/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/about-initializing-progress-billings)

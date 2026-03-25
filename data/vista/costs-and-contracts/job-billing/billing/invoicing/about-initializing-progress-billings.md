---
title: "About Initializing Progress Billings | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/about-initializing-progress-billings"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/about-initializing-progress-billings"
---

# About Initializing Progress Billings

To initialize progress billings, contract items must be set up as ‘Progress’ or ‘Both’ bill types in JC Contract Items.
You must have selected one of the following options in the Initialize Option field in JB Bill Initialization:

- P-Progress (P) Items Only

- B-Progress (P) and Both (B) Items – Initialize (B) Items as T&M

- X-Progress (P) and Both (B) Items – Initialize (B) Items as Progress

You must first specify whether to initialize billings by contract range or by processing group. If you initialize by processing group (defined in JB Processing Group), the system generates billings for all contracts assigned the specified processing group. If you initialize by contract range, you can initialize a single contract or a range of contracts.
You also have the option to restrict initialization by the item bill group assigned to contract items in JC Contract Items. Initialization will include only those contract items with a bill group matching the one specified here. See Related Topics below for more information on Bill Groups.
If you are initializing only progress billings (Initialize Option P or X), use the Progress Billing Date Range section to specify the beginning and ending bill date for the initialized billings. Note: These dates are informational only and do not control the data included when initializing billings. For example, you might use these dates to identify the range this billing covers.

If you are initializing progress billings with T&M items (Initialize Option B), you will also need to specify a beginning/ending cost detail date and a cost detail cutoff month. These dates identify the dates/month through which cost detail will be pulled from Job Cost to include on billings. You may enter a date in one or all of these fields. If you make an entry in all fields, the detail must meet all requirements in order to be included in the invoice generating process.
If you will be using a different cutoff date for labor detail, check the Use Different Labor Cutoff Date box and then specify the labor cutoff date.
Note: When determining the costs to include based on the specified date range/cutoff month/labor cutoff date, the system uses the ‘Actual Date’ posted in JC.

If you are using the Invoice Delivery feature and have set up recipients for the selected contract(s) in [JC Contract Recipients Detail](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-recipients-detail-form), the initialization process automatically adds the recipients to the Recipients tab in JB Progress Bills. You can then modify, add, or delete recipients as needed for each billing.
The following are related topics:

- [JB Progress Billing Form](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/jb-progress-billing-form)

- [JB Processing Group Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-processing-group-form)

- [JB Bill Groups Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-bill-groups-form)

- [JC Contract Items Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-items-form)

- [About Initializing T&M Billings](/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/about-initializing-tm-billings)

- [Set Up Recipients for JB Invoice Delivery](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/set-up-recipients-for-jb-invoice-delivery)

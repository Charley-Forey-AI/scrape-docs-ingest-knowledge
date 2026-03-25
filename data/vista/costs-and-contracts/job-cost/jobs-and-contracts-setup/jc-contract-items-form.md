---
title: "JC Contract Items Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-items-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-items-form"
---

# JC Contract Items Form

Use the JC Contract Items form to set up and maintain items
 for a contract.
You can only access this form by double-clicking an
 item record on the Items tab in JC Contracts, or by selecting any item in the grid
 and then selecting Records > Open
 Related Record.
Note: Information entered here automatically updates PM Contract
 Items, since both programs share the same file (JCCI).
A contract item is a breakdown of the contract, according to the owner’s coding. For example, if the contract is for a general contractor, the contract items will typically be the schedule of values. If the contract is for a heavy/highway contractor, then contract items will typically be the state’s bid items. These items will be the breakdown on a job billing, generally a progress billing.

- Start Month - You must specify a start month for each contract item. The
 start month is used to store the original contract amount and cost estimates
 for the contract item. If you change the start month after you set up
 original amounts and cost estimates for the contract item, the system will
 move the original amounts and cost estimates to the new month.Note: If you change the contract's start
 month (header level), you will receive a message asking if you want to
 update contract items with the old month to the new month. Because
 original amounts and cost estimates follow the contract item start
 month, consider the ramifications before selecting to update
 items.

- Bill Type - For each item on the contract, the
 Bill Type option determines how the item is to be billed
 (in Job Billing):

- Progress - Items will be billed on a percent
 complete or units complete basis.

- T & M - Items will be billed on a Time &
 Materials basis.

- Both - Items will be billed on a Time &
 Materials and/or Progress basis. You will typically use this option
 for items that you bill on a T&M basis with a progress backup.

- None - Items will not be billed through Job
 Billing.

Note: If you change the Bill
 Type for an item after it has been billed, a message
 displays informing you that the item has been previously billed, and
 that the change may result in differences to the Previous Billed amounts
 in JB. The record will be saved; however, you may need to edit the
 previous amounts manually.
For information on how items are initialized based on
 bill type, see JB Bill Initialization in Related Topics below.

- Taxes - For each contract item you set up, you must
 determine whether or not taxes will be posted, and how they will be updated
 and tracked. If not posting taxes to the contract item, leave the Tax
 Code field blank.

- Markup Rate - If you will be billing on a T&M basis,
 the markup rate specified here will be used when the Markup
 Option field is set to S-Rate for a template
 sequence. If the template sequence does not specify a markup rate, the
 markup rate specified here is used. Each item on the billing will use its
 own rate when calculating billing amounts, unless the sequence type is Total
 Addon, and a contract item has been specified for the template sequence. In
 which case, the markup rate for the specified contract item is used. If that
 contract item does not have a markup rate specified here, then each item on
 the billing will use its own markup rate.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC
 Contracts
[](/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/jb-bill-initialization-form)JB Bill Initialization

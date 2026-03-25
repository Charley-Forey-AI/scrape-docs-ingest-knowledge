---
title: "About Closed Contract Billings | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/about-closed-contract-billings"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/about-closed-contract-billings"
---

# About Closed Contract Billings

For both Progress and T&M billings, the ability to add or
 make changes to a billing once you have closed the contract will depend on the ‘Allow Posting
 to Soft-Closed Jobs’ and ‘Allow Posting to Hard-Closed Jobs’ flags in JC Company
 Parameters.
For both Progress and T&M billings, the ability to add or make changes to a billing once you have closed the contract will depend on the Allow Posting to Soft-Closed Jobs and Allow Posting to Hard-Closed Jobs flags in JC Company Parameters.

- If you allow posting to closed jobs and the billing’s contract is soft- or hard-closed, the contract's description will display as "Contract is closed" in red. However, the system allows you to save the record.

- If you do not allow posting to closed jobs and the billing's contract is soft- or hard-closed, in addition to the contract description indicating the contract is closed, you will receive a message stating that the contract is soft-closed (or hard-closed) and that billing is not allowed.

If you are posting a T&M Billing, you cannot save the record. However, if you are posting a Progress Billing, you will be able to save the record. This allows you to add a bill header for releasing retainage. You will be able to view item detail, but you will be unable to change any values for bill items. Once you have released retainage and interfaced the billing, you will be unable to change information on the bill header.

GL Considerations
If you allow posting to a closed contract and the
 contract is 'hard closed', the system will post old and new values to the Closed Revenue
 Account specified in JC Departments. It is assumed that when the contract was closed,
 revenue was updated (moved) from the Open Revenue Account to the Closed Revenue Account
 either automatically or via journal entries. If a contract is 'soft closed' or 'open', the
 system updates GL in the normal manner.
The following are related topics:

- [JB Progress Billing ](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/jb-progress-billing-form)

- [JB T&M Bill Edit ](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-edit-form)

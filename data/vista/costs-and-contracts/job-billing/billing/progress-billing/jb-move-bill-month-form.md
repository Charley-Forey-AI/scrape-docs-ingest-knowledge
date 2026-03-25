---
title: "JB Move Bill Month Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/jb-move-bill-month-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/jb-move-bill-month-form"
---

# JB Move Bill Month Form

Use this form to move active job billings (Progress, T&M, and Both) to a new month.
One common use for this feature is when you need to close out a month, but have invoices that are not yet ready for interfacing to Accounts Receivable. Moving the bills to a new month allows you to close out the month without having to delete unposted billings and manually re-enter them in a new month.
Although you will typically move a bill forward to the next month, you can move a bill back to an earlier a month if needed.
In order to move a bill, the following criteria must be met:

- The bill's current and target months must be open within the AR and GL ledgers.

- The bill and any subsequent bills for that contract must be unposted (not yet interfaced to AR), and cannot exist in an open interface workfile or batch.

When you move a bill, the following occurs:

- For Progress and Both-type bills:

- If the bill is moved to a later month, all subsequent bills for that customer/contract within the same month are also moved to the later month, and previous amounts and % complete for bill items adjusted. If any bills exist for the contract in the later month, they are moved forward in that later month to maintain bill order.

-  If the bill is moved to an earlier month, any previous bills for that customer/contract within the original month are also moved to the earlier month. Any subsequent bills created for that contract remain as they are.

- For straight T&M bills (those where all items are T&M):

- Regardless of whether you are moving the bill to an earlier month or a later month, only the selected billing is moved, since T&M bills are not dependent upon 'previous' values, nor are they all associated with a contract.

- All Job Cost detail associated with the bill is updated, regardless of whether the bill is moved to a later month or earlier month.

- For all bill types, when you move a bill to a new month, the bill number changes based on the last bill number for the destination month.
In addition, if you are using the Invoice Delivery feature, all recipients defined for the billing (on the Recipients tab in the related billing form) are also moved.

Click the link below for more information about moving bills to a new month.
[Move Active Job Bills to a Different Month](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/move-active-job-bills-to-a-different-month)

Related information

- [JB T&M Bill Edit Form](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-edit-form)

- [JB Progress Billing Form](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/jb-progress-billing-form)

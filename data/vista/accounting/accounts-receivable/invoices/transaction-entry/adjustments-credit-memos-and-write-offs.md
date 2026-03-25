---
title: "Adjustments, Credit Memos, and Write-Offs | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/invoices/transaction-entry/adjustments-credit-memos-and-write-offs"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/invoices/transaction-entry/adjustments-credit-memos-and-write-offs"
---

# Adjustments, Credit Memos, and Write-Offs

Adjustments, Credit Memos, and Write-Offs are entered in the
 AR Invoice Entry form, but are posted somewhat differently in that they are applied to
 existing invoices and therefore, are not assigned invoice numbers.
Additionally, they can be used to make adjustments or amendments to invoices that were interfaced to AR from Job Billing or Material Sales. Note: If an adjustment/credit memo/write off is needed on an invoice created in JB, it is strongly recommended that the change be made in JB and interfaced through to AR. The only exception is if you will no longer be billing on the contract (i.e. correction made after final billings.)

## Adjustments

Adjustments are generally used to amend invoices that have been posted incorrectly. If you need to back out an existing invoice, it is strongly suggested that you DO NOT post a negative invoice. Instead, use a negative Adjustment transaction to correct the amount. Using a negative Invoice transaction may result in the original invoice balance displaying incorrectly in the age analysis report.
You can also use an adjustment to add amounts to an invoice. For example, you may have posted an invoice for $69.00 that should have been for $96.00. You want to correct the amount, but GL has already been closed, so the original invoice cannot be accessed. Therefore, you could apply an adjustment to the original invoice to add the difference.
Since adjustments are applied to an existing invoice transaction, they will be properly reported on various AR reports, such as the AR Age Analysis report.

## Credit Memos

Credit memos are used to reduce the amount owed by a customer on a selected invoice. For example, you might use a credit memo to credit amounts for damaged or returned goods, or for an invoice on which the customer was over billed.
Credit Memos and Adjustments will update Job Cost if the Job Cost
 Interface level in AR Company Parameters is set to Transaction Line (one
 JC transaction/invoice line item). If a Credit Memo or Adjustment is applied to a
 contract-related invoice, and the contract has been purged from the JC Contracts file
 (JCCM), no JC update will occur.

## Write-Offs

Write-offs are used to remove debts from Accounts Receivable that are considered uncollectible. Although posted in the same manner as Adjustments and Credit Memos, they DO NOT update JC, regardless of the update level, and they debit a write-off account set up by receivable type in AR Receivable Types. Write-offs can be entered manually (in AR Invoice Entry) or automatically (in AR Automatic Write-Off).

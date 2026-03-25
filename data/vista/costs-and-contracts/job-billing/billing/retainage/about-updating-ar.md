---
title: "About Updating AR | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/retainage/about-updating-ar"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/retainage/about-updating-ar"
---

# About Updating AR

When release retainage batches are run (JB Batch Process), the
 system checks AR to determine whether the amount being released is greater than the
 available open retainage in AR plus the amount being brought over by the current bill.

 If so, a warning displays in the Error List report, noting that there is not enough
 retainage for AR to release. If the release amount is equal to or less than the
 available amount, the system credits the previous billing in full until meeting the
 percentage.
Note: Contracts determine the available retainage, but customer/contract does
 not. However, when interfacing to AR, the system validates the available retainage by
 customer/contract. If the released amount exceeds the available amount, a warning
 displays in the Error List report. In this case, check the available retainage for
 customer using applicable AR reports.
Released retainage appears in the customer account in AR after
 JB Interface runs. The interface process creates AR credit transactions for the released
 retainage, assigning them a transaction type of “R” and applying them to each of the
 previous billing invoices for the contract. If you release less than 100% of the
 retainage, the system credits the previous billing in full until meeting the percentage.
 The system then creates a new invoice (with a transaction type of “R”) for the released
 retainage, which provides a single transaction for applying receipt of payment in AR.
Note: The “R” transaction type displays in reports such as AR Customer Accounts
 by Contract.
The system assigns the new retainage invoice to the retainage
 receivables type or a current receivables type based on the Release Retainage to Current
 A/R checkbox setting. This also determines which Account Receivables GL account the
 system debits and whether the invoice appears in the Retainage column or on an AR aging.

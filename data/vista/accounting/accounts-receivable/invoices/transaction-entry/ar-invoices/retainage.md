---
title: "Retainage | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/invoices/transaction-entry/ar-invoices/retainage"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/invoices/transaction-entry/ar-invoices/retainage"
---

# Retainage

Retainage is the portion of an invoice's gross amount that the
 customer will not be required to pay until a later date, usually
 upon completion of the job.
The designated retainage amount is held by the system until it is either paid or released. Although you will generally designate retainage at the time of invoice entry, you can designate retainage at the time you post a payment to the invoice.
Retainage is initially set up for a contract item in
 JC Contract Items. Retainage is also set up at the
 contract level in JC Contracts, but is only used as
 a default when adding contract items. (If it is
 determined retainage should apply to a contract
 after the items have been set up in PM or JC, the
 retainage must be added or changed for each item.)
 Job Billing and Accounts Receivable will default the
 retainage for each item, and AR only records the
 retainage at the item level.
When posting invoices in the AR Invoice Entry program, the customer to whom the invoice applies must have their Use Retainage option selected (in AR Customers) before retainage can be calculated.
If the invoice is contract-related, the retainage percent assigned to the contract item is used to calculate the retainage amount. If the invoice is not contract-related, the retainage percent must be entered manually.

## Applying Payments to Retainage

Retainage can be paid at any time, even if it has not yet been released. If you elect to apply a payment to the retainage balance of any given invoice, you may do so by entering the payment manually, or letting the system apply the payment to retainage automatically.
If you wish to have the system apply the payment
 automatically, check the Include Retainagebox in the AR
 Initialize Receipts form (appears each time the >> button is used in AR Cash
 Receipts). The system will automatically apply the appropriate portion of the
 payment to the retainage balance of a selected invoice, as long as the payment
 sufficiently covers both the retainage amount and the total due on the invoice. If
 the payment is not sufficient, the payment will be applied only to the current
 invoice balance; you will need to apply payment to retainage manually.

## Releasing Retainage in AR

The release of retainage is handled using the AR Release Retainage program.
When you release retainage, the original invoice is credited the retainage amount and a new transaction is created with a description of "Released Retainage", making cash application easier. Retainage can be released in fixed amounts or by percentage of the retainage balance.
How the system handles release retainage
 transactions depends on how the Release Retainage to Current A/R
 checkbox is set in AR Company Parameters:

- If the option is checked, the system will report the released retainage transaction as a current transaction, age it on its own transaction date, and if a separate GL account is used for AR Retainage, it will credit this account and debit the regular AR account.

- If the option is not checked, the system will treat released retainage transactions as retainage and they will remain in the retainage GL account.

Retainage is tracked by the system in both Job Cost and Accounts Receivable. When processing and releasing retainage, the following tables are affected:

- JCCI (Contract Items) - Retainage is tracked at the contract item level.

- ARTL (Transaction Lines) – This table tracks the retainage applied to each invoice in AR, including those interfaced from Material Sales and Job Billing. When the system processes the release retainage transaction, it uses this table to determine the amount of retainage to release.

Because the system tracks contract revenue, paid, and retainage amounts in different tables, this can sometimes cause a discrepancy in the billed-to-date and paid-to-date amounts that display in the AR Release Retainage program. This discrepancy may be caused by one of three conditions:

- The Job Cost tables were not properly updated when the AR startup was implemented.

- The JC Cost Interface level in AR Company Parameters is set to 'No Update'.

- Multiple customers share the same contract. (Retainage is released only for currently selected customer.)

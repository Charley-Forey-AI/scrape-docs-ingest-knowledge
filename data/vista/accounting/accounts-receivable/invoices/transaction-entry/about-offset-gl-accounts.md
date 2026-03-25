---
title: "About Offset GL Accounts | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/invoices/transaction-entry/about-offset-gl-accounts"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/invoices/transaction-entry/about-offset-gl-accounts"
---

# About Offset GL Accounts

The GL accounts assigned to AR invoices lines are used to
 offset the AR entry in the General Ledger.
 When you enter invoices in AR Invoice Entry, you must assign a GL offset account. This account is generally a revenue account and is use to offset the AR entry in General Ledger.
When you enter revenue, the system supplies the default GL account by one of two methods, depending on the type of invoice:

- Contract Invoices — The default
 GL Account comes
 from the Open Revenue
 Acct (or Closed
 Revenue Acct if the job/contract is closed) field from the JC
 Departments form for the department that shown in the JC Contracts form
 Department
 field.Note: You can change this default value if the
 Allow GL Account Override
 When Posting Revenue checkbox in JC Company Parameters form
 (GL Revenue tab) is selected.

- Non-Contract Invoices — The default GL Account is the Revenue account assigned to the Receivable Type. The Receivable Type used comes from one of two possible locations:

- The Receivable Type field in the AR Customers form.

- The Receivable Type field in the AR Company Parameters form, if none is specified in the AR Customers form.

## Finance Charge Write-Offs

If you are writing off finance charges, whether manually or using the Auto Write-Off feature in AR Invoice Entry (File > Auto Write-Off), the account that defaults for the transaction line is the Write-Off account for the transaction's receivable type.
If a Write-Off account is not specified (which may be typical for finance charge receivable types), the account defaults as null and may be entered manually. However, the account that is actually debited for the write-off amount is the FC WriteOff account specified for the transaction's receivable type (in AR Receivable Types). This 'switch' occurs during batch processing. Once you validate the batch, if you review the audit lists, you will note that the AR Invoice Audit List shows the 'Write Off' account specified in the transaction line. However, the AR GL Invoice Distribution List shows the actual account being debited as the FC WriteOff account.

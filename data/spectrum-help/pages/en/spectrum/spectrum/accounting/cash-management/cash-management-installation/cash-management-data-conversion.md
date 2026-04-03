---
title: "Cash Management Data Conversion | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/cash-management/cash-management-installation/cash-management-data-conversion"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/cash-management/cash-management-installation/cash-management-data-conversion"
---

# Cash Management Data Conversion

Learn how to complete the cash management data conversion
 installation. The steps on this list correspond to the Conversion Worksheet found in the
 User's Guide.

## Part 1

- Complete the Cash Management Installation screen.

- Set the processing date to the conversion date using
 Processing Date Change.

- Enter bank accounts using Account Code File Maintenance if a
 bank import file will be used. Print the associated listing.

- Enter file layout for ASCII import using Clearing Data File
 Format Maintenance. Print the associated listing.

- Enter bank information in the Accounts Receivable
 Transaction Code File Maintenance screen.

## Part 2

- Conversion Date:_________________

- Confirm that there are no Accounts Receivable cash receipts,
 Accounts Payable payments, or Payroll cycles are in progress during the Cash
 Management conversion.

- Confirm that the Post to G/L checkbox on the
 General Ledger Installation - Properties tab is clear for Cash Management
 transactions.

- Set the processing dates to the new period for Cash
 Management using Processing Date Change.

- Create the list of outstanding checks from Accounts Payable
 and/or Payroll for each bank account as of the conversion date using the Cash
 Management Utility to Convert Outstanding Checks.

- Confirm that the Allow entry of opening
 balance checkbox in the Cash Management Installation screen is
 selected.

- Enter the beginning balances for each bank account of the
 conversion date using Bank Reconciliation Entry. The beginning balance in each
 bank account will generally be set equal to the ending balancen of the prior
 month's reconciled bank statement. The beginning balance in each account should
 also be adjusted for any checks that cleared the bank but were not included in
 step 3 above.

- If applicable for this company, leave the Allow entry of opening balance
 checkbox in the Cash Management Installation screen blank after
 the beginning balances have been recorded.

- If applicable, deselect the Force G/L balance before next
 reconciliation checkbox in the Cash Management Installation
 screen after all pre-conversion checks reflected in the GL balance, but not
 reflected in the outstanding checks, are cleared.

- If applicable for this company, select the Post to G/L checkbox for
 Cash Management in the General Ledger Installation.

---
title: "Reconciling a Bank Statement Using a Cleared Check File | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/data-entry-overview/bank-reconciliation-entry/reconciling-a-bank-statement-using-a-cleared-check-file"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/data-entry-overview/bank-reconciliation-entry/reconciling-a-bank-statement-using-a-cleared-check-file"
---

# Reconciling a Bank Statement Using a Cleared Check File

Many banks will provide you a file of cleared checks. You
 can use this file when reconciling a Cash Management bank account to your bank statement.
Complete the following step-by-step procedure to reconcile your
 period end bank statement with your Spectrum records.
Bank statements can also be [Reconciling a Bank Statement Manually](/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/data-entry-overview/bank-reconciliation-entry/reconciling-a-bank-statement-manually).

1. Download the bank transactions for the current period in ASCII file format and save the file in the Spectrum data directory.

1. On the Site Map screen, select Cash Management  >  Data Entry  >  Bank Reconciliation.

1. Click the Import button to import the bank data.

1. On the Import Cleared Checks screen, press Enter through all of the fields to accept the software defaults and then click OK. The software will produce an error report for any checks that (a) have cleared the bank but are not in the software or (b) have cleared the bank in an amount that differs from what is entered in the software.

1. On the Site Map screen, click Cash Management  >  Data Entry  >  Bank Reconciliation.

1. Complete the Bank account, GL date, Statement date, and Ending balance fields or press Enter to accept the software defaults.

1. Click the Deposits button. Because Spectrum does not read deposits in the cleared check file, they must be reconciled manually.

1. To reconcile deposits one at a time, select the checkbox next to each deposit that you want to reconcile.Tip: To reconcile all deposits at once, click the red check mark
 button next to the Deposits button. In the Select Items window, complete the
 Beginning date, Ending date, and Check number fields. In the Options section,
 select Reconcile and then click OK. On the Bank Reconciliation Entry screen, clear
 the checkboxes next to any deposits that you do not want to reconcile.

1. At this point, the Difference fields in the Statement Recon and GL Recon sections should show $0.00. If not, further investigation is required to determine the cause of the imbalance. If both Difference fields are $0.00, click OK until the Listing button displays.

1. Click the Listing button and print the Bank Reconciliation Summary Listing. Keep the listing with the bank records.Note: On the Bank Reconciliation Summary Listing, the cleared
 deposits and cleared checks should match the amounts on the bank statement. If
 not, it could be because reverse payments show up as a negative deposit in
 Spectrum as a negative deposit and may show up as a withdrawal on the bank
 statement.

1. Click the Update button.

1. On the Bank Reconciliation Update screen, complete the Bank account code field, select Continue and then click OK until you return to the Site Map screen.

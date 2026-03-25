---
title: "About the GL Month End Close Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/general-ledger/gl-setup-and-maintenance/about-the-gl-month-end-close-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/general-ledger/gl-setup-and-maintenance/about-the-gl-month-end-close-form"
---

# About the GL Month End Close Form

When you are finished posting and processing entries for a month, you can use the GL Month End Close form to close the sub ledgers and/or the general ledger for a specified month.
 The act of closing a month indicates that it is complete and accurate, and that no additions or corrections are needed. Once closed, you will still be able to run journal and trial balance reports as well as financial statements on the month, but you will no longer be able to post or make corrections to the month.

## Subsidiary Ledgers

You have the option to close all of the subsidiary ledgers at one time or to close
 the AP and/or AR independently from all other sub ledgers.
Closing AP and/or AR separately allows
 you to restrict posting in AP and/or AR, while leaving other modules open for
 month-end activities (e.g. posting cost and/or month-end adjustments, running
 allocations, etc.).
Be aware that closing a month in AP
 and/or AR before closing the other subsidiary ledgers will limit the batches created
 in AP and/or AR, as well as batches initiated in other modules containing AP and/or
 AR transactions:

- Closing AP limits batches
 created in PR AP Update, SL Update, MS Hauler and Material Payments, and IM
 uploads of AP transaction data.

- Closing AR limits batches
 created in JB Progress Billing, JB T&M Bill Init, JB Interface, JB Batch
 Process, MS Invoice Edit, MS Invoice Initialize, and IM uploads of AR
 transaction data.

Note: If closing only AP and/or AR, you must uncheck
 the All Others option, since the last month closed in AP and AR must be equal to or
 later than the last month closed for all other subledgers. Likewise, choosing to
 close 'all other' subledgers requires also closing AP and AR; therefore, all options
 will be checked and the AP/AR options disabled (preventing closure of other
 subledgers while AP and AR are still open).
You can keep the subsidiary ledgers open
 for as many months as desired, depending on the maximum number of open months
 allowed (defined in GL Company Parameters).

## General Ledger

The General Ledger may be closed in any month equal or prior to the subsidiary
 ledgers. In other words, you cannot close the General Ledger for any month in which
 the subsidiary ledgers have not been closed.

## Close Check

When this button is pressed, a system-wide search is made for unprocessed information
 based on the modules being closed.
If none is found, the OK button can be
 pressed to close the month. However, if unprocessed information is found, a message
 displays indicating that the month is not ready to close. You will need to check
 each of the tabs at the bottom of the form to identify the information that must be
 processed before you can close the month.

- Unposted
 Batches — Lists all unposted batches. Information shown
 includes the HQ company, month, batch ID, source, the batch creator, who the
 batch is in use by, and status.

- AP
 Prepaids — Lists all unprocessed prepaid transactions.
 Information shown includes the AP company, month, transaction #, vendor, and
 CM reference number.

- AP Unapproved
 Invoices**— Lists all unapproved invoices. Information shown
 includes the AP company, month, sequence, and vendor. Informational only—not
 required to close a month.

- JB
 Invoices — Lists all unprocessed JB invoices. Information
 shown includes the JB company, bill month and number, and contract/customer.


- PR Pay
 Periods — Lists all payroll periods that have not been fully
 processed and closed. Information shown includes the PR company, PR group,
 pay period ending date, and the final update status for JC, EM, GL, and AP.


- MS Uninvoiced
 Tickets — Lists all unprocessed MS invoices. Information
 shown includes the MS company and month, and the transaction, customer,
 ticket, and haul transaction number.

- MS Hauler
 Payments** — Lists all unprocessed hauler payments.
 Information shown includes the MS company, month, transaction number,
 vendor, ticket number, and haul transaction number. Informational only—not
 required to close a month.

- MS Interco
 Invoices — Lists all unprocessed intercompany MS invoices.
 Information shown includes the MS company and month, the invoice number,
 ‘sold to’ company, and invoice date.

- MS Vendor
 Payments** — Lists all unprocessed MS vendor payments.
 Information shown includes the MS company and month, transaction number,
 material vendor, and ticket number. Display on this tab is limited to 500
 records, so the list may not show all existing hauler payments.
 Informational only—not required to close the month.

- SM
 Invoices - Lists all unprocessed SM invoices. Information
 shown includes the SM company, GL month, invoice number, SM work order and
 work order scope, and the 'bill to' customer.

- PM
 Corrections - Lists all PM module error corrections that
 have not been interfaced.

Note: For SM users only: If you have entered
 miscellaneous work completed lines on a work order, but have not pulled them into a
 batch (via SM Batches) and processed them, the close check will display a
 message in the message box above the grid indicating that there are unprocessed
 miscellaneous work completed lines for the post month. You will need to pull the
 transactions into a batch (in SM Batches) and process them in order to close
 the month.If you have pulled Miscellaneous work completed lines into a batch, but
 have not posted the batch, they will display on the Unposted Batches list with a
 Source of "SMLedgerUp".

** A month can be closed when unapproved
 invoices and/or hauler payments exist, as long as no other unprocessed detail
 exists. If all other detail is processed, but you have existing unapproved invoices
 and/or hauler payments, you will receive a message (or messages) indicating that you
 will be closing Sub Ledgers that still have unapproved AP invoices and/or MS hauler
 payments once you press OK to close the month. You can select Yes to go ahead and
 close the month or No to cancel.
Use the information shown to locate and
 process the necessary items. Once all information has been processed, the month can
 be closed.
Note: If you are only closing AP, the close check will
 look for unposted batches with an AP, MS HaulPay, or MS MatlPay source. If only
 closing AR, the close check will look for unposted batches with an AR, JB, or MS
 source.

## Reopening a Month

You may reopen a month in either the subsidiary ledgers or General Ledger by entering
 any previously closed month.
Once the month has been entered, the
 following message is displayed:
“Last month closed will be rolled back
 to XX/XX. You will only be able to post batches between XX/XX and XX/XX Continue?
Be aware that if you answer Yes and
 reopen the closed month, this may restrict the processing capabilities of other
 employees, depending on the Max # of Open Months specified in GL Company Parameters.
 Because of the implications of this action, it is suggested that access to this
 program be restricted to only one or two people.
Note: After answering yes to continue, you must select Close Check, then answer Yes to the "You will be reopening the General
 Ledger (or Sub Ledgers). Do you wish to continue?" prompt to successfully reopen the
 month.

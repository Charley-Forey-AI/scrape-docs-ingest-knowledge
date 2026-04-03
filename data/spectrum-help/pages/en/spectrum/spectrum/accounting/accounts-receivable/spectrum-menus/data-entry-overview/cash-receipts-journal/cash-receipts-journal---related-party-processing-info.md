---
title: "Cash Receipts Journal - Related Party Processing Info | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/cash-receipts-journal/cash-receipts-journal---related-party-processing-info"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/cash-receipts-journal/cash-receipts-journal---related-party-processing-info"
---

# Cash Receipts Journal - Related Party Processing Info

When processing related party invoices, note how the override
 G/L codes will default.

- Cash G/L comes from the Transaction Code.

-
A/R Trade G/L comes from the related party override trade G/L code on the customer.

-
A/R Retention comes from the related party override retention G/L code on the customer.

## About Cash Receipts Journal Validation

Spectrum validates the transaction details during this report/update's compilation
 process. For the date portion of the validation, Spectrum compares the current
 Accounts Receivable minimum/maximum date range with the individual check/adjustment
 date. Spectrum also confirms that the G/L account code is valid and available for
 use. If an error is found during the compilation, the following message displays on
 the last screen of the report: "G/L account errors have been encountered. All errors
 must be corrected before proceeding." Additionally, a message displays directly
 below each disallowed detail line to indicate the specific problem.
During the update, the software runs through one update that posts
 to both the module's master and history files and to the General Ledger. Error
 correction entries are not saved by the software if the user cancels before the
 updated confirmation takes place. If the user corrects all errors and completes the
 update, the changes will be reflected in the General Ledger log file and the
 Accounts Receivable history report.
If Spectrum discovers an error, the G/L Error Correction screen
 automatically displays, allowing you to enter the necessary changes. Once you close
 the G/L Error Correction screen, Spectrum will recompile the data and apply the
 corrections; the report will reprint automatically.
Zero-dollar payments do not show up on the report.
 If you cancel out of the A/R Cash Receipts Journal Update screen
 prior to continuing, no error correction changes will be saved in the Accounts
 Receivable or General Ledger log files.
If the Accounts Receivable Post to G/L checkboxes on the
 General Ledger are not selected, the software will not perform error validation.

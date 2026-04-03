---
title: "Sales Journal / Update Validation | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-invoice-entry/sales-journal--update/sales-journal--update-validation"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-invoice-entry/sales-journal--update/sales-journal--update-validation"
---

# Sales Journal / Update Validation

Spectrum validates the transaction details during this report/update's compilation process. For the date portion of the validation, Spectrum compares the current Accounts Receivable minimum/maximum date range with the invoice date. Spectrum also confirms that the G/L account code is valid and available for use. If an error is found during the compilation, the following message displays on the last screen of the report: "G/L account errors have been encountered. All errors must be corrected before proceeding." Additionally, a message displays directly below each disallowed detail line to indicate the specific problem.
If Spectrum discovers an error, the G/L Error Correction screen automatically displays, allowing you to enter the necessary changes. Once you close the G/L Error Correction screen, Spectrum will recompile the data and apply the corrections; the report will reprint automatically.
During the update, the software runs through one update that posts to both the module's master and history files and to the General Ledger. Error correction entries are not saved by the software if the user cancels before the updated confirmation takes place. If the user corrects all errors and completes the update, the changes will be reflected in the General Ledger log file and the Accounts Receivable history report.
If the Accounts Receivable Post to G/L checkboxes on the General Ledger are not selected, the software will not perform error validation.
Because the Recurring Invoice Update, Draw Request Update, and Reverse Open Invoice Entry/Update screens automatically link to the Sales Journal/Update screen, the entries in those screens will also receive G/L error protection.

---
title: "A/P Transaction Update | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-invoice-entry/ap-transaction-update"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-invoice-entry/ap-transaction-update"
---

# A/P Transaction Update

When the report is complete, the software automatically proceeds to the update screen. After the A/P Transaction Register has printed correctly and is accurate, click Continue to run the update.

- When the update is run, it sorts information by G/L code first, then by job so that you can see both the G/L totals and then subtotals by job on one report.

- If you choose to sort the report by Time of entry, the report will sort by G/L date and time of entry.

- Running the update will post information to the General Ledger, Equipment Control, Work Order and Job Cost files. This information may not be changed after the update.

-  If you cancel out of the A/P Transaction Report/Update
 screen before completing the update, the changes made in the [G/L Error Correction](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/gl-error-correction)
 screen will not be saved to the A/P G/L distribution history file. The A/P
 Transaction Update will add one record to the Work Order Cost History table for each
 invoice distribution line associated with work order # and Direct Work Order Cost G/L
 account.

- If the G/L account is set to Direct
 equipment cost, the Equipment code and Cost category code will be
 updated from the invoice distribution line.

Warning: If the A/P Transaction Register is out of balance, updating
 will not be allowed. Once the transaction report prints correctly, this update
 should be run, even if the General Ledger module is not on your system. "Balanced
 entry" protection is incorporated into this function to assure the General Ledger
 will stay in balance. Consult Viewpoint Support for instructions if it is
 necessary to correct an out-of-balance error.
When a purchase order is received and then the A/P invoice is posted for
 a Time + Material job, the vendor name and item description is recorded in the Time +
 Material module. The Time + Material Installation screen provides an
 A/P post vendor name or item code checkbox. For operations selecting Vendor, the invoice
 update writes the vendor name to Time + Material module. If option item is selected, the
 item code and item description will post to Time + Material module, instead of the vendor
 code and item description. For stock items originating from Purchase Order, the price
 updated to Time + Material is determined based on the material level field in the
 Time + Material Job Billing Maintenance. If the field is blank,
 cost is updated. If level 1-5 is specified, the associated price from Item
 Master File Maintenance is used. Any associated markups are calculated based
 on the same figure.
If this is a sub-job billed from a master job, the software will read
 for job-specific setup rates for the master job, and if none are found use standard
 settings. If this is a sub-job billed at the sub-job level, the software will read for
 job-specific setup rates for the sub-job first, and if billing rates are not found then the
 master job, and if none are found there use standard settings.
Note: About A/P Transaction Update Validation, Spectrum validates the
 transaction details during this report/update's compilation process. For the date portion
 of the validation, Spectrum compares the current Accounts Payable minimum/maximum date
 range with the invoice date. Spectrum also confirms that the G/L account code is valid and
 available for use. If an error is found during the compilation, the following message
 displays on the last screen of the report: "G/L account errors have been encountered. All
 errors must be corrected before proceeding." Additionally, a message displays directly
 below the detail line (in the Detail transaction register and Transaction register
 formats), indicating the specific problem. If Spectrum discovers an error, the G/L Error Correction screen automatically
 displays, allowing you to enter the necessary changes. Once you close the G/L Error Correction screen, Spectrum
 will recompile the data and apply the corrections; the report will reprint automatically.
 During the update, the software runs through one update that posts to both the module's
 master and history files and to the General Ledger. Error correction entries are not saved
 by the software if you cancel before the updated confirmation takes place. If you correct
 all errors and complete the update, the changes will be reflected in the General Ledger log
 file and the Accounts Payable history report.

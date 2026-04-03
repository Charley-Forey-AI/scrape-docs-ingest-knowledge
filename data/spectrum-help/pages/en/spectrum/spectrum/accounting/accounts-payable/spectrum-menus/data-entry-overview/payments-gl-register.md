---
title: "Payments G/L Register | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/payments-gl-register"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/payments-gl-register"
---

# Payments G/L Register

This option is used to update Accounts Payable payment figures to the General Ledger. Transactions from manual, void, computer checks and credit card payments will all be updated; only pre-paid checks are not processed through this screen; they are processed through [A/P Transaction Register](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-transaction-register) instead.

- This screen displays automatically after running the Manual Check Log Print, Void Check Register, and A/P Payment Register to help ensure that the Accounts Payable information is updated on a timely basis.

- By default, the G/L Detail Report will show only manual, void, or regular checks depending on the previous update that was performed. Print and review the report and verify its accuracy before proceeding with the update.
Important: This report should be retained as a permanent audit record of the company.
Note: Spectrum validates the transaction details during this report/update's compilation process. For the date portion of the validation, Spectrum compares the current Accounts Payable minimum/maximum date range with the G/L date on the individual check. Spectrum also confirms that the G/L account code is valid and available for use. During the update, the software runs through two updates - first posting to the Accounts Payable master and history files and then posting to the General Ledger. If Spectrum discovers an error, the [G/L Error Correction](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/gl-error-correction) screen displays, allowing you to enter the necessary changes. Once you close the G/L Error Correction screen, Spectrum will recompile the data and apply the corrections; the report will reprint automatically.

[Sample Reports - Payments G/L Detail Report](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/payments-gl-register/payments-gl-detail-update/sample-reports---payments-gl-detail-report)
[Payments G/L Detail Report - G/L Account Sequence](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/payments-gl-register/payments-gl-detail-update/sample-reports---payments-gl-detail-report/payments-gl-detail-report---gl-account-sequence)
[Payments G/L Detail Report - Vendor Sequence](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/payments-gl-register/payments-gl-detail-update/sample-reports---payments-gl-detail-report/payments-gl-detail-report---vendor-sequence)

---
title: "Reverse Last Draw Request - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/draw-request-entry/reverse-last-draw-request/reverse-last-draw-request---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/draw-request-entry/reverse-last-draw-request/reverse-last-draw-request---field-descriptions"
---

# Reverse Last Draw Request - Field Descriptions

A reference for completing the fields on this screen.
Field
 Description

Selections
JobEnter the number of the job for which a draw request is to be reversed. The job description displays.
If an alternate bill-to address is specified for the selected contract in Contracts, then this address will be used transferred during the reversal. If the job status is Completed and the Disallow revenue entry checkbox is selected in Job Main Properties, you will not be able to reverse draw requests referencing a contract for the selected job.

CustomerThe customer name appears; press Enter. If the customer code is not recorded in the job file, or you want a different customer, enter the customer code.
If the customer code's status is set to Not used, then no entry is allowed. If an alternate bill-to address is specified for the selected contract in Contract File Maintenance, then this address will be transferred during the reversal.

ApplicationEnter the number of the draw request application to be reversed. This must be the last posted draw request. If the application entered has not yet been posted, or if an application following the one entered has already been posted, an error message occurs.
To view all applications for the specified job/customer, press F4 or double-click on this field. Only the most recently posted draw request may be reversed.

Overrides
G/L dateEnter the General Ledger date for the credit memo.
This date is available for use when posting to a different G/L period than the one on the original invoice.

Batch codeEnter the Accounts Receivable batch code or press Enter to accept the default.
Invoice dateDefault value is the Application date as seen when pressing F4 in the Application field. Press Enter to accept it, or enter a different invoice date.
Clear current period amounts?Clear this checkbox to reverse the draw request, but retain the numerical values that have been entered for the application. Otherwise, select this checkbox to clear the numerical values. Typically, this field should be left cleared.
This is provided as a convenience for correction. If many line items need to be corrected, select this checkbox to clear values. If only one or two lines will be changed, clear this checkbox to retain the "current" percentages.

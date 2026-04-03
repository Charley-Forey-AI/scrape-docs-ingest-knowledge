---
title: "Summary Billing Entry - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/draw-request-entry/summary-billing-entry/summary-billing-entry---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/draw-request-entry/summary-billing-entry/summary-billing-entry---field-descriptions"
---

# Summary Billing Entry - Field Descriptions

Use this table for reference when completing the fields on this screen.
Field
Description

Job
Enter the job number for this draw request.

Customer
The customer code will default from the Jobs screen. If
 the customer code is not recorded in the Jobs screen,
 or a different customer is desired, enter the customer code. If the customer
 code's status is set to Not used, then to entry is
 allowed.

Application #
Enter the application number for this draw request. Data will display corresponding to the requested draw request application.

Application date
The application date displays. When the multiple rates window is used, the components' rates are based on the date in this field.

Period to
The period-ending-date for the application's work displays.

Architect's project #
The architect's project number displays, if applicable.

Contract

Contract sum to date
The current dollar amount for the contract displays. Click the lookup icon to view contract information.

Total completed and stored to date
The completed and stored dollar amount displays.

Retention

Work completed
The total dollar amount for completed work displays.

Retainage
Enter the retention percent for the work completed to date. The retention dollar amount will be calculated, then displayed after the % sign. Press Enter to accept the calculated amount, or enter the desired dollar amount for work completed retention.
If the Retention %
 override checkbox is selected for any item in the
 Draw Request Billing Entry screen, the amount in
 this field may not be changed here. If you try to change the retention
 amount or percent in this field, a window with the following message
 displays: Detail overrides
 exist – please use the window to set summary retention. Click
 OK to close
 this message and open the Work Completed Retainage
 window. You can change the retention percentage and amount in the Work Completed Retainage
 window.

Materials stored
The dollar value of materials stored but not yet used displays.

Retainage
Press Enter to accept the default retention percent for materials stored. Otherwise, enter the desired retention percent for stored materials for this fixed price billing. Note that on the final billing for a job, the retention may be set to zero. This will enable the software to bill the retention amount for the job.
The retention dollar amount will be calculated, then displayed after the % sign. Press Enter to accept the calculated amount, or enter the desired dollar amount for stored materials retention.
If the Retention %
 override checkbox is selected for any item in the
 Draw Request Billing Entry screen, the amount in
 this field may not be changed here. If you try to change the retention
 amount or percent in this field, a window with the following message
 displays: Detail overrides
 exist – please use the window to set summary retention. Click
 OK to close
 this message and open the Materials Stored Retainage
 window. You can change the retention percentage and amount in the Material Stored Retainage
 window.

Total retainage
The total amount retained displays.

Balance

Total earned less retainage
The total amount earned, minus any retainage amounts, displays.

Less previous certificates at payment
The total amount, minus any previous billing amounts, displays.

Tax code
Enter the sales tax code for this draw request, or enter * for multiple sales tax codes. Sales tax codes may be up to 15 alpha-numeric characters long.
After the code has been entered, the tax percentage displays and tax is calculated. Enter an asterisk (*) in this field to allocate sales tax among multiple sales tax codes, or click the Tax Allocation button. A window will then open allowing you to enter multiple tax codes for various portions of the dollar amount on this billing.

Tax allocation
Click this button to open the [Sales Tax Allocation window](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/sales-tax-allocation-window) window to enter multiple sales tax codes for the selected invoice or draw request.
If the Allocate PST on holdback checkbox is selected on the sales tax
 code entered on Contract Defaults, the Tax allocation button will be
 hidden. When the Allocate PST on holdback checkbox is selected,
 Spectrum will calculate provincial sales tax on holdback for Canadian
 companies.

Current payment due
The current amount due displays.

Balance to finish, including retainage
The dollar value of work not yet completed displays. The software calculates this number as the Total completed and stored to date amount subtracted from the Revised contract amount plus Total Retainage.

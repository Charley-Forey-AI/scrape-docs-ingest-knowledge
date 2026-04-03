---
title: "Sales Tax Allocation window | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/sales-tax-allocation-window"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/sales-tax-allocation-window"
---

# Sales Tax Allocation window

Use this window to enter multiple sales tax codes for the selected invoice or draw request. For each tax jurisdiction, enter the associated portion of the billing total attributed to that code.
When the draw request is updated, the sales tax allocation list automatically resets to contain one tax code, which is first tax code listed in this window for the selected draw request.
Field
Description

Total amount subject-to-tax
The portion of the taxable amount for which you have entered tax codes displays.

Unallocated
The unallocated amount of the invoice displays in this field.

Total amount allocated
The total amount subject to tax minus the unallocated amount displays in this field.

Total tax amount
The total taxable amount of the invoice displays.

Composite tax rate
The average total of all the tax rates will display in this field.

Tax code
Enter the sales tax code for this portion of the invoice. This must be a valid sales tax code previously defined in Sales Tax Code Maintenance. The first tax code defaults in Invoice Entry from the Contracts screen, if specified. The tax code description displays to the right of this field.
The first code defaults in Summary Billing Entry from the first allocation sales tax code on the previous draw request and from Contracts for the initial application.

Tax rate
Based on the sales tax code entered, the tax percentage displays from the sales tax code file. No entry is allowed.
Whenever the Accounts Receivable processing date changes, Spectrum examines the rate file to determine if the current processing date equals or exceeds the next tax rate's effective date. If so, the next tax rate becomes the current rate.

Invoice amount
The taxable dollar amount of the invoice for which no tax has yet been specified displays. Press Enter to accept the default, or enter the desired partial dollar amount.
Note that on line one, the full taxable invoice amount displays. After line one is complete, line two displays the difference between the full taxable invoice amount and the amount specified on line one. Up to six lines are provided for sales tax allocation. The full taxable amount must be allocated among specified sales tax codes.

Tax amount
Once Enter is pressed from the Amount column, the software calculates the tax based on the percent and dollar amount specified. Press Enter to accept the calculated amount, or enter the desired tax amount.

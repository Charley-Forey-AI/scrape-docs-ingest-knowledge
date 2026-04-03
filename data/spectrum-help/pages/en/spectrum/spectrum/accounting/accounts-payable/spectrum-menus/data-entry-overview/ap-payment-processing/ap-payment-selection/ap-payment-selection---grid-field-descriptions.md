---
title: "A/P Payment Selection - Grid Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/ap-payment-selection/ap-payment-selection---grid-field-descriptions"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/ap-payment-selection/ap-payment-selection---grid-field-descriptions"
---

# A/P Payment Selection - Grid Field Descriptions

Use this table for reference when completing the fields on this screen.
Fields/Buttons
Descriptions

Pay All button
Clicking this button will set the amount in the Make payment column equal to the Outstanding amount (less any discount) for all eligible rows currently displayed. In addition, the Take discount amount will be set equal to the Discount column for all rows. Rows already selected for payment elsewhere (for example, Manual Check Entry) will not be changed.

Clear All button
Clicking this button will set the amount in the Make payment and Take discount columns to zero for all rows currently displayed.

Add Invoice
After you have selected a group of invoices, you may add another one to the list using this button.
Follow these steps:

1.  Enter the vendor code, invoice # and invoice type (or use the search windows to find).

1. You are prompted to enter the Payment amount for the current balance, retention and any discounts.

1. Click OK and this invoice will be added to the bottom of the list.

Status filter
Use this button to determine which types of records will display in the grid. Options include those items already selected for payment, those items that are eligible for payment, and those items that are currently on hold (and therefore not available for payment).
All 'Pymt disallowed' lines are processed like 'Eligible' records during status selection.

Line
Vendor
Name
Invoice #
Type
These fields do not allow changes.
The screen only provides access to vendors meeting the selection criteria when
 the processing group was initiated in the [New Processing Group](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/ap-payment-selection/new-processing-group) window. In
 other words, vendors assigned a 'Payment method' (in [About Vendor Payment Setup](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-main-properties/about-vendor-payment-setup)) that was not selected in the New Processing
 Group window will automatically be excluded from the selection process.

Due days
This column is calculated using the Prepare to pay as of date and the due date of the current row.

Disc days
This column is calculated using the Prepare to pay as of date and the discount date of the current row.

Outstanding
This column displays the amount available to pay from open items.

Inquiry button (magnifying icon)
Click this button to display the Vendor Invoice Inquiry window where you can
 see the invoice details. If you have security authorization to the
 Change Invoice Due
 Dates screen, you will be able to change the hold status,
 check stub remarks, due date, discount due date, and discount amount in this
 window.

Pay button
Click this field once to move to the Make payment column and enter a payment amount.
Double-clicking this field will set the amount in the Make payment column equal to the Outstanding amount (less any discount) for the selected row. In addition, the Take discount amount will be set equal to the Discount column for this row.

Make payment
Enter the amount of the payment (full or partial) you want to make for this line item. To pay all items in full, click the Pay All button.

Take discount
Enter a value for open item invoices that have discounts.

Hold
Select this checkbox to put an item on hold and zero out any amounts in the
 Make payment
 and Discount taken
 columns. You can only access this checkbox if you have security
 authorization to the Change Invoice Due Dates
 screen.

Status
Options include:

- Hold - if the item is on hold.

- Eligible - if the Make payment and Take discount columns are blank.

- Selected - if the Make payment and Take discount columns are non-zero.

Due date
Check stub remarks
Job
Invoice date
Discount date
Discount
Previously applied
Original amount
Much of this information defaults from the invoice header or has been entered elsewhere.

Payment method
The selected vendor payment method will display in this column:
 Check, Electronic,
 Comdata, or ePayments.
Tip: If multiple payment methods are selected for the same pay cycle, sort by this column to select invoices by payment method.

Cost center
This field only displays if cost centers/cost groups are enabled for the current company in the Enterprise Installation screen.

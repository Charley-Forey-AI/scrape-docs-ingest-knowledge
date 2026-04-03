---
title: "Vendor Recurring Invoice Entry - Field Descriptions (header) | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/vendor-recurring-invoice-entry/vendor-recurring-invoice-entry---field-descriptions-header"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/vendor-recurring-invoice-entry/vendor-recurring-invoice-entry---field-descriptions-header"
---

# Vendor Recurring Invoice Entry - Field Descriptions (header)

Use this table for reference when completing the fields on
 the header portion of the screen.
Fields/Buttons
Descriptions

Vendor
Enter the vendor code or press F4 to select from a list of available vendor codes.
Note: If you press F4 to display the
 Search Vendors window, there is an additional
 window in the Add/Change field to be used to add new
 vendors or make revisions to existing information

Recurring #
Enter the recurring invoice number for this vendor/invoice. Up to 999 recurring invoices may be entered for each vendor. This number is used only in the Vendor Recurring Invoice Entryportion of Spectrum; when invoices are created by the software, they are numbered "AUTO1," "AUTO2," and more.

Invoice type
Use the drop -down menu to select whether the selected line item is for an Invoice or Credit memo.
Note: Credits are entered with positive dollar amounts. The system
 recognizes credit memos as negative amounts.

Total amount
Enter the total invoice dollar amount, for example, the amount due for rent, the loan payment amount, or the insurance premium due. Positive amounts should be used for both invoices and credit memos.

Invoice day
Enter the day of the month that should be used for the invoice date (1-31). This invoice date is used to age the invoice, and is also used for calculating the invoice due date. When the invoice date specified (such as "31") is greater than the number of days in the month, the actual final day of the month is used.

Frequency code
Select the invoice frequency from the drop-down menu: Monthly, Quarterly, Annually.

Recurring status
When adding records, this field defaults to Active. To accept the default,
 press Enter. To
 change the recurring invoice's current status, enter the letter
 I or use the drop-down menu to select the
 Inactive option. Entry in this field is required.

Limit recurrences?
Select this checkbox to limit the frequency of this recurring invoice. Once
 this checkbox is selected, the More Invoice
 Information window and Range of recurrence
 section is enabled, which allows you to set the parameters for the limits of
 the recurrence. If you select this checkbox and assign a date restriction
 to the invoice, the recurrence's end date displays with the invoice's
 information on the Recurring Invoice Listing.

History

Last invoice #
The identification number associated with the vendor's recurring invoice defaults from the Recurring History file.

Last create date
The date that the recurring invoice was created defaults from the Recurring History file.

Invoices created
This field include access to a drill-down Recurring Invoice
 History window.

More Info button

Click this button to display the More Invoice
 Information window.
View field descriptions

> Routing code
Enter an invoice approval routing code, if applicable.

Invoice remark

Range of recurrence

Starting invoice date
If the Limit recurrence checkbox is selected, this field defaults to the current Accounts Payable processing date, but changes are allowed.

End by
Select this option to enter a stop date for the recurring invoice.
 For example, if you want the invoice to stop as of January 2, 2012, enter
 010212 in this field. This date can exceed the maximum
 Accounts Payable processing date, but cannot be earlier
 than the date entered in the Starting invoice
 date field.

End after
Select this option to stop the recurring invoice after a specified number of
 instances. For example, if you want the invoice to stop
 after four recurrences, enter 4 in
 this field. Entry in this field must be a positive and
 whole number.
Note: If the End by option is selected, then the End
 after ___ invoices field is blank. If a
 number is entered in this field, when the Recurring
 Invoice Update is run, Spectrum compares the maximum
 invoice count recorded in this field with the number of
 invoices already created. If the invoices created count is
 equal to or greater than the maximum set in this field,
 Spectrum sets the recurring invoice status to Inactive.

Payment due calculation
Select either the From invoice date or From 1st of next month option from the radio group to determine if the payment due date is calculated based on the day of the month entered in the previous field.
If the From 1st of next month option is selected, enter the number of days to be used in calculating the invoice due date in the Days field. For example, if rent is due on the first day of every month, enter "1".

Discount due calculation
Select to determine any discounts calculated from the invoice date, or select to determine any discounts calculated from the first of the month.
After pressing Enter, enter the number of days to be used in calculating the discount. For example, 3 would mean that a discount may be taken if paid within three days of the invoice date. Also enter the discount percent.

Remit to alternate payment location?
If the Default payment location? checkbox is selected in the [Vendor Locations](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-main-properties/vendor-locations) screen, the remit checkbox will automatically be selected and the Location code defaults, along with the corresponding name and address. You can use the available drop-down arrow to select a different location code.
If no location code is present, the vendor name and address displays.

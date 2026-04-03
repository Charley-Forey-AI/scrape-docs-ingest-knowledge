---
title: "New/Edit Purchase Order Detail Line | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/purchase-order-receiving-detail/newedit-purchase-order-detail-line"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/purchase-order-receiving-detail/newedit-purchase-order-detail-line"
---

# New/Edit Purchase Order Detail Line

Use this window to add a new detail line to the purchase order during receiving. If a new row is added, you are allowed to re-open this window to edit fields while still adding the new invoice entry.
Note: If the purchase order is revision 001 or higher, any fields that are display only in Purchase Order Entry are display-only in this window.
Field/Button
Description

Item on order

Item code
Enter the inventory item code being ordered. The item code entered here should have been previously defined in Inventory Item File Maintenance (if Inventory Control is installed or Price Update is used) or in Purchase Order Item Code Maintenance. The item description will display to the right of this field.

- For one-step receiving, both stock and non-stock items can be added.

- For two-step receiving, only non-stock items can be added.

If the item is an invalid item, an error message will prompt whether to enter a new item code or proceed as a non-stock item. Alternately, to enter a non-stock item, insert an exclamation point as the first character in this field.
If this is a lump sum purchase order, the item code must be non-stock.
If there are no revisions in the Other Purchase Order Information window, this field will be hidden. If revisions are present, click the notepad icon to open the Revision History Inquiry window.

Description
Enter a description for the non-stock item codes in this field. This field will be display-only for stock items.
 Click the Additional button to open the Additional Itemization on Form window. Use this window to add additional notes about the item description. This window will be display-only for pre-existing rows from the Purchase Order Receiving Detail window.

Quantity
For unit price orders, enter the quantity of the item being ordered.
Note: If this is a lump sum P.O., the quantity is automatically set to 1 and this field is skipped.

Unit of measure
The unit of measure for this line item displays in this field. Press Enter to accept, or enter a new unit of measure. This field will be display-only if the unit of measure was added in a prior revision.
 If C displays in this field, the price is per hundred. If M displays in this field, the price is per thousand. If either C or M displays on a non-stock line, the extension is per-hundred and per-thousand respectively.
When the phase and cost type is changed, the unit of measure will be automatically re-assigned from the new phase.
When editing a non-stock line item, if the unit of measure is changed reset the price-per-factor so that the extension will be correct.
 When you press Enter to exit this field, a dialog box will display containing the text found in the Message field in Vendor Special Cost Maintenance. If a dialog box does not display, the Message field in Vendor Special Cost Maintenance is blank or the vendor doesn't have any special costs set up.

Warehouse
The warehouse code for this item will default from the Form Info window or the Default warehouse code from Inventory Control Installation). If this code is valid, and the One warehouse? checkbox is selected, this field will be display only. If the checkbox is not selected, a different valid code can be entered in this field. If the default warehouse code is not valid (or blank),
If this is a non-stock entry or direct cost line, this field will be blank and skipped.
This field will be display-only if the warehouse was added in a prior revision.

Unit price
Enter the price per unit of the item being ordered, or the price will default as follows:

- If there is a job special cost for the designated item, this price will default first.

- If there is a job special cost for the 'category' of the designated item, this price will default second.

- If there is a vendor special cost for the designated item or 'category' of the designated item, this price will default third.

- If there are no special costs found, the price will default from Inventory Item File Maintenance.

- If the item is configured to use the Standard cost costing method, the warehouse standard cost will default here. If the warehouse-specific standard cost is blank or zero, the standard cost from the Item Main Properties screen will be used instead.

Discount %
Enter the discount percent for this line number, if applicable, or press Enter to accept the default from Vendor Special Cost Maintenance. When the discount percentage is changed, the extension or the line is automatically adjusted accordingly.

Extension (before tax)
The extension total for this line number displays. The extension = units ÷ price per factor X unit price and excludes sales tax.
 If C displays in the unit of measure (UM) field, the price is per hundred. If M displays in this field, the price is per thousand. If either C or M displays on a non-stock line, the extension is per-hundred and per-thousand respectively.

Distribution

G/L account
Press Enter to accept the default General Ledger account for this vendor. Otherwise, enter the G/L account code for this line transaction. This account must have been previously set up in G/L Master File Maintenance. If this item is a direct cost account, entry of a valid job or equipment code will then be required.
This field will be display-only if the G/L account was added in a prior revision.
When entering P.O. Receiving lines in Vendor Invoice entry that include freight or other miscellaneous charges, the Distribution fields in this window will default from the last line of the purchase order in context to simplify the process. the Operator can override these defaults and keep all existing validations.
If the cost center feature is enabled in the Enterprise Installation screen for this company, if you change the G/L account code, cost center security validation is performed. Spectrum compares the new G/L account's list of shared cost centers with the cost center assigned to the line. You will be permitted to enter any G/L account, regardless of its cost center security because the correct override to use cannot be determined until the account work-in-progress flag is known.

Job
Phase
Cost type
If the selected G/L account is direct job cost the following fields appear in this section:

- Enter the Job to which the item should be charged, or press Enter to accept the default from the main screen.

- Enter the Phase to which the item should be charged, or press Enter to accept the default. Note that the default comes first from the Inventory Item File Maintenance. If the phase code field in Inventory Item File Maintenance is blank, then the phase defaults from the previous line transaction.

- Enter the Cost type to which the item should be charged, or press Enter to accept the default. Note that the default comes first from the Inventory Item File Maintenance; if the cost type field is blank in Inventory Item File Maintenance, then the cost type associated with the specified G/L code in the chart of accounts. Finally, it defaults from the previous line transaction.

If the phase cost-to-date amount will exceed the revised estimate amount, an error message will appear if the Enable Phase over revised estimate warning in invoice detail checkbox is selected in the Accounts Payable Installation.
If this is a sub-job transaction set up on a master job, double-click on this field to search phases for the sub-job. This will allow you to easily select a phase set up on a master job, but not present on the sub-job. Spectrum will add a new phase to the sub job if the current job is a sub-job of a valid master job, the phase lengths of both jobs match, and the Phase + Cost type combination for the current job is valid and not 'Complete'.

Equipment
Cost category
Equipment W/O
If the selected G/L account is direct equipment cost the following fields appear in this section:

- Enter the Equipment code in this field, or press Enter to accept the default. This field will be hidden if the Equipment Control module is not installed.

- Enter the Cost category code in this field, or press Enter to accept the default. This field will be hidden if the Equipment Control module is not installed.

- Enter an Equipment work order number. If a closed work order is entered in this field, a warning displays, but does not prevent further data entry. The equipment code must match equipment code on the Equipment work order. This field will be hidden if the Preventive Maintenance module is not installed.

Work order
Site equipment
Component
Service contract
Unit bill
If the selected G/L account is direct work order cost the following fields appear in this section:

- Enter a Work order in this field. If the current invoice originated from Purchase Order Receiving, the work order number will be display-only. The work order number will default from the previous line when entering multiple detail lines. This field will be hidden if the Work Order module is not installed.

- Enter the Site equipment ID in this field. The Site Equipment code will default from the previous line when entering multiple detail lines. If this detail line has already been selected for billing in Work Order > Material Entry, no changes are permitted. This field will be hidden if the Work Order module is not installed.

- Enter a Component ID. This field will only be enabled if components are set up for the previously selected site equipment. The Component code will default from the previous line when entering multiple detail lines. If this detail line has already been selected for billing in Work Order > Material Entry, no changes are permitted. This field will be hidden if the Work Order module is not installed.

- Enter a Service contract number. The contract number will default from the previous line when entering multiple detail lines. If the work order is changed, entry in this field will be removed and a new service contract will need to be entered. This field will be disabled if the Service Contract module is not present, or no contract exists for the equipment/component combination. If a contract is specified in the work order header, this contract # will default if valid for the equipment component and the Operator will not be allowed to assign a different contract # on the work order. If a contract is not specified in the in the work order header, the Operator will be allowed to enter any combination of contracts (or blank contract) in the work order detail. If this detail line has already been selected for billing in Work Order > Material Entry, no changes are permitted.

- Enter a Unit billing price in this field. If the invoice originated in Accounts Payable, this field will be accessible for entry. If the invoice originated in Purchase Order Receiving, this field will be view-only. If the previously specified work order is for Time + Materials, the software will automatically calculate the lowest price for a stock item. For more information on this calculation, refer to the Determining the Material Price in-depth topic in the Purchase Order help. The Operator can still edit the Unit billing price before continuing with further purchase order entries. The unit billing price is only calculated from within the Work Order Cost Detail window. For non-stock items, if the Operator edits the Unit cost, Quantity, or Work order fields the software will re-compute the Unit billing price. For stock items, if the Operator edits the Work order field the Unit billing price will be recalculated. To calculate the Unit billing price based on a different date, click on the Inquiry button to open the Item Price Inquiry window. This column will be hidden if the Work Order module is not installed for the current company.

Other info

Delivery date
The purchase order delivery date will display in this field.
This field will be display-only if the tax code was added in a prior revision.

Message
Enter a description or message for this item, if desired. This field will allow entry of up to 250 characters.

Cost center
If the cost center feature is enabled, the Cost center row will appear on the grid and only purchase orders you are allowed to access will display on this page. This is determined by comparing the cost center assigned to the purchase order with cost centers in your scheme, and if the purchase order cost center is not present, then the purchase order will not be displayed.

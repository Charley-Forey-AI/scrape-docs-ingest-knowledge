---
title: "Purchase Order Entry - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/purchase-order-entry/purchase-order-entry---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/purchase-order-entry/purchase-order-entry---field-descriptions"
---

# Purchase Order Entry - Field Descriptions

Use the table below for assistance when completing the fields on this screen.
Field/Button
Description

Preferences
Click this button to open the [Operator PO Entry Preferences](/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/purchase-order-entry/operator-po-entry-preferences) window.
 This button will not be available if a purchase order is opened in
 context.
Save and New PO
Click this button to save the current
 purchase order and start a new purchase order.
Save and Continue Entry
Click this button to save the current
 purchase order and move to the next entry line, or start a new purchase order.
 This is helpful in cases of lengthy entries.
Header

Purchase order
Enter the purchase order
 number.
Vendor
Enter the code of the vendor with whom
 this order is being placed. A lookup window is available for viewing existing
 or adding new vendor codes. Note: When adding
 a new purchase order, if the specified vendor has any Document Tracking
 warnings, these will be displayed immediately.

For
Select whether the purchase order is
 for a warehouse, job or work order and specify the corresponding code.

- If a default warehouse code was specified in
 Inventory Control, this code will default. If the warehouse was not
 specified, no detail lines are added, and this window is not opened, the
 purchase order will be saved without a warehouse code.

- If this window was accessed in context to a job, the
 job code will default.

- If the Work Order module is not installed, the work
 order option will not be available.

Purchase amount
The purchase order total (before tax)
 displays in this field.
Sales tax
The sales tax total calculated from the
 tax settings in the grid details displays in this field.
Purchase order total
The sum of the purchase amount and
 sales tax displays in this field.
Purchase order status
The current purchase order status will
 be displayed in this field: Proposed, Open or Closed. To default the status of new
 purchase orders, click the Preferences button on the command bar and select the
 Default new purchase order
 status.
When editing an existing
 purchase order, you will conditionally be allowed to set the status to
 Proposed, Open, or Closed, depending on your security authorization. After
 packing list or receiving has occurred, or the purchase order is at revision
 001 or higher, this field cannot be switched back to Proposed.
If the purchase order has been closed, this field and the
 detail lines will be display only.

Current revision
If the purchase order status is open,
 the current revision will start with 000. Click the Create Next button to revise
 to 001. Revision changes will display in the Revision history column of
 the detail grid.If editing a purchase order with a
 revision = 001 or higher, certain columns in the grid will be display-only
 for rows added in a prior revision.
If you do not
 wish to track revisions, simply leave the revision as 000 for the entire
 life of the purchase order.
Note: If
 the purchase order has been closed, this field and the detail lines will be
 display only.

Buttons

Form Info
Click this button to open the [Standard Form Information](/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/purchase-order-entry/standard-form-information) window. Use
 this window to enter payment and shipping terms, as well as order information
 for this purchase order. When entering a new purchase order, this window will
 automatically open after the purchase order status is selected.
Form Notes
Click this button to open the
 Notes to Appear on P.O.
 Form window. Use this window to enter any notes to appear on the
 Purchase Order Form.Note: When editing an
 existing purchase order, notes entered on this window will be committed to
 the purchase order, even if changes to the purchase order are canceled on
 the entry screen.

Other Info
Click this button to open the [Other Purchase Order Information](/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/purchase-order-entry/other-purchase-order-information) window. Use this
 window to enter sales tax and routing information for the purchase order, as
 well as credit card payment information (if applicable).
Internal Notes
Click this button to open the
 Internal Purchase Order
 Notes window. This window is used to record internal information
 pertaining to the purchase order. These entries do not print on the purchase
 order form.
User-Defined
Click this button to open the
 Purchase Order User-Defined
 Fields window. Use this window to set specific details for the
 purchase order being entered, such as approval status, request date, received
 date, written/oral quote, and so forth. Your System Administrator must have set
 up user-defined fields if this feature is to be used.
Details

Type
Select a purchase order type:
 Detail or
 Message. This
 field will default to Detail, but if Message is selected the cursor moves
 directly to the Message field.
Quantity
For unit price orders, enter the
 quantity of the item being ordered.Note: If
 this is a lump sum P.O., the quantity is automatically set to 1 and this
 field is skipped.

Item code
Enter the inventory item code being
 ordered. The item code entered here should have been previously defined in
 Inventory Item File Maintenance (if Inventory Control
 is installed or Price Update is used) or in Purchase Order Item Code
 Maintenance. The Item description will display to the right of this field. If
 the item status is set to 'Not used' entry will be disallowed.If the item is an invalid item, the Search
 Inventory Items window will open to enter a new item code or
 proceed as a non-stock item. Alternately, to enter a non-stock item, insert
 an exclamation point (!) as the first character in this field.
If this is a lump sum purchase order, the item code must
 be non-stock.
If there are no revisions in the
 Other Purchase Order
 Information window, this field will be hidden. If revisions
 are present, click the notepad icon to open the [Revision History Inquiry](/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/purchase-order-entry/revision-history-inquiry)
 window.

Additional description
This field will default to 'No'. If the
 Operator changes this setting to 'Yes', the Additional Itemization on
 Form window will open automatically. Use this window to add
 additional notes about the item description.This field
 will be display-only if an additional description was created in a prior
 revision.

Um
The unit of measure for this line item
 displays in this field. Press Enter to accept, or enter a new unit of measure. This field
 will be display-only if the unit of measure was added in a prior revision.If C displays in this field, the price is per hundred. If
 M displays in
 this field, the price is per thousand. If either C or M displays on a non-stock
 line, the extension is per-hundred and per-thousand respectively.
When the phase and cost type is changed, the unit of
 measure will be automatically re-assigned from the new phase.
When editing a non-stock line item, if the unit of
 measure is changed reset the price-per-factor so that the extension will be
 correct.
When you press Enter to exit this field,
 a dialog box will display containing the text found in the Message field in
 Vendor Special Cost Maintenance. If a dialog box
 does not display, the Message field in Vendor Special Cost
 Maintenance is blank or the vendor doesn't have any special
 costs set up.

Warehouse
The warehouse code for this item will
 default from the Form Info window or the Default warehouse code from
 Inventory Control Installation). If this code is
 valid, and the One
 warehouse? checkbox is selected, this field will be display
 only. If the checkbox is not selected, a different valid code can be entered in
 this field. If the default warehouse code is not valid (or blank).If this is a non-stock entry or direct cost line, this
 field will be blank and skipped.
This field will be
 display-only if the warehouse was added in a prior revision.

Unit price
Enter the price per unit of the item
 being ordered, or the price will default as follows:

- If there is a job special cost for the designated
 item, this price will default first.

- If there is a job special cost for the 'category' of
 the designated item, this price will default second.

- If there is a vendor special cost for the designated
 item or 'category' of the designated item, this price will default third.

- If there are no special costs found, the price will
 default from Inventory Item File Maintenance.

- If an override exists at the warehouse level, the
 standard cost will default from here. If the warehouse-specific standard
 cost is blank or zero, the standard cost from the Item Main
 Properties screen will be used instead.

Discount %
Enter the discount percent for this
 line number, if applicable, or press Enter to accept the default
 from Vendor Special Cost Maintenance. When the discount
 percentage is changed, the extension or the line is automatically adjusted
 accordingly.
Extension (before tax)
The extension total for this line
 number displays. The extension = units ÷ price per factor X unit price and
 excludes sales tax. If C displays in the unit of measure
 (UM) field, the price is per hundred. If M displays in this field, the price
 is per thousand. If either C or M displays on a non-stock line, the
 extension is per-hundred and per-thousand respectively.

G/L account
Press Enter to accept the default
 General Ledger account for this vendor. Otherwise, enter the G/L account code
 for this line transaction. This account must have been previously set up in
 G/L Master File Maintenance. If this item is a direct
 cost account, entry of a valid job or equipment code will then be required. This field will be display-only if the G/L account was
 added in a prior revision.
If the 'Automate G/L
 defaults' option was selected in Accounts Payable
 Installation, you can enter a shortcut in this field to
 automatically default the G/L direct cost codes defined on the installation
 screen:
J - This will set the G/L
 code to the direct job cost setting E - This will set the G/L
 code to the direct equipment cost setting W - This will set the G/L
 code to the direct work order cost setting N - This will set the G/L
 code to pass in the non-direct cost setting
If
 this option is selected and you do not enter a shortcut, the Select Type of
 Distribution window will open to select the G/L account codes
 specified in the installation screen. If no direct-cost G/L account was
 specified, the Search G/L accounts window will open instead.

- If the 'Type = Job' and the 'Automate G/L Defaults'
 option is selected in AP Installation, the direct
 job cost G/L account code will default in this field if exactly one
 shortcut is available.

- If the 'Type = Work Order' and the 'Automate G/L
 Defaults' option is selected in AP Installation,
 the direct work order cost G/L account code will default in this field if
 exactly one shortcut is available.

If the cost center feature is enabled in the
 Enterprise Installation screen for this company,
 if you change the G/L account code, cost center security validation is
 performed. Spectrum compares the new G/L account's list of shared cost
 centers with the cost center assigned to the line. You will be permitted to
 enter any G/L account, regardless of its cost center security because the
 correct override to use cannot be determined until the account
 work-in-progress flag is known.

Job
Enter the job to which the item should
 be charged, or press Enter to accept the default from the main screen. This field is only available if the G/L account is a
 Direct job cost. If the G/L account is changed to a different direct cost
 type, the entry in this field will be removed.
This field will be display-only if the job was added in a prior
 revision.

Phase
Enter the phase to which the item
 should be charged, or press Enter to accept the default. Note that the default comes first
 from the Inventory Item File Maintenance. If the phase
 code field in Inventory Item File Maintenance is blank,
 then the phase defaults from the previous line transaction. If the "Enable Phase over revised estimate' warning in
 invoice detail?" option is selected in the AP
 Installation screen, a warning displays in the detail grid
 when you enter a phase that is over budget.
This
 field is available only if the G/L account associated with this line is a
 Direct job cost. If the G/L account is changed to a different direct cost
 type, the entry in this field will be removed.
This field will be display-only if the phase was added in a prior
 revision.
If this is a sub-job transaction set up
 on a master job, double-click on this field to search phases for the
 sub-job. This will allow you to easily select a phase set up on a master
 job, but not present on the sub-job. Spectrum will add a new phase to the
 sub job if the current job is a sub-job of a valid master job, the phase
 lengths of both jobs match, and the Phase + Cost type combination for the
 current job is valid and not 'Complete'.

Ct
Enter the cost type to which the item should be charged, or press Enter to accept the
 default. Note that the default comes first from the Inventory
 Item File Maintenance; if the cost type field is blank in
 Inventory Item File Maintenance, then the cost
 type associated with the specified G/L code in the chart of accounts.
 Finally, it defaults from the previous line transaction.
If the 'Automate G/L Defaults' and 'Job G/L account defaults from cost type'
 options are selected in AP Installation, and the
 'Validate job division with G/L department' option in Job Cost
 Installation is not selected, the G/L account stored in the
 Cost Type Master Table will be assigned to this distribution line.
If the phase cost-to-date amount will exceed the revised estimate amount, an
 error message will appear if the 'Enable Phase over revised estimate warning
 in invoice detail' checkbox is selected in the Accounts Payable
 Installation.
This field is available only if the General Ledger account associated with this line is a Direct Job Cost. If the G/L account is changed to a different direct cost type, the entry in this field will be removed.
This field will be display-only if the cost type was added in a prior revision.

Equipment
Enter the equipment code in this field,
 or press Enter to
 accept the default. This field will be hidden if the
 Equipment Control module is not installed in the current company.
This field is available only if the G/L account
 associated with this line is a Direct equipment cost. If the G/L account is
 changed to a different direct cost type, the entry in this field will be
 removed.
This field will be display-only if the
 equipment code was added in a prior revision.

Cost category
Enter the cost category code in this
 field. This field will be hidden if the Equipment Control
 module is not installed in the current company.
This field is available only if the G/L account associated with this line
 is a Direct equipment cost. If the G/L account is changed to a different
 direct cost type, the entry in this field will be removed.
This field will be display-only if the cost category code
 was added in a prior revision.
If both the
 'Automate G/L Defaults' and 'Equipment G/L account defaults from cost
 category' options are selected in Accounts Payable
 Installation, the G/L debit account for the entered Cost
 Category will write in the G/L Account field, overwriting the currently
 entered G/L account.

Equipment W/O
Enter an equipment work order number.
 If a closed work order is entered in this field, a warning displays, but does
 not prevent further data entry. The equipment code must match equipment code on
 the Equipment work order.This field will be hidden if the
 Preventive Maintenance module is not installed.
This field is available only if the G/L account associated with this line
 is a Direct equipment cost. If the G/L account is changed to a different
 direct cost type, the entry in this field will be removed.
This field will be display-only if the equipment work
 order number was added in a prior revision.

Work order
Enter a work order in this field. If
 the current invoice originated from Purchase Order Receiving, the work order
 number will be display-only. The work order number will default from the
 previous line when entering multiple detail lines. This
 field will be hidden if the Work Order module is not installed.
This field is available only if the G/L account
 associated with this line is a Direct work order cost. If the G/L account is
 changed to a different direct cost type, the entry in this field will be
 removed.
This field will be display-only if the
 work order was added in a prior revision.
Entry of
 a work order with a status of 'proposed' will be disallowed.
If the 'Automate G/L Defaults' and 'Work order G/L
 account defaults from department assigned to work order type' options are
 selected in AP Installation, the non-inventory
 material cost of goods sold G/L account from the Work Order G/L Department
 Table will be assigned to this distribution line.

Site equipment
Enter the site equipment ID in this
 field. The Site Equipment code will default from the previous line when
 entering multiple detail lines. If this detail line has already been selected
 for billing in Work Order > Material Entry, no changes are permitted. Entry in this
 field is required if the Work Order Installation
 option to 'Require equipment code for work order transactions?' is
 selected.
This field will be hidden if the Work
 Order module is not installed.
This field is
 available only if the G/L account associated with this line is a Direct work
 order cost. If the G/L account is changed to a different direct cost type,
 the entry in this field will be removed.
This
 field will be display-only if the work order was added in a prior
 revision.

Component
Enter a component ID. This field will
 only be enabled if components are set up for the previously selected site
 equipment. The Component code will default from the previous line when entering
 multiple detail lines. If this detail line has already been selected for
 billing in Work Order > Material Entry, no changes are permitted. Entry in this
 field is required if the Work Order Installation
 option to 'Require component code for work order transactions?' is
 selected.
This field will be hidden if the Work
 Order module is not installed.
This field is
 available only if the G/L account associated with this line is a Direct work
 order cost. If the G/L account is changed to a different direct cost type,
 the entry in this field will be removed.
This
 field will be display-only if the component was added in a prior
 revision.

Service contract
Enter a service contract number. The
 contract number will default from the previous line when entering multiple
 detail lines. If the work order is changed, entry in this
 field will be removed and a new service contract will need to be
 entered.
This field will be disabled if the Service
 Contract module is not present, or no contract exists for the
 equipment/component combination. If a contract is specified in the work
 order header, this contract # will default if valid for the equipment
 component and the Operator will not be allowed to assign a different
 contract # on the work order. If a contract is not specified in the in the
 work order header, the Operator will be allowed to enter any combination of
 contracts (or blank contract) in the work order detail. If this detail line
 has already been selected for billing in Work Order > Material Entry, no changes are permitted.
This
 field is available only if the G/L account associated with this line is a
 Direct work order cost. If the G/L account is changed to a different direct
 cost type, the entry in this field will be removed.
This field will be display-only if the component was
 added in a prior revision.

Unit bill
Enter a unit billing price in this
 field. If the invoice originated in Accounts Payable, this field will be
 accessible for entry. If the invoice originated in Purchase Order Receiving,
 this field will be view-only. When a direct work order
 cost entry is added, the software automatically calculates the Unit bill
 price, including material markup rates.
If the
 previously specified work order is for Time + Materials, the software will
 automatically calculate the lowest price for a stock item. For more
 information on this calculation, refer to the [Determining the Material Price](/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/purchase-order-entry/determining-the-material-price) in-depth topic.
The
 Operator can still edit the Unit billing price before continuing with
 further purchase order entries. If the Work order #, Unit cost, or Quantity
 is changed the software will automatically recalculate and default a new
 Unit bill value.
This column will be hidden if the
 Work Order module is not installed for the current company.
This field is available only if the G/L account
 associated with this line is a Direct work order cost. If the G/L account is
 changed to a different direct cost type, the entry in this field will be
 removed.
This field will be display-only if the
 component was added in a prior revision.

Tax code
Enter the sales/use tax code for this
 line, or press Enter
 to accept the default. Tax codes must have been previously set up in
 Accounts PayableUse Tax Code
 Maintenance. If no tax code is entered here, the purchase order
 will be non-taxable.For direct equipment cost, direct
 work order cost, and non-direct cost rows, the sales/use tax code will
 default from the Other
 Purchase Order Information window.
For a direct job cost row, if the there is a tax classification code
 assigned to the job and the tax classification is set to 'Yes' in
 Job Cost Installation, the A/P invoice tax code
 specified in the Tax Classification Maintenance
 screen will default in this field. If no tax code is available in this
 screen, the sales/use tax code will default from the Other Purchase Order
 Information window.
This field will
 be display-only if the tax code was added in a prior revision.

Tax type
The tax code type (Sales or Use) plus
 applicable tax percentage as set up for this tax code displays in this field.
Tax $
The tax amount for the corresponding
 tax code displays in this field.
Total amount
The sum of the extension total plus tax
 amount will display in this field.
Delivery date
The purchase order delivery date will
 display in this field.This field will be display-only if
 the tax code was added in a prior revision.

Terms discount
The terms discount percentage specified
 in the Other Purchase Order
 Information window displays in this field. Press Enter to accept the default,
 or enter a new terms discount.This field will be hidden
 if the 'Recalculate terms discounts by line item' checkbox is not selected
 in Accounts Payable Installation.
This field will be display-only if the tax code was added
 in a prior revision.

Qty received
The quantity stored in the detail
 record representing the dollar amount received during Vendor Invoice entry will
 display in this field.Note: This field will
 be hidden for lump sum purchase orders.

$ received
The amount received in the detail
 record representing the dollar amount received during Vendor Invoice entry will
 display in this field.
Message
Enter a description or message for this
 item, if desired. This field will allow entry of up to 250 characters.

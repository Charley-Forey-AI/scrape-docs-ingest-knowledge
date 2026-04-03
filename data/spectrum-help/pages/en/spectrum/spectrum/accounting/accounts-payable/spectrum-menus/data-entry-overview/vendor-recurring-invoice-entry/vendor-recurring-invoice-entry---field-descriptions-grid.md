---
title: "Vendor Recurring Invoice Entry - Field Descriptions (grid) | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/vendor-recurring-invoice-entry/vendor-recurring-invoice-entry---field-descriptions-grid"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/vendor-recurring-invoice-entry/vendor-recurring-invoice-entry---field-descriptions-grid"
---

# Vendor Recurring Invoice Entry - Field Descriptions (grid)

Use this table for reference when completing the fields on
 the grid portion of this screen.
Fields/Buttons
Descriptions

Line
Line numbers are assigned and maintained by the software.

G/L account
The default General Ledger account to which this vendor's invoices should be
 posted displays (as entered in the Vendors). When transactions are posted to
 the General Ledger, this account will be debited and the A/P G/L trade
 account defined on the Accounts Payable Installation
 screen will be credited.

- If the invoice should be distributed to a job, the General Ledger account MUST
 have the Job
 cost option selected in the G/L Master File Maintenance > Direct cost menu.

- If the No direct
 cost option is selected in the G/L Master File Maintenance > Direct cost menu, then the software will skip the job and phase
 prompts. This validation ensures that Work-in-Progress direct costs in
 the General Ledger are always in balance with the job cost system.

- If a related-party vendor is entered, the override A/P trade G/L account
 will default when updated.

Amount
Enter the amount to be distributed to the entered General Ledger account (and, as appropriate, job/phase/cost type or equipment/cost category). The default is the undistributed portion of the invoice.
The system will display an error message if this line plus the job-to-date amount exceeds the estimate for this job, phase, and cost type.

Job
An invoice may be distributed to multiple jobs, phases, and cost types. The defaults are for convenience only, and may be overwritten.

Phase
Enter the phase to which this invoice is to be distributed; the description will display on line two. An invoice may be distributed to multiple jobs, phases, and cost types.
If the "Enable Phase over revised estimate' warning in invoice detail?" option
 is selected in the AP Installation screen, a warning
 displays in the detail grid when you enter a phase that is over budget.

Ct
Enter the cost type or equipment work order number to which this invoice is to be distributed; the description will display on line two. An invoice may be distributed to multiple jobs, phases, and cost types.

Equipment

- This field only displays if the Equipment Control module is present.

- Enter the code for the piece of equipment used for this invoice. The full equipment name will display on the next line.

- Equipment with a Retired status cannot be selected.

- If the checkbox in the Preventive Maintenance
 Installation screen is selected, a valid maintenance
 work order number must be entered.

Cost category
The Equipment Control module must be present and the previously-entered
 General Ledger account must have the Equipment cost option selected in the G/L Master File Maintenance > Direct cost menu for this prompt to display.
 Enter the cost category for this invoice/piece of equipment.

Equipment W/O
If this transaction line is related to a equipment work order and the Equipment Control > Cost Category File Maintenance > Data entry radio group is set to Require equipment work
 order, then entry in this field is required.

Work order
Enter a work order in this field, or press F4 to open the
 Search Work Orders window.The work order number
 will default from the previous line while adding records.
 The Site field will auto-populate from the selected work order. Use the inquiry buttons to view work order and site information.
If the current invoice originated from Purchase Order Receiving, the work order number will be display only.
Note: Entry of a work order with a dispatch status of 'proposed'
 will be disallowed.

Item code
Enter an inventory item for this work order, or press F4 to open the
 Search Inventory Items window. The item
 description displays to the right of this field.

- If the invoice originated from Purchase Order Receiving, the item code will
 default from the Purchase Order Detail screen
 and this field will be display only.

- If the invoice originated from Accounts Payable, the item code field will be must-enter.

-  If the item code is a non-stock item, this field will be display only.

Item description
Unless the item is a non-stock item, no changes are allowed.

Quantity
Enter a quantity for the Item Number in this field. This is not a required field, but when left blank the A/P Transaction Update will store a quantity of '1' in the Work Order cost history table.
If the original P.O. line has already been selected for billing in Work Order > Material Entry, the quantity will default from the Purchase Order
 Detail screen and the fields in the
 Details section will be view-only.

Um
When the phase + cost type is changed, this field automatically re-assigns the unit of measure of the new phase to this detail line.

Site equipment
Enter the site equipment ID in this field, or press F4 to open the
 Search Equipment window.
The Site Equipment code will default from the previous line if you are entering multiple lines.

Component
Enter a component ID, or press F4 to open the Search Components
 window. This field will only be enabled if components are set up for the
 previously selected site equipment.
The Component code will default from the previous line if you are entering multiple detail lines.

Service contract
Enter a service contract number, or press F4 to open the
 Search Service Contracts window. Use the inquiry
 button to view contract details.
This field will be disabled if the Service Contract module is not present, or no contract exists for the equipment/component combination.

- If a contract is specified in the work order header, this contract # will default if valid for the equipment component and you will not be allowed to assign a different contract # on the work order.

- If a contract is NOT specified in the in the work order header, you will be allowed to enter any combination of contracts (or blank contract) in the work order detail.

Unit bill

- This field only displays if the Work Order module is installed.

- If the invoice originated in Accounts Payable, this field will be accessible for entry.

- If the invoice originated in Purchase Order Receiving, this field will be view-only.

If the previously specified work order is for Time + Materials, the software will automatically calculate the lowest price for the item. For more information on this calculation, refer to the [Determining the Best Material Price](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-hierarchies/determining-the-best-material-price) in-depth topic. You can still edit the Unit billing price before continuing with further purchase order entries.
When a direct work order cost entry is added, the software automatically calculates the Unit bill price, including material markup rates. If the Work order #, Unit cost, or Quantity is changed the software will automatically recalculate and default a new Unit bill value.
To calculate the Unit billing price based on a different date, click on the inquiry button to open the [Item Price Inquiry](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/vendor-recurring-invoice-entry/item-price-inquiry) window.

Unit cost
For non-stock items the unit cost is displayed in this field. The unit cost is used to compute the Unit billing rate.
This column will always displays, showing the simple math calculation of "Amount column divided by Quantity column" unless used as in past versions for non-stock work order costing.

Remark

Cost center
This column only displays if cost centers are being used in the current company.

Contract hours
This column is display-only unless one or more cost types are entered in the Contract labor cost types field in the [Accounts Payable Installation - Properties tab](/en/spectrum/spectrum/accounting/accounts-payable/installation-overview/accounts-payable-installation---properties-tab) screen.
When a new transaction line is being entered, the [Contract Hours](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/vendor-recurring-invoice-entry/vendor-recurring-invoice-entry---field-descriptions-grid/contract-hours) window opens automatically.

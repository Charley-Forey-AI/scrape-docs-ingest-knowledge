---
title: "Work Order Materials for Job work orders - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/work-order-materials/work-order-materials-for-job-work-orders/work-order-materials-for-job-work-orders---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/work-order-materials/work-order-materials-for-job-work-orders/work-order-materials-for-job-work-orders---field-descriptions"
---

# Work Order Materials for Job work orders - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Field
Description

Item code
Enter the item code from the
 Work Order Material Item File Maintenance or from
 Inventory Item File Maintenance (including Price
 Update). This field will be view-only when editing a material item.Alternately, non-stock items may be entered by typing "!"
 before entering an item code. This field will utilize a "price per factor"
 for non-stock items based on unit of measure (C=100, M=1000). This permits
 Purchase Order detail lines with non-stock unit of measure C or M to
 transfer successfully into Work Order Material Entry or this window. Click
 the Proceed as
 Non-Stock button to proceed with the invalid entry.
 The item description will automatically display once the
 item code is entered. If a non-stock item is being entered, type the
 description. The description field will be display-only for inventory items.


Warehouse
Enter the warehouse in which this item
 can be located. Entry in this field is required for stock items, and is not
 applicable for non-stock items. Once a line has been created, this field may
 not be changed; the line must be deleted and a new one added.
Quantity
Enter the quantity used for this item
 on this particular work order.
U/m
This item's unit of measure displays.
 "Price per factor" pricing for non-stock items may be used based on the unit of
 measure. Enter C for price per 100 or
 M for price for 1000.
Price
The unit price for this item displays,
 based on the material pricing level specified on the Work Order
 Entry screen. Press Enter to accept
 default, or enter the unit price charged for this particular item. Note: If the Price field
 in the Work Order Entry screen is set to
 Flat Rate for this work order, this field will be
 blank.

Extension
The system calculates the extended
 total, but this total can be manually overriden. If you do change this total, a
 warning will display stating that the unit price will be recalculated. Click
 OK to continue. The amount that displays in the
 Price field will
 be re-calculated. The extension is calculated in one of
 two ways:

- If the price per factor field in
 Inventory Item File Maintenance (including
 Price Update) is blank or 1, the extension is calculated by multiplying
 the quantity by the price.

- If the price per factor field in
 Inventory Item File Maintenance (including
 Price Update) is not blank or 1, the extension is calculated by
 multiplying the quantity by the price, then dividing by the price per
 factor. Note: If the
 Price field in the Work Order
 Entry screen is set to Flat Rate for this work order,
 this field will be blank.

Phase Ct
Enter a phase code and valid cost type.
 The phase + cost type must be set up for the selected job. The default cost
 type is specified on the Work Order Installation
 screen.Note: If the selected job is a
 sub-job of a master job, and the phase + cost type are not set up on the
 current job, validate against the master job and then auto-create in the
 sub-job.

Updated to job?
If this transaction has already been
 updated to Job Cost, this column will be marked with a 'Yes'.
Inv detail?
Select this checkbox if you want
 material items to remain separate on the Accounts Receivable invoice. Enter
 No if you want to combine material items into a
 single line on the Accounts Receivable invoice labeled 'MATERIAL USED'. The
 stock and non-stock items will be combined unless one of the following
 conditions exists:

- Lines are assigned to different Work Order G/L
 departments

- Lines are assigned to the same department, but the
 Cost of Goods Sold G/L accounts in the Work Order G/L Department file are
 different for material and inventory.

The entry in this field is a default only, and may
 be over-written during Material Entry for each line item.
 Enter Yes to post this material
 line item in detail in the accounts receivable invoice. Enter
 No to include this material line item in a
 one-line summary when posting material to Accounts Receivable invoices.


Taxable?
Select this checkbox if this item is
 taxable, or No if the item is not taxable. This field defaults as follows:

- If the Job/Site file field is set to non-taxable,
 this field defaults to (N)o.

- If the work order is taxable, and the
 Material taxable checkbox is not selected on
 the Work Order Installation > Defaults tab, there will be no default for this field. You will
 have to specify the tax status on a line-by-line basis.

- If the Sales tax checkbox in the Inventory Control > Inventory Item File Maintenance > Properties window is selected, this field defaults to
 Yes provided the taxable flags in the site file
 are also set to Taxable. Otherwise, if the
 Inventory Control checkbox is clear, this
 field defaults to No regardless of the World Order
 Entry or site file flags.

Task
Enter the task associated with this
 line item, double-click in this field to select from a list of available tasks,
 or press Enter to leave this field blank.
Complete?
Select this checkbox if the task for
 this line item has been completed and transferred to Accounts Receivable;
 otherwise, leave this checkbox clear.
G/L dept
The G/L department will default based
 on the type defined for this work order on the Work Order
 Entry screen.  If changes are necessary,
 back-tab to change the G/L department. The GL department must have been
 previously defined in Work Order > G/L Department File Maintenance.

Task description
The selected task description will
 display in this field.
Phase description
The selected phase description will
 display in this field.

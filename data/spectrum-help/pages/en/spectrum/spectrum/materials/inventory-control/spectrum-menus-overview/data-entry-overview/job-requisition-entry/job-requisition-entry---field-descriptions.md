---
title: "Job Requisition Entry - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/job-requisition-entry/job-requisition-entry---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/job-requisition-entry/job-requisition-entry---field-descriptions"
---

# Job Requisition Entry - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Field/ButtonDescription
Batch codeEnter the unposted inventory batch code in this field. The current operator code defaults in this field and the Entered by field, but can be changed. It is OK to assign the same batch code across entry screens.Note: Select Preferences to specify whether to place the focus first in this field.

RequisitionEnter a unique transaction reference number, up to seven characters in length. If this field is left blank, the software auto-assigns the next requisition number.
JobThe current company code defaults in the first field. If the Inventory Control Installation setting for multi-company job requisitions is selected, the company code can be changed.
In the next field, enter the job code this item is to be charged to. To requisition items for miscellaneous use, press Enter to leave this field blank. Double-click in this field to select from a list of valid job numbers. Within this window is the add/chg window that you may add new jobs or edit existing job information.

StatusEnter the requisition status: Ordered or Shipped. When a back order is created by the software during the Inventory Transaction Update, the status of the new back order is set to Ordered. In order for the IC job requisition to update, it's necessary to change the status to Shipped. Note: Select Preferences to specify whether to default new requisitions to Ordered or Shipped status.

InstructionsEnter any specific instructions pertaining to this requisition.
Requisition dateThe current Inventory Control processing date displays. To change the date, arrow back to the field and enter the new date or double-click in this field to select a date from the Date Change window.
Ship dateEnter the date this requisition is being shipped, or press Enter to accept the default requisition date. If the requisition date is outside the inventory minimum/maximum date range, this field defaults blank and a valid date within the range must be entered.
Ship viaEnter shipping information. If the requisition is an open order, the cursor skips directly from the status field to the job field.
Default warehouseThe default warehouse code displays. To change the warehouse from which this item is shipped, arrow back to the From warehouse field. Warehouse codes may be up to 10 characters long.
Details
Item codeEnter the code of the item being requisitioned. In this field, you have the ability to enter non-stock items as Category + exclamation point (!) + Description. A valid category code must be entered followed by an exclamation point (!), followed by the description, such as: 1!NON-STOCK.
When adding a new row:

- If an invalid item is entered, the Search Inventory Items window opens to allow you to build a non-stock item code.

- If a valid item code is entered, the item status is verified. If the item status or date is discontinued, a warning message appears.

If you choose to import items as 'stock items', the import uses the category file to determine whether an item mask is specified. If so, the new item is created in the software using the next available item code for this category. If no mask is indicated, then the software adds the item using the EDP number as the new item code.

DescriptionThe corresponding item code description displays. For non-stock items enter the desired description, or accept the default descriptions based on the category.
WarehouseEnter the warehouse for the item. The warehouse code defaults when adding multiple rows on this screen.
MarkupEnter the markup percentage for this requisition line item, or press Enter to accept the software default. This information defaults from the Inventory Item File Maintenance screen.
U/mEnter the unit of measure for non-stock items. Otherwise, the item code unit of measure (um) displays and no entry is allowed for stock items.
Order quantityEnter the transaction quantity, or double-click in this field to enter the Standard cost for the line item. A positive entry means the quantity leaves the warehouse; and a negative entry means the quantity is returned to the warehouse.
If a Markup amount has been specified, this amount is added to the Standard cost to determine the unit Job cost.
The Order window is especially helpful when recording negative quantity requisitions; for example, when items are returned from the job site to inventory because the cost of those items may not have been purchased at "standard" cost.

Ship quantityThe quantity to be shipped displays. If the item's status is an open order, this field is skipped. A positive entry means the quantity leaves the warehouse; and a negative entry means the quantity is returned to the warehouse.
Back order quantityThis screen displays the back ordered quantity to the job for shipped items, even if the quantity is zero. If the job requisition status is shipped, the back order number displays. Back order quantity is computed by subcontracting the quantity shipped from the quantity ordered.
MessageEnter a message for this requisition line item.
DepartmentThe department code field displays. Arrow back to enter another inventory G/L code, if desired.
The department default hierarchy is as follows:
The system first looks to the Category File Maintenance for the G/L department code. If it is blank, the software looks in the Warehouse File Maintenance. If this is also blank, the code defaults from a previous line.

G/L accountThe General Ledger account code previously entered in the Inventory G/L Department File Maintenance screen displays. To change the General Ledger account, arrow back to this field and enter the desired code. The G/L account code must be set to Direct job cost the company where the job is set up. G/L accounts with a status of 'Not Used' are not allowed.
JobThe job number displays based on entry in the header portion of the screen. To enter information for a different job, arrow back-tab to this field and enter the desired code.
PhaseThe default phase for this inventory item displays. Press Enter to accept the default, or enter the desired phase number. If a job code was specified in the header, the entered phase code comes from the job.
For non-stock lines, the phase code defaults from the line above. The phase code must be a valid phase for this job.
The phase list in the master job is automatically used to create a phase in the sub-job if it does not already exist in the sub-job list.
Note: Data entry is prevented if the phase status is set to 'Complete'. A warning displays if the status is set to 'Inactive'.

CtThe default cost type for this inventory item displays in this field. Press Enter to accept the default, or enter the desired cost type code. The cost type code must be a valid cost type for this job and phase.
Use tax?Select this checkbox if there is a tax on this item.
If this checkbox is selected, the Job Requisition Report uses the tax rate from the shipped job requisition based on the ship date. The report shows the use tax percentage for shipped requisitions only. The use tax percentage that displays is calculated when the job requisitions' status is set to Shipped; it may be out-of-date and will be recalculated when it is posted.

Use tax codeEnter the tax code, or double-click in this field to select from a list of valid tax codes. Up to 15 characters are allowed.
The use tax code defaults from the tax class associated with the job number in the Job field. If the Job field is blank, then the use tax code defaults from the warehouse file.
Spectrum uses the ship date to compute the use tax percent and rate.
The Job Requisition Report uses the tax rate from the shipped job requisition based on the ship date. The report shows the use tax percentage for shipped requisitions only. The use tax percentage that displays is calculated when the job requisitions' status is set to Shipped; it may be out-of-date and will be recalculated when it is posted.
For job requisitions that aren't shipped, the use tax percentage does not display; because it may be several months before the item is shipped, Spectrum cannot accurately determine what the use tax percentage will be when it is shipped compared to when the requisition was entered into the software.
For job requisitions that are shipped, the use tax percentage was updated on the data entry screen when the requisitions were shipped. These will typically be posted close to the time they are set to shipped, and will have the use tax percentage updated during the update. The percentage on the report is only an estimate; when the update is run, Spectrum will determine the actual rate that is used.
This field will be reset if the Job, Phase or Cost type (Ct) fields are edited.

Standard costThe standard cost amount defaults for inventory items. If the amount is changed, the actual cost is transferred to Job Cost during the update. This field is optional for non-stock items.

- For items configured to use the Standard Cost costing method, Spectrum reads first for the warehouse standard cost. If this field is zero or blank, the amount is read from Item Main Properties, and is view-only.

- For all other items, Spectrum looks first for whether an override exists at the warehouse level, and that value defaults. Otherwise, if the warehouse-specific standard cost is zero or blank, the standard cost from Item Main Properties default.

Unit markupThe unit markup amount displays in this field.
Unit job costThe unit job cost displays in this field.
Est. costThe estimated cost amount for the inventory item displays in this field.
Est. markup $The estimated markup amount for the inventory item displays in this field.
Est. job cost $The estimated job cost amount for the inventory item displays in this field.

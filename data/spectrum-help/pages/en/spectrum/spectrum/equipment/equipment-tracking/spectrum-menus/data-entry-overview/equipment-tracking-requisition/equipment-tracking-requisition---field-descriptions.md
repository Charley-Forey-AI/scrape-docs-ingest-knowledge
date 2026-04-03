---
title: "Equipment Tracking Requisition - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-tracking/spectrum-menus/data-entry-overview/equipment-tracking-requisition/equipment-tracking-requisition---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-tracking/spectrum-menus/data-entry-overview/equipment-tracking-requisition/equipment-tracking-requisition---field-descriptions"
---

# Equipment Tracking Requisition - Field Descriptions

To get started, enter a Requisition number or press Enter to auto-assign the next number, then use the table below for reference when completing the screen fields. If the requisition entered is an Issue or a Return, the screen will display slightly different fields.
Fields / Buttons
Descriptions

Requisition
Enter an unposted requisition number in this field, or press Enter to have the software auto-assign the next sequential number.
When you enter an existing requisition number, the software will display the posted requisition from the Requisition History Tables. If it is an 'Issue', the screen will display the transaction. Otherwise, if it is a 'Return', the screen will display slightly differently.

Transaction code

- If the requisition entered = Issue, the transaction code and description display.

- If the requisition entered = Return, this field will say "Return" and no description will display.

More info on returns:
Returns will only allow you use transaction codes that are set up specifically for returns. The returns can be direct cost (returned from a job) or non-direct cost returns, based on the flag in the transaction code. The direct cost returns will force the user to enter the job that the items were returned from. The job status will be validated just like it is on the issue. The division will display, but no entry is allowed. The equipment codes that are entered or loaded will be validated that the status is correct and that the last job they were issued to is the same job that they are returning from. The inventory items returned will allow the user to enter the quantity returned as a positive number. The returns for inventory items will create a negative job requisition when the transactions are updated to inventory. These will credit the job and put the inventory quantity back in inventory (for direct cost returns).
For non-job inventory returns, it will create a positive adjustment entry for
 the return to inventory. The equipment returns will change the status in the
 Equipment File Maintenance to what is set up for
 the transaction code. In Addition, the return date will be updated at the
 time of the transaction update and the system will look at the greater of
 the last issue date and the last billing date to determine the final
 billing. The final billing will create Equipment Standby (ES) transactions
 for the job, if it is a non-job transaction code, then it will create a
 rental billing using the rental billing rates.

Issued to job
If the multi-company option was selected in Equipment Control Installation, enter the company code where the job to be issued to is set up and the job code. If the Installation option is not selected, these fields will be hidden.
Enter a job code. The system will validate this code in the specified company.
Note: When the transaction code is a Site deployment type, this field will say
 "Issued to site" instead of "Issued to job."

Requisition date
Enter a requisition date and time. Entry must be within the Equipment Tracking minimum/maximum processing date range. You can also enter the time.

Minimum billing period
The minimum billing period defaults from Equipment Tracking Installation.

Contact name
[Optional] Enter a contact name to associate it with the requisition. An email icon is also available to open a new message window, and a person icon is available to allow you to add the selected contact person tot he Job Contacts list for the specified job.

Buttons

Report
Click this button to open the [Requisition History Report](/en/spectrum/spectrum/equipment/equipment-tracking/spectrum-menus/reports-overview/requisition-history-report) with the requisition # in context.

Notes
Click this button to open the Requisition Notes window.

User-Defined
This button only displays if Equipment Tracking > Requisition user-defined fields have been set up.

Import
Click this button and browse to locate the file for import. Perform the associated update to bring the detail rows into the new requisition from text file. If you have already added lines to a requisition, the system will append the lines coming from the text file to whatever already exists in the requisition detail. [Importing Equipment Requisitions into Equipment Tracking Requisition](/en/spectrum/spectrum/equipment/equipment-tracking/spectrum-menus/data-entry-overview/equipment-tracking-requisition/importing-equipment-requisitions-into-equipment-tracking-requisition)
The import file can be from wedge bar code scanners, or a fixed-length text file.
Variable / Position:
Item/Equipment Code / Characters 1-15
Quantity / Characters 16-20

Columns

Type
Defaults to Equipment when adding a line, also allows you to enter Inventory.

Code
This column accepts Inventory codes and Equipment codes, depending upon 'Type'. The item status is verified when adding a code and a warning displays if the item is discontinued.

Description
The description displays from Equipment or Inventory Items.

Phase
The phase defaults from Installation. If the phase has a completed status, an error will displays.

Ct
The cost type defaults from the Installation and is validated against several settings (including G/L validations, the Job Cost settings, and cost center settings if cost centers are being used).

Message
Enter any message related to this piece of inventory or equipment.

Warehouse
The warehouse defaults from Inventory Control
 Installation or you can select a different warehouse.

Quantity
Enter the number of items.

Um
The unit of measure displays from Inventory Items.

Division
The G/L account displays from the Transaction code setup.

Phase description
The description for the selected phase displays in this field.

Additional columns that display when viewing requisitions

Department
The department code and description displays.

G/L account
The G/L account code displays in this column.

Returned from req#
If this is a Returned requisition, the original Issue requisition number displays. Otherwise, this column will be blank. A View 'issue' requisition link displays above the grid to display the returned requisition details.

Orig issue date
If this is a Returned requisition, the issue date of the returned requisition number displays.

---
title: "Job-to-Date Detail window | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/projected-cost-overview/projected-cost-entry-by-phase-summary/projected-cost-entry-by-phase-summary---field-descriptions/job-to-date-detail-window"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/projected-cost-overview/projected-cost-entry-by-phase-summary/projected-cost-entry-by-phase-summary---field-descriptions/job-to-date-detail-window"
---

# Job-to-Date Detail window

Use the Job-to-Date Detail window to view a history of job-to-date transactions for the job.
Note: The total on the Projected Cost Entry screen includes
 all costs as of the build date, but the Job-to-Date window only allows you to drill down
 into costs up to the Job Cost processing date. To view all of the costs actually associated
 with the entry in Projected Cost Entry, it may be necessary to change the Job Cost
 processing date.
Fields
Descriptions

Phase
The phase code and description display.

Cost type
The cost type displays as the code and description.

Pre-post cost
If the Include unapproved A/P invoices checkbox is selected in the Build Projected Cost Transaction File - Selections window, the unapproved A/P cost amount displays.

Pre-post hours
If the Include pre-time card entries checkbox is selected on the Build Projected Cost Transaction File - Selections window, the pre-time card hours displays.

Total cost
The total for this phase and cost type displays.

Variance amount Variance percentage Phase totals
The variance is calculated as the projected hours minus the total estimated hours. Therefore, a negative number would indicate that the project is ahead of schedule.
The variance percent is the variance divided by the total estimate, multiplied by 100.
Click the lookup icon to view the Phase Totals window, where you can view hour and cost totals for the selected phase.
Note: These fields will be hidden if the Group summary has been set to 'Phase summary'.

Buttons

Time card
Click to display the Time Card History Detail screen for the selected line.
If you have the Document Imaging module, this screen can display the employee-specific time card image or the job time card image. Spectrum will first look for the employee-specific document (originally created in Pre-Time Card Entry or Time Card Entry).
If no image is found, the software will search for the job document (created in Pre-Time Card Entry by Job or in Time Card Entry by Job). A Document Imaging drawer for timecards in the Job cabinet stores the employee time card documents.

AP Invoice User Defined
Click these buttons to display the A/P Invoice window and the User-Defined Fields window for the selected line.

Remarks
Click to view or enter any additional notes concerning this phase.

List box

Reference #
The reference number displays for each line of the transaction detail.
The reference number varies with transaction type:

> Transactions
Reference

Accounts Payable
Vendor code

Equipment
Equipment code

Inventory
Inventory item code

Payroll
Employee code

Type
The transaction type displays for each line of detail. Valid transaction types include:
AP = Accounts Payable
PR = Payroll
JC = Job Cost
EQ = Equipment
IC = Inventory
GL = General Ledger
OT = Overhead

Check
This column applies only to Accounts Payable and Payroll transactions. (For A/P transactions, check numbers display only for pre-paid invoices; for A/P items where the invoice is held as an open payable and a check is issued at a later date, the check number will not display in this field.) When applicable, the check number displays for the detail transaction line.

Invoice
For Accounts Payable transactions, the invoice number displays.

Purchase order
For Accounts Payable transactions that include a purchase order, the purchase order number displays.

Hours / qty

- For EQ, JC, and PR transactions, the hours displays.

- For IC transactions, the quantity displays.

Amount
The total dollar amount for this line transaction displays.

Name
Any names associated with the reference line display.

Description
Any descriptions associated with the reference line display.

Phase/ct total
The total for this phase and cost type displays.

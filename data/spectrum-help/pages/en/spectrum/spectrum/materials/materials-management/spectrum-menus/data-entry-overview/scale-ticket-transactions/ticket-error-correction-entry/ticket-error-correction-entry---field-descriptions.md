---
title: "Ticket Error Correction Entry - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions/ticket-error-correction-entry/ticket-error-correction-entry---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions/ticket-error-correction-entry/ticket-error-correction-entry---field-descriptions"
---

# Ticket Error Correction Entry - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields
Descriptions

Listing
Click to display the Print Listing window. Use this
 window to produce a ticket form for the selected ticket.

- Click Preview to view the [Import Errors Edit Listing](/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions/ticket-error-correction-entry/import-errors-edit-listing) report.

- Click [My Reports](/en/spectrum/spectrum/getting-started/reports--printing-overview/my-reports)
 to change the report default, set up a new report, or modify an
 existing one.

Revise All
Click to display the [Revise All Import Errors](/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions/revise-all-import-errors) screen.
Note: This option will not display if you do not have security
 authorization.

Delete AllClick this button to delete all tickets with errors on them.Note: This action cannot be reversed once the update is
 performed, and these transactions will have to be re-entered.

Errors box
This section displays a list of every error associated with the current ticket.

Edit/Delete
Click to modify or remove a line item.

Click to display the [More Ticket Error Information](/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions/import-scale-tickets/more-ticket-error-information) window.

Multiple items
Click to display the [Multiple Items on Ticket](/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions/import-scale-tickets/multiple-items-on-ticket) window.

User-Defined
Click to display the [Ticket Error User-Defined Fields](/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions/ticket-error-correction-entry/ticket-error-user-defined-fields) window.

Grid

Line
Line numbers are assigned and maintained by the software.

Plant/pit
The plant/pit code displays. If an error exists for this line, make the
 desired correction. Press F4 to view a list of valid
 plant/pit codes.

Ticket
The ticket number displays. If an error exists for this line, make the desired correction.

Item code
If an error exists for this line, make the desired correction. A search window is available for viewing valid item codes.
If multiple items were entered for this ticket, this field will display the first item and a yellow informational diamond icon will display beside the Multiple Items button below. Click on this button to view and change items for this ticket.
Note: Item codes with a status of Not used are considered to be errors.

Description
The full item description displays for valid codes.

Quantity
The net quantity for this ticket displays. If an error exists for this line, make the desired correction by clicking the Truck button.

U/m
The unit of measure (UM) displays.

Date
If an error exists for this line, make the desired correction. The date must
 be within the minimum/maximum date range, which is set in the System Administration > Installation > Processing Dates screen.

Time
Click this button to display the Date + Time window.
 Make any necessary date or time changes in this window.

Ticket type Code
Select the transaction type for this ticket:

- Customer

- Job

- Receipt

- Transfer

Transfers are not allowed for tickets that are associated with a vendor plant.
The code that displays is based on the Ticket type.

Name
For Sales transactions, the full job/customer name displays.

Order/req#
Enter or search for the customer's open order.

Customer P.O.
The customer's purchase order number for this ticket displays.

Unit price Extension
The item's unit price displays. Click the arrow to display the [More Ticket Error Information](/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions/import-scale-tickets/more-ticket-error-information).

Freight chg
Enter the freight charge rate.

Tax freight?
Enter the freight haul rate.

Misc chg
Enter any miscellaneous charges.

Tax misc?
This checkbox will be selected if the miscellaneous charge is taxable.
This checkbox will be reset to its default after error(s) are corrected. This checkbox is not available if you are calculating totals for a job sale ticket

Sales tax
The sales tax amount is calculated based on the sales tax code you have selected and can be overwritten as needed. This amount will be recalculated to reflect any changes made to the customer code, item code, or sales tax code (based on defaults) when the ticket is updated to Scale Ticket Entry.

Total
The total charge for this ticket displays. Press F4 to
 display the Totals
 window and view detailed dollar information for this ticket. This field
 appears only when you click the Expand button.

Message
Messages for this ticket display.

Batch code
Enter the batch code to assign these tickets to, or search for valid batch codes. The operator's user ID will default.

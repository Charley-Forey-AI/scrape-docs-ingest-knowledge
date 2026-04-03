---
title: "Scale Ticket Transactions - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions/scale-ticket-transactions---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions/scale-ticket-transactions---field-descriptions"
---

# Scale Ticket Transactions - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields/Buttons
Descriptions

Batch code
Type a unique code to identify the batch of tickets being entered. To view a batch of tickets imported from the scale software (or otherwise in-progress) type or search for the desired batch code.
When adding a new ticket, the batch code defaults to the code specified on the
 main Scale Ticket Transactions screen. Exception:
 unless the main screen is set to ALL, the operator code will be the default.
 If adding multiple tickets, the previous code will be the default.
You can change the assigned batch code while adding or editing.

Plant / pit
Enter or search for the plant or pit number for the ticket.
Note: If you are editing a ticket, the plant number cannot be
 changed.

Ticket #
 Up to 15 characters can display. In the New Scale
 Ticket window, enter the ticket number in this required
 field. The warehouse code and description display to the right. The
 description will be "From warehouse." If you select Receipt in the
 Ticket Type
 field below, then the description will be "Warehouse."
 In the Edit Scale Ticket window, If
 Customer, Job, or
 Transfer type tickets are selected in the
 Ticket Type field below, The Ticket # description will
 be "From warehouse."If Receipt is selected. the description will be
 "Warehouse." Note that the ticket number cannot be changed.

Ticket type
There are four types of scale tickets that can be added to the system. Use this field to select the type of ticket transaction you are adding. If you are editing a ticket, the type cannot be changed. Options include:

- Customer

- Job

- Receipt

- Transfer
Some plants are set up to accept only one of each ticket type. If you attempt
 to add a ticket to a plant that is not set up to accept a particular
 type of ticket, an error message displays. Plant settings are
 maintained in the Maintenance > Plant / Pit File Maintenance screen.
Note: This field is required in the New window and
 display only in the Edit window.
Note: Freight and miscellaneous charges can be for
 Receipt and Transfer ticket types. These additional ticket charges
 will be updated to the Inventory Control module. Receipt and Transfer
 tickets can also be posted to Freight Cost Reconciliation if an
 outside hauler is used. The Inventory Control G/L
 Department Maintenance screen has two new G/L accounts
 for Transfer Freight Variance and Receipts Freight Variance, which are
 used to post differences made to the freight charge during
 reconciliation.

Customer, Job, or To warehouse
This field displays with a label of Customer,
 Job, or To warehouse
 depending on what you selected in the Ticket type
 field above.
Customer: This field displays if you selected
 Customer above. Enter or search for a valid customer code in this required
 field.
Job: This field displays if you selected Job above.
 Enter or search for a valid job number in this required field.
To warehouse: This field displays if you selected
 Transfer above. Enter or search for a valid warehouse code in this required
 field. Warehouse codes may be up to 10 characters long.

Date / time
Enter or search for a valid date, and enter the time when this ticket was issued.

Sales order or Requisition #
 Sales order: This field displays if you selected
 Customer in the Ticket type field above.
 Enter or search for an order number for this ticket.
 Requisition #: If you are entering or editing a Job sale ticket, enter a valid job requisition number in this field.
If this is selected as a validated field in Scale Data Format Maintenance, the system will set this ticket as either an Order Processing order (for Customer sale type tickets updating to O/P Invoice Entry), or job requisition number (for Job sale type tickets). Upon completing this ticket, the item prices on the ticket will come from the order and the order quantities will be decremented when the ticket is updated. The order will be processed as if confirmed during the update, and an invoice will be created.
For example, if you enter a customer order for 100 items, then update a scale ticket for a quantity of 10 items through Order Processing, then the order will reflect the 90 items remaining. When the total quantity ordered or a quantity that exceeds that total has been processed through Order Processing, then the order will close.

- If this field is not validated, then the order number is used to group tickets together on an invoice.

- This field is not valid if you are updating this customer ticket to Accounts Receivable.

- This field can be validated in the [Scale Data Format Maintenance - File Layout](/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions/scale-ticket-transactions---field-descriptions/scale-data-format-maintenance---file-layout) by typing Yes in the Validatedcolumn for
 the 30.SIORDERNO row.

Customer P.O.
Enter the customer's purchase order number.

Message
Enter a message for this ticket.

Financials

Total extension
The extension amount displays. It is the sum of the Extension column lines in the grid below.

Freight charge
Any freight charges associated with this ticket display. This comes from the
 Freight charge
 field in the More Info window.

Misc. charge
Any miscellaneous amounts associated with this ticket display.
If the item is changed in the grid, miscellaneous charge amounts will revert back to the default amount.

Misc. charge taxable?
Any taxes associated with this ticket display.
Select this checkbox if the miscellaneous charges are taxable and you want this tax to appear on the ticket total. Selecting this checkbox allows you to edit the Sales tax and Ticket total fields below.
Note: This checkbox is available only for customer
 tickets.

Total $ (before tax)
This is calculated as the Total extension plus the Freight charge plus the Misc. charge.

Sales tax
Enter the sales tax amount for customer tickets that will be updated to Accounts Receivable. This field is not applicable for job, receipts, or transfers, however it is available for customer tickets being transferred to the Order Processing module.
Sales tax will only be recalculated when the user enters a new tax code or the total extension, freight charge or misc. charge is changed.

VAT code
If the Utilize value added tax
 (VAT) tracking? checkbox was selected in Company
 Installation, specify a VAT code in this field. Once
 specified, the VAT tax amount will automatically be calculated.
Note: If the ticket type is Job,
 Receipt or Transfer, this
 field will be hidden regardless of installation setting.

Ticket total
The total displays based on information entered in the previous fields. If the Misc. charge checkbox is selected, you can enter a different amount.

Buttons

Click to display the [More Scale Ticket Information](/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions/scale-ticket-transactions---field-descriptions/more-scale-ticket-information) window.

User-defined
This button is available if user-defined fields are set up for this company in
 Ticket User-Defined Fields Maintenance. Click to
 display the [Ticket User-Defined Fields](/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions/scale-ticket-transactions---field-descriptions/ticket-user-defined-fields) window.

Grid

Item code
Enter or search for the item code that you are including on this ticket. You can enter more than one item on any ticket.
If you are editing an existing ticket, this item number cannot be changed. You can, however, delete an unwanted item number and then add a new item, as needed.
Item codes with a Not used status cannot be entered. The description of the item displays.

Quantity
Enter the item quantity. If you are editing an existing ticket, this quantity can be changed.

U/m
The unit of measure associated with the corresponding item code displays.

Unit price
The unit price defaults from any special pricing defined for the job in Job Contract File Maintenance. If there is no special pricing defined in this screen, the system then looks to the standard cost defined in Inventory Item File Maintenance. The unit price defined here can be overwritten.
If an override exists at the warehouse level, default the standard cost from there. If the warehouse-specific standard cost is blank or zero, the standard cost from Item Main Properties will default instead.
Note: If the area code is changed from the code that defaults,
 then the system will automatically apply any price adjustments to those
 items that have been specially priced in the Job Contract File Maintenance > Special Pricing window. If the system does not find any area-specific special
 costs, then the system checks for special costs applied to any blank area
 where no other special costs for that item are entered. If special costs are
 not located, then the system will apply the standard cost associated with
 this area. This special pricing only applies to job tickets.

Sell price
You can change the sell price if you are editing an existing ticket. Scale
 Ticket Data Entry defaults the sell price for stock items on non-contract
 customer tickets based on the material level (1-5) specified in the Accounts Receivable > Maintenance > Customer screen. If the material price levels are blank in Accounts
 Receivable, then the level #1 price will default. If this is a contract
 customer ticket, the price level defaults from Materials Management Customer
 Contract File Maintenance.

Extension
The system calculates this amount based on the Item code you chose and Sell price you entered.

Taxable?
This checkbox is applicable only for Customer sale type tickets. Select it if this item is taxable.

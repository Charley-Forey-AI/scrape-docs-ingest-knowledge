---
title: "Scale Ticket Journal Update - by Customer | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions/scale-ticket-journal-update---by-customer"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions/scale-ticket-journal-update---by-customer"
---

# Scale Ticket Journal Update - by Customer

If multiple items were entered for a ticket, a list of these items for each ticket will display when the update is previewed.
Note: When miscellaneous charges are included on the ticket, then any costs associated with the miscellaneous charge will also be applied. To view the miscellaneous charges hierarchy, click [Scale Ticket Miscellaneous Charges Hierarchy](/en/spectrum/spectrum/materials/materials-management/hierarchies-overview/scale-ticket-miscellaneous-charges-hierarchy). If sales Invoices are selected, the following information is included: customer item code description ticket# date um quantity total Sales Invoices (the example shown is Order processing, but A/R invoices are similar).
Spectrum
Materials Management
Comments

Invoice#
N/A
System generated

Customer
si.custno
valid customer code

Ship To Address
N/A
blank

Invoice date
SI transaction date
this is the transaction date entered at time of update

Warehouse
si.plant
summarized by whse

P.O. number
si.pono
summarized by po number (could be blank)

Ship via
N/A
blank

Terms Code
SI contract file
from customer file if blank - also could be set to COD terms code from installation - summarized by terms code

Salesperson
si.slsman
summarized by salesperson

Remarks
N/A
blank

Item Code
si.item
summarized by item

Description
N/A
from item master

Unit of Measure
N/A
from item master

Drop Ship
N/A
always set to 'N'

Quantity
si.netwt
qty is summarized

List Price
si.unit
unit price is summarized

Sell Price
si.sell
sell price is summarized

Sales Tax Code
si.taxcode
summarized by tax code for each line, up to 15 characters are allowed

G/L category
N/A
from category in item master file

Message
ticket numbers
list ticket numbers

Sales tax
si.slstax
total of sales tax

The customer invoices are summarized by customer, warehouse, and item with up to nine tickets being summarized per detail line item. The Order Processing and Accounts Receivable systems have a 65-character message line that allows posting of up to nine ticket numbers with spaces between (job requisition only allows up to four ticket numbers because of the 30-character message line). Also, if the scale file has a Purchase Order number, salesperson, terms (some COD versus other), then these fields will also be used to create separate invoices with the respective fields filled in the invoice header. If separate line items are specified for miscellaneous charges, then these will be created as non-stock items with the category code "!" and the item code, as specified in the installation. If separate line items are specified for freight, then these will be created as non-stock items with the category code "!" and the item code as specified in the hauler file. If these are not separate, then the freight and miscellaneous charges are summarized into the total billing and cost for each line item.
The transfer to Order Processing module will create invoices, not orders. The transfer to Accounts Receivable (OP and AR are determined in Materials Management Installation) creates invoices. Also, the scale tickets are posted into the scale ticket inquiry file. The history file will have the same information with key being the plant ID + ticket number, plus new fields for actual freight quantities and cost and actual outside material purchase quantity and cost.
In addition, the software will calculate and store an end time for the truck cycle calculation. The ticket history file will have an end time field, in addition to the ticket time. This end time will be calculated during this update, the tickets will be sorted by truck, date, and time; the next sequential ticket start time will be the end time for this ticket being calculated. The last ticket of the day won't have another ticket for calculation, so a running average cycle time will be kept for that truck for the day and used to plug an end time for this last ticket. This information is used for the Truck Cycle Inquiry and Truck Cycle Report.

---
title: "Using Special Order Pricing | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/order-processing/spectrum-menus/data-entry-overview/sales-order-entry/using-special-order-pricing"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/materials/order-processing/spectrum-menus/data-entry-overview/sales-order-entry/using-special-order-pricing"
---

# Using Special Order Pricing

You can take advantage of special order pricing; for
 example, if you offer discounts for particular jobs or for cash sales.

1. For customer tickets, in the Order Processing module, set up your customer order in the Data Entry  >  Orders  >  Order Entry screen and Order Details sub-window.For job tickets, in the Inventory Control module, set up your job tickets in Job Requisition Entry.

1. In your scale software, record the same order number that you entered in Spectrum Order Processing.

1. In Materials Management  >  Maintenance  >  Data Format File Maintenance, open the Properties window and configure your import to run calculations. Select the Calculate pricing on charge sales and Calculate pricing on cash sales checkboxes, as applicable to your special pricing needs.

1. In Data Format File Maintenance, make sure the variable SI.ORDERNO is set to be validated (Validate = Y).

1. Import your scale tickets. Because we set this field to be validated in Step 3, the system will set this ticket as either an Order Processing order (for customer sale type tickets updating to O/P Invoice Entry), or job requisition number (for job sale type tickets). Upon completing this ticket, the item prices on the ticket will come from the order and the order quantities will be decremented when the ticket is updated. The order will be processed as if confirmed during the update, and an invoice will be created. If this field is not validated, then the order number is used to group tickets together on an invoice.

1. In the Data Entry  >  Scale Ticket Data Entry screen, enter a Batch code and click the Edit button to review the imported ticket data. At the Order # field, you can press F4 to select an order number from the system. If you are entering or editing a Job sale ticket, enter a valid job requisition number in this field.Example:
If you enter a customer order for 100 items, then update a scale ticket for a quantity of 10 items through Order Processing, then the order will reflect the 90 items remaining. When the total quantity ordered or a quantity that exceeds that total has been processed through Order Processing, then the order will close.

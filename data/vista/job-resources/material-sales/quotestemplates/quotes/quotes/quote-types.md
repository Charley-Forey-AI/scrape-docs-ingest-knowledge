---
title: "Quote Types | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/quotestemplates/quotes/quotes/quote-types"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/quotestemplates/quotes/quotes/quote-types"
---

# Quote Types

There are three types of quotes.
There are three types of quotes that can be set up
 in MS Quotes. For each of these quote types, you can define pricing by material (quote
 detail), pricing overrides, haul code and pay code overrides and haul zone defaults.
 Other information may be entered that is specific to the quote type. For example, if a
 customer quote, you can also set up invoice overrides (i.e. print and subtotal levels,
 ship to address, etc.) and discount overrides. With job quotes, you can set up
 phase/cost type defaults.
For each of these quote types, you can define pricing by material (quote detail), pricing overrides, haul code and pay code overrides and haul zone defaults. Other information may be entered that is specific to the quote type. For example, if a customer quote, you can also set up invoice overrides (i.e. print and subtotal levels, ship to address, etc.) and discount overrides. With job quotes, you can set up phase/cost type defaults.

## Customer Quotes

Customer quotes are used when you are
 supplying materials to a customer for jobs they perform, and can be set up at the
 customer, customer job, or customer PO level. Your specific needs may determine
 which level best suits your purpose:

- Customer – By setting a quote up
 at this level, you can define one master quote that can be used for several
 jobs. Master quotes are typically used when the materials being sold are not
 specifically related to a job for which the customer is purchasing the
 materials, or when materials are specially priced because of the customer’s
 purchase/payment record or the longevity of their relationship with your
 company. For example, if you routinely discount purchases for a specific
 customer because of their continual pattern of large quantity orders,
 setting up a quote at this level allows you to set up a discount rate or
 standard unit price for all materials purchased by them on a regular basis.
When initially setting up a quote, you can leave the Customer field blank.
 For example, you might leave the Customer blank for an initial quote for
 several contractors. When the job is bid and awarded to a specific
 contractor, you can then fill in the Customer.

- Customer/Customer Job – This
 level is typically used when quoted prices are based on a per job basis,
 allowing you to tailor prices for each job without affecting the pricing of
 other jobs for that customer. Material pricing, discounts, and haul
 information set up at this level will override information set up at the
 customer level.

- Customer/Customer Job/Customer
 PO# – This level is used when specific pricing and/or discounts are to be
 used only for a specific purchase order.

When customer-related tickets are
 entered in MS Ticket Entry, a hierarchical search is made for a customer quote. The
 system will first search for an active quote matching the customer/customer
 job/customer PO#. If no quote is found at that level, then a search is made for an
 active quote matching the customer/customer job. If not found at that level, it then
 searches for an active master quote for the customer.
In addition to pricing, discount, and
 haul and pay code overrides, you can override invoice information for each customer
 quote. This includes the billing frequency, print and subtotal levels, ship to
 address, and the option to create separate invoices based on the Invoice Level
 assigned to the customer in AR Customers.

## Job Quotes

Job quotes are used when you are
 supplying the materials for jobs your company performs, and are set up on a per job
 basis. You will generally only need to set up a job quote if you want to override
 standard prices and haul charges for the materials required on the job. You can also
 set up phase and cost type defaults that will be used when entering or editing
 tickets and hauler time sheets. This information will determine which phases and
 cost types will apply to each specified material and haul charges of a Job sale, and
 will override the standard phase and cost type defined for a material in HQ
 Materials.

## Inventory Quotes

Inventory quotes are used when you are
 supplying materials to another inventory location or company, and are set up on a
 per location basis.
Note: It is important that you understand the
 difference between sales of materials to other inventory locations and transfers of
 materials to other inventory locations. The GL implications and file updates are
 different for Inventory sales than they are for Inventory transfers. See [Inventory Sales](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/ticket-entry/inventory-sales) for more information.

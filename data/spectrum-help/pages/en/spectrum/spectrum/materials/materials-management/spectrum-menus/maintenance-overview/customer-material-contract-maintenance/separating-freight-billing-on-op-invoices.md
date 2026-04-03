---
title: "Separating Freight Billing on OP Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/materials-management/spectrum-menus/maintenance-overview/customer-material-contract-maintenance/separating-freight-billing-on-op-invoices"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/materials-management/spectrum-menus/maintenance-overview/customer-material-contract-maintenance/separating-freight-billing-on-op-invoices"
---

# Separating Freight Billing on OP Invoices

Freight can be separately stated on the Order Processing
 invoice or it can be summarized into the billing for the material item. This can be controlled
 at the customer or company level.
There is a hierarchy within Spectrum for separating freight billing. If
 the customer has a customer contract set up in Materials Management (in Customer Material
 Contract Maintenance), then Spectrum will look to this screen first when updating tickets
 to Order Processing. If the customer is not set up in Customer Material Contract
 Maintenance, then Spectrum will look to the to the Materials Management Installation screen
 when updating tickets to Order Processing.
Note: Two lines will appear on the Order Processing invoice if the
 material item is taxable and the freight is not. The reverse is also true. the software
 separates these lines in order to differentiate between the taxability of material and of
 freight in Order Processing Invoice.
Note: Additionally, Materials Management may create an "extra" line for
 freight on the invoice, even though your taxability flags are the same. For example, if you
 are charging an estimate hauling cost, there will be an extra line on the Order Processing
 invoice in order to create the journal entry to record the haul/freight cost. This "extra"
 line will appear on the invoice as $0.00. If you do not want this line to appear, then
 select the Invoice Print Crystal-Link report format; this version of the report suppresses
 all zero lines.
Note: Whether or not freight is taxable is determined by the Tax on
 freight checkbox in Accounts Receivable Sales Tax Code Maintenance. To indicate that
 freight is taxable, select this checkbox and freight will default to taxable.
If the customer is set up in Customer
 Material Contract Maintenance

1. On the Site
 Map screen, click Materials Management  >  Maintenance  >  Customer Contract.

1. In the Customer
 field, enter the customer code for the customer whose freight billing you
 are separating or press F4 to
 search for a valid customer code.

1. In the Properties
 section of the screen, make sure the Separate freight billing line item on
 invoices checkbox is selected. If it is clear, select it and click
 OK. If it is already
 selected, then click Cancel to exit the screen and return to the main menu.

If the customer is NOT set up in Customer
 Material Contract Maintenance
If the customer is not set up in Materials Management  >  Customer Contract File
 Maintenance, then you will have to make sure the Materials Management Installation
 screen is set to separate freight billing on invoices.

1. On the Site Map screen, click Admin  >  Installation  >  Materials Management.

1. On the Properties tab, make sure that the Separate freight billing
 item on invoices checkbox is selected.

1. If you made any changes to the screen, click OK to save your changes; otherwise,
 click Cancel to return to the Installation menu.

---
title: "About Billing Flat Price Work Orders | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/sm-invoices/about-billing-flat-price-work-orders"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/sm-invoices/about-billing-flat-price-work-orders"
---

# About Billing Flat Price Work Orders

Flat price work orders are billed based on the flat amount specified for the work order scope, rather than on work completed lines associated with the scope.
When you bill work orders using SM Work Order Billing, the upper grid displays eligible work orders based on the filter criteria you selected.
For T&M work orders/scopes, the lower grid displays a list of work completed lines associated with that scope sequence.
However, if you select a Flat Price work order/scope sequence in the upper grid, the lower section displays the Invoice Flat Price screen, showing the Flat Price amount, any previously billed amounts/percents, and Billing Amount fields for designating the amount/percent to bill for the current session. You can enter either an amount or percent; the system will automatically calculate the other value (i.e. if you enter a percent, the system auto-calculates the billing amount).
When you generate an invoice, the system creates a single invoice line for each flat price scope on the work order that you selected for billing, and sets the Price Total for each sequence equal to the amount you specified to bill. If you need to change this amount, you can do so by clicking the Edit Record button to access the SM Invoice Flat Price Change form.
Note: You can only edit billable amounts for flat price scopes on a customer work order or manually added agreement-related work orders. You cannot change billable amounts for work order scopes generated from an agreement (via SM Generate PM Work Orders).
Note: If you selected the Use Review Process checkbox in SM Company Parameters (which allows authorized users to assign reviewers by center, division, customer, work order, and site), flat price items are not editable in the Work Order Detail grid.

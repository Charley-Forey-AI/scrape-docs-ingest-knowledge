---
title: "Work Orders - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/work-orders/work-orders---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/work-orders/work-orders---cost-center-information"
---

# Work Orders - Cost Center Information

If the cost center feature is enabled in the Enterprise Installation screen for this company, Spectrum assigns the cost center from the job or work order site for the Accounts Receivable invoice header when an instant transfer to Accounts Receivable is done using the Transfer button. The update also assigns the invoice header cost center to every detail invoice line, except in the case where there is a phase override cost center for material, labor, or other cost entry.
The Work Order Entry screen only displays work orders that the operator is permitted to access; if the Restrict access in work order entry checkbox has been selected, then only allowed zones and statuses are displayed. The software compares the cost center assigned to the work order site with cost centers in the operator's assigned scheme, and if the site's cost center is not present, then that work order is not accessible. When Operator scheme overrides for Work Order are present, then this screen is displayed based on the override setting. The Search Work Orders advanced search option filters work orders based on the cost center in the Work Order Header Table.
Spectrum checks the work order type and validates that a cost center exists for that job or site. (Operator security and cost center status are not validated so that previously entered work orders can be updated.) Labor cost of sales debit and credit accounts are also validated.
If the cost center isn't validated, then an error message displays when you click the Transfer button on the main screen. For job work orders, if an Accounts Receivable contract record has not yet been created, Spectrum validates that the job cost center is valid for the customer's list of cost centers. If this is the case, the update creates an Accounts Receivable contract during the transfer and assigns the job cost center to the contract file.
If an Accounts Receivable invoice is created for a service contract manufacturer (from the Service Contract module on a work order being transferred), then the site cost center is assigned to the header and every detail line on the invoice.
If cost centers are on the Work Order Type, Spectrum looks to see if the Work Order header has a cost center assigned to it. When there is no cost center on the Work Order Type, Spectrum will look to the service contract for a cost center. When there is no cost center on the service contract, Spectrum will use the cost center assigned to the site.

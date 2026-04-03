---
title: "Invoice Register Report - Sample Report | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/order-processing/spectrum-menus/data-entry-overview/order-processing-invoice-entry/invoice-register-report/invoice-register-report---sample-report"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/order-processing/spectrum-menus/data-entry-overview/order-processing-invoice-entry/invoice-register-report/invoice-register-report---sample-report"
---

# Invoice Register Report - Sample Report

View the Invoice Register Report.
View cost center information
If cost centers are being used, then for each detail line of each invoice, Spectrum assigns a cost center from the warehouse for the G/L accounts for sales, cost of sales, inventory, and so forth.
For each detail line, Spectrum will determine if the warehouse cost
 center matches the invoice header cost center. If not, then Spectrum will create balancing
 debit and credit entries for cost center inter-posting account information is defined in
 the Order Processing Installation screen. When cost centers are used
 and the Enterprise Installation > Allow G/L account overrides by cost
 center checkbox is selected, Spectrum will assign inter-posting amounts to
 multiple General Ledger accounts by cost center, based on a list of override G/L accounts
 in the Inter-posting Overrides window in Order Processing
 Installation. For an invoice, Spectrum will debit the detail line extension
 to the inter-posting account for the warehouse cost center and will credit the detail
 extension to the inter-posting account for the invoice header cost center. A credit memo
 will have the debit and credit amounts reversed.
When the Enterprise Installation > Allow G/L account overrides by cost
 center checkbox is selected, Spectrum will assign commission payable, commission
 expense, and freight amounts to multiple General Ledger accounts by cost center, based on a
 list of override G/L accounts in the respective Order Processing Installation > Override window.
The A/R G/L Trade account will use the invoice header cost center. The Commissions Payable and Expense accounts, the Freight G/L account, and the sales tax G/L account will use the header cost center. The Inventory Sales G/L account, Inventory cost of sales, and Inventory value will use the header cost center.

Related information

- [Invoice G/L Summary Update](/en/spectrum/spectrum/materials/order-processing/spectrum-menus/data-entry-overview/order-processing-invoice-entry/invoice-gl-summary-report/invoice-gl-summary-update)

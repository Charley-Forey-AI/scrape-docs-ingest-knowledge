---
title: "Exclude Invoices from Finance Charges | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/invoices/how-finance-charge-types-are-used/exclude-invoices-from-finance-charges"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/invoices/how-finance-charge-types-are-used/exclude-invoices-from-finance-charges"
---

# Exclude Invoices from Finance
 Charges

You can use the AR Exclude From Finance Charge form to exclude invoices from finance charges.
Use the sort criteria on this form to filter invoices for finance charge exclusion. Invoices must be sorted by Customer, although additional restriction options are available.
The following instructions discuss how to exclude invoices from finance charges.

1. Enter the customer in the Customer field.

1. (Optional) Enter the receivable type in the RecType field to restrict the sort by receivable type.

1. (Optional) Click the Show $0.00 checkbox to display invoices with a zero balance.

1. (Optional) Select the Contract checkbox to restrict by contract. The system enables the JCCo and Contract # fields. This checkbox is inaccessible if you select the Exclude Contract Invoices from Finance Charges checkbox for this customer in AR Customers.

1. (Optional) If restricting by contract, enter a JC company and/or contract number to restrict by in the JCCo and Contract # fields, respectively.

1. Click Refresh. All invoices meeting the sort criteria display in the grid.

1. Check the ExcludeYN box for each invoice to exclude from finance charges. To exclude all invoices, check the Set Exclude box.

1. Click Update. The grid clears and the system skips all excluded invoices when calculating finance charges in AR Finance Charge. Note: Invoices remain excluded unless you manually uncheck them using this form.
To clear the grid and start over with the sort process, click the Clear All button. A message displays stating that the system has cleared the ExcludeYN checkbox for each invoice. Click Close to return to the AR Exclude From Finance Charge form and perform another sort; the system removes all invoices from the grid.

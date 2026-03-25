---
title: "Module Integration in Service Management | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/module-integration-in-service-management"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/module-integration-in-service-management"
---

# Module Integration in Service Management

Service Management is integrated with the Accounts Payable, Accounts Receivable, Equipment Management, General Ledger, Inventory, Payroll, and Purchase Order modules.

- Accounts Payable - Invoices posted to SM work orders in AP Transaction Entry are interfaced to Service Management as work completed miscellaneous lines in SM Work Orders.

- Accounts Receivable - Invoices generated in Service Management when billing for work completed on SM work orders are interfaced to Accounts Receivable for payment.

- Equipment Management - Equipment usage captured on SM work orders is updated to Equipment Management.

- General Ledger - Subledgers and general ledgers are updated for work completed on SM work orders.

- Inventory - On-hand quantities are updated for materials pulled from inventory for services performed on a work order.

- Payroll - Labor captured on an SM work order will automatically generate timesheets in Payroll. Timesheets and timecards entered in Payroll will automatically generate work completed labor entries on work orders in Service Management.

- Purchase Order - Purchase orders created for work orders in Service Management will be updated to PO; likewise, purchase orders posted to SM work orders in PO will be updated to the work order in Service Management. POs received via PO Receipts Entry will update received units/amounts for the corresponding work completed purchase line.

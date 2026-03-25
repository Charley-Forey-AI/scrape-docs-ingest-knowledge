---
title: "Purchase Order Cost Information | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/purchase-order-cost-information"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/purchase-order-cost-information"
---

# Purchase Order Cost Information

Purchase order cost information appears in display-only fields throughout the system.
When tracking purchase orders throughout the ordering and receiving process, it is important to know how the system tracks cost information. These fields work together to show what you have ordered, received, and the amounts that you are committed to.
Purchase order cost information fields display on a number of forms throughout the system: PO Purchase Order Entry (Costs tab, item section); PO Change Order Entry (lower section of the form); PO Receipts Entry (lower section of the form); PO Initialize Receipts (selected fields display in the grid); AP Transaction Entry (Other Info tab, item level); and AP Unapproved Invoice Entry (Other Info tab, item level). You can also view cost information by running the PO Drilldown report.
The following list discusses each cost information field and what it represents.

- Original (Units, Unit Cost, Total Cost) – These amounts represent what was initially entered for the purchase order in PO Purchase Order Entry. These numbers do not change, regardless of any change order or differences in receiving.

- Current (Units, Unit Cost, Total Cost) – These amounts mirror the Original amounts unless you enter a change order in PO Change Order Entry (or PO Purchase Order Entry) that affects the number of units or unit cost.

- Received (Units, Total Cost) – These amounts represent what you have received into the system through PO Receipt Entry or PO Initialize Receipts. The amounts may not match the Current or Original amounts, depending on your receiving process, or how the vendor fulfilled the order (e.g., undershipment, delayed shipments, etc.).

- Backordered (Units, Total Cost) – These amounts represent what you have not yet received. The amounts mirror the Current amounts unless you enter a change order that only affects backordered amounts, or until you receive units.

- Total (Units, Total Cost) – These amounts equal the Received amounts plus the Backordered amount. The Total Cost amount reflects the actual cost of the purchase order.

- Invoiced (Units, Total Cost) – These amounts equal what you have invoiced/paid for this purchase order through the AP module.

- Remaining (Units, Total Cost) – These amounts equal the Total amounts minus the Invoiced amounts. The Remaining amounts should equal zero once you have invoiced the purchase order in AP (using AP Transaction Entry and AP Unapproved Invoice Entry). If this amount does not equal zero, the Remaining costs remain committed.

[](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-initialization-form)PO Purchase Order Entry
[](/en/vista/vista/costs-and-contracts/purchase-order/change-orders/po-change-order-forms/po-change-order-entry-form)PO Change Order Entry
[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipts-entry-form)PO Receipts Entry
[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-initialize-receipts-form)PO Initialize Receipts
[](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-transaction-entry-form)AP Transaction Entry
[](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-entry-form)AP Unapproved Invoice Entry

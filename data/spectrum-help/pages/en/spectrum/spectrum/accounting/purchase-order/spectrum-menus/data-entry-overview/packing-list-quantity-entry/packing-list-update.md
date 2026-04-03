---
title: "Packing List Update | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/packing-list-quantity-entry/packing-list-update"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/packing-list-quantity-entry/packing-list-update"
---

# Packing List Update

After the Packing List Quantity Edit Listing page is
 printed, the Packing List Update page opens.
This page appears only if the Two-step with pack list update receiving method is selected
 on the Purchase Order Installation screen. Do not continue until the Packing List Quantity
 Edit Listing has printed correctly. Once it has printed and is accurate, continue with the
 update.
This update adjusts quantities on-hand and on-order and creates records in the inventory history file, and jobs before invoicing if this option is selected on the Purchase Order Installation screen. This update also prepares entries for the General Ledger; the debit and credit entries are included on the next Inventory G/L Summary Report printed. The G/L account codes are determined based on setup in Inventory Control G/L Department File Maintenance. The default hierarchy for which G/L department code to use is first from the inventory category file; if blank there, the G/L department specified in the warehouse file is used. If also blank, the Inventory G/L account specified in Inventory Control Installation is used as a last resort. This update will not include the updated packing list in the 'on order' amount inventory of the Inventory Detail Maintenance page.
If multi-currency is enabled and the vendor has a default local currency, amounts from the local currency will be converted to the reporting currency as part of the packing list update as follows:

- For Purchase Order Accruals, the cost is calculated as PO accrual
 cost x exchange rate of packing list

- For Job Expense, the cost is calculated as (PO accrual cost x
 exchange rate or packing list) - (invoice cost x exchange rate of A/P invoice). Will be
 a debit if positive, or a credit if negative.

- For A/P, the cost is calculated as invoice cost x exchange rate of
 A/P invoice If the item is configured to use the standard cost
 costing method, the quantity will be updated using the warehouse-specific standard
 cost. If the warehouse-specific standard cost is blank or zero, then the unit cost
 will be updated to the Item Warehouse Table.
Note: When the Purchase Order receiving method has been set to
 Two-step with pack list
 update, the Packing List Update will not adjust inventory when stock
 item quantities are received on a direct work order cost detail line, and no history
 record is created.

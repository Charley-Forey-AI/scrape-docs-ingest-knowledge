---
title: "Equipment Parts Entry - Field Definitions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/equipment-parts-entry/equipment-parts-entry---field-definitions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/equipment-parts-entry/equipment-parts-entry---field-definitions"
---

# Equipment Parts Entry - Field Definitions

A table reference for completing the fields on this screen.
Field/ButtonDescription
Batch codeEnter the unposted inventory batch code in this field. The current operator code will default in this field, but can be changed. You can assign the same batch code across entry screens.
ReferenceEnter a unique transaction reference number, up to seven characters in length. If this field is left blank, the software will auto-assign the next requisition number.
EquipmentEnter the equipment code.Note: If the equipment code is changed, all the existing transaction rows will be assigned to the new equipment code. However, if any of the transaction rows are assigned to a Preventive Maintenance work order, the equipment code cannot be changed.

Details
Item codeEnter the item code to be adjusted.

- If you enter an invalid item code, the Search Inventory Items window opens. Select a valid one or add a new one.

- If the item code status is 'Not used,' entry is disallowed.

DescriptionThe item code description displays.
WarehouseEnter the warehouse for the item. The warehouse code will default when adding multiple rows on this screen.
DateThe current Inventory Control processing date will default in this field, but can be changed as necessary.
U/mThe equipment unit of measure displays.
Quantity usedEnter the quantity by which the current quantity-on-hand is to be adjusted. A positive entry means the quantity leaves the warehouse; and a negative entry means the quantity is returned to the warehouse.
Unit costIf a positive quantity entry was entered above, this field will be skipped. If a negative quantity entry was entered above, this field will default to the standard cost, but another positive quantity can be entered.

- For items configured to use the Standard Cost costing method, Spectrum will read first for the warehouse standard cost. If this field is zero or blank, the amount will be read from Item Main Properties, and will be view-only.

- For all other items, Spectrum will look first for whether an override exists at the warehouse level, and that value will default. Otherwise, if the warehouse-specific standard cost is zero or blank, the standard cost from Item Main Properties will default.

MessageEnter a message related to the equipment transaction, if desired.
DepartmentThe inventory/General Ledger department code displays.The defaulting hierarchy for department codes is as follows: The system first looks to the Category File Maintenance for the G/L department code. If the field is blank there, the software will then look to the Warehouse File Maintenance. If this is also blank, enter a valid code.
G/L accountThe General Ledger account code displays based on G/L entry in the G/L department file. However, this code may be overridden.The G/L account code Direct cost option must be set to No direct cost in G/L Master File Maintenance. G/L accounts with a status of 'Not Used' are not allowed.
Cost categoryThe cost category code will default from the item code setup, if specified.When adding a new row, Spectrum will verify the assigned G/L account is not a restricted G/L account for this equipment cost category code.

- If the assigned G/L account is not on the list of restricted accounts, you will be able to advance to the next column in the grid.

- If the assigned G/L account is on the restricted accounts, an error message appears and will not be able to proceed.

When searching for cost categories, the search window will only display cost category codes that have no restrictions for the specified G/L account.
Eq. work orderThe equipment work order code displays in this field.Note: This field is hidden if Preventive Maintenance is not installed for this company.

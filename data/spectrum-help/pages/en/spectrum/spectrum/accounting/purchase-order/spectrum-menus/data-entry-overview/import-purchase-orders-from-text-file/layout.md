---
title: "Layout | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/import-purchase-orders-from-text-file/layout"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/import-purchase-orders-from-text-file/layout"
---

# Layout

Use this window to view the maximum file lengths in the header and detail files.
The import process reads a comma-separated text file for the information about the purchase orders. Each imported p.o. in the file has a header record and at least one detail record. For each p.o. the first line represents the header record and is labeled with an identifier "H." All subsequent lines with the same p.o. number are interpreted as detail records and will have the identifier "D." The file must have at least one header and detail record per purchase order. The table below shows the formats for the Header and Detail records.
You can create your import files in Excel, as long as they are saved as type CSV. In some instances Excel will put quotes around each alpha data item, in other instances it will not – either is acceptable to Spectrum.
Field (field #)
Description

Header fields

Record ID (1)
Required field.
PO number (2)
Required field.
Batch code (3)
The system will use the start screen
 value if this is blank in the import file.
Vendor code (4)
Required field.
Remarks (5)

Job number (6)
This field is validated, but not
 mandatory.
Order date (7)
Format MMDDYYYY
Delivery date (8)
If blank, the order date is used.
Ordered by (9)

Ship-to name (10)

Address 1 (11)

- If the 'PO Type' is Job, the job address will
 default in this field.

- If the 'PO type' is Warehouse, the warehouse address
 will default in this field.

Address 2 (12)

City (13)

State (14)

Zip (15)

Ship terms (16)

Ship via (17)

F.O.B. location (18)

Warehouse (19)
The system will use the start screen
 value if this is blank in the import file.
Work Order number (20)
This field is validated, but not
 mandatory.
P.O. type (21)
This field looks for an "L" for Lump
 Sum POs, or "U" for Unit Price POs. When detail rows are stored for a lump sum
 purchase order, the quantity ordered is automatically set to 1, and the item
 must be non-stock only. This defaults from the start screen (J)ob, (W)ork
 Order.
Routing code (22)

Cost center (23)
This is required in cost center companies
 and should otherwise be left blank.
Credit card account (24)

Card # (25)

Special instructions (26)

Receiving method (27)

Accrue PO costs? (28)
This field will be ignored in the
 import if the 'Update packing lists to jobs before invoicing' option is not
 selected.
Detail fields

Record ID (1)
Required field.
P.O. number (2)
Required field. Use
 CAPITALS.
P.O. line number (3)
If adding lines to an existing purchase
 order, then new lines are appended.
Quantity (4)
Required field.
EDP item code (5)

Spectrum item code (6)

Vendor item code (7)
This is required if both EDP item code
 (5) and Spectrum item code (6) are left blank in the import file.
Item description (8)
This is required for non-stock items.
 The data in the Vendor item code (7), invalid data in the EDP item code (5), or
 Spectrum item code (6) fields are added as non-stock items in the import
 file.
Unit of measure (9)
Required field.
Price (10)
You must enter field 4 and field 12 to
 populate this field.
Sales/use tax (11)
This is optional in the Detail line of
 the import file, and the code is set based on the Spectrum setup if a valid
 code is not specified in the import file.
Line extension (12)
This is the total amount of the PO
 line. The Quantity
 and Line extension
 are used to create the price field.
G/L account (13)

Job or Equipment code (14)
A Job code is required with a Job Cost
 G/L account, and Equipment code is required with an Equipment
 Cost G/L account. Spectrum validates that the equipment code assigned to the
 equipment work order matches the equipment code specified in the import
 file.
Phase or Cost category (15)
A Phase category is required with a Job
 Cost G/L account, and a Cost category is required with an Equipment Cost G/L
 account.
Cost type (16)
This is required with a Job Cost G/L
 account.
Warehouse (17)

Delivery date (18)

Work order (19)
This is required with a Direct Cost
 Work Order G/L account. The work order must be valid in the current company, it
 must be a site work order, and the status cannot be complete. If the Work Order
 module is not present, then no entry is allowed.
W/O sale price (20)

Site equipment (21)
This is required with a Direct Cost
 Work Order G/L account, and if the checkbox, Require equipment code for work order
 transactions? is selected in the Work Order Installation page.
 Note: The record will still import
 successfully even if the equipment status is inactive.

 Site component (22)
This is required with a Direct Cost
 Work Order G/L account, and if the checkbox, Require component code for work order
 transactions? is selected in the Work Order Installation page.
Cost center (23)
This is required in cost center companies
 and should otherwise be left blank.
Service contract (24)

Equipment work order (25)

Message (26)

Accrue PO costs? (28)
This column will enable the Job PO
 Accrual functionality for the purchase order.

- (Y)es: Select the 'Accrue PO costs' checkbox in the
 header.

- (N)o or <BLANK>: Deselect the 'Accrue PO
 costs' checkbox in the header. Note: Job PO Accruals must be enabled. If the 'Update packing list to jobs
 before invoicing' option is not selected on the Purchase Order
 Installation screen, this column will be ignored.

In order to prevent mismatched amounts in the resulting Spectrum purchase order, the import update uses the following conditions:
Note: The extension figure in the import file is defined as
 "before sales tax". To import credit card account and Card # columns, the Cash Management
 module must be present.
Condition #1: Price is 0.00 / Extension is non-zero

- The import stores the Extension (before tax) in the new purchase
 order.

- The import calculates Price by dividing the extension by the
 Quantity x Price-per-factor.

Condition #2: Price is non-zero / Extension is 0.00

- The import stores the Price in the new purchase order.

- The import calculates the Extension by multiplying the Price times
 the Quantity divided by Price-per-factor.

Condition #3: Price is 0.00 / Extension is 0.00

- The import stores 0.00 as the Extension in the new purchase order.

- The import stores 0.00 as the Price in the new purchase order.

Condition #4: Price is non-zero / Extension is non-zero

- Spectrum uses the extension from the import file and then
 calculates the corresponding price, as in condition #1.

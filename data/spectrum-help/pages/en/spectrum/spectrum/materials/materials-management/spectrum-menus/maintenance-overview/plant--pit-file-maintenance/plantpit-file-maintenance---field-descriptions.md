---
title: "Plant/Pit File Maintenance - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/materials-management/spectrum-menus/maintenance-overview/plant--pit-file-maintenance/plantpit-file-maintenance---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/materials-management/spectrum-menus/maintenance-overview/plant--pit-file-maintenance/plantpit-file-maintenance---field-descriptions"
---

# Plant/Pit File Maintenance - Field Descriptions

Use the table below for reference when completing the fields on this screen.
FieldsDescriptions
Plant / pitEnter a unique code to identify the plant or pit. For instance, set up a different code for each plant and pit used. Select the arrow to search for existing codes.
Properties
DescriptionEnter a full description of the plant/pit. For instance, the code might be "GBEL," and the full description "Gravel Pit - Bellingham."
WarehouseThe warehouse code entered here must have been previously set up in the Inventory Control module.Enter or search for a warehouse code (up to 10 characters) for this plant/pit. The corresponding description displays. Entry in this required field allows the software to accurately track materials.

VendorThe entry in this field is provided for instances when materials for a job are purchased from an outside source instead of your own plant. If a vendor code is entered, a warehouse should still be entered and set up for that plant. Note: If the vendor's status is Not used then entry is not allowed. Enter or search for a vendor code for this plant/pit.

Data formatEnter or search for the data format code to be used as a default when scale tickets are imported from this plant/pit. The code entered here must have been previously set up in [Scale Data Format Maintenance](/en/spectrum/spectrum/materials/materials-management/spectrum-menus/maintenance-overview/scale-data-format-maintenance).
Actual cost jobEnter or search for the job from which to calculate actual costs, or leave blank if none.The actual job cost is used on the plant profitability report if Actual cost instead of Standard cost is chosen when the profitability report is selected.

VAT codeThis field only displays when the Utilize value added tax (VAT) tracking? checkbox in Company Installation is selected. Select the Value Added Tax Code you want to use (for example, GST).
Transfer type
Transfer typeSelect the appropriate code indicating the transaction type for inventory items at this plant/pit.

- ALL

- Sales only

- Receipts only

- Transfers only

 If a vendor is specified in the Vendor field, then the Transfers only option cannot be selected.
A/P invoice approval
Note: The following fields are unavailable if the Use Invoice Approval processing checkbox is not selected in Accounts Payable Installation  > Invoice Approval.

Default routing codeEnter or the default routing code, or search for valid routing codes.
Invoice dollar limit
Routing code over limit
The dollar limit which should trigger the use of the over-limit routing code, and the routing code to use when an invoice amount exceeds the dollar limit. If there is no established invoice dollar limit, leave this field blank.Note: You can opt to leave both fields blank and instead manage the approval routing by entering Approval Limits on the Routing Code. For additional information, see [Approval Limits](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/about-invoice-approval/approval-limits).

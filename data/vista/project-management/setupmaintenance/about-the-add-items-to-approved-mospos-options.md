---
title: "About the Add Items to Approved MOs/POs Options | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/setupmaintenance/about-the-add-items-to-approved-mospos-options"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/setupmaintenance/about-the-add-items-to-approved-mospos-options"
---

# About the Add Items to Approved MOs/POs Options

You can specify to allow adding items to approved material orders, purchase orders, and open purchase order using specific setup options in the PM Company Parameters form.
When defining formatting for purchase orders and material orders for a PM company, you can specify whether materials can be added as items on approved, non-interfaced material orders or purchase orders, or as items on open purchase orders. The following describes this functionality:

## Material Orders

The following option applies to material detail lines with a Material Type of M-Material Order.

- Add
 Items to Approved Material Orders Not Interfaced – If this checkbox is
 selected and a material order exists for the IN location that has been approved but
 not interfaced, the material will be added as a new item to the MO. If no approved, non-interfaced material orders are found, initialization will create a new material order for the material.

If
 this option is not selected, initialization will always create a new material order for each material.

## Purchase Orders

TThe following options apply to material detail lines with a Material Type of P-Purchase Order.

- Add
 Items to Approved Purchase Orders Not Interfaced – If this checkbox is
 selected and a purchase order exists for the vendor that has been approved but not
 interfaced, the material will be added as a new item to the PO. If no approved, non-interfaced purchase orders are found for the vendor or this box is not selected, how materials are initialized will depend on the Add Original Items to Valid Open Purchase Order for Vendor and Add Change Order Items to Valid Open Purchase Order for Vendor checkboxes. See below for more information.

-

Add Original Items to Valid Open Purchase Order for Vendor - If this checkbox is
 selected, initialization will assign materials to the highest existing purchase order with the latest date for the vendor. If no approved, non-interfaced material orders are found, initialization will create a new material order for the material.

-

Add Change Order Items to Valid Open Purchase Order for Vendor - If purchase order material detail is set up on an approved or pending change order, and this checkbox is
 selected, initialization will add the material detail lines as items on the highest existing purchase order with the latest date for the specified vendor. If one does not exist, a new purchase order will be created.

If none of these options is checked, initialization will always generate a new purchase order for each material.

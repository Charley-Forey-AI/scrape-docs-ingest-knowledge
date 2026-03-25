---
title: "When to Use POs, MOs, Quotes, and Requisitions | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/materials/when-to-use-pos-mos-quotes-and-requisitions"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/materials/when-to-use-pos-mos-quotes-and-requisitions"
---

# When to Use POs, MOs, Quotes, and Requisitions

The PM Material Detail form allows you to set up materials on a project for purchase orders, material orders, quotes, and requisitions.
When entering material detail, you must specify the material type. The four material types are as follows:

- Purchase Orders – These are identified by a Material Type of P (Purchase
 Order) and are used when the materials needed are to be purchased from
 a vendor. Materials set up on purchase orders in this program are
 updated to, and processed in, the Purchase Orders module. Note: Although you are not required
 to have the PO in Use box checked in PM Company Parameters to
 create purchase orders, it must be checked in order to interface
 them.

- Quotes – These are identified by a Material Type of Q (Quote) and are used
 when the specified material is to be set up on a Material Sales quote.
 (Must have MS in Use box
 checked in PM Company Parameters in order to create quotes.

- Material Orders – These are identified by a Material Type of M (Material
 Orders) and are used when the materials needed are to be pulled from
 your inventory. Materials set up on material orders in this program
 are updated to, and processed in, the IN Material Orders programs.
 (Must have IN in Use box
 checked in PM Company Parameters in order to create material orders.)

- Requisitions – These are identified by a Material Type of R (Requisition)
 and used when the materials needed are to be set up on a requisition
 for routing to a quote (for vendor pricing) or purchase order.
 Materials set up on requisitions in this program are updated to, and
 processed in, the PO requisitions forms. (Must have PO
 Requisitions in Use option checked in PM Company
 Parameters in order to create requisitions.)

When setting up material data, you have the option to work with the original estimate, approved change orders, or pending change orders. If you accessed PM Material Detail directly (i.e. via main menu), the Record Type input is enabled, allowing you to specify whether to work on ‘O-Original’, ‘A-Approved CO’s’, or ‘P-Pending CO’s’. However, if you access PM Material Detail from PM Approved Change Orders or PM Pending Change orders, the Record Type is disabled and you can only work on approved or pending change orders.
You will note that as you enter material detail,
 information about the material line is displayed at the top of the screen.
 This includes Original Estimate units, unit of measure, unit cost, and total
 cost, as well as standard, purchase, and sales unit cost and units of
 measure. Other information, such as vendor name and phase description may
 display as well, depending on whether you have specified to show the
 description above the grid (via F3 Properties).
Note: Although materials imported from estimating are
 cross-referenced with the HQ Material file, specific material information such as the
 U/M, unit cost, and material description may have been overridden in estimating while
 processing the estimate. That information will display in the appropriate fields, rather
 than the information originally specified for that material in HQ Materials.
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Detail

---
title: "PM Material Detail Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/materials/pm-material-detail-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/materials/pm-material-detail-form"
---

# PM Material Detail Form

Use this form to create purchase orders, material orders, quotes, and requisitions.
In addition to the main menu, you can access this form from PM Project Phases, PM Pending Change Orders, or PM Approved Change Orders.
The type of material detail records displayed on the Non-Interfaced and Interfaced tabs depend on how you accessed this form.

- If accessed from the main menu or PM Project Phases, grids display original material detail records (Record Type O-Original)

- If accessed from PM Pending Change Orders, grids display pending change order material detail (Record Type Pending CO’s)

- If accessed from PM Approved Change Orders, grids display approved change order material detail (Record Type A-Approved CO’s)

When you access this form from the main menu, you can change the Record Type from Original (default) to either approved or pending change orders. When you change the record type, additional fields related to approved or pending change orders will display in the grids (for example, ACO and ACO Item or PCO Type, PCO, and PCO Item). Note that these additional fields do not display if PM Material Detail is accessed from any of the other forms listed above, since the record display is limited to records related to the calling form.
The ability to set up material orders, quotes, and requisitions using this form depends on whether you have selected the "in use" options for IN, MS, and PO Requisitions (respectively) in PM Company Parameters. If you have not selected the appropriate options, related fields will not display in either the Non-Interfaced or Interfaced grids, nor will the related option be available in the drop-down menu of the Material Type drop-down.
Note: Purchase orders can be set up here regardless of whether the PO in Use box is checked in PM Company Parameters; however, if not checked, purchase orders cannot be interfaced.

There are two methods to set up material detail: manual entry or import from third-party estimating software using PM Data Import. If importing estimate detail, all materials associated with an estimate are automatically set up here. Material costs are pulled from the estimating material files at the time of interface.
Materials can be set up for the same phase/cost type more than once. For example, you may stock a material, but do not have enough to finish the job and therefore need to purchase an additional amount. You would set up the material on a material order for the stocked portion and on a purchase order for the additional needed amount.
Note: If you enter a phase that does not already exist for the project and you have the Auto-add Cost Type from Material option set to2 (With No Estimates) in PM Company Parameters, the phase/cost type will be added to the project detail automatically, but the original estimate will not be updated. If option is set to 1 (No), you must add the phase/cost type to the project in PM Project Phases before it can be entered with material detail.

Note: If you check the Send box for a material detail line with a Material Type of P-Purchase Order or M-Material Order, you will need to approve the associated purchase order (in PM PO Header) or material order (PM MO Header) before it can be interfaced.

## Available Estimate / Non-Interfaced / Remaining Estimate

These display-only fields are visible in the informational display above the Non-Interfaced and Interfaced tabs. They show estimate information for the selected material detail line. These values are calculated as follows:
FieldCalculation
Available EstimateCurrent Estimated Cost - Actual Cost - Remaining Committed Cost + Non-Interfaced Estimated Cost
Non-InterfacedThis is a more complex calculation that takes a number of factors into consideration. However, in general, this calculation is the sum of the amount and taxes from PM Material Detail and based on certain factors, the subtraction of some PO Item and PO Change Order detail costs (which can include taxes), plus Non-Interfaced Estimated.
Remaining EstimateAvailable Estimate - Non-Interfaced

## Interfaced tab

 When you interface a project to accounting (via PM Interface), all material lines with the Send checkbox selected are interfaced and moved to the Interfaced tab (with the exception of requisition lines, which are moved to this tab as soon as they are initialized). Once a material is moved to the Interfaced tab, it cannot be edited
Note: Before you interface material detail, you must approve the associated purchase order (in PM PO Header) or material order (in PM MO Header). Once approved, you must then select the Send checkbox for each applicable material line in this form.

 You cannot change the dollar amounts for interfaced material detail; however, if you need to change original amounts after interfacing, you can create a change order using PM Change Orders.
Note: Interfaced material detail updates the Purchase Order, Inventory, and Material Sales modules.

Related concepts

- [Material Buyout Overview](/en/vista/vista/project-management/materials/material-buyout-overview)

- [When to Use POs, MOs, Quotes, and Requisitions](/en/vista/vista/project-management/materials/when-to-use-pos-mos-quotes-and-requisitions)

- [About PO/MO/Quote/Requisition Numbers](/en/vista/vista/project-management/materials/about-pomoquoterequisition-numbers)

Related tasks

- [Correct an Interfaced Purchase Order Item](/en/vista/vista/project-management/materials/correct-an-interfaced-purchase-order-item)

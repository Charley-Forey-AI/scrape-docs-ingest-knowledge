---
title: "About PO/MO/Quote/Requisition Numbers | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/materials/about-pomoquoterequisition-numbers"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/materials/about-pomoquoterequisition-numbers"
---

# About PO/MO/Quote/Requisition Numbers

Project Management allows you to enter materials for a project using purchase orders, material orders, quotes, and requisitions. This topic discusses both manual and automatic numbering for these items.
You can enter purchase order, material order, and quote numbers manually or via initialization. The initialization process generates PO and MO numbers based on the numbering options defined in PM Company Parameters (Material Parameters tab).
For both material orders and purchase orders, additional company options
 determine whether material detail will be initialized to approved/not interfaced
 material order and purchase orders, or to open purchase orders (purchase order material
 detail lines only). For more information about these options, see [About the Add Items to Approved MOs/POs Options](/en/vista/vista/project-management/setupmaintenance/about-the-add-items-to-approved-mospos-options).
For quotes, numbers are generated based on the Last Used Quote # field in MS Company
 Parameters; however initialization is only possible if you have checked the Auto-Generate Quote #'s box.
 Requisition numbers must be initialized; no manual assignment is allowed. However, you
 will need to check the Send
 flag before initialization can occur. In addition, once initialized, the material line
 will be moved to the Interfaced tab and cannot be edited, since initialization
 automatically updates the requisition to PO. Any necessary changes must be made via the
 PO module. If you delete a requisition in PO and its status is not set to ‘5’
 (Complete), the requisition number will be cleared from the material line and the
 material line will be redisplayed on the Non-Interfaced tab. (Note: The status of a
 requisition is shown in the Req Line Status column on the
 Interfaced grid.)

## Initializing PO/MO/Quotes/Requisitions

Initialization allows you to have the system automatically assign purchase order,
 material order, quote, and requisition numbers to the material detail.
When initializing PO and MO numbers, the
 system uses the formats specified in [PM Company Parameters ](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form).

- Purchase Orders – If the
 Project/Vendor option is used for number assignment, only one purchase order
 can be assigned per vendor. If more than one material is assigned to a
 vendor, each material will be set up as a sequentially numbered item on one
 purchase order. If the Project/Seq or Auto-Number option is used for number
 assignment, the header status is considered during initialization to
 determine whether to generate a new PO. If a PO already exists for a vendor
 and it has not yet been interfaced (i.e. it is pending), initializing new
 materials with the same vendor will create new items on the existing PO. If
 the PO's status is ‘open’ (interfaced or created in PO Entry), a new PO will
 be created for that vendor, and all materials assigned to that vendor will
 become items on the new purchase order.
Note: PO items can be created across multiple
 projects (where vendor is the same and the PO Number Type is Project/Vendor
 or Project/Seq), depending on how you have set the
 Significant PO Job Characters
 field in PM Company Parameters. The larger the value, the
 less chance that multiple projects will share the same purchase order.


- Material Orders – Material order
 assignment is based on the
 Group Materials by Location When Initializing
 checkbox in PM Company Parameters. If checked, materials will
 be grouped by location and a separate material order created for each
 location. Materials assigned the same location will be set up as
 sequentially numbered items on the material order, regardless of the format
 specified. If unchecked, materials will be added as items on a single
 material order, regardless of location.

- Quote Numbers – When
 initializing Quote numbers, the system assigns the next available sequential
 number based on the
 Last Used Quote #
 field in MS Company Parameters. However, initialization is
 only possible if you have checked the
 Auto-Generate Quote #'s
 box. Only one quote can exist for a job (project); therefore,
 when using the initialize feature, the system will generate one quote number
 and assign that quote number to all quote lines for the project. Once the
 quote number has been generated, all additional quote lines added will
 automatically be assigned that same quote number.

- Requisition Numbers –
 Requisition numbers must be initialized—they cannot be assigned manually.
 When initialized, the system will assign requisition numbers based on the

 Automatically Generate RQ #
 checkbox in PO Company Parameters. If checked, the

 Last Used RQ #
 field (PO Company Parameters, Requisition Info tab) will
 determine the next sequential number assigned. If not checked, the system
 will assign a number using the highest requisition number and adding one.


Note: In order for requisition numbers to be
 initialized, you must check the
 Send
 flag for the material line. Initialization will assign the
 requisition number, update the line to PO and move the material line to the
 Interfaced tab.
You can use the initialize feature as
 often as desired. If there is a particular material that you do not want a number
 initialized for, make sure to leave the information required for initialization
 blank (i.e., vendor for POs; INCo and IN Location for MOs; MSCo and IN Location for
 Quotes; and the
 Send
 checkbox unselected for requisitions).

Related concepts

- [PM Material Detail Form](/en/vista/vista/project-management/materials/pm-material-detail-form)

- [PM Company Parameters Form](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)

- [Material Buyout Overview](/en/vista/vista/project-management/materials/material-buyout-overview)

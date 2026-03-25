---
title: "About the HQ Materials Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form"
---

# About the HQ Materials Form

Use this form to set up the materials that will be used when processing material requisitions, purchases, sales or use.
Materials set up here are used by various modules throughout the system, such as PO and AP (when purchasing materials), EM (when charging parts to equipment), and JC (when charging materials to jobs).
Note: This file is NOT a master file. Materials entered here are
 automatically set up in the material group designated (in HQ Company Setup) for the
 currently active Company. All information set up here applies only to the currently
 active company and any companies that may be sharing the specified material group.

You can use the Escalation Price Index tab to assign indexes to a finish material. You will only use this feature for finished
 good materials having component materials that are eligible for price escalation
 adjustments. The finished good material and specified component must be set up in IN
 Bill of Materials or IN Bill of Materials Override, and the price index must already be
 defined (in HQ Escalation Index) for the specified country and state. For more
 information about pricing indexes, see HQ Escalation Index in Related Topics below.

- The Escalation Price Index grid will
 automatically display all price indexes set up for this material in HQ
 Escalation Index.

- The MS Oil Price Setup report
 provides an easy way to review the material setup for pricing indexes by state.


Use the Additional Units of Measure tab to set up any additional measures. Purchase and Sales U/Ms not equal to the
 standard unit of measure for the specified material must be set up here. For each unit of measure that you set up,
 you must define a conversion factor. This will be used to convert the unit of measure to
 the standard unit of measure. Once you specify the conversion factor, the cost and price
 values will be calculated based on the unit cost and unit price specified for standard
 unit of measure. Cost and price will be in the same ECM as the standard unit of measure.
 (Note: It is important that you understand the effects that the conversion factor will
 have when posted units are updated to IN/GL.
Note: If a material is stocked, you can initialize
 additional units of measure to all of the locations at which the material is stocked
 using the Initialize Inventory option in the File menu. However, once initialized to
 Inventory, changes to the unit of measure here will not be updated to any of the
 locations. You will need to make the changes manually in IN Location Materials. For
 information about initializing UMs to Inventory, see [](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-material-insert-locations-form)HQ Material Insert Locations.

[](/en/vista/vista/administration/headquarters/material-setup/payment-discounts)Payment Discounts
[](/en/vista/vista/administration/headquarters/material-setup/material-conversion-costprice-calculations)Conversion Cost/Price Calculations
[](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-material-insert-locations-form)HQ Material Insert Locations
[](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-material-categories-form)HQ Material Categories
[](/en/vista/vista/job-resources/inventory/setup--maintenance/location-materials/about-the-in-location-materials-form)IN Location Materials
[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-vendor-materials-form)PO Vendor Materials

Related information

- [Material Units](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/material-units)

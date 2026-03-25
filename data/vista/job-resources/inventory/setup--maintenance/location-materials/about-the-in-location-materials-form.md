---
title: "About the IN Location Materials Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/setup--maintenance/location-materials/about-the-in-location-materials-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/setup--maintenance/location-materials/about-the-in-location-materials-form"
---

# About the IN Location Materials Form

Use this form to set up materials at specific Inventory
 locations (that are already set up in the IN Locations form).
Materials can only be set up for a location if the
 Stocked in
 Inventory box in [HQ Materials](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form) is selected. Inventory locations represent
 the plants or warehouses where materials are manufactured or stored. Information set up
 here is specific to the material/location.
In addition to manual setup in this form, materials
 can be set up automatically using IN Material Initialize (File > Initialize
 Material). Use the initialize feature to quickly set up a range of materials (in a
 category or range of categories) to a specified location. Once initialized, the material
 can be edited by location using IN Location Materials.
Info tab
Use this tab to define standard information about the
 material/location, such as the last vendor from which the material was purchased, the last
 unit cost of the material, low stock and reorder quantities, weight conversion, physical
 location (e.g. the bin number, shelf, or aisle), and the last count date.
The Material Options section is used to
 indicate whether the material is active for the location, the material is produced as it
 is sold, whether units produced and/or sold are updated to GL, and whether warning will
 display when posting the material on a ticket will result in a negative 'on hand'
 quantity.
Cost & Quantities tab
Use this tab to set up costs and quantities for each
 material/location, as well as the markup/discount rates to use when selling the material to
 customers, jobs, inventory, equipment, or service centers (in SM).

With the exception of the markup/discount
 rates, the fields on this tab are automatically maintained by the system when processing
 in various material posting forms; therefore, once the required information is set up,
 changes made in this form should be unnecessary.
If you find it necessary to change the Std
 Unit Cost or Std Unit Price for a material, when saving or moving off the record, a
 message displays indicating the change and asking if you want to update matching Std
 Unit Costs and Prices in Additional Unit of Measures. Select Yes to perform the update;
 the system will update any additional unit of measure having a unit cost and/or unit
 price equal to the Std Unit Cost and/or Unit Price x Conversion Factor.
If you select No, the record is saved
 without updating the changes for the additional units of measure; you will need to
 update changes manually.
Note: Adjustments made directly in this form do not
 automatically update General Ledger; you will need to make the GL adjustments
 manually.

Additional Units of Measure
Use this tab to set up additional units of measure in which a
 material may be bought or sold, without affecting the original unit of measure information
 set up in HQ Materials.
Each additional unit of measure must have a
 conversion factor, unit cost, and unit price, which will be used to track and update the
 material when it is bought or sold in a non-standard unit of measure.
First, set up each additional unit of
 measure for the selected material in HQ Material Unit of Measures. Then when assigning
 materials to locations in this form, use this tab to change the conversion factor, unit
 cost, and/or unit price for a specific unit of measure/material/location. This will not
 affect other locations using the same material and units of measure. This tab also
 tracks the last unit cost of the material when purchased in each additional unit of
 measure. After initial entry of the last unit cost, ECM, and last cost update, the
 system automatically updates the information whenever the material is purchased in that
 unit of measure.
Note: The 'bUnits' datatype has a decimal precision of
 three (i.e. .000); therefore, it is important that you understand the effects that the
 conversion factor specified here may have when updating IN/GL with posted units. If the
 conversion factor has a non-zero value in the 4th (.0245) or 5th position (.00245),
 rounding may occur. See the example below:
Posted Units:10.00
Unit Cost:128.2500
Conversion Factor:.00245
Conversion to Std
 Units:.025 (10.00 x .00245 = 0.0245,
 rounded to .025)
Total Cost:3.21

Calculation with
 decimal precision of 5 (.00000)
Posted Units:10.00
Unit Cost:128.25
Conversion Factor:.0245
Converted Units:.0245 (10.00 x .00245 =
 0.0245)
Total Cost:3.14 (.0245 x 128.25 - 3.14212,
 rounded to 3.14)

Variance:.07 (3.21 - 3.14 = .07)

Related information

- [About the IN Material Copy Form](/en/vista/vista/job-resources/inventory/setup--maintenance/location-materials/about-the-in-material-copy-form)

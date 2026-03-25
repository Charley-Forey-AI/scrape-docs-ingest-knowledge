---
title: "Set up an Override Bill of Materials | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/production/about-setting-up-an-override-bill-of-materials/set-up-an-override-bill-of-materials"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/production/about-setting-up-an-override-bill-of-materials/set-up-an-override-bill-of-materials"
---

# Set up an Override Bill of Materials

Use the IN Bill of Materials Override form to set up an override bill of
 materials.
When you set up an override bill of materials, you
 have the option to set up the component materials manually or by initialization.
 However, you can only use the initialization feature if:

- you have set up a bill of materials for the location group associated with
 the finished good's location, AND

- you only want to change the composition of the raw materials, AND

- changes to initialized values are specific to the location and will not
 affect the standard Bill of Materials.

 If you want to use component materials from different locations, you must set these up manually.
To set up an override bill of materials:

1. In the Location field, enter the location of the finished good or
 press F4 to select from a list of valid locations.

1. In the Finished
 Material field, enter the finished good or press F4
 to select from a list of valid materials. The system automatically defaults the
 description and UM, which cannot be changed.

1. In the Notes field, enter any pertinent information about this
 finished good.

1. Save the record. A
 message displays asking if you want to initialize the components.

1. Click Yes
 to initialize the components defined on the standard bill of materials for the
 location group to this override bill of materials or No
 to set up an override bill of materials manually.Note:If a standard bill of
 materials does not exist for the location group, no components will be
 initialized to the grid and you will need to enter them manually (see
 below).

1. Click on the Components
 tab.

1. If you are setting up the override bill of materials manually:

1. In the
 Component Location
 field, enter the location of the component (raw) material or press
 F4 for a list of
 valid locations.

1. In the
 Component Material
 field, enter the component needed for this finished good or press
 F4 to select from a
 list of valid materials for the specified location.

1. If the finished good is
 measured in units, use the Units field to enter the
 number of units needed of the raw material to complete one unit of the finished
 good. If the finished good is
 measured in weight, use the % Weight field to enter
 the percentage of the raw material that makes up one weight unit of the
 finished good for this location. For example, if the unit of measure for the
 finished good is TON, enter the percent of one ton that is needed of the raw
 material.

1. Save the record.

1. Repeat steps 7-9 for
 each additional component that makes up one unit of the finished good.

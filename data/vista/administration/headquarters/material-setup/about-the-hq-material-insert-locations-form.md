---
title: "About the HQ Material Insert Locations Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/material-setup/about-the-hq-material-insert-locations-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/material-setup/about-the-hq-material-insert-locations-form"
---

# About the HQ Material Insert Locations Form

This form is used to initialize materials and additional units of measure to inventory locations.
It is accessed by clicking the Initialize Inventory button (Info tab) in HQ Materials, or by selecting the Initialize Inventory option from the File menu of HQ Materials.
Note: This feature is only available for materials that are
 flagged as ‘active’ and ‘stocked in inventory’.
You can only initialize the material on which you currently have focus. However, you can initialize that material to one or more Inventory locations at one time. If additional units of measure exist for the material, they will be updated to each location as well.
Note: If you wish to initialize multiple materials to a single
 location, use IN Material Initialize (IN Location Materials à File à Initialize
 Materials).
To initialize the material, you must first specify the destination Inventory company. The destination company must share the same material group (defined in HQ Company Setup) as the current company. Once specified, the location selection grid displays all of the locations available for that company based on the selected Location Insert option.

- Locations Without Material – If this option is selected, the grid will display only those locations at which the material does not already exist. You might find this option most useful when you want to add an existing material to new locations or to existing locations that have not already been updated with the material.

- All Locations – If this option is selected, the grid will display all locations for the IN company. This option is most useful when you are initializing a new material or when you want to initialize new units of measure for an existing material to all locations.

The UM Insert Options allow you to specify whether to initialize all units of measure or a selected unit of measure. If you are just adding a new unit of measure, you can use the Select UM option. This will allow you to update only that UM for all selected locations.
The Active Locations option allows you to restrict initialization to only those Inventory locations that are currently active (i.e., locations with the Active flag checked in the IN Location Materials form). When checked, materials flagged as ‘inactive’ will be skipped during the copy process.
Once you have set your criteria, click the Insert button. The material and units of measure will be updated to each of the specified locations.
Note: You cannot use this program to update changes to existing
 material detail.

[](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form)HQ Materials
[](/en/vista/vista/job-resources/inventory/setup--maintenance/location-materials/about-the-in-location-materials-form)IN Location Materials
[](/en/vista/vista/job-resources/inventory/setup--maintenance/location-materials/about-the-in-material-initialize-form)IN Material Initialize

---
title: "Field Definitions: HQ Material Insert Locations Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/material-setup/about-the-hq-material-insert-locations-form/field-definitions-hq-material-insert-locations-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/material-setup/about-the-hq-material-insert-locations-form/field-definitions-hq-material-insert-locations-form"
---

# Field Definitions: HQ Material Insert Locations Form

The following is a list of field descriptions for the HQ
 Material Insert Locations form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  IN Co

 Specify the IN company to which you are initializing this material. Must be an IN company that shares the same material group as the currently active company.

##  UM Insert Options

- All UM's – Select this option to initialize all ‘additional’ units of measure for this material. Units of measure will be initialized to locations specified below, skipping those locations for which the units of measure already exist.

- Select UM – Select this option to initialize a specific ‘additional’ unit of measure (indicated to the right) for this material. The selected unit of measure will be initialized to locations specified below, skipping those locations for which the units of measure already exist.

##  Select UM

 Enabled only when ‘Select UM’ insert option is selected.
 Specify the additional unit of measure to initialize to locations indicated below.

##  Location Insert Options

- Locations Without Material – Select this option to initialize the specified material/UM’s to locations that do not already stock the material. Location selection grid will refresh to display only those locations at which the material specified above does not already exist.

- All Locations – Select this option to initialize the specified material/UM’s to all locations. Location section grid will refresh to display all locations for the specified IN company.

Note: These options do not control the actual selection of
 locations to initialize. They only control which locations are displayed for selection. You
 must manually select the locations you want to initialize.

##  Active Locations

 Check this box to initialize only those selected locations that have the Active flag checked in IN Location Materials.
 Leave this box unchecked to initialize all selected locations, regardless of their ‘active/inactive’ status.

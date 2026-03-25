---
title: "About the IN Material Copy Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/setup--maintenance/location-materials/about-the-in-material-copy-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/setup--maintenance/location-materials/about-the-in-material-copy-form"
---

#  About the IN Material Copy Form

Use this form to copy materials from one Inventory location to
 another.
Although materials can be initialized to a location
 (File > Initialize Materials) in the IN Locations form, overrides to existing values and entry of
 additional information must be handled individually for each material as applicable to
 that location. Use this form to copy materials already set up at one location to another
 location, without having to re-enter the overrides or additional information. It can
 also be used as a quick method of copying new materials (that were added to HQ after
 initial setup), by adding to one location, editing information as needed, then copying
 to other applicable locations.
Note: Materials may only be copied if they are flagged as Active
 and exist in both IN Location Materials and HQ Materials.
To copy materials, you must specify the source
 location, the category or material to copy (cannot be both), and the destination
 location(s). When selecting destination locations, you can specify to show only those
 locations not currently stocking the material or all locations. In addition, you can
 specify to show only the ‘Active’ locations. Then select the desired locations or check
 the Copy All Locations option to select all locations. Then click the Copy button to
 begin the copy process. The system copies all information defined for the material to
 the selected locations, with the exception of the following:

- Last Vendor

- Last Cost Update

- Last Count Date

- Physical Location

- Current Quantities (On Hand, Allocated, etc.)

Additionally, if the source location specifies JC
 Costing Phase, and the destination location does not have a JC Co and Job specified (in
 the IN Locations form), the JC phase is copied, but grayed out, and a message is
 displays stating that the JC company and/or Job are missing. Once a JC company and Job
 for the new location are specified, the message disappears and the field is enabled.
Note: Existing information will not be overwritten. If a material
 already exists at a location, no update will occur for that location and
 material.
 Once copied, information can be edited/added as
 necessary.

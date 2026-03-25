---
title: "About the IN Production Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/production/about-the-in-production-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/production/about-the-in-production-entry-form"
---

# About the IN Production Entry Form

Use this form to enter production activity (production of
 finished goods from component materials).
This form is strictly for use with manual entry of
 production; it cannot be used to view or edit production entries posted via the Material
 Sales module.
When a finished good is produced, inventory is relieved of the necessary components based on specifications defined in the Bill of Materials. The system first checks to see if an override Bill of Materials exists for the specified Location. If it does, the system uses the override Bill of Materials to produce the finished good and relieve Inventory. If no override Bill of Materials is found, the system uses the standard Bill of Materials for the Location Group.
You can also have the system update the average cost
 of a finished good with the sum of the component costs during production. To do this,
 you must select the Update Average Cost of Material with Sum of
 Component Costs checkbox for the finished good in IN Location Materials
 and set the Cost
 Method for the location to Average Cost in the IN Locations form or the
 IN Location Category Override form (if overriding accounts by location/category). Then,
 when you add the finished good to a production batch, the system will automatically
 update the unit cost for the finished good based on the current costs of the
 components.
Tasks
[Manually Entering Production Activity](/en/vista/vista/job-resources/inventory/production/manually-entering-production-activity)

Related information

- [Material Pricing](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/material-pricing)

- [How Component Materials are Handled During Production](/en/vista/vista/job-resources/inventory/production/how-component-materials-are-handled-during-production)

- [About the GL Updates for Posted Production](/en/vista/vista/job-resources/inventory/production/production-posting/about-the-gl-updates-for-posted-production)

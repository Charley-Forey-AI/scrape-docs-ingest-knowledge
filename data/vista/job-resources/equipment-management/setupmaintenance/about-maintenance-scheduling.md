---
title: "About Maintenance Scheduling | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-maintenance-scheduling"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-maintenance-scheduling"
---

# About Maintenance Scheduling

If you are using the maintenance scheduling feature, you can
 schedule maintenance for components just as you would for a regular piece of equipment.
Scheduling for components can coincide with that
 of the primary piece of equipment, or it can differ. However, because scheduled
 maintenance is based on the equipment’s usage, you must check the Update
 Hours, Update Miles, and/or Update Fuel
 boxes for the component (in EM Equipment, Comp/Attach tab) in order for the scheduling
 feature to work. For example, you might check the Update Miles box for the tire
 components and check the Update Hours box for the engine
 component. Although usage is not posted directly to a component, the hours, miles,
 and/or fuel will be updated as applicable for the component when usage is posted to the
 primary piece of equipment.
Fuel usage is updated by adding the
 additional units to the Fuel Used for each component flagged for fuel update. Hours and
 miles are updated by adding the difference between the old reading and the new reading
 of the equipment to the component meter.
Example:
Equip/ComponentUpdate MilesOld Odometer
 ReadingNew Odometer
 Reading
Equipment 10101n/a65,00066,000(66,000 - 65,000 =
 1,000)
Component 100
 (Transmission)Yes 5,0006,000(5,000 + 1,000 =
 6,000)
Component 200
 (Engine)No00

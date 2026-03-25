---
title: "Manually Entering Production Activity | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/production/manually-entering-production-activity"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/production/manually-entering-production-activity"
---

# Manually Entering Production Activity

You can manually enter production activity using the IN Production Entry form.
Finished goods are produced using one of two methods: Auto Production or Manual Production. You will generally use auto production for finished goods that you produce as they are sold. For these materials, the Auto Production checkbox is selected in IN Location Materials for each location that produces the finished good. The system will then initiate automatic production each time you post the finished good to a ticket in MS Ticket Entry.
For finished goods that you produce and sell later, you will use IN Production Entry to manually enter production activity. When you post a production entry batch, the system adds the finished good to the on hand inventory, where it is stored until it is sold in MS Ticket Entry. As with auto-produced materials, manually produced finished goods require a bill of materials for each production location or location/category (if using location/category overrides). In addition, you will need to clear the Auto Production checkbox for each production location in IN Location Materials.
To manually enter production activity for a finished good:

1. Launch IN Production Entry and [create a new batch](/en/vista/vista/system-tools/user-interface-guide/system-forms/batch-processing/about-the-batch-selection-form).

1. In the Seq# field, enter N or +.

1. In the Date field, enter the production date.

1. In the Location field, enter the production location for the finished good. This is the location that will be updated with the finished good.Note: If a standard Bill of Materials is used for the finished good (i.e. no override Bill of Material is found), this is also the location the system will use to pull the component materials.

1. In the Finished Material field, enter the finished good being produced or press F4 to select from a list of valid finished goods for the specified location.

1. In the Units field, enter the number of units being produced of the finished good.

1. If you allow overriding the unit cost (setting in IN Company Parameters), enter the override unit cost in the Unit Cost field, if applicable. Otherwise, accept the defaulted unit cost.If you do not allow overriding the unit cost, proceed to the next step.

1. In the Memo field, enter any notes applicable to this production entry.

1. Save the record.

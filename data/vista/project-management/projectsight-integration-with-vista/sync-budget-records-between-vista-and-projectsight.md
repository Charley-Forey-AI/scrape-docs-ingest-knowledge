---
title: "Sync Budget Records Between Vista and ProjectSight | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projectsight-integration-with-vista/sync-budget-records-between-vista-and-projectsight"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projectsight-integration-with-vista/sync-budget-records-between-vista-and-projectsight"
---

# Sync Budget Records Between Vista and ProjectSight

Create budget codes and items in either Vista or ProjectSight and sync the data to the other system. However, after the initial creation of the budget record, you must make all modifications in ProjectSight.
Note: The format of Vista job phases and cost types must be configured during the integration setup. You can also configure the integration to *only* send original estimates from Vista to ProjectSight if the original Hours, Units, and Cost are greater than zero (0).

The integration supports lump sum (LS) and unit-based phase codes.

Send Budget Data from Vista to ProjectSight
To send budget data from Vista to ProjectSight, complete the following:

1. If you haven't already, set up job phase information in Vista by going to the JC Job Phases form. Enter Phase codes and Cost Types. For linked jobs / projects, new Vista job phases and cost types set up on the JC Job Phases form automatically flow into ProjectSight.

1. Set up budget amounts in Vista on the JC Original Estimates form. Enter a unit of measure (UM), Hours, Units, Unit Cost, and Cost.

1. Make all budget modifications in ProjectSight after the phase codes have been synchronized to ProjectSight budget codes.ProjectSight Help: For more information about budget records in ProjectSight, see [Budgets](https://prod.projectsightapp.trimble.com/Web/Web%20Help/Content/Online_Help/Records/BCM/Budgets.htm).

Send Budget Data from ProjectSight to Vista
To send budget data from ProjectSight to Vista, complete the following:

1. Set up budget items in ProjectSight. Enter the Budget Code, UOM, Original Budget Hours, Original Budget Quantity, Original Budget Unit Price, and Original Budget.

1. Set the budget items to the correct status to send them to Vista. Typically, this status is Approved, but your organization can determine the status during initial setup.After you create budget items in ProjectSight and the records are in the correct status, the data is queued to go to Vista.

1. Make all budget modifications in ProjectSight.ProjectSight Help: For more information about budget records in ProjectSight, see [Budgets](https://prod.projectsightapp.trimble.com/Web/Web%20Help/Content/Online_Help/Records/BCM/Budgets.htm).

Note:

- Changes to existing phase codes and original estimates in Vista do *not* update linked ProjectSight budget items.

- Modifications to budget records in ProjectSight that are in the correct configured status overwrite budget records in Vista.

- Even if you delete an original estimate line in Vista, it is *not* deleted from the ProjectSight budget item.

- If you delete an original budget line in ProjectSight, the original estimate in Vista is deleted.

Associated fields in
 Vista and ProjectSight:
Vista JC Original Estimates Field NameProjectSight Budgets Field Name
Job Phase
Cost Type
Budget Code
UMUOM
HoursOriginal Budget Hours
UnitsOriginal Budget Quantity
Unit CostOriginal Budget Unit Price
CostOriginal Budget

---
title: "Field Definitions: EM Work Order Init Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-initialize-form/field-definitions-em-work-order-init-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-initialize-form/field-definitions-em-work-order-init-form"
---

# Field Definitions: EM Work Order Init Form

The following is a list of field descriptions for the EM Work
 Order Init form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## WO Date

Required.
Enter the date you want assigned as the creation date for all initialized work orders.

## Days in Advance

Required.
Specify the number of days in advance for scheduled items to be included on work order. The system will update the Standard Maintenance Groups Matching Criteria grid with all maintenance groups scheduled by time that are not already on an open work order and have at least one item due for maintenance within the number of days specified here. For example, if an item is scheduled for maintenance every 90 days and will be due for maintenance in 15 days, enter a number equal to or greater than 15 to include this item as needed.
The system compares the value entered here
 with the maintenance item’s Last Done Date and scheduling time interval to determine if it
 is due for maintenance. If the Last Done Date field is null (blank) and
 a time interval is specified for the maintenance group, it will be considered due for
 maintenance. If no time interval is specified for the maintenance group and the Last Done
 Date is null, the equipment will only be added to the grid once it meets the Hours, Miles,
 or Gallons requirement.
Note: Depending on how you set the Standard Maintenance
 Group Options in EM Company Parameters, the system may include maintenance items and linked
 standard maintenance groups during initialization, even if they are not due for
 maintenance. For more information, see [About the Standard Maintenance Group Options](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-standard-maintenance-group-options).Annual Fixed Date SMGs
For standard maintenance groups with a Basis
 of Annual Fixed Date, the Days in Advance value will be used during the selection process
 only if the Create
 Work Order: ___ days prior to annual fixed date field is blank in EM
 Standard Maintenance Groups. In this case, the system will add items to the grid when
 either of the following conditions apply:

-  the equipment has not been serviced within 45 days difference between the Last Done date of the item and the WO Date, plus the specified Days in Advance (current and following years).

- the equipment has been serviced within 45 days difference between the Last Done date of the item and the WO Date (current or prior year).

## Variances in Advance

Required.
Specify the number of variances in advance (0-32,767) for scheduled items to be included on work order. The system will update the 'Standard Maintenance Groups Matching Criteria 'grid with all maintenance groups scheduled by meter with a 'warning' interval falling within the variance specified here that are not on an open work order and have at least one maintenance item due. The Variance specified here will be a multiple of the warning interval.
For example, if an item is scheduled for maintenance every 3000 miles/kilometres with a warning interval of 200 miles/kilometres and is due for maintenance in 300 miles/kilometres, enter a number equal to or greater than 2 in this field. This number is multiplied by the interval value to determine the variance value (2 x 200 = 400). If you enter 1 as the variance, the item will not be identified as due for maintenance.
Note: Depending on how you set the Standard Maintenance Group Options in EM Company Parameters, the system may include maintenance items and linked standard maintenance groups during initialization, even if they are not due for maintenance. For more information, see [About the Standard Maintenance Group Options](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-standard-maintenance-group-options).

## JC Co

Enter the JC company (from JC Company Parameters) by which to restrict initialization or leave blank to include all companies.
Refresh / Clear Criteria
Click the Refresh button to populate the grid with
 items meeting criteria. Click the Clear Criteria button to clear criteria
 parameters and entries in grid.

## Job

Enter
 the job (from JC Jobs) by which to restrict initialization or leave blank to include all
 jobs.
Refresh / Clear Criteria
Click the Refresh button to populate the grid with
 items meeting criteria. Click the Clear Criteria button to clear criteria
 parameters and entries in grid.

## Location

Enter the location (from EM Locations) by which to restrict initialization or leave blank to include all locations.
Refresh / Clear Criteria
Click the Refresh button to populate the grid with
 items meeting criteria. Click the Clear Criteria button to clear criteria
 parameters and entries in grid.

## Category

Enter the category (from EM Categories) by which to restrict initialization or leave blank to include all categories.
Refresh / Clear Criteria
Click the Refresh button to populate the grid with
 items meeting criteria. Click the Clear Criteria button to clear criteria
 parameters and entries in grid.

## Department

Enter the department (from EM Departments) by which to restrict initialization or leave blank to include all departments.
Refresh / Clear Criteria
Click the Refresh button to populate the grid with
 items meeting criteria. Click the Clear Criteria button to clear criteria
 parameters and entries in grid.

## Assigned Shop

Enter the shop (EM Shops) by which to restrict initialization or leave blank to include all shops.
Refresh / Clear Criteria
Click the Refresh button to populate the grid with
 items meeting criteria. Click the Clear Criteria button to clear criteria
 parameters and entries in grid.

## Equipment

Enter the equipment (from EM Equipment) by which to restrict initialization or leave blank to include all equipment.
Refresh / Clear Criteria
Click the Refresh button to populate the grid with
 items meeting criteria. Click the Clear Criteria button to clear criteria
 parameters and entries in grid.

## Beginning / Ending Std Maint Group

Enter the beginning and ending group in a
 range of maintenance groups by which to restrict initialization or leave blank to include
 all maintenance groups.
Refresh / Clear Criteria
Click the Refresh button to populate the grid with
 items meeting criteria. Click the Clear Criteria button to clear criteria
 parameters and entries in grid.
Note: If you use the linking feature for maintenance groups
 (i.e., you have linked maintenance groups via the Linked Groups tab in EM Standard
 Maintenance Groups), the filtering process will include maintenance groups linked to those
 in the specified range, regardless of whether they are within the specified range. For
 example, if you linked SMG1 to SMG2 and SMG3, and SMG2 to SMG3, and you enter SMG3 as the
 beginning/ending maintenance group, the system will update the grid with SMG1, SMG2, and
 SMG3, even though SMG1 and SMG2 were not in the specified range.

## Create

Check this box to create a work order for this maintenance group. If an open work order exists for this equipment and maintenance group, it will be skipped.
Note: The system automatically checks this box for all maintenance groups added to the grid.
Uncheck this box to skip this maintenance
 group when creating work orders. You can also click the Unselect All
 button to uncheck all items simultaneously.
Note: Checking/unchecking this box for a maintenance group
 automatically checks/unchecks the Initialize box for the related
 maintenance items.

## Initialize

Check this box to include this item when
 creating work orders. The system automatically checks this box for all items in a
 maintenance group when the Create box is checked for the maintenance
 group (in the Std Maint Groups Matching Criteria grid).
Uncheck this box to exclude this item when creating work orders.
Note: Checking/unchecking this box for all maintenance items
 in a group automatically checks/unchecks the Create box for the related maintenance
 group.

##  Override Shop

 Enter the shop (from EM Shops) that will be responsible for all work orders generated by this program. If left blank, each work order/item will be assigned the shop specified for the equipment in EM Equipment.

##  PR Co

 Enter the PR Co of the mechanic being assigned to all initialized work orders. Leave blank to assign the PR Co manually in EM Work Order Edit.

##  Mechanic

 Enter the mechanic (from PR Employees) to assign to all work orders generated by this program. Leave blank to assign the mechanic manually in EM Work Order Edit.

## IN Co

Specify the IN company supplying the parts needed for all work orders generated by this program. Initially defaults the IN company specified in EM Company Parameters.

##  IN Location

 Specify the inventory location supplying the parts needed for all work orders generated by this program. If left blank, you can assign the location manually in EM Work Order Edit.

## Due

Enter the date by which all work orders generated by this program are due for completion.

## Schedule

Enter the date on which to schedule maintenance for all items on work orders generated by this program.

##  Repair Code

 Enter the repair code, up to 10 characters, for all work orders generated by this program.

## Beginning WO

This field is only enabled when not using the
 auto-sequencing feature for work orders (i.e, the Auto Sequence Work Order # box is
 unchecked in EM Company Parameters.
Enter the beginning work order number, up to
 10 characters. All work orders will be assigned a sequential number beginning with this
 number.

---
title: "About Linked Maintenance Groups | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/work-orders/about-linked-maintenance-groups"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/work-orders/about-linked-maintenance-groups"
---

# About Linked Maintenance Groups

Information about linked maintenance groups.
If you are using the linking feature for maintenance groups (via Linked Groups tab in [EM Standard Maintenance Groups](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-standard-maintenance-groups-form)), when you initialize standard maintenance groups for work order generation in EM Work Order Initialize, the system uses the Standard Maintenance Group Options in EM Company Parameters in conjunction with the search criteria to determine which linked groups to add to the grid. The options are as follows:

- Initialize all Standard Maintenance Group Items

- Always Initialize Linked Standard Maintenance Groups

These options determine whether you will include items and/or linked maintenance groups, regardless of whether they are due for maintenance. For more information about these options, see [About the Standard Maintenance Group Options](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-standard-maintenance-group-options).
If you filter by standard maintenance group (SMG), the system will include linked maintenance groups, regardless of whether all groups are within the specified range.
 For example, in EM Standard Maintenance Groups, say you link SMG1 to SMG2 and SMG3, and link SMG2 to SMG3. When initializing work orders in EM Work Orders Initialize, you select to filter by standard maintenance group range, entering SMG3 as the beginning/ending maintenance group. When you click the Refresh button, the system updates the grid with SMG1, SMG2, and SMG3, even though SMG1 and SMG2 were not in the specified range. If SMG2 was not linked directly to SMG3, it would not be included in the grid; only SMG3 and SMG1 would be displayed.
Note: Because you can have multiple links between maintenance groups, the grid will show only the highest parent for linked groups. In the example above, SMG3 is the highest parent for both SMG1 and SMG2 and will therefore display as the Linked To SMG for both SMG1 and SMG2.

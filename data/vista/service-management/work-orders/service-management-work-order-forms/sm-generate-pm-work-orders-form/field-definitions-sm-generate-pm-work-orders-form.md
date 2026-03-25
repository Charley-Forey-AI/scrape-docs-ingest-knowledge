---
title: "Field Definitions: SM Generate PM Work Orders Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-generate-pm-work-orders-form/field-definitions-sm-generate-pm-work-orders-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-generate-pm-work-orders-form/field-definitions-sm-generate-pm-work-orders-form"
---

# Field Definitions: SM Generate PM Work Orders Form

The following is a list of field descriptions for the SM
 Generate PM Work Orders form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Service Center

Enter the service center (from SM Service Centers) by which to filter agreements with services due.
 Upon clicking the Search button, the grid (below) will display all services that are assigned this service center (at the service level in SM Work Schedule or at the service site level in SM Service Sites) and match all other filter criteria.

## Division

Division field in the Search Criteria section of the PM Work Order form.

Enter the division by which to filter agreements with services due.
 Upon clicking the Search button, the grid will display all services for agreements with this agreement type that match all other filter criteria.
Leave blank if not filtering by division.

## Customer

Enter the SM customer by which to filter agreements with services due.
 Upon clicking the Search button, the grid (below) will display all agreements/services for this customer that match all other filter criteria.

## Service Site

Enter the service site (from SM Service Sites) by which to filter agreements with services due.
 Upon clicking the Search button, the grid (below) will display all services that are assigned this service site and match all other filter criteria.

## Agreement Type

Enter the agreement type (from SM Agreement Types) by which to filter agreements with services due.
 Upon clicking the Search button, the grid (below) will display all services for agreements with this agreement type that match all other filter criteria.

## Due Within the Next ___ days

Enter the number of days to use in determining services due for work order generation.
Upon clicking the Search button, the grid (below) will display all agreements/services that are due within the number of days specified here and that match all other filter criteria.

## View Skipped Work Orders

Select this checkbox to view a list of
 agreement services that are flagged as "skipped". When you click the Search button, only
 those services with the Skip checkbox selected will display in
 the grid.
Leave this checkbox unselected to view
 scheduled agreement services that are available for work order generation. When you click
 the Search button, only those services that do not have the Skip checkbox
 selected will display in the grid.

## Create

Check this box to create a work order for this service/due date.
When you click the Process button (below), the system will generate a preventative maintenance work order (in SM Work Orders) and add a single scope to the work order for this service.
Leave this box unchecked if you do not want to create a work order for this service/due date at this time.
Important: If you will be creating a work order for this
 service/due date instance later, do not check the Skip box. Checking the Skip box
 removes the due date instance for the service from the grid, and flags it so that is no
 longer available for work order generation. It does not, however, remove future due date
 instances for the service.

## Skip

Check this box to skip this service/due date instance when generating preventative maintenance work orders.
When you click the Process button (below), the system will flag this service/due date instance as "skipped" and will make it unavailable for future work order generation.
Important: You should only check this box for services that
 you do not intend to perform and therefore, will never create a work order for. If you wish
 to exclude a service from the current work order generation session, but leave it available
 for a future session, leave both the Create and Skip boxes
 unchecked.
Leave this box unchecked if you do not want skip this service/due date instance when generating work orders.

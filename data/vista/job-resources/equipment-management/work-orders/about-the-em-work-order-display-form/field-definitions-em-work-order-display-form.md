---
title: "Field Definitions: EM Work Order Display Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-display-form/field-definitions-em-work-order-display-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-display-form/field-definitions-em-work-order-display-form"
---

# Field Definitions: EM Work Order Display Form

The following is a list of field descriptions for the EM Work
 Order Display form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Work Order Search Option

The Work Order Search Option drop-down on the EM Work Order Display form.
Select the option by which to search for work orders.

- B - Both. Search for both work order headers and work order items. When this option is selected, both the Work Order Header Criteria and Work Order Items Criteria sections are enabled.

- I - Work Order Items Only. Search for work order items only. When this option is selected, the Work Order Item Criteria section is enabled and the Work Order Header Criteria section is disabled.

- H - Work Order Header Only. Search for work order headers only, based on the specified selection criteria. When this option is selected, the Work Order Header Criteria section is enabled and the Work Order Item Criteria section is disabled.

## Search Dates by Work Order Header or Items

The Search Dates by Work Order Header or Items section on the EM Work Order Display form.
Select the date option by which to filter work orders.

- None – Select this option if you do not want to search for work orders by date.

- Created – Select this option to search for work orders based on the creation date. All work orders created on a date that falls within the specified date range will display in the grid.

- Due – Select this option to search for work orders based on the work order due date. All work orders with a due date that falls within the specified date range will display in the grid.

- Scheduled – Select this option to search for work orders based on the scheduled date. All work orders with work scheduled for a date within the specified date range will display in the grid.

Related information

- [Refresh / Clear All](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-display-form/field-definitions-em-work-order-display-form#ID-0000d2f6--en)

- [About the EM Work Order Display Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-display-form)

## Beginning/Ending Date

The Beginning Date and Ending Date fields on the EM Work Order Display form.
These fields are disabled when None is selected in the Search Dates by Work Order Header or Items section.
Enter the beginning and ending in a range of dates by which to search for work orders. All work orders with a Created, Due, or Scheduled date (depending on the Search By Date option above) that falls within this date range will be displayed in the grid below.
Note: Search process applies to work order headers only—it does not apply to work order items.

Related information

- [Refresh / Clear All](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-display-form/field-definitions-em-work-order-display-form#ID-0000d2f6--en)

- [About the EM Work Order Display Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-display-form)

## Work Order Header: Shop

The Shop field on the EM Work Order Display form, Work Order Header Criteria section.
Enter the work order header shop by which to filter work orders. Only work orders with this shop assigned in the work order header will display.
Leave this field blank to include all work orders, regardless of assigned shop.

## Work Order Header: PR Co

The PR Co field on the EM Work Order Display form, Work Order Header Criteria section.
If restricting work order selection by mechanic, enter the PR Co of the mechanic by which to filter work orders. Only work orders assigned this payroll company in the work order header will display in the search results.
 Leave this field blank if not filtering work orders by payroll company and mechanic.

## Work Order Header: Mechanic

The Mechanic field on the EM Work Order Display form, Work Order Header Criteria section.
If restricting work order selection by mechanic, enter the mechanic (from PR Employees) by which to filter work orders. Only work orders assigned this mechanic in the work order header will display in the search results.
 Leave this field blank if not filtering work orders by payroll company and mechanic.

## Work Order Item: PR Co

The PR Co field on the EM Work Order Display form, Work Order Item Criteria section.
If restricting work order selection by mechanic, enter the PR Co of the mechanic by which to filter work orders. Only work orders with items assigned this payroll company will display in the search results.
 Leave this field blank if not filtering work orders by payroll company and mechanic.

Related information

- [Refresh / Clear All](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-display-form/field-definitions-em-work-order-display-form#ID-0000d2f6--en)

- [About the EM Work Order Display Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-display-form)

## Work Order Item: Mechanic

The Mechanic field on the EM Work Order Display form, Work Order Item Criteria section.
If restricting work order selection by mechanic, enter the mechanic (from PR Employees) by which to filter work orders. Only work order items assigned this mechanic will display in the search results.
 Leave this field blank if not filtering work orders by payroll company and mechanic.

Related information

- [Refresh / Clear All](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-display-form/field-definitions-em-work-order-display-form#ID-0000d2f6--en)

- [About the EM Work Order Display Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-display-form)

## Work Order Item: Item Status

The Item Status field on the EM Work Order Display form, Work Order Item Criteria section.

- All - Select this option to display all active and inactive work order items for work orders matching search criteria.

- Active Only - Select this option to display only active work order items for work orders matching search criteria

Related information

- [Refresh / Clear All](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-display-form/field-definitions-em-work-order-display-form#ID-0000d2f6--en)

- [About the EM Work Order Display Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-display-form)

## Equipment

The Equipment field on the EM Work Order Display form.
Specify the equipment (from EM Equipment) by which to filter work order selection. Only work orders for this equipment will display.
 Leave this field blank if not filtering work orders by equipment.
Note: Search process applies to work order headers only—it
 does not apply to work order items.

Related information

- [Refresh / Clear All](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-display-form/field-definitions-em-work-order-display-form#ID-0000d2f6--en)

- [About the EM Work Order Display Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-display-form)

## JC Co

The JC Co field on the EM Work Order Display form.
Specify the JC company (from JC Company Parameters) by which to filter work order selection. Only work orders with equipment assigned this Job Cost company (in EM Equipment) will display.
 Leave this field blank if not filtering work orders by equipment Job Cost company.
Note: Search process applies to work order headers only—it
 does not apply to work order items.

Related information

- [Refresh / Clear All](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-display-form/field-definitions-em-work-order-display-form#ID-0000d2f6--en)

- [About the EM Work Order Display Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-display-form)

## Job

The Job field on the EM Work Order Display form.

This field is enabled only when a company is specified in the JC Co field.
Enter the job (from JC Jobs) by which to filter work order selection. Only work orders with equipment assigned to this job (in EM Equipment) will displays.
Leave this field blank if not filtering work orders by equipment job.
Note: Search process applies to work order headers only—it
 does not apply to work order items.

Related information

- [Refresh / Clear All](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-display-form/field-definitions-em-work-order-display-form#ID-0000d2f6--en)

- [About the EM Work Order Display Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-display-form)

## Location

The Location field on the EM Work Order Display form.
Specify the location (from EM Locations) by which to filter work order selection. Only work orders with equipment assigned this location (in EM Equipment) will display.
Leave this field blank if not filtering by equipment location.
Note: Search process applies to work order headers only—it
 does not apply to work order items.

Related information

- [Refresh / Clear All](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-display-form/field-definitions-em-work-order-display-form#ID-0000d2f6--en)

- [About the EM Work Order Display Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-display-form)

## Category

The Category field on the EM Work Order Display form
Specify the equipment category (from EM Categories) by which to filter work orders. Only work orders with equipment assigned this category (in EM Equipment) will display.
Leave this field blank if not filtering work orders by equipment category.
Note: Search process applies to work order headers only—it
 does not apply to work order items.

Related information

- [Refresh / Clear All](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-display-form/field-definitions-em-work-order-display-form#ID-0000d2f6--en)

- [About the EM Work Order Display Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-display-form)

## Department

The Department field on the EM Work Order Display form.
 Specify the department (from EM Departments) by which to filter work order selection. Only work orders with equipment assigned to this department (in EM Equipment) will display.
Leave this field blank if not filtering work orders by equipment department.
Note: Search process applies to work order headers only—it
 does not apply to work order items.

Related information

- [Refresh / Clear All](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-display-form/field-definitions-em-work-order-display-form#ID-0000d2f6--en)

- [About the EM Work Order Display Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-display-form)

## Show Work Orders: Shop

The Shop field on the EM Work Order Display form.
Enter the shop by which to filter work orders. Only work orders for equipment with this shop assigned will display in the results.
 Leave this field blank if not filtering work orders by shop.
Note: Search process applies to work order headers only—it
 does not apply to work order items.

Related information

- [Refresh / Clear All](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-display-form/field-definitions-em-work-order-display-form#ID-0000d2f6--en)

- [About the EM Work Order Display Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-display-form)

## Refresh / Clear All

Refresh – Click this button to populate the grid with all work orders meeting the specified criteria.
Note: Be aware that if you enter new criteria and click this button, the grid is cleared of existing entries and repopulated with entries meeting the new criteria.
Clear All - Click this button to clear the selection criteria and the grid.

Related information

- [About the EM Work Order Display Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-display-form)

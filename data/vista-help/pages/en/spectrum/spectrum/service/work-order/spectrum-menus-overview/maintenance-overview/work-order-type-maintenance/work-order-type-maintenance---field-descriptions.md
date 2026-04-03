---
title: "Work Order Type Maintenance - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/maintenance-overview/work-order-type-maintenance/work-order-type-maintenance---field-descriptions"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/maintenance-overview/work-order-type-maintenance/work-order-type-maintenance---field-descriptions"
---

# Work Order Type Maintenance - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Field
Description

Type code
Enter a unique type code for every type
 of work order (for example, JC = Job Cost, BID = Bid, TAM =Time + Materials,
 SVC = Service, WAR = Warranty, and so forth).
Description
Enter the work order type description.
G/L department
Enter a valid G/L department to be used
 in determining how revenue posts for this type of work order. This field is
 required. This department must have been previously set up in G/L Department
 Maintenance.
Override standard payroll overhead method?
Select this checkbox to override the
 standard payroll overhead method specified in Work Order Installation and
 specify a new payroll overhead calculation for a site work order.
Payroll overhead
If the override checkbox is selected,
 specify whether or not to accrue overhead based on labor cost charges to site
 work orders during the Payroll update, and if so, whether to calculate based on
 a percentage or as a rate per hour.
Overhead % / rate
Enter an overhead percentage or rate
 per hour, based on the Payroll overhead method selected above.
Cost center
If the cost center feature is enabled
 in the Enterprise Installation screen for this company, enter a cost center.
 Spectrum compares the cost center assigned to the work order site with cost
 centers in the operator's assigned scheme, and if the site's cost center is not
 present, then that work order is not accessible. If the
 G/L department is a 'Direct job cost', the cost center on the job will be
 used on job work orders and no entry will be allowed.

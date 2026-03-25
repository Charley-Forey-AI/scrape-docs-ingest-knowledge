---
title: "About the HR Asset In/Out by Resource Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-asset-inout-by-resource-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-asset-inout-by-resource-form"
---

# About the HR Asset In/Out by Resource Form

This form allows assets to be checked out by resource, similar to HR Company Asset Check Out.
 This form can be accessed from the HR main menu or by double-clicking the grid on the Assigned Assets tab in HR Resources.
 Once a resource is entered, the grid displays all assets the resource is currently assigned to (whether added via this form or HR Company Asset Check Out). New assets can be assigned or assets may be checked in that have been previously assigned to the resource.
 When assigning new assets, specify an asset that is flagged as available (Status 0). If the asset is flagged as unavailable (i.e. assigned to another resource or out for repairs) or disposed (lost, sold, discarded, etc.), a message displays indicating that the asset is unavailable for checkout.
 Once the asset has been specified, enter the checkout date and memo. This sets the asset's status to 1 (Unavailable) and adds a record to the History tab in HR Company Assets, as well as to the Assigned Assets tab in HR Resources. Once the asset is returned and checked in, the asset's status is set to 0 (Available) and the check-in information is updated for the asset in HR Company Assets (History tab). The record will be cleared from this form, as well as from the Assigned Assets grid in HR Resources
Once an asset has been assigned, the checkout date and/or memo can be modified, if necessary. However, if you elect to change the checkout date, the new date cannot conflict with the checkout/check-in dates of other assignment records for the asset. In other words, the new date must be after the checkout and check-in date of any of the previous assignment records.
 Asset records can be deleted for a resource, as necessary; however, there are some limitations:

- Asset assignments cannot be deleted for a resource if you have checked the asset in and either exited the form or moved to another resource; this causes the asset record to be cleared from the grid.

- An asset record cannot be deleted for a resource if the asset has been checked in, then in the same session, a new record is added for the same asset and resource.

[About the HR Company Assets Form](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-company-assets-form)
[ About the HR Company Asset Check Out Form](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-company-asset-check-out-form)
[About the HR Resources Form](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form)

---
title: "Service Management Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r2/service-management/service-management-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r2/service-management/service-management-features"
---

# Service Management Features

Vista 2023 R2 delivers on user-requested Service Management enhancements, fixes, and other improvements.

## Create Separate WO Scopes Per Service Item

If you are using the Tasking feature for agreements, you can now have the system create separate work order scopes for each service item on an agreement. This allows you to track all costs captured on a work order scope to a specific serviceable item.
To enable this functionality, a new Separate Scope Per Service Item checkbox was added to the SM Agreements form (Info tab). When selected, the work order generation process (in SM Generate PM Work Orders) creates a separate work order scope (on the related work order) for each applicable service item.
 If you selected the Separate Work Order checkbox for an agreement service, the system creates a separate work order for that service and sets up the remaining services on one work order with separate scopes per service item.
It is important to note that this feature only works with serviceable items (on a service site) that meet the following criteria:

- One or more maintenances are set up for the serviceable item class assigned to the serviceable item (in SM Serviceable Item Class, Maintenance tab).

- One or more tasks exist for each maintenance (Tasks tab in SM Class Maintenance) and the Recommended checkbox is selected for each task.

- Serviceable items/maintenances are added to your agreement using SM Agreement Maintenance (via the Tasking button in SM Agreements).

- Selected maintenance tasks are scheduled using SM Agreement Task Schedule (via the Task Scheduling button in SM Agreements).

Note: If you want to select the Separate Scopes Per Service Item for existing agreements, you can do so if the following applies:

-  The agreement is in quote status.

-  The agreement is active, but no work orders have been generated. In this case, you can create an amendment, select the checkbox, and activate the amendment.If work orders have been generated, you must first delete the work orders, and then create the amendment.

For more information about the Tasking feature for agreements, see [About Tasking / Task Scheduling](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/about-tasking--task-scheduling).

## Enter QR Code IDs for Service Items – Vista Field Service

In Vista Field Service, technicians can create QR codes for service items, in order to quickly and accurately identify items and complete tasks. Now in Vista, you can add these QR code IDs in the field Field Service - ID for QR Code to link a QR code to a service item. This field is accessible from the SM Service Sites form Serviceable Items tab, or directly from the SM Serviceable Items form.
For more information, see [Field Service - ID for QR Code](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-serviceable-items-form/field-definitions-sm-serviceable-items-form#ID-0482m4og--en).

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.

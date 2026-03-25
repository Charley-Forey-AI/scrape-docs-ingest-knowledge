---
title: "About the EM WO Item Init Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-wo-item-init-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-wo-item-init-form"
---

# About the EM WO Item Init Form

Use this form (accessed by selecting File > Initialize WO Item from Std Maint Group in EM Work Order Edit) to initialize work order items to a work order based on standard maintenance items set up in EM Standard Maintenance Groups.
The upper area on this form shows the target work order and the equipment to which the work order applies (this will be the equipment specified in the work order header in EM Work Order Edit). You must then specify the standard maintenance group to initialize. If you are initializing items for a component of the equipment, check the Assigned Component option and specify the standard maintenance group (for the component) to initialize. Once you have specified the equipment’s or component’s standard maintenance group, the Potential Items to Initialize section shows the number of standard maintenance groups and items available for initialization (includes linked maintenance groups). If items are available, click the Initialize button to begin initialization process. When initialization is complete, the Initialized section shows the number of maintenance groups and items actually initialized. In addition, a message displays giving you the option to initialize more work order items. Click ‘Yes’ to continue, ‘No’ to close the form and return to EM Work Order Edit.
During initialization, all items set up for the maintenance group (including parts and notes) that are not currently on an open work order will be set up on the work order in EM Work Order Edit. You may initialize items for as many maintenance groups as you want, as long as the maintenance group exists for the equipment. Once initialized here, you may edit the items as normal in EM Work Order Edit, without affecting the maintenance item set up in EM Standard Maintenance Groups.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

- [About the EM Work Order Initialize Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-initialize-form)

---
title: "About the EM Equipment Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-form"
---

# About the EM Equipment Form

Use this form to create and maintain equipment and components.

- What are components? - Components are set up and maintained just like equipment, except that several of the fields that are used for equipment setup are not applicable to components. For example, when setting up a piece of equipment, you must assign a category and department. You can also assign a location, revenue code, job, and license information (license number, state, and expiration date). When setting up a component, the assignments are assumed the same as that of the equipment to which the component is attached, and therefore, are not entered. For more information about components, see Related Topics below. Note: If you delete a piece of equipment, any
 components assigned to the deleted equipment will be automatically
 unattached and set up as primary pieces of equipment.

- Job and Location - If you intend to use the location-tracking feature, you should populate these fields by using the location transfer features ([EM Location Transfer](/en/vista/vista/job-resources/equipment-management/equipment-transfers/about-the-em-location-transfer-form) or [EM Mass Location Transfer v11](/en/vista/vista/job-resources/equipment-management/equipment-transfers/about-the-em-mass-location-transfer-v11-form)) or by importing location transfers. This will create the initial location history records. When posting equipment usage, updates to the job and location for a piece of equipment here will depend on the update option selected in EM Company Parameters (Updates tab). See Meter & Job/Location Update Options in Related Topics below for more information. It is suggested that you do not change these fields after the initial setup; if these fields are changed directly in this form, no transfer history will be recorded.

- Date of Last Usage - This field is updated when posting usage to equipment in EM Usage, PR Timecards, and MS Ticket Entry where the new usage date is greater than the 'date of last usage' for the equipment. The update from EM Usage Posting will occur upon the creation of the batch record, but the updates from PR Timecard Entry and MS Ticket Entry will not happen until the batches are posted.

- Changing Categories - If you elect to change the category assignment for a piece of equipment after you have begun posting usage and costs, it is important that you first review from where equipment usage (revenue) rates are being pulled.

- EM Revenue Rates by Category — If you defined equipment usage rates at the category level (as they frequently are), and you change the equipment’s category, the system will use the new rate on all new usage transactions. (Existing transactions are not affected.)

- EM Revenue Rates by Equipment — If you override the category rate by defining usage rates at the equipment level, changing the equipment’s category will NOT change the equipment’s usage rate.

- Ownership Info = This tab is used to enter miscellaneous information about ownership, lease, or rental of equipment. The type of information entered depends on the Ownership Status selected (e.g. if you select ‘Owned’, the purchase information inputs are enabled, allowing you to enter the necessary information). You also have the option to enter additional information regarding the date the equipment was put into service, the expected life of the equipment, replacement cost, appraised value, and sale price and date. Note: If you enter lease or rental information about the
 equipment, then at a later date purchase the equipment, the lease/rental
 information will be disabled, but the values will remain.

- Components/Attachments - The Comp/Attach tab is used to assign attachments and components to primary equipment. For more information, see [About Components/Attachments](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-componentsattachments#concept-2617--en__concept-2617).

- Meters/Fuel Usage - The Meters tab is used to set up hour meter, odometer, and fuel usage tracking for equipment. For more information, see [About Meters/Fuel Usage](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-metersfuel-usage#concept-9491--en__concept-9491).

- Deleting Equipment - You can delete a piece of equipment as long as no detail exists for the equipment. If you have posted detail to a piece of equipment,first purge the detail using the [EM Equipment Detail Purge](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-detail-purge-form) form. This will purge meter, location transfer, and component transfer history, as well as work orders and cost/revenue detail. After you have purged equipment detail, you must then remove the following setup detail for the equipment:

- Assets/Depreciation – Using [EM Asset Setup](/en/vista/vista/job-resources/equipment-management/depreciation/em-asset-setup-form), delete all assets set up for the equipment.

- Std Maintenance Groups – Using [EM Standard Maintenance Groups](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-standard-maintenance-groups-form), delete all maintenance groups associated with the equipment.

- Warranties – Using [EM Warranties](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-warranties-form), delete all warranties set up for the equipment.

- Components – In EM Equipment, make sure there are no components assigned to the equipment. Note: It is suggested
 that you transfer all components (of value) off the equipment
 BEFORE running EM Equipment Detail Purge. However, if a
 component has no value, you can leave it assigned to the
 equipment, run the purge form to remove all detail, and then
 change the component to an 'Equipment' type. This will
 automatically remove its 'assignment' to the primary piece of
 equipment (without generating a detail record) and allow the
 component to be deleted.

Once you have completed these steps, you can then delete the equipment.

- Revenue Rates - Use this tab to review the revenue rates for a piece of equipment. You can add or modify rates directly in the grid, but you cannot delete existing rates; that must be done using the EM Revenue Rates by Equipment form (accessed by double-clicking on any line in the grid). Information entered in EM Revenue Rates by Equipment will be updated to the grid once focus is returned to this form.Note: If
 multiple breakdown codes exist for a category/revenue code, you will be
 unable to override the revenue rate here. You will need to enter the
 override rate directly in the [EM Revenue Rates by Equipment ](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-rates-by-equipment-form)
 form.
Click [here](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-codes-form) for additional information on setting up/maintaining revenue rates for equipment.

- Warranties - Use this tab to create and maintain warranties on the equipment, attachments, and/or components. Double click on a warranty to open the [EM Warranties ](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-warranties-form) form.

- Parts - This tab is used to set up and maintain equipment parts. If you have specified to validate parts (in EM Company), you will need to associate parts entered for equipment with a valid HQ material. Parts not associated with a valid HQ material cannot be used when entering work orders or cost adjustments. Note: Double-clicking on any line in the grid will access the [EM Equipment Parts ](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-parts-form) form.

- Depreciation - Use this tab to set up equipment assets that you want to depreciate. Setup includes assigning one or more asset codes to each piece of equipment, and then specifying the depreciation method (straight line or declining balance), the asset life, and asset value. With this information, the system can calculate a schedule of the depreciation amounts to take each month for the life of the asset. This schedule will be used by the Depreciation Processing form to determine the actual depreciation amount to post each month, quarter, year, or whatever interval you choose.Note: Double-clicking on any line in the grid will access
 the [EM Asset Setup ](/en/vista/vista/job-resources/equipment-management/depreciation/em-asset-setup-form) form.

- Transfers - Use this tab to add, edit, delete, or view transfers of this equipment to different jobs and/or locations. You may also initiate transfers using [EM Location Transfer](/en/vista/vista/job-resources/equipment-management/equipment-transfers/about-the-em-location-transfer-form), [EM Mass Location Transfer v11](/en/vista/vista/job-resources/equipment-management/equipment-transfers/about-the-em-mass-location-transfer-v11-form), or import. When adding a transfer, you can specify the company, job, and/or location to which you are transferring the equipment, as well as the date and time of transfer. Because you have the option to enter transfer times , you can track multiple transfers of a piece of equipment for each date. It is strongly suggested that you enter transfer times if you are using the [EM Automatic Usage ](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-automatic-usage-form) feature to process automatic usage posting, since the system will automatically charge equipment usage to jobs based on the length of time the equipment is located on the job. If the equipment to transfer has attachments, the attachments are automatically transferred with the equipment. Note: Double-clicking on any line
 in the grid will access the [EM Location Transfer](/en/vista/vista/job-resources/equipment-management/equipment-transfers/about-the-em-location-transfer-form)[EM Asset Setup Form](/en/vista/vista/job-resources/equipment-management/depreciation/em-asset-setup-form) form.

Related information

- [Component Tracking](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/component-tracking)

- [About Attaching Documents to Data Records](/en/vista/vista/system-tools/document-management/dm-workflow/manage-documents/about-adding-documents/about-attaching-documents-to-data-records)

- [About the EM Equipment Parts Form](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-parts-form)

- [EM Asset Setup Form](/en/vista/vista/job-resources/equipment-management/depreciation/em-asset-setup-form)

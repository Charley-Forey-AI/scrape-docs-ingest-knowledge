---
title: "About the EM Equipment Detail Purge Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-detail-purge-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-detail-purge-form"
---

# About the EM Equipment Detail Purge Form

Use this program to purge data (in a closed month) from the Equipment Management system.
You can purge data for a single piece of equipment, an equipment category, a component, or all equipment.
Note: You cannot use this form to delete equipment—you must use the EM Equipment form. However, you can only delete a piece of equipment after you have first purged its existing detail here.
The purge options on this form allow you to select the data to purge and the month/date through which to purge. These options are as follows:

- Meter Reading History – Removes all records from the meter reading history table through the specified Reading month.

- Location Transfer History – Removes all records from the Location Transfer History table, through the specified ‘transfer out date’. If you check the Include Last Transfer Record box, the system will purge the final transfer record for the equipment if it is the only transfer record left in the file after purging through the specified date. If multiple transfer records are left after purging through the specified ‘transfer out date’, the last transfer record will not be purged, regardless of how the flag is set.

Note: The system will purge all transfer records with a null ‘Out Date’ where a future transfer exists that has an ‘Out Date’ less than or equal to the ‘purge through’ date.

- Work Orders – Removes work order records, including headers, items, parts, and notes, through the Completion Date specified.

- Cost Detail – Removes records from the cost detail table, through the specified month.

- Revenue Detail – Removes records from the revenue detail table, through the specified month.

- Component History – Removes records from the component transfer history table, through the Transfer Off Date specified.

Once you have purged equipment detail in this program, you can delete the equipment in [EM Equipment](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-form). However, before you delete a piece of equipment, make sure you have also deleted the following for the equipment:

- Assets/Depreciation – Using [EM Asset Setup](/en/vista/vista/job-resources/equipment-management/depreciation/em-asset-setup-form), delete all assets set up for the equipment.

- Std Maintenance Groups – Using [EM Standard Maintenance Groups](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-standard-maintenance-groups-form), delete all maintenance groups associated with the equipment.

- Warranties – Using [EM Warranties](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-warranties-form), delete all warranties set up for the equipment.

- Components – In EM Equipment, make sure there are no components assigned to the equipment.

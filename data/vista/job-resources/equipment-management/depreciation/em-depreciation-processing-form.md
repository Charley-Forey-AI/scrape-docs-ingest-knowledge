---
title: "EM Depreciation Processing Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/depreciation/em-depreciation-processing-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/depreciation/em-depreciation-processing-form"
---

# EM Depreciation Processing Form

Use this form to post depreciation monthly, quarterly, yearly, or on whatever cycle you choose for a single asset or all assets.

You can post depreciation only for assets that have been set up and have calculated schedules in the [EM Asset Setup](/en/vista/vista/job-resources/equipment-management/depreciation/em-asset-setup-form) form.
Note: If you calculate depreciation using a third-party depreciation package, do not use the EM Depreciation Posting program. Instead, import your depreciation data using the Imports (IM) module. The Imports module provides a series of programs that allow you to set up import templates and cross-references, import your depreciation data, edit or delete the imported data as necessary, then update the data to EM and GL. For more information, see [Importing Data from Third-Party Systems](/en/vista/vista/administration/imports/processing/importing-data-from-third-party-systems).
The depreciation process uses the asset's Amount to Take and Amount Taken values (in EM Asset Setup > Schedule tab) to determine the depreciation amount for that asset and updates the amount as the "amount taken" for the current month. Depreciation transactions are stored in the EM Cost Detail table (EMCD). Until you post the depreciation batch, you can access and edit the transactions in EM Cost Adjustments; however, there is usually no reason to do.
For more information about depreciation calculations, see [About Posting Depreciation](/en/vista/vista/job-resources/equipment-management/depreciation/about-depreciation/about-posting-depreciation).

## Before You Begin

Prior to posting depreciation for the first time, assign a Depreciation Cost Code and Depreciation Cost Type (in EM Company Parameters) to each depreciation cost entry.
Additionally, you must set the Last Month Calculated field (in EM Company Parameters) before you can begin posting depreciation. The system uses this month to calculate the correct depreciation amount to post. After the initial setup, the system will update this field automatically each time you run the depreciation process.
Note: Automatic update to the Last Month Calculated field will occur only if you post depreciation for all assets; that is, you leave the 'Post Depreciation for Select Assets' option unchecked when running this program.

## When to Run Depreciation

It is not necessary to run depreciation calculations every month. At a minimum, you must calculate through the 12th period of your year before you can close that period and before you can post any depreciation to the next year. Whenever you run this program, the process will calculate enough depreciation to bring the asset current and post the amount to the current month.
For example, if you last ran the depreciation process through period 03/23 and you now run for period 06/23, the system will calculate three months of depreciation and post it to period 06/23.
Note: You can set the Calculations Required option in EM Company Parameters to Monthly if you want the system to restrict you from closing a period until you have run EM Depreciation Processing.

## Inactive Equipment

If you are running depreciation for a specific piece of equipment, and that piece of equipment is flagged as 'Inactive' (in EM Equipment), you will receive a message informing you that the equipment is inactive, but you will be allowed to proceed with the depreciation process. If you are running depreciation for all equipment, the system will not display the warning message for inactive equipment; it will just proceed with the depreciation process.

## GL Account Posting

Posting depreciation has the following General Ledger effect:

- Debits the GL account assigned (in EM Departments) to the Depreciation Cost Type designated in EM Company Parameters

- Credits the Accumulated Depreciation GL Account defined in EM Departments.

You can override these accounts in the EM Asset Setup if necessary.

Related information

- [About Depreciation](/en/vista/vista/job-resources/equipment-management/depreciation/about-depreciation)

- [About the Depreciation Schedule](/en/vista/vista/job-resources/equipment-management/depreciation/about-depreciation/about-the-depreciation-schedule)

- [About Declining Balance / Diminishing Value Depreciation](/en/vista/vista/job-resources/equipment-management/depreciation/about-depreciation/about-declining-balance--diminishing-value-depreciation)

- [About Posting Depreciation](/en/vista/vista/job-resources/equipment-management/depreciation/about-depreciation/about-posting-depreciation)

- [Equipment Depreciation Using Third-Party Software](/en/vista/vista/job-resources/equipment-management/depreciation/about-depreciation/equipment-depreciation-using-third-party-software)

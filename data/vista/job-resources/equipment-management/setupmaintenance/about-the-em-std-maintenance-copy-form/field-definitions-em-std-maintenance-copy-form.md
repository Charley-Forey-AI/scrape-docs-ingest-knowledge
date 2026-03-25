---
title: "Field Definitions: EM Std Maintenance Copy Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-std-maintenance-copy-form/field-definitions-em-std-maintenance-copy-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-std-maintenance-copy-form/field-definitions-em-std-maintenance-copy-form"
---

# Field Definitions: EM Std Maintenance Copy Form

The following is a list of field descriptions for the EM Std
 Maintenance Copy form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Copy From: Equipment

 Specify the equipment from which to copy maintenance groups.

##  Copy From: Begin/End Maint Group

 Enter the beginning and ending group in a range of maintenance groups to copy.
Note: Since maintenance group codes are left justified, make sure you enter the range correctly. For example, if copying maintenance groups 1, 2, 3, 10, and 100, you must enter the range as 1 – 3 to include all groups. If you enter 1 – 100, the system will only copy groups 1, 10, and 100.

##  Copy To

- Category – Select this option to copy the specified maintenance group(s) to an existing category of equipment.

- Equipment – Select this option to copy the specified maintenance group(s) to another piece of equipment.

##  Copy To: Category

 Specify the category to which you are copying the maintenance groups indicated above.
Note: The copy process will skip equipment flagged as ‘inactive’.

##  Copy To: Begin/End Equipment

 Specify the beginning and ending equipment in a range of equipment to which you are copying the maintenance group(s) indicated above.
Note: The copy process will skip equipment flagged as
 'Inactive'.

##  Update Option

 Specify how to handle existing and new maintenance items/parts during the copy process.

- Add New Items/Parts Only - Select this option to skip existing maintenance items and/or parts and add only those items and/or parts that do not already exist for the destination category/equipment.

- Replace Existing Items/Parts - Select this option to update all existing maintenance items and/or parts for the destination category/equipment with new information. Add items and/or parts that do not already exist for the maintenance group.

##  Save 'Last Done' Meter Data

 This option is only accessible if you are using the ‘Replace Existing Items/Parts’ update option.
 Check this box to save the Last Done meter data (Hours, Gallons, Miles, and Date) when copying maintenance groups/items to the destination equipment/category. The system will only save data for replaced maintenance items. If new items are added, meter data defaults as null.
 Leave this box unchecked if not saving the ‘Last Done’ meter data when copying maintenance group/items to the destination equipment/category.

## Copy Header Custom Fields / Copy Item Custom Fields/ Copy Item Part Custom Fields

 Use these boxes to select which information
 entered in custom fields on the EM Standard Maintenance Group form will be copied.
If you have not added any custom fields to the EM Standard Maintenance Group form, these boxes do not apply.

- Copy Header Custom Fields - Check
 this box to copy the information in the custom fields on the Header tab in the upper
 portion of the EM Standard Maintenance Group form.

- Copy Item Custom Fields - Check
 this box to copy the information in the custom fields on the Item tab in the lower
 portion of the EM Standard Maintenance Group form.

- Copy Item Part Custom Fields -
 Check this box to copy the information in the custom fields on the Parts tab in the
 lower portion of the EM Standard Maintenance Group form.

Custom fields are added to standard forms using the [VA Custom Fields Wizard](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form).

---
title: "About Monitoring Scheduled Data Changes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/about-monitoring-scheduled-data-changes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/about-monitoring-scheduled-data-changes"
---

# About Monitoring Scheduled Data Changes

As a system administrator you can use VA Scheduled Changes to
 monitor all scheduled data changes in the system.

You can edit or delete scheduled changes, as well as review the status of scheduled changes.
To use this form in its administrative capacity, you should access it from the VA Programs folder on the Main Menu.When you access the form in this manner, the system displays a few additional fields. In the Header section of the form, the system displays the Key ID to Update field. This field is used as a way to separate records from each other as you sort through the list of scheduled changes in the system. Additionally, the Key Fields field displays which shows the key fields for the record that changed and helps to locate the exact record in the system.

- Editing Scheduled Changes - You can edit scheduled change records prior to their effective date. Once the effective date has passed, the system will apply the scheduled change and you can only delete the record of the change from VA Scheduled Changes. If you need to edit the scheduled change for a field, enter the new change value in the New Value field. If the effective date is incorrect, you will need to delete the existing record, go to the form, locate the record, and add a new scheduled change to the correct field.

- Monitoring Scheduled Changes - The system monitors all changes in the system
 and, on a regular schedule, updates the applicable fields automatically.
 Once the fields are updated, the system also updates the Update
 Status and Update Message fields in
 VA Scheduled Changes. If the scheduled change was successful, the system
 also updates the Applied On field with the
 date the change was made and Applied displays in the
 Update Status field. If a scheduled change was
 unsuccessful, Error will display in the
 Update Status field and the system will display a message
 in the Update Message field. If
 you want to re-add the scheduled change, the Key
 Fields field displays the key field values for the record in
 question. For example, if you made a change to record in HR Resources in
 company 1 for resource number 65, the Key Fields field would
 display HRCo = 1, HRRef = 65.

Related information

- [About the VA Scheduled Changes Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/about-the-va-scheduled-changes-form)

- [Schedule Data Changes for Fields](/en/vista/vista/system-tools/user-interface-guide/system-forms/schedule-data-changes-for-fields)

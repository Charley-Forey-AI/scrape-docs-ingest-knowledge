---
title: "PM Migrate Data Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/issuessubmittalsother-documents/request-for-quote---overview/pm-migrate-data-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/issuessubmittalsother-documents/request-for-quote---overview/pm-migrate-data-form"
---

# PM Migrate Data Form

Use the PM Migrate Data form to migrate legacy RFQs into the new PM Request For Quote form.
Consider the following when migrating RFQs:

- You can run this process at any time and multiple times on a single project or for a company.

- Any RFQs that have already been migrated to the new form are ignored by this process.

- When you run the migration, any custom fields on the PM Request For Quote - 6.6 form are automatically created on the new PM Request For Quote form and the data copied to the new RFQs.

For an overview of RFQs, see [Request for Quote - Overview ](/en/vista/vista/project-management/issuessubmittalsother-documents/request-for-quote---overview).
Follow the steps below to migrate legacy RFQs into the new PM Request For Quote form.

1. Open the [PM Request For Quote](/en/vista/vista/project-management/issuessubmittalsother-documents/request-for-quote---overview/pm-request-for-quote-form) form.

1. Select Tools >  Migrate RFQ Data. This will open the PM Migrate Data form.

1. By default the PM Company and Project field will populate with the current company and project. You can change this information if it does not apply. For example you can remove the value in the Project field if you want to migrate all of the RFQs for a specific company.

1. Select Validate.

1. The total number of RFQs that will be migrated displays.

1. The duplicate RFQs will display in the lower portion of the form. These are RFQs that were created using the legacy PM Request For Quote form that have an RFQ number that has already been assigned to a new RFQ using the PM Request For Quote form.

1. Assign the duplicate RFQs a new number.

- Manually - Use the RFQ column to manually assign a new RFQ number to each duplicate RFQ. For example, assign a duplicate RFQ a new RFQ number and then press TAB. The duplicate RFQ will be removed from the list in the lower portion of the form.

- Automatically - Select the Generate next available record # for all duplicates checkbox to have the system automatically assign duplicate RFQs the next available number when they are migrated to the new form.

1. Select Migrate.

1. Select Yes on the message that displays.

1. A message will display the total number of RFQs that have been migrated to the new form.

1. Open the PM Request For Quote form and verify that the RFQs have migrated correctly. If the system added a new custom field to the PM Request For Quote form, you should move it to the correct location.

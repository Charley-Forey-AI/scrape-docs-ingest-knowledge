---
title: "Amend an Agreement | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-agreement-amendments/amend-an-agreement"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-agreement-amendments/amend-an-agreement"
---

# Amend an Agreement

You can amend any agreement as long as the agreement is Active, there is not an existing amendment quote, and no open invoices exist.
Before you amend an agreement, you must do the following:

- If pending invoices exist, cancel or process them.

- If a pending amendment quote exists, activate or delete it.

You can modify most of the information on an amendment. If you adjust the pricing and/or remaining to bill for the agreement or any periodic services being billed separately, make sure you adjust the billing schedules and amortization schedules (if deferring revenue) to accommodate the changes. If you adjust the pricing for flat price services, the system automatically adjusts the split revenue entries (once you save the record) based on the percentages defined for each entry. However, you can manually adjust the entries if you do not want them automatically adjusted.
If you are using the Equipment Tasking feature, you can make changes to the task schedule for any month within the original agreement term, even if the month has already passed. However, if the original Effective Date falls after the first of the specified month, that month is disabled in the task schedule. For example, if the Effective Date for the originating agreement is 1/15/15 and you initiate an amendment on 3/1/15, the system disables January and enables February forward. This is because service dates for scheduled tasks are always the first of the month. Using our example, this means that January is ineligible for editing since the Effective Date (1/15/15) falls after the January service date (1/1/15).

1. Open SM Agreements.

1. Select the Active agreement to amend.

1. Select Amend. The system creates an amendment quote, leaving the
 originating agreement intact and active.

1. Edit the amendment as needed.Note: If you enter a date in the Start
 Date field, it becomes the new default date for
 auto-scheduling (for both billing and amortization) and supersedes the date in
 the Effective Date field.

1. Select Activate.The system sets the amendment status to Active, sets
 the original agreement status to Terminated, and sets the termination date to
 one day prior to the new effective date.

Related information

- [About Agreement Amendments](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-agreement-amendments)

- [Modify the Remaining Amount to Bill for an Agreement](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-modifying-agreements--services/modify-the-remaining-amount-to-bill-for-an-agreement)

- [Modify the Remaining Amount to Bill for an Agreement Service](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-modifying-agreements--services/modify-the-remaining-amount-to-bill-for-an-agreement-service)

- [Set Up Equipment Tasking](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking)

- [SM Agreements Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form)

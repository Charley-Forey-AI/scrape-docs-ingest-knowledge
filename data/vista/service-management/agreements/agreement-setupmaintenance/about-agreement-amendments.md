---
title: "About Agreement Amendments | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-agreement-amendments"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-agreement-amendments"
---

# About Agreement Amendments

Amendments allow you to modify the information on an agreement after it has been activated.
You can amend any agreement as long as the agreement is active and there are no existing amendment quotes or open invoices. If pending invoices exist, you must cancel or process them. If a pending amendment (quote) exists, you must either activate it or delete it.
When you amend an agreement, the system automatically copies the original agreement/revision and sets the amendment status to Quote. The original agreement/revision is left intact, and will remain active until you activate the amendment. In addition, the following occurs:

- The quote description, alternate agreement, agreement type, and
 customer fields default from the original agreement/revision; with the exception of
 the agreement type, these fields cannot be edited.

- The system sets the effective date as follows:

- If the effective date on the original agreement has
 already occurred, the effective date for the amendment will be set to the
 current date.

- If the effective date on the original agreement is the
 current date, the effective date for the amendment will be set to the
 current date plus one day.

- If the effective date on the agreement has not occurred,
 the effective date for the amendment will be set equal to the original
 effective date.

- The expiration date is set equal to the original expiration date.

- The rate template, material tax override, material tax option, and revenue recognition information default from the original agreement/revision.

- The system copies all budget entries to the amendment.

- The system copies the agreement's billing schedule, minus any billings that have
 already been processed. Processed billings will remain with the originating
 agreement. The system does not copy the billing schedule notes.

- The system copies the agreement's amortization schedule, minus any revenue that has
 already been billed. The portion of the amortization schedule containing the billed
 amount(s) will remain with the originating agreement revision. The system does not
 copy the amortization schedule notes.Note: Amounts that have been recognized in the
 Revenue Recognition process have no affect on the agreement
 schedule.

- Agreement services are copied to the agreement, along with their related work and/or
 task schedule patterns; equipment, labor, material, and miscellaneous requirements;
 and split revenue entries (Flat Price services only). For periodic services billed
 separately, the system also copies the billing and revenue deferral schedules, minus
 any processed billings and recognized revenue. Processed billings and recognized
 revenue will remain with the originating agreement.

- Service dates generated from work and task schedules on an agreement service are
 handled as follows:

- Service dates that are associated with a work order will
 be left intact, regardless of whether they fall before, on, or after the
 termination date.

- Service dates not associated with a work order that fall
 after the termination date (of the originating agreement/revision) will be
 deleted.

- Service dates not associated with a work order that fall
 on or before the termination date (of the originating agreement/revision)
 will be left intact.

- New service dates will be generated as needed based on
 the work/task schedule patterns and the new term dates. For work schedules
 using the "every __ day/week/month" options, the system will generate new
 service dates based on the agreement term Effective Date rather than the
 Effective Date of the amended agreement

- Custom fields are copied to the amendment, along with the custom fields associated
 with agreement services, budgets, required tasks and resources (equipment,
 materials, labor, and miscellaneous), amortization schedules, and billing schedules.

- The system sets the pricing for the amendment and agreement services priced
 separately equal to the original agreement and service prices, respectively. If
 multiple revisions exist, the pricing will be set equal to the pricing of the last
 revision.

You can modify most of the information on an amendment, including term dates, budgets,
 services, scheduling, and the ricing and/or remaining to bill for the agreement or any
 periodic services being billed separately. For more information, see [Amending an Agreement.](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-agreement-amendments/amend-an-agreement)

## About Deactivating / Terminating an Amendment

You can deactivate an amendment as long as there are no associated work orders or
 agreement billings. Once you generate work orders and billings for the amendment,
 the Deactivate button is no longer available, leaving the option to amend or
 terminate the amendment. If you need to deactivate an amendment with work orders or
 billings, you must first delete the associated work orders and invoices. This
 enables the Deactive button, allowing you to deactivate the amendment to make your
 changes.
You can terminate an activated amendment if needed by selecting the Terminate button
 in SM Agreements. Once you terminate the amendment, the system toggles the Terminate
 button to a Reactivate button. This allows you to [reactivate the amendment](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-agreement-termination/reactivate-a-terminated-agreement) if you terminated it in error.
For more information about deactivating/terminating amendments, see [SM Agreement Activation / Deactivation Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-activation--deactivation-form).

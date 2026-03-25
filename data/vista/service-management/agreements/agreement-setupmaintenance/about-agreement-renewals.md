---
title: "About Agreement Renewals | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-agreement-renewals"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-agreement-renewals"
---

# About Agreement Renewals

The Agreement Renewal feature allows you to renew existing
 agreements that are expired or about to expire.
Using the Renew button in SM Agreements, you
 can renew an agreement anytime prior to or after its expiration date, as long as the
 following applies:

- The agreement cannot have an
 existing renewal quote. If one exists, the agreement will not display in this
 form.

- The agreement cannot have a pending amendment. If one exists,
 it displays in the grid, but you must either delete or activate the amendment
 (using the Edit Agreement button) before you can create renewal quote.

- There are no pending (open) invoices. If pending invoices
 exists, you must cancel or process them.

When you renew an agreement, the system
 automatically creates a renewal quote, copying all of the information from the
 originating agreement, including custom fields; however, it does not copy notes entered
 for the originating agreement, agreement services, or billing schedules. You can edit
 all information on the renewal except the agreement description, alternate agreement,
 and customer. This includes setting up new services on the work schedule or deleting
 existing ones, adding or deleting service work schedule tasks, and adjusting budgets and
 labor allocations. If you add or delete periodic services that are billed separately,
 make sure to adjust the billing schedule accordingly.
After you complete edits to the renewal quote, select the Activate the
 button to open the SM Agreement Activation form and complete the process. For more
 information about activating agreement renewals, see [SM Agreement Activation / Deactivation Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-activation--deactivation-form).
Note: If you have multiple agreements due for renewal at
 the same time, you can use the SM Agreement Renewal form to create, edit, and activate
 the renewals. For more information, see [SM Agreement Renewal](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-renewal-form).

## Renewal Term & Pricing

The renewal quote is set for the same term as the originating
 agreement, with the effective date starting one day after the expiration date of the
 originating agreement. For example, if the originating agreement term was 10/1/11 -
 09/30/12 (1 year), the renewal will have an Effective Date of 10/1/12 and an
 Expiration Date of 09/30/13. You can adjust the term as applicable, as long as it
 does not overlap any existing active, expired, or terminated revisions for the
 agreement.
The agreement price for a renewal is set equal to the original
 agreement price, regardless of how many billings have been processed. The only time
 the renewal price will differ from the original agreement price is if the agreement
 price was modified for a revision prior to the current renewal; in which case, it
 will default to the last price change for the agreement. Agreement services that are
 priced separate from the agreement (Periodic and Time of Service) are handled in the
 same manner. You can adjust the agreement and service pricing as needed.

## Work/Task Schedules and Service Dates

When you renew an agreement, the system copies the work schedules defined for agreement services (in SM Service, Schedule tab), as well as task schedules defined in SM Agreement Task Schedule. Service dates generated for the originating agreement (and displayed on the Work Orders tab) will be left intact, including those generated for any revisions/versions prior to the renewal. When you activate the renewal, the system will generate new service dates based on the defined work or task schedules and the new agreement term. For more information about service work schedules and task scheduling, see [Setting up Service Work Schedules](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/service-schedules/about-service-work-schedules/set-up-service-work-schedules) and [SM Agreement Task Schedule](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-task-schedule-form).

## Billing Schedule

In instances where billing schedules are auto-scheduled using the Frequency drop-down, the new term's billing will reflect this frequency.
In cases where the auto-scheduling was not used, the system copies the billing dates (agreement and periodic services billed separately) to the renewal, incrementing the dates based on the new term. For example:
Original TermBilling Dates Renewal TermBilling Dates
1/1/17 – 12/31/1703/30/171/1/18 – 12/31/1803/30/18
06/30/1706/30/18
09/30/1709/30/18
12/30/1712/30/18

Note: If you extend the term of the renewal (say from 1 year to 2 years), the system
 does not automatically add additional billing dates for the extra year. If you
 wish to spread the payments over the new term, set up additional billing dates
 and adjust the amounts on existing billing dates as applicable.

## Revenue Deferrals

In instances where
 deferral schedules are auto-scheduled using the Frequency drop-down, the new term's
 deferral schedule will reflect this frequency. In instances where
 the originating agreement revision is set up with a deferral schedule, the system
 copies all unrecognized deferral entries for the agreement to the renewal and sets
 the deferral dates incrementally based on the new term. This applies also to any
 Periodic, Billed Separately services that are set up with deferral schedules.
 Recognized amounts will remain with the originating agreement revision or agreement
 service (respectively).
If a Periodic, Not Billed
 Separately service was removed via an amendment, its amount will be removed equally
 from billing schedule amounts and deferral schedule amounts. For Periodic, Not
 Billed Separately services that were added via an amendment, their amounts will be
 added equally to the billing schedule and revenue deferral schedule amounts. Note: In all cases, the revenue deferral amounts must equal the
 billing schedule amounts for both the agreement and any Periodic, Billed
 Separately agreement services.

## Change Customer with Single Site at Agreement

When renewing or changing an agreement, you can change the
 customer for one or more sites that are covered under that agreement. Once you opt
 to change the customer in SM Service Sites, agreements that are in quote or active
 state for that site appear in the SM Change Agreement Customer form. If you have
 more than one site on an agreement in SM Services Sites, the existing agreement is
 terminated and a new agreement created. For sites where the customer has not
 changed, the agreement is terminated and a new quote created for the same agreement.
 For more information, see [Change the Customer for a Service Site](/en/vista/vista/service-management/service-management-setup/about-service-sites/change-the-customer-for-a-service-site).

Related information

- [SM Agreements Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form)

- [SM Agreement Activation / Deactivation Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-activation--deactivation-form)

- [SM Agreement Cancellation Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-cancellation-form)

- [Change the Customer for a Service Site](/en/vista/vista/service-management/service-management-setup/about-service-sites/change-the-customer-for-a-service-site)

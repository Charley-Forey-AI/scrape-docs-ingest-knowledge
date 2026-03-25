---
title: "Agreement Activation Requirements | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-activation-requirements"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-activation-requirements"
---

# Agreement Activation Requirements

Before you can activate an agreement, the agreement must meet all of the setup requirements.
When you activate an agreement, the system first validates
 the agreement to ensure you have set up the required information. If missing or incorrect information is found, a message displays indicating what is missing or incorrect. You must make the adjustments before you can continue with the activation process.
The following is a list of information that
 is required in order to activate an agreement:

- Agreement Type

- Effective Date

- Expiration Date (must be greater
 than effective date)

- All services defined for an agreement (on the
 Work Schedule tab) must have a description

- All services on the agreement must have a [service
 schedule](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/service-schedules/about-service-work-schedules/set-up-service-work-schedules)
For services with a Task Scheduled recurring pattern, you must
 have schedule at least one month (in SM Agreement Task Schedule).

- Agreement Billing Schedule (required
 only if you have set up a work schedule for the agreement)
[You must fully schedule the agreement](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreementservice-billing-schedule-setup/set-up-an-agreement-billing-schedule-manually); that is, the sum of the
 billing schedule must equal the sum of the agreement price and all periodic
 service prices included in the agreement billing (those not being billed
 separately). Additionally, billing dates must fall within the term of the
 agreement (that is, after the effective date and prior to the expiration
 date)

- Agreement Amortization Schedule
 (required only if you selected to amortize revenue for the agreement)
[You must set up an amortization schedule for the agreement](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreementservice-amortization-schedule-setup/set-up-an-agreement-amortization-schedule-manually), with the
 sum of all entries equal to the total billable amount (that is, the sum of the
 agreement price and all periodic, not billed separately services). Revenue
 deferral dates must fall within the term of the agreement.

- Agreement Service Billings (required
 only if you have set up periodic services that are billed separately from the
 agreement)
[You must set up a billing schedule for each periodic service](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreementservice-billing-schedule-setup/set-up-a-periodic-service-billing-schedule-manually) (being
 billed separately), with the sum of all entries equal to the periodic service
 price. Additionally, billing dates must fall within the term of the agreement
 (i.e. after effective date and prior to expiration date).

- Agreement Service Deferral Schedules
 (required only if you selected to amortize revenue for the agreement and you
 have set up periodic services that are billed separately from the
 agreement)
[You must set up a revenue deferral schedule](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreementservice-amortization-schedule-setup/setting-up-a-service-revenue-deferral-schedule-manually) for each applicable
 agreement service, with the sum of all deferral entries equal to the total
 billable amount of the agreement service. Revenue deferral dates must fall
 within the term of the agreement.

Related concepts

- [SM Agreement Activation / Deactivation Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-activation--deactivation-form)

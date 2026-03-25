---
title: "SM Agreement Activation / Deactivation Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-activation--deactivation-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-activation--deactivation-form"
---

# SM Agreement Activation / Deactivation Form

Use the SM Agreement Activation / Deactivation form to activate/deactivate agreements, renewals, and amendments.
The name of this form changes depending on the access method:

-  The SM Agreement Activation title displays when you click Activate in SM Agreements for an agreement, amendment, or renewal quote.

- The SM Agreement Deactivation title displays when you click Deactivate in SM Agreements for an active agreement or renewal (does not apply to amendments) for which there are no work orders or billings.

Once you activate an agreement, amendment, or renewal, the system sets the revision status to Active and disables entry so that you can no longer modify the agreement information. If the effective date for the agreement is prior to or equal to the current date (i.e. today's date), the Current Status is also set to Active. However, if the effective date is in the future, the Current Status remains Inactive until the effective date is reached; at that time, it becomes Active. The revision number remains the same.Note: You cannot manually change the status or revision of an agreement; the system does this automatically through each phase of the agreement (setup, activation, amendments, and renewals).
You can make simple changes to an agreement after activation by deactivating the agreement in SM Agreements. For more information, see [About Deactivating an Agreement](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-deactivating-an-agreement#concept-5672--en__concept-5672).
For changes that affect the terms already approved by the customer (pricing, budgets, etc.), use the Amendment feature. For more information, see [Amend an Agreement](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-agreement-amendments/amend-an-agreement).

## Agreement Activation

You will typically activate an agreement once you have gotten approval of the defined services, budget, price, and billing schedules. When you initiate activation, the system displays information about the agreement, including the revision, agreement type, customer, and agreement effective and expiration dates. You cannot edit this information. Clicking Activate completes the activation process.Note: Certain information is required to activate an agreement. See [Agreement Activation Requirements](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-activation-requirements#concept-3232--en__concept-3232) for details.

When you generate an amendment or renewal, you can modify the information as necessary in SM Agreements before you initiate the activation process.
For renewals, the activation process sets the new agreement/revision to Active. If the originating agreement/revision has reached or passed its expiration date, its status is set to Expired. However, if the original agreement has not yet expired, the status remains Active until the expiration date is reached (at which time it is then set to Expired). The new agreement remains Active in either case.
When initiating activation for amendments, if there open work orders and/or new work orders, the Notification section of this form indicates how many open and new work orders exist. If new work orders exist, the screen also displays a Delete existing new work orders on termination checkbox to allow deleting all new work orders for the originating agreement and all prior revisions.
During the activation process, the system sets the amendment status to Active, the original agreement status to Terminated, and the termination date to one day prior to the new effective date. If the new effective date is in the future, the original agreement remains Active until the termination date has passed.

Related concepts

- [SM Agreements Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form)

- [About Agreement Amendments](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-agreement-amendments)

- [About Agreement Renewals](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-agreement-renewals)

Related information

- [SM Agreements Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form)

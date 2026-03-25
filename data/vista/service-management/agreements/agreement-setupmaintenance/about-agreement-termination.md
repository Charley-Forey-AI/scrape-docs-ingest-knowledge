---
title: "About Agreement Termination | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-agreement-termination"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-agreement-termination"
---

# About Agreement Termination

Termination of an agreement typically occurs when the agreement is no longer valid or needed.
There are two types of termination used in Service Management:

- Automatic Termination - This type occurs when you amend or renew an existing agreement. The system automatically terminates the originating agreement revision, leaving the new amendment or renewal quote available for activation.

- Manual Termination - This type occurs when you need to terminate an agreement that you have deemed invalid for specific reasons and will not be amending or renewing.

When you select to manually terminate an agreement, the system runs a check for outstanding quotes, pending invoices, open work orders, and new work orders. If any of these items exist, they are listed in the Notifications area of this form.

- Outstanding Quotes – If an outstanding quote exists,
 the screen displays a Cancel Quote checkbox. You
 must select this checkbox to proceed with the termination. If you do not select
 the checkbox, the Terminate button is disabled, allowing you to exit the form
 without terminating the agreement.

- Pending Invoices – If pending invoices exist, you have the option to process them prior to or after terminating the agreement; the system will leave all unprocessed invoices intact when the agreement is terminated.

- Open/New Work Orders – If open work orders exist,
 they will remain open upon termination of the agreement, allowing you to
 complete them later. If new work orders exist, the screen displays a Delete new work
 orders checkbox displays. If you select the checkbox, the
 system deletes all new work orders (for the current revision, as well as all
 previous revisions) upon termination of the agreement. If you leave the box
 unchecked, new work orders will be left intact.

During the termination process, the system deletes any service dates for the current version/revision that fall after the termination date. If an open work order exists for a service date, it is left intact, regardless of whether it falls before, on, or after the termination date. If a work order has a status of New and you selected to delete new work orders, the service date is either deleted (if after the termination date) or marked as 'Skipped' (if on or before the termination date). If there are scheduled billing and scheduled revenue recognition dates that fall after the termination date, they are ignored. Scheduled billings on previous revisions are set with a status of 'D', but are not deleted. When generating invoices (in SM Agreement Billings Due), scheduled billings with this status do not appear in the list.
In addition, the system sets the agreement revision to Terminated and updates the agreement term to reflect the termination date (that is, the effective date through the termination date). You can process pending invoices (if you did not process them prior to termination), create adjustment billings as needed, and post work completed to existing work orders for the agreement. However, you cannot create amendments or renewals, generate new invoices (via SM Agreement Billings Due), or generate new preventative maintenance work orders (via SM Generate PM Work Orders).
Note: You can reactivate manually terminated agreements if necessary using the Reactivate button that displays at the bottom of the screen after terminating an agreement. For more information, see [Reactivating a Terminated Agreement](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-agreement-termination/reactivate-a-terminated-agreement).

Related information

- [Terminate an Agreement](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-agreement-termination/terminate-an-agreement)

- [SM Agreement Termination / SM Agreement Reactivation Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-termination--sm-agreement-reactivation-form)

- [SM Agreements Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form)

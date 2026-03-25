---
title: "SM Work Order Quote Approval / Unapproval Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-order-quotes/work-order-quotes-forms/sm-work-order-quote-approval--unapproval-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-order-quotes/work-order-quotes-forms/sm-work-order-quote-approval--unapproval-form"
---

# SM Work Order Quote Approval / Unapproval Form

Use the SM Work Order Quote Approval/Unapproval form to
 approve/unapprove work order quotes.
The name of this form changes
 depending on the access method:

-  The SM Work Order Quote Approval title
 displays when you click the Approve button in SM Work
 Order Quotes for any quote with a status of "New".

- The SM Work Order Quote Unapproval
 title displays when you click the Unapprove button in SM
 Work Order Quotes for any quote with a status of "Approved".


## Approval Requirements

Before you can approve a
 quote, it must meet the following requirements:

- Quote must
 be assigned a valid customer, service site, and
 service center

- Quote must
 be have a status of New

- Scopes with
 a Pricing
 Method of T-Time and Material must
 have a valid rate template assigned

- Scopes with
 a Pricing
 Method of F-Flat Price must specify a
 Price and have revenue breakdown defined

If this criteria is not met,
 a message displays upon clicking Approve indicating what information
 is invalid or missing. If all criteria is met, the system generates
 a work order, with one scope for each quote scope. Tasks defined for
 the quote scopes are set up for the work order scopes and
 miscellaneous cost detail becomes work completed miscellaneous lines
 (with a Provisional status) on the work order. In addition, the
 system sets the quote status to Approved.

## Quote Unapproval

You can unapprove a quote
 after it has been approved by clicking the Unapproved button in SM
 Work Order Quotes. Once you unapprove a work order quote, the system
 deletes the associated work order and its scopes, and sets the quote
 status to New. If the work order associated with a quote has one or
 more trips assigned, you must delete the trips before you can
 unapprove the quote.Note: You cannot delete work orders generated
 from a work order quote in SM Work Orders. You must
 unapprove the related quote in order to delete the work
 order.

Related tasks

- [Approve a Work Order Quote](/en/vista/vista/service-management/work-order-quotes/approve-a-work-order-quote)

- [Unapprove a Work Order Quote](/en/vista/vista/service-management/work-order-quotes/approve-a-work-order-quote/unapprove-a-work-order-quote)

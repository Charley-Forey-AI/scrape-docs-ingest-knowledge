---
title: "Field Definitions: JB T M Template Equipment Rate Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-equipment-rate-form/field-definitions-jb-t-m-template-equipment-rate-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-equipment-rate-form/field-definitions-jb-t-m-template-equipment-rate-form"
---

# Field Definitions: JB T M Template Equipment Rate Form

The following is a list of field descriptions for the JB T M
 Template Equipment Rate form.Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Template

 Specify the T&M template the equipment rates apply to. If this form is accessed from JB T&M Template Setup, this field defaults the currently active template and is disabled.

##  EM Co

 Specify the EM company for equipment rates.

## Category

Specify the equipment category (EM Categories) to which the specified equipment rate applies.

## Seq

Display only, the sequence number (assigned by the system) for this equipment rate.

##  Restrict by Equipment

 Check this box if the equipment rate applies to a specific piece of equipment.
 Leave this box unchecked if the equipment rate for this category applies to all equipment.

## Equipment

If restricting by equipment, indicate the piece of equipment (EM Equipment) to which this equipment rate applies.

##  Restrict by Rev Code

 Check this box if the equipment rate applies to a specific revenue code.
 Leave this box unchecked if the equipment rate for this category applies to all revenue codes.

## Revenue Code

If restricting by revenue code, specify the revenue code (EM Revenue Codes) to which this equipment rate applies.

## Rate Option

Indicate how the equipment rate for this category is calculated.

- C-Actual Costs – Use the actual costs posted to JC.

- R-Equip Rate – Use the equipment rate specified in either the New or Old Rate fields (the Rate field used depends on the labor rate effective date).

## Old Rate

This field enabled only when Rate Option is
 set to R-Equip Rate.
Specify the rate that will be used for billing
 equipment of this category. This rate will only apply to equipment usage posted prior to
 the equipment effective date that meets the restriction criteria (e.g. if restricting by
 equipment, only equipment usage posted to the specified category/equipment will use this
 rate).

## New Rate

This field enabled only when Rate Option is
 set to R-Equip Rate.
Specify the rate that will be used for billing equipment of this category. This rate will only apply to equipment usage posted on or after the effective date (specified above) that meets the restriction criteria (e.g. if restricting by equipment, only equipment usage posted to the specified category/equipment will use this rate).

---
title: "Field Definitions: JB T M Template Labor Rates Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-labor-rates-form/field-definitions-jb-t-m-template-labor-rates-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-labor-rates-form/field-definitions-jb-t-m-template-labor-rates-form"
---

# Field Definitions: JB T M Template Labor Rates Form

The following is a list of field descriptions for the JB T M
 Template Labor Rates form.Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Template

 Specify the T&M template for which to set up labor rate overrides. If you access this form from JB T&M Template Setup, this field defaults the currently active template and is disabled.

##  Labor Category

 Specify the category (from JB Labor Categories) to which the specified labor rate applies.

##  Seq

 Indicate the sequence number for this labor rate. Enter “New” to specify the next available sequence number.

##  Restrict by Earn Type

 Check this box if the labor rate for this category applies to a specific earnings type only.
 Leave this box unchecked if the labor rate for this category applies to all earnings types.

##  Earn Type

 If restricting by earnings type, indicate the earnings type (HQ Earnings Types) this category’s labor rate applies.

##  Restrict by Factor

 Check this box if the labor rate for this category applies to a specific earnings factor only.
 Leave this box unchecked if the labor rate for this category applies to all earnings factors.

##  Factor

 If restricting by factor, indicate the earnings factor (e.g. 1.0, 1.5, 2.0) this category’s labor rate applies.

##  Restrict by Shift

 Check this box if the labor rate for this category applies to a specific shift only.
 Leave this box unchecked if the labor rate for this category applies to all shifts.

##  Shift

 If restricting by shift, specify to which shift this category’s labor rate applies.

## Rate Option

Indicate how the labor rate for this category
 is calculated.

- C-Actual Costs – Use actual costs as posted to
 JC.

- R-Labor Rate– Use the labor rate specified in either
 the New
 Rate or Old Rate fields (the rate field
 used depends on the labor rate effective date).

- F-Earnings Factor– Use the earnings factor posted in
 JC multiplied by the rate specified in the next field.

## Old Rate

This field enabled only when Rate Option is
 set to R-Labor Rate or F-Earnings Factor.
Specify the rate that will be used for billing
 labor for this category. This rate only applies to detail posted prior to the rate
 effective date specified in JB T&M Template Setup and displayed in the New Labor Rate Effective
 Date field on this form (for example, if restricting by earn type, only
 labor detail posted to the category/earn type will use this rate).

## New Rate

This field enabled only when Rate Option is
 set to R-Labor Rate or F-Earnings Factor.
Specify the rate that will be used for billing
 labor for this category. Rate only applies to detail posted on or after the effective date
 specified in JB T&M Template Setup and displayed in the New Labor Rate Effective
 Date field on this form (e.g. if restricting by earn type, only labor detail
 posted to the category/earn type will use this rate).

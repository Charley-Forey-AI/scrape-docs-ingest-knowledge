---
title: "Field Definitions: JB T M Template Labor Override Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-labor-override-form/field-definitions-jb-t-m-template-labor-override-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-labor-override-form/field-definitions-jb-t-m-template-labor-override-form"
---

# Field Definitions: JB T M Template Labor Override Form

The following is a list of field descriptions for the JB T M
 Template Labor Override form.Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Template

 Specify the T&M template for the labor rate overrides. If you accessed this form from JB T&M Template Setup, this field defaults the currently active template and is disabled.

## Category

Specify the category (from JB Labor Categories) to which the specified labor rate override applies.

##  Seq

 Indicate the sequence number for this labor rate. Enter “New” to specify the next available sequence number.

##  Restrict by Employee

 Check this box if the labor rate override applies to a specific employee.
 Leave this box unchecked if the labor rate override for this category applies to all employees.

##  PRCo

 If restricting by employee, specify the PR company for the specified employee.

## Employee

If restricting by employee, specify the employee (from PR Employees) to which the override rate applies.

##  Restrict by Craft

 Check this box if the labor rate applies to a specific craft.
 Leave this box unchecked if the labor rate for this category applies to all crafts.

## Craft

If
 restricting by craft, specify the craft (from PR Crafts) to which this override rate
 applies.

##  Restrict by Class

 Check this box if the labor rate applies to a specific class.
 Leave this box unchecked if the labor rate for this category applies to all classes.

## Class

If restricting by class, specify the class to which this override rate applies. If restricting by craft, a class must also be specified.

##  Restrict by Earn Type

 Check this box if the labor rate applies to a specific earnings type.
 Leave this box unchecked if the labor rate for this category applies to all earnings types.

## Earn Type

If restricting by earnings type, indicate the earnings type (HQ Earnings Types) to which this category’s labor rate applies.

##  Restrict by Factor

 Check this box if the labor rate applies to a specific earnings factor.
 Leave this box unchecked if the labor rate for this category applies to all earnings factors.

## Factor

If restricting by factor, indicate the earnings factor (e.g. 1.0, 1.5, 2.0) to which this labor rate applies.

##  Restrict by Shift

 Check this box if the labor rate applies to a specific shift.
 Leave this box unchecked if the labor rate for this category applies to all shifts.

##  Shift

 If restricting by shift, specify the shift this category’s labor rate applies to.

## Rate Option

Indicate how the labor rate for this category is calculated.

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
 effective date specified in JB T&M Template Setup and displayed in the  New Labor Rate Effective
 Date field on this form (for example, if restricting by earn type, only
 labor detail posted to the category/earn type will use this rate).

## New Rate

This field enabled only when Rate Option is
 set to R-Labor Rate or F-Earnings Factor.
Specify the rate that will be used for billing
 labor for this category. Rate only applies to detail posted on or after the effective date
 specified in JB T&M Template Setup and displayed in the New Labor Rate Effective
 Date field on this form (for example, if restricting by earn type, only
 labor detail posted to the category/earn type will use this rate).

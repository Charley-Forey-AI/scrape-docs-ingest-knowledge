---
title: "Field Definitions: HQ Earn Types Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/payroll-related-setup/about-the-hq-earn-types-form/field-definitions-hq-earn-types-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/payroll-related-setup/about-the-hq-earn-types-form/field-definitions-hq-earn-types-form"
---

# Field Definitions: HQ Earn Types Form

The following is a list of field descriptions for the HQ Earn
 Types form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Earnings Type

 Enter a number (0-9999) to identify this earnings type.

##  Description

 Enter a description of this earnings type, up to 30 characters.

## Annual Limit

The Annual Limit field on the HQ Earn Types form.
Enter the annual limit for this earnings type or accept the default of 0.00 if no annual limit applies (0.00 represents a 'null' value).
 This annual limit applies to all codes using this earnings type and overrides any limits set at each individual code level when you use PR Post Auto Earnings. If you set an annual limit here and do not have multiple codes using this type, the system uses the limit set in PR Earnings Codes (Limit for Auto Earnings field). The amount that you specify here does not display in PR Automatic Earnings.
Typically, you will set an annual limit when you have two 401(k) plans (standard and Roth) and both plans share the same annual limit. By assigning this type to the earnings codes for both plans, the system uses this single annual limit.
Note: If you have employees participating in a 401(k) catch-up plan, do not use the same earnings type as the standard 401(k) plan. This limit is in addition to the standard 401(k) plan.

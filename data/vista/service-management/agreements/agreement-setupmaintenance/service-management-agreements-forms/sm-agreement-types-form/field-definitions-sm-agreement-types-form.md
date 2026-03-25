---
title: "Field Definitions: SM Agreement Types Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-types-form/field-definitions-sm-agreement-types-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-types-form/field-definitions-sm-agreement-types-form"
---

# Field Definitions: SM Agreement Types Form

The following is a list of field descriptions for the SM
 Agreement Types form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Agreement Type

Enter an agreement type, up to 15 characters.
Examples:

- Full Coverage

- Standard PM

- Full Maint Labr

- Full Maint Matl

## Description

Enter a description of this agreement type. Up to 60 characters allowed.

## Department

Delete this text and replace it with your own content.

## Active

Check this box to activate this agreement type. Once activated, you can assign the agreement type to service agreements (in SM Agreements).
Uncheck this box to deactivate this agreement type. Inactive agreement types cannot be assigned to service agreements; however, you can use them for filtering services due for work order generation or agreements due for billing.
Note: You cannot delete an agreement type once it is assigned to one or more agreements. However, deactivating an agreement type will prevent further use of the agreement type on service agreements.

## Auto Renew

Select this checkbox to enable auto-renewal for agreements assigned this agreement type. If you assign this agreement type to an agreement (in [SM Agreements](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form)), the system enables additional fields for entering a renew through date and markup percentage.
Note: The auto-renewal functionality is not currently available for agreements, but will be available in a future release. However, selecting this checkbox and then entering a [Renew Through](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form/field-definitions-sm-agreements-form#ID-00041182--en) date for the agreement (in SM Agreements) allows forecasting labor allocations for the agreement prior to its renewal.
Do not select this checkbox if you plan to manually renew agreements with this agreement type.

## Call Type

Enter the call type to associate with this
 agreement type or press F4 to select from a list of valid call
 types. The call types set up here will identify coverage needs for any agreement assigned
 this agreement type.

## Planned

Check this box if the specified call type represents "planned" work.
Note: Call types with this box checked will be included in
 the Planned Call Types lookup available when pressing F4 from a Call Type
 field.
Leave this box unchecked if the specified call type is generally associated with "unplanned" work.

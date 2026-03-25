---
title: "Set Up Call Types | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/set-up-call-types"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/set-up-call-types"
---

# Set Up Call Types

You must set up call types that represent classifications of work performed on a work order in order to capture work completed for the work order.
You can set up as many call types as needed, each representing a classification of work, work classified by accounting treatment, or any other classification related to work performed on a work order. Although you are not required to enter a call type when first setting up a work order scope, you must assign a call type before you can post work completed lines to that scope.

1. From the Main Menu, select Service Management > Programs > SM Call Types.

1. In the Call Type field, enter a number or code to identify this call type.Note: Call types represent the types of work you perform when making service calls. Some examples of call types might be: HVACRepair, ELECTRICAL, WARRANTY, etc.

1. In the Description field, enter a description of the call type.

1. In the SM Call Type Category field, enter a call type category or press F4 to select from a list of valid call types.

1. Select the Track WIP checkbox to track WIP account updates for this call type when capturing and billing work completed for a work order.Note: If you leave the Track WIP box unchecked, only the Cost and Revenue accounts will be updated when capturing and billing work complete. See the Tracking WIP topic above.

1. Select the Active checkbox to activate the call type.Note: Inactive call types are not included in call type lookups (F4s) and cannot be assigned to service centers, divisions, or work orders.

1. Select the Prevent Scope Auto Close when Billing checkbox in order to prevent scopes with this call type from closing when fully billing.

1. From the Matl Tax Override drop-down, select the tax override option for materials. Options are:

- Blank

- N-No Tax

- S-Sales Tax

- U-Use Tax

For more information about these options, see the F1 help for [Matl Tax Override](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-call-types-form/field-definitions-sm-call-type-form#ID-00042761--en).

1. From the Tax Option
 Override drop-down, select how to apply tax to material-related
 work completed for a work order. For more information about these options, see the F1 help for [Tax Option](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-call-types-form/field-definitions-sm-call-type-form#concept-240b2b40-791b-47fb-9157-82e9bad15158--en).

- N - Not Taxable

- P - Taxable at Purchase Only

- B - Taxable at Billing Only

- M - Taxable at Purchase/Markup at Billing

- F - Full Tax

You can now assign call types to service centers, divisions, and work orders.

Related information

- [SM Call Types Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-call-types-form)

- [SM Service Centers Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-service-centers-form)

- [SM Divisions Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-divisions-form)

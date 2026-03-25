---
title: "Field Definitions: AP Payable Types Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payable-types-and-categories/ap-pay-typescategories-forms/ap-payable-types-form/field-definitions-ap-payable-types-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payable-types-and-categories/ap-pay-typescategories-forms/ap-payable-types-form/field-definitions-ap-payable-types-form"
---

# Field Definitions: AP Payable Types Form

The following is a list of field descriptions for the AP Payable Types form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Payable Type

 Enter a number (0-255) that identifies this payable type. This payable type determines the GL account to credit when posting AP invoices and debit when posting payments. Payables types are also used for payment selection. It may be a good idea to have a separate payables type even when not using a separate GL account. See Help on this Form (Help Menu) for more information.

## Description

 Enter a description of the payable type, up to 30 characters.

## GL Account

 Specify the GL account to credit when posting AP invoices and debit when posting payments. It must be an active account with a subledger type of “null” or “P” (payables). Cannot be a Heading or Memo account.

## Restrict Pay Type to Pay Category

This field is only enabled if the
 Using Payable Category checkbox is selected in AP Company
 Parameters.
If you want this pay type restricted to a
 specific pay category, enter that pay category here. Only this pay category is used with
 this pay type. If left blank, this pay type is used alone or with any pay category.
Note: You might typically use this feature for pay types that should only be used for
 specific divisions, regions, branches, locations, etc. Assigning them to a specific pay
 category prevents the pay type from being used with any other pay category. It also
 restricts the pay type from being referenced on a transaction without its assigned pay
 category.

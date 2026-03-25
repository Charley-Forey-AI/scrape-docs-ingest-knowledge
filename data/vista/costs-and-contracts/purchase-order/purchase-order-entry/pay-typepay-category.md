---
title: "Pay Type/Pay Category | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/pay-typepay-category"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/pay-typepay-category"
---

# Pay Type/Pay Category

If entry of pay types with purchase orders is allowed (i.e.
 you have checked the
 Specify Pay Type
 during PO Entry
 box in PO Company Parameters), the Items section (of PO Purchase Order Entry)
 will include an input for pay type.
The pay type defaults based on the line type
 specified. For example, when entering a Job line, the default is the standard job
 expense pay type from AP Company Parameters. If you are also using pay categories
 (
 Using
 Payable Category
 box is checked in AP Company Parameters), the pay type default is based
 on the pay category and the line type.
As with pay types, pay category defaults are
 determined by the line type. However, since there are multiple places from which a pay
 category can default, the following hierarchy is used to determine which default to use:

- If you have set up a standard or
 user pay category override in the F3 Properties window (not recommended), the
 pay category will default from the F3 setup.

- IF no F3 override exists, the pay
 category will default as specified for the current user in VA User Profile.

- If no override is defined for the
 user, the pay category will default from AP Company Parameters.

- If no default is defined for the
 company, the pay category will default as null.

Once the pay category is determined, the pay
 type will automatically default from the pay category based on the line type. In the
 case where pay category defaults are not defined (as specified above), the system uses
 the standard pay type default specified in AP Company Parameters.
Note: The pay category and/or pay type specified for the
 purchase order will override any defaults set by F3, VA User Profile, or AP Company
 Parameters when the purchase order is invoiced in AP Transaction Entry.

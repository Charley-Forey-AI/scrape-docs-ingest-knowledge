---
title: "Field Definitions: AP Vendor Merge Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendor-merge-form/field-definitions-ap-vendor-merge-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendor-merge-form/field-definitions-ap-vendor-merge-form"
---

# Field Definitions: AP Vendor Merge Form

The following is a list of field descriptions for the AP
 Vendors form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Confidence Level

The Confidence Level field on the AP Vendor Merge form.
Select the level to use for identifying duplicate vendors.

- High - Select this level to have the system look for vendors with minimal differences; that is, vendors that are very similar. Since this level is the most restrictive, it may produce fewer duplicate vendors than what you actually have.

- Medium (Default / Recommended) - Select this level to have the system look for vendors with a few differences; that is, vendors that are somewhat similar. With this level, the system also includes vendors that fall in the High level.

- Low - Select this level to have the system look for vendors with more differences; that is, vendors that are less similar. Since this level is the least restrictive, it may produce a large list of potential duplicate vendors. With this level, the system also includes vendors that fall in the Medium and High levels.

The system uses the confidence level and the Identify By options you select to search for duplicate vendors.
 For example, if you select the Identify By: Name option and

- you select a confidence level of High, the system would show "J&B Materials" and "C&B Materials" as potential duplicates.

- you select a confidence level of Medium, the system would show "Haines Sand & Gravel" and "Greely Sand & Gravel" as potential duplicates.

- you select a confidence level of Low and the Identify By: Name option, the system would show "Schneider Excavations, Ltd" and "Drake Excavations, Ltd" as potential duplicates.

## Identify By: Name

The Identify By: Name checkbox on the AP Vendor Merge form.
Select this checkbox to search for duplicate vendors using the vendor name.
Leave this checkbox unselected if not searching for duplicate vendors using the vendor name.

## Identify By: Purchasing Address

The Identify By: Purchasing Address checkbox on the AP Vendor Merge form.
Select this checkbox to search for duplicate vendors using the vendor's purchasing address.
Leave this checkbox unselected if not searching for duplicate vendors using the vendor's purchasing address.

## Identify By: Payment Address

The Identify By: Payment Address checkbox on the AP Vendor Merge form.
Select this checkbox to search for duplicate vendors using the vendor's payment address.
Leave this checkbox unselected if not searching for duplicate vendors using the vendor's payment address.

## Identify By: Phone/Email

The Identify By: Phone/Email checkbox on the AP Vendor Merge form.
Select this checkbox to search for duplicate vendors using the vendor's phone/email.
Leave this checkbox unselected if not searching for duplicate vendors using the vendor's phone/email.

## Limit To Vendor

The Limit To Vendor field on the AP Vendor Merge form.
Enter the vendor to use for comparison when searching for duplicate vendors. The system compares all vendors to this vendor and determines possible duplicate vendors using the selected search criteria.
 For example, if you select a Confidence Level of Medium and the Identify By: Address checkbox, the system searches for all vendors with an address that is very similar or somewhat similar to the address of the vendor specified here.
Once the Identify Duplicates process is complete, the system refreshes the grid with your selected vendor and its potential duplicate vendors displayed at the bottom of the grid. You can sort by the MatchID column in descending order to place the vendor and its duplicates at the top of the grid for easier access.
Note: Remember, the system includes the next highest level of confidence when searching for duplicate vendors. For example, if you select the Medium confidence level, the system includes the High confidence level in the duplicate vendor search.

## Only show vendors previously marked as unique

The Only show vendors previously marked as unique checkbox on the AP Vendor Merge form.
Select this checkbox to show only vendors that were marked as unique in a previous session (that is, merge sessions that have been processed).
If not selected, the grid will not include any vendor that is marked as unique.

## Actual

The Actual checkbox on the AP Vendor Merge form.
Select this checkbox to designate this vendor as a 'parent' vendor; that is, the vendor to which selected duplicate vendors will be merged. You can only select one vendor as Actual per merge session.Note: Vendors with this checkbox selected will continue to display in the grid when performing subsequent vendor merges if they meet the filter criteria. Only vendors flagged as unique or duplicates are removed from the grid.

Leave this checkbox unselected if this vendor should be designated as a duplicate vendor or a unique vendor. You can also leave this checkbox unselected if you are not sure whether this vendor is an actual, duplicate, or unique vendor.

## Duplicate

The Duplicate checkbox on the AP Vendor Merge form.
Select this checkbox if this vendor is a duplicate that should be merged with the vendor marked as Actual.
Leave this checkbox unselected if this vendor should be designated as a unique vendor or actual (parent) vendor. You can also leave this checkbox unselected if you are not sure whether this vendor is an actual, duplicate, or unique vendor.

## Unique

The Unique checkbox on the AP Vendor Merge form.
Select this checkbox if this vendor is a unique vendor; that is, it is not a duplicate of any other vendor.
Leave this checkbox unselected if this vendor should be designated as a duplicate vendor or actual (parent) vendor. You can also leave this checkbox unselected if you are not sure whether this vendor is an actual, duplicate, or unique vendor.

## Match ID

The Match ID field on the AP Vendor Merge form.
Display only, the system-assigned ID that identifies vendors with matching information. Typically grouped by the duplicate or similar information. For example, if the payment addresses are similar or the same for one or more vendors, the system will group them together and assign them the same Match ID.

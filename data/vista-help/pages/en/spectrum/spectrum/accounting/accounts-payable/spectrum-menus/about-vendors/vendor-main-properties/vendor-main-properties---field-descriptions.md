---
title: "Vendor Main Properties - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-main-properties/vendor-main-properties---field-descriptions"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-main-properties/vendor-main-properties---field-descriptions"
---

# Vendor Main Properties - Field Descriptions

Use this table for reference when completing the fields on this screen.
Fields/Buttons
 Descriptions


 Vendor
 The vendor code is a unique group of letters and/or numbers that identify each vendor to the computer. This is a key field and cannot be easily changed, and it can only be changed here. This code will sort according to length, then numbers, and then letters.
If the System Administration > Installation > Accounts Payable > Use auto-sequenced vendor numbers? checkbox is selected, when you leave the Vendor code field blank, the next available vendor code will default automatically.
To easily sort the vendor codes in listings and reports where you can sort by vendor code, it is best to use the same length for all vendor codes. One way to assign vendor codes is to use the first three letters of the first name and the first three letters of the second name. This way, most vendor codes can be readily interpreted. Also, never use the following characters in your vendor codes.

> Characters
 Names
 Meaning in Spectrum

/
 slash
 Defines a range

*
 asterisk
 Wild card

#
 pound sign
 Exclude from the search

,
 comma
 Defines a list of items

?
 question mark
 Indicates a character match

ALL
 ALL
 Returns all records


 Alpha reference
 The first six characters of the vendor's full name display as the vendor's alphabetical reference name, which will be used for sorting purposes. The first six digits will default automatically during vendor setup. For this reason, it is important that each vendor has a unique alpha ref field.


 Vendor type
 The vendor type is used to group vendors by function, or by any other desired classification. Sample vendor types might be SUB for subcontractor, UTIL for utilities, O for office, and GEN for general. Press Enter if no type will be entered for the vendor. Some of the available reports may be run for specific types of vendors.Note: You can also use organization attributes to assign unlimited pre-defined identifiers to the vendor.

 Account reference
  Enter the account number this vendor uses for your company, if any. Up to 25 characters are allowed. This information will appear on the A/P check stub, for the vendor's use in applying payment correctly.


 Status
 Assign the vendor status.

- New vendor status will default to Active.


- If Inactive is selected and then an attempt is made to assign a new transaction to this vendor, the following message displays: Warning – vendor code entered has inactive status. To continue, clickOK and proceed with entering the new data.


- If Not used is selected and then an attempt is made to assign a new transaction to this vendor, the following message displays: Error – vendor code entered is not available for use. This error message disallows further data entry.
 Important: If the Not used status is selected, all areas in Spectrum where the vendor code exists (PR Deduction Code, PR Recurring Code, etc.) should be checked and the vendor code changed.

Access to this field is limited to users who have the minimum required security level. The cursor will not advance to this field when the user is not authorized to access it. The option group's data is visible to users who have insufficient security, but they cannot access the radio group to make any changes. Security for this radio group is set in the Admin > Function Security Maintenance > Function Links Security window.
If a workflow is in progress, this field is unavailable.

 Communication

Address 1
Address 2
Telephone
Fax
Vendor email
Web site
 The full address entered on this screen will print on computer-generated checks, so be sure to complete the City, State, and Zip code fields. If ePayments is selected as the vendor payment method, the Address fields will be required.
 Select the Email button to open a new email message window and send a message to the selected vendor.

 Primary contact
 Contact-specific information is entered on the [Vendor Contacts](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-main-properties/vendor-contacts) screen.

 Insurance


 Certificate
 Expiration date
 Use the drop-down menu to select the insurance certificate option and enter the expiration date of the vendor's insurance certificate, if one exists.
To use the expiration or lack of insurance as a flag and receive a warning during data entry, set up document tracking items in [Document Tracking Item Maintenance](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/document-tracking-item-maintenance). This setting defaults when new subcontracts for this vendor are added to the software.

 Business Classification


 Checkboxes
 Select the options that apply to the current vendor.
In reporting for government contracts, on any specific job, the DBE J/C History Report will print all applicable vendors with the Disadvantaged business enterprise (DBE) checkbox selected.

 Type
  Enter the type of DBE (for example, Minority Business Enterprise or Women's Business Enterprise). In reporting for government contracts, the DBE J/C History Report prints vendors and totals for each type entered in this field.
Example:
For job 93 100, first all MBE vendors with dollar amounts and percents will print, an MBE subtotal prints, then all WBE vendors used on job 93-100 will print with dollar amounts and percents. Following the MBE subtotal, totals for the job are printed.

 Attributes

Build Vendor Attribute ListUse this window to assign attribute codes to the specified vendor code.

1. Select the attribute you want to apply to the current vendort from the left pane and click the Select button to move the attribute to the pane on the right . Multiple attributes may be selected at once by holding down the Ctrl key while clicking on your choices.

1. The attributes (if any) that appear in the right pane upon opening this window are the attributes previously-assigned to the specified vendor. To remove an attribute prior to performing the update, select the attribute from the right pane and click Deselect.

1. Once the list of attributes that you want to add to this vendor is finalized in the right pane, select OK to run the update. If any of the attributes includes an image, the picture path will also be added to the vendor's attribute record when the update is run.

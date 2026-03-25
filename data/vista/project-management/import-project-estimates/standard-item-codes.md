---
title: "Standard Item Codes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/import-project-estimates/standard-item-codes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/import-project-estimates/standard-item-codes"
---

# Standard Item Codes

Standard item codes (PM Templates, Import Parameters tab) are
 used for all templates except Timberline templates.
Since item codes are typical to estimating, the Import Item Code as Standard Item checkbox allows you the option to import the item codes into the work file as standard item codes.
If importing item codes, make sure the Create
 Standard Item Codes option (PM Templates, Edit/Upload Parameters tab) is
 checked so that any item codes in the text file that are not already set
 up in JC Std Item Codes (JCSI) can be added during the upload. If the
 Create Standard Item Codes option is not checked, item codes will be
 brought in, but error messages will display for each non-valid item code
 and you will need to set them up manually.
Once you check the Import Item Code as Standard Item Code option, the remaining options (Create Item Option and Increment By) are enabled. The Create Item Option allows you to define how contract items will be assigned to the standard item codes. Methods available are:

- I-Use Next Sequential Item – This option will assign a contract item to each item code using the next available sequential number.

- S-Use Standard Item Code – This option will assign a contract item to each item code that matches the item code.

Example:
If the Item Code in the text file is ‘504.00 (Structural Concrete)’, resulting contract item for each of the options described above would be as follows:

Contract Item
Standard Item Code

Use Next Sequential Item:
1
504.00

Use Standard Item Code:
504.00
504.00

When bringing in items as standard items, you must specify the Standard Region to which the item codes will be assigned. The standard items do not have to be set up in JC Std Item Codes for the region at the time of the import. However, if you are allowing items to be set up automatically (Create Standard Item Codes option), the region must exist before the item can be added.
Note: If the Import Item Code as Standard Item Code option
 is not checked, the item code comes in as the contract item.

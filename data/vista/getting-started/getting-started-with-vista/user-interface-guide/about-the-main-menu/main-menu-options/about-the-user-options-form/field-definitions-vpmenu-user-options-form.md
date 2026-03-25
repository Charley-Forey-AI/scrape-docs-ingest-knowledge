---
title: "Field Definitions: VPMenu User Options Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/about-the-main-menu/main-menu-options/about-the-user-options-form/field-definitions-vpmenu-user-options-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/about-the-main-menu/main-menu-options/about-the-user-options-form/field-definitions-vpmenu-user-options-form"
---

# Field Definitions: VPMenu User Options Form

The following is a list of field descriptions for the VPMenu
 User Options form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Allow Multiple Instances of a Form

Check this option to allow multiple instances of a form to be opened at a time. If unchecked, only one instance of a form can be opened at a time.

- Check this box if you are using the [Related Links](/en/vista/vista/project-management/about-related-items) feature in the PM module. If this box is not checked, you will not be able to open records of the same document category from a form when using the Related Records panel. For example, you will not be able to open project issues from PM Project Issue using the Related Links panel.

- This option affects only the current user; it does not affect the ability of multiple users to have the same form open at the same time.

-  The User Options form and the VA User Profile form update each other, so you only need to set this field once to affect both forms.

## Alternate Grid Row Colors

Check this box to display grid rows in alternating colors of light blue and white. (Note: Applies to the Grid tab and any related grids on a form.)
Leave this box unchecked to display all grid rows as white.

## Confirm Updates

Check this box to have the system flash a ‘confirm update’ message when moving off a record that has been changed. You will be given the option to save the record or cancel the change.
If unchecked, no message is displayed when moving off a changed record. Instead, the record is automatically saved and you are moved to the next record.
Note: The User Options form and the VA User Profile form update each other, so you only need to set this field once to affect both forms.

## Extend Controls When Editing

Check this option to extend inputs where the number of characters entered exceeds the display allowance. For example, if you enter an address of 35 characters in an input that allows 60 characters but it only displays 30 characters, the input will extend to accommodate the 35 characters.
If unchecked, inputs will not expand to accommodate values that exceed the display allowance. You will need to scroll through the field to see the entire value.
Note: The User Options form and the VA User Profile form update each other, so you only need to set this field once to affect both forms.

## F8 Hot Key: Form to Launch

Using the drop-down menu, select the form to access when the F8 button is pressed (in any form). Typically, this will be a form that you frequently need quick access to (e.g. PM Notes, AR Credit Notes, HQ Attachment Search, HQ Document Review, AP Unapproved Invoice Review, etc.). Once assigned, the specified form will display any time you press the F8 key.
Note: You can also designate the Hot Key form via the Main Menu. Just click on the desired form in the Items pane, then choose the Select as F8 Jump-to Form option from the Items menu or the shortcut menu (accessed by right-clicking mouse).

## Map Site

Using the drop-down menu, select the map site to access (on the Internet) when the Map button is clicked from any form in the software where an address is specified. Available options are:

- Google Maps

- MapQuest

- Yahoo Maps

## Merge Grid Key Columns

Check this box to merge the key columns of grids when multiple records exist where one or more key values are the same. This prevents the values from being repeated for each record in the grid.For example, in PR Craft Classes, you might have multiple classes assigned to a single craft. When the grid key columns are merged, your grid records look like this:
Craft
Craft Description
Class
Description

100
Carpenter
100
Apprentice

101
Journeyman

103
Foreman

If unchecked, key columns are not merged and key values are repeated for every record. When the grid key columns are not merged, your grid records look like this:
Craft
Craft Description
Class
Description

100
Carpenter
100
Apprentice

100
Carpenter
101
Journeyman

100
Carpenter
103
Foreman

Note: The User Options form and the VA User Profile form update each other, so you only need to set this field once to affect both forms.

## Notify By

Use this field to select how the user will receive WF module notifications - for example if the user is an approver/reviewer in a workflow in the [Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow) feature.

- 0-Email – Select this option if the user should receive an email message..

- 1-VP Message – Select this option if the user should receive a VP message that can be viewed using the [VA Messages ](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-the-va-messages-form) form.

This option can also be set by an administrator using the [VA User Profile ](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form) form.
Click [here](/en/vista/vista/system-tools/work-flow/about-automated-notifications) for more information on using notifications.

## FormsPage Size

FormsPage Size field in the User Options Form (Main Menu Options)
You can use this field to help make Vista forms load faster.
Enter the maximum number of records per page that you want the system to return when you open any form. Forms associated with tables containing thousands - or tens of thousands - of records will initially retrieve only the number of records that you choose here so the form can load faster.
The limit you specify here will affect all your forms. When you open a form with more records than the number you enter here, all records over that number will be grouped into subsequent pages with up to that same number of records. You can use the navigation buttons to view any additional pages of records.
Consider setting a limit that will affect only those forms returning a larger number of records, but not those forms returning a smaller number of records. For example, if you maintain a material file with 100,000 records, but your vendor file contains only 8,000 records, you can set a limit of 10,000 to increase the material records load speed without restricting any vendor records.
Note: The use of wildcards or comparison operators, as well as the ability to add additional fields to the filter criteria (via the Include in Filter option in Field Properties) will allow you more control over the records returned to the form. [More Info](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/about-the-field-properties-form)
Note: Changes to this field will update the Page Size field in the VA User Profile form, so changes in either form affect both forms.

## Lookups

Lookups field in the User Options Form (Main Menu Options)
Enter the maximum number of records to return to a lookup when F4 is pressed. Useful when you have lookups associated with tables containing hundreds or thousands of records, which can affect the refresh speed.
The limit you specify here will affect all your lookups. When you open a lookup with more options than the number you enter here, all options over that number will be grouped into subsequent pages with up to that same number of records.
Consider setting a limit that will restrict the larger lookups, but not affect the smaller ones. For example, if you have some lookups with 1,000 options, but others with only 80 options, you can set a limit of 100 to improve the load speed of those with more than 100 without restricting any lookups with fewer than 100.
When using lookups, if the number of options
 available to you exceeds your designated limit, a message displays within the lookup form
 indicating that there are more records than can be displayed. If the record you are looking
 for is not in the current record set, you can enter selection criteria and click Refresh to
 re-query the database. You can include wildcards (*, %) or comparison operators (<, ,
 <, =, =, <=) to refine your search as necessary (e.g. M, *60, etc.). Once you click
 Refresh, the lookup will return a record set based on the criteria
 entered.
Note: Changes to this field will update the Lookups field
 in the VA User Profile form, so you can set this field in either form to affect both
 forms.

## Save Printer Settings with Each Report

Check this box to save the printer settings for reports to the registry. Printer settings will be used each time the report is run.
If unchecked, printer settings will not be saved to the registry and report will use the default settings (unless overridden at time of printing).
Note: The User Options form and the VA User Profile form update each other, so you only need to set this field once to affect both forms.

## Use Enter as Tab

Check this box to have the ENTER key work like the Tab key. When this box is checked and you press ENTER, the cursor will move to the next input in the tab sequence. If pressed to trigger an 'action' (for example, the Save and Go button ), once the action has been performed, you will be moved to the next input or action.
If unchecked, the Enter key will only be used to trigger an action (e.g. validating/posting batches). When Enter is pressed at an input field, the cursor will remain at the field and you will need to use the Tab button to move to the next input.
Note: The User Options form and the VA User Profile form update each other, so you only need to set this field once to affect both forms.

## Use Smart Cursor

Check this box to activate smart cursor. When in use, active inputs are highlighted to make them easier to identify.  The highlight color is determined by the Smart Cursor setting in the [Color Selections](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/about-the-main-menu/main-menu-options/change-the-system-color-scheme) form and should be a color that stands out with your current color scheme.
If unchecked, inputs will not be highlighted when active. However, you will be able to identify active inputs by the blinking cursor. In addition, the value in the active input will be selected and highlighted in gray.
Note: The [User Options ](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/about-the-main-menu/main-menu-options/about-the-user-options-form) form and the [VA User Profile ](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form) form update each other, so you only need to set this field once to affect both forms.

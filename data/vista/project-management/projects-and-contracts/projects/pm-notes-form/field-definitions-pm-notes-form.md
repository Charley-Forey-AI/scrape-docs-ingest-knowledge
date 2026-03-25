---
title: "Field Definitions: PM Notes Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projects-and-contracts/projects/pm-notes-form/field-definitions-pm-notes-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projects-and-contracts/projects/pm-notes-form/field-definitions-pm-notes-form"
---

# Field Definitions: PM Notes Form

The following is a list of field descriptions for the PM
 Notes form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Project

Enter the project or press F4 to select it from a list.

## Sequence

Enter the sequence number of an existing project note or enter N, New, or + to add a new sequence. The system will automatically assign the next available sequential number.

## Firm

Enter the firm the project note applies to or
 press F4
 to select it from a list. Firms are created and maintained in[PM
 Firms ](/en/vista/vista/project-management/setupmaintenance/about-the-pm-firms-form).
Tip:The sort name can be used instead of the firm number
 when selecting firms in PM module forms. Generally the sort name is the first several
 letters of the firm name.  For example when creating a subcontract in the [PM Subcontracts](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form) form for 'Bryan Electrical', you can
 enter the sort name 'bryan' in the Vendor field instead of the firm
 number '10042'. The sort name of a firm is set up using the Sort Name
 field on the [PM Firms](/en/vista/vista/project-management/setupmaintenance/about-the-pm-firms-form) form.

Note: Entering a firm that is not associated with the project will not add that project to the Firms tab of [PM Projects](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form).

## Contact

Enter the firm contact the project note applies to or press F4 to select it from a list.
Firm contacts are created and maintained in [PM Firm Contacts ](/en/vista/vista/project-management/setupmaintenance/about-the-pm-firm-contacts-form).

## Status

Specify the status (from PM Status IDs) of this project note. Initially defaults the ‘Default Beginning Status’ defined in PM Company Parameters.

## Summary

Enter a summary for this project note, up to 60 characters.
Note: If you enter a new issue this project note, the entry in this field will become the issue's description.

## Notes

Use this tab to enter the project notes for this entry. Notes cannot be entered directly on this tab, they must be added via the Time Stamp Notes window, which you can access by double-clicking the mouse anywhere on the Notes tab. (Note: If adding project notes via the Grid tab, the Time Stamp Notes window be activated by double-clicking the mouse or typing in the Notes column.)
The Time Stamp Notes window is divided into two sections. The upper section is display only, and shows all notes entered for the project note entry. Each note is date-stamped and includes the login name of the person who entered the notes. Existing notes cannot be edited or deleted.
The lower section is used to add new notes. Once you have entered your note text, click the Add button. This will add the note, along with the date, time, and login name, to the upper section of screen.
Note: Because several notes may exist for an invoice, they will typically not display in the Notes column. Instead, the date and login name of the first note entered displays, indicating that notes exist.

Add Standard Notes
To add standard notes (set up in HQ Standard
 Note), place focus in the lower pane and select the Standard Notes option from the toolbar
 or shortcut menu. From the Std Note Copy window, enter the standard note to copy and click
 OK
 to insert the note. Click Add to add the note to the upper
 pane.
Spelling Check
You can run a spell check for any notes entered in this window; however, the spell check must be run before you add the notes to the upper pane. To run the spell check, click the Spelling button in the toolbar () .
Tip:To use the Tab feature (such as to indent the first
 line of a paragraph or create columns), press Ctrl + Tab for each tab increment.

## Reviewer

Specify the user login (as defined in VA User Profile) to assign as a reviewer for this project note. Press F4 for a list of valid Vista users.
Note:When you add a reviewer here, an email is sent to the reviewer notifying them that they have project notes to review. The email indicates the company and project to which the project notes are associated, as well as who added the notes and when. In addition, a note instructs the reviewer that they have project notes to review and that they need to run PM Notes Review.

## Review Status

Specify the review status of this project note.

- New – Indicates the project notes for this entry are new and/or have not been reviewed. All newly assigned reviewers default this review status and are sent an email notifying them they have project notes to review.

- Reviewed – Indicates the selected reviewer has completed review of the notes for this project note entry.

Note:An email notification will also be sent if the review status is changed from ‘Reviewed’ to ‘New’ (typically when additional information is added to an existing note and needs to be reviewed).

---
title: "Additional Error Messages | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/info-link/procedures-overview/troubleshooting/additional-error-messages"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/tools/info-link/procedures-overview/troubleshooting/additional-error-messages"
---

# Additional Error Messages

Learn how to troubleshoot additional error
 messages.

## Invalid User ID

Problem: The user ID and password being entered do not match the user ID/password combination in the Info-Link table that was used to set up security in the database.
Solution: Make sure that the user name is being entered is exactly as it was setup in Info-Link and is the 3-digit company code followed immediately by the operator ID. For example, if you worked in the XYZ company and your operator ID was ABC, then the Info-Link logon name would be XYZABC.
This message may also display if the user does not have security to any tables. Go into the Info-Link User Security Maintenance area and enter the company code and operator ID. If you get a message "Record Not in File," then this operator is not set up and must be added to this screen.

1. At the bottom of this screen, the system will list the categories that this user has security access to. Verify that at least one category is listed and make note of the read access levels.

1. Go into the Table Security Maintenance. Enter the category in the table category field. Press Enter to move past the Partial table name field.

1. Make sure you can see tables that are associated with this category; verify that at least one of them has a read access level that is less than or equal to the read access level in the User Security Maintenance for this category.

1.  If you do not see any tables listed, you must add one). If the files are all listed with a read access level higher than the User Security Maintenance read access level, then you must change the level on at least one of the tables.
It is also possible that the Info-Link password is different than you might
 expect. The Info-Link security system is independent of the main Spectrum Security
 System. If you changed your Spectrum password, it would not have automatically
 changed your Info-Link password. If you need assistance verifying what your
 Info-Link password is set to, please have your system administrator submit a case
 through the [Viewpoint Customer Portal](https://support.viewpoint.com/s/).

---
title: "Invalid User ID | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/info-link/procedures-overview/troubleshooting/invalid-user-id"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/tools/info-link/procedures-overview/troubleshooting/invalid-user-id"
---

# Invalid User ID

There are three reasons why this error message will appear:

- The user ID and password enter do not match the user ID/password combination in the Info-Link table that is used to validate passwords. Verify that the User Name entered is in all capital letters and that the 3-digit company code is followed immediately by the operator ID. For example, if you work in the XYZ company and your operator ID is ABC, then the Info-Link logon name would be XYZABC. The password also should be entered in all capital letters.

- This message may also appear if the user does not have security clearance to any tables.

## Invalid User ID - Steps to rectify this problem

Follow the steps to rectify the Invalid User ID error.

1. On the Site Map screen, click Info-Link > User Security Maintenance.

1. Enter the Company/division code and Operator ID. If you get the message "Record Not in File", then this operator is not setup and must be added to this screen.

1. If the user has security clearance, the system will list the categories that
 this user has access to. Verify that at least one category is listed and make note
 of the read access levels. Close this screen and return to the Site
 Map screen.

1. On the Site Map screen, click Info-Link > Table Security Maintenance.

1. Enter the table category in the Table category field or
 leave it blank to display ALL table categories.

1. Complete the Partial table name field or leave the
 field blank to display ALL partial table names.

1. Verify that at least one of the associated category tables has a read access
 level equal to or less than the read access level in the Operator Security
 Maintenance for this category. If you do not see any tables listed, you must add
 one using the ADD (F5) mode. If all of the tables listed
 have a read access level higher than the User Security Maintenance read access
 level, then you must change the level for at least one of the tables.

- It is also possible that the incorrect Info-Link password is being used. The Info-Link security system is independent of the main Spectrum Security System. If you change your Spectrum password, your Info-Link password is not automatically updated. If you need assistance verifying what your Info-Link password is, please have your system administrator contact Viewpoint Support at 1-800-352-8939. If the caller is not listed as the primary contact for your company, Support will not be able to assist you in looking-up Info-Link passwords; your system administrator must be the person to contact Support.

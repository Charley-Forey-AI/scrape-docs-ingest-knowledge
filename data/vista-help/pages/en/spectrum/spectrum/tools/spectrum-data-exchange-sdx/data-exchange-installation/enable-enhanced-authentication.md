---
title: "Enable Enhanced Authentication | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/spectrum-data-exchange-sdx/data-exchange-installation/enable-enhanced-authentication"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/tools/spectrum-data-exchange-sdx/data-exchange-installation/enable-enhanced-authentication"
---

# Enable Enhanced Authentication

The additional Web Services security provided by Enhanced Authentication is available only to hosted customers.
Important:

- The Time Entry Workbook is not compatible with Enhanced Authentication.

- Enabling Enhanced Authentication may cause integrations with other software vendors to fail. Please contact them prior to enabling enhanced authentication and verify that their application can support it.

While still requiring the correct Authorization ID, Enhanced Authentication also requires these additional items in order to connect to Spectrum Web Services:

- Client ID

- Secret code

 The secret code expires after a set number of days that you choose during configuration, and you must reset it before that date passes.

## Set Expiration Time

1. Navigate to System Administration > Installation > Data Exchange.

1. Select the Settings button on the command bar.

1. Check the Enhanced authentication box.

1. Enter the number of days required to rotate the secret, from 7 to 120 days.

1. Select OK.

Enabling or disabling enhanced authentication takes effect after services restart overnight.

## Rotate Secret Code with Existing Authorization ID

When enhanced authorization is enabled, the Client ID and Secret Status buttons appear in the Authorization ID window, however values populate only after you select OK. Spectrum then requests this information from theTrimble Construction One platform.

1. Navigate to System Administration > Installation > Data Exchange.

1. Open an existing Authorization ID.

1. Select Secret Status.The Client ID and secret code appear.

1. To enter a different expiration date, select the Override checkbox and choose a date that is 7 to 120 days away.

1. To allow your application to call the Client ID to return the newly rotated secret code, select the Allow self-rotation checkbox.

1. To manually rotate the secret code, select Rotate Secret.

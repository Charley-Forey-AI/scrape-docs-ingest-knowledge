---
title: "Enhanced Authentication | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication"
---

# Enhanced Authentication

A reference of the endpoints available for Spectrum's authentication, which is based on the OAuth client credentials flow.
Upon a successful call, OAuth returns an access token to the user which can then be used as a bearer token authentication header in future calls to the Spectrum API. For more information, see [OAuth documentation](https://www.oauth.com/oauth2-servers/access-tokens/client-credentials/).Note: In order to use enhanced authentication, the feature must be enabled in the
 Data Exchange Installation
 screen. See [Enable Enhanced Authentication](/en/spectrum/spectrum/tools/spectrum-data-exchange-sdx/data-exchange-installation/enable-enhanced-authentication).

- client_id: found in Data Exchange installation screen.

- client_secret: found in Data Exchange installation screen.

- scope: spectrumapi

- grant_type: client_credentials

/connect/token
Required fields:

- client_id: found in Data Exchange installation screen.

- client_secret: found in Data Exchange installation screen.

- scope: spectrumapi

- grant_type: client_credentials

Returns:

- access_token: Is used to call Spectrum API as an Authentication bearer token.

- expires_in: duration the bearer token is valid.

- token_type: Bearer

- scope: spectrumapi

Example:

/secretRotation
Required fields:

- client_id: found in Data Exchange installation screen.

- client_secret: found in Data Exchange installation screen.

- scope: spectrumapi

- grant_type: client_credentials

Returns:

- client _secret: Updated secret that can be used to pull a bearer token.

- estimated_expiration: Estimated expiration date based on current Spectrum settings.

Example:

# SVAP option (US Core v5.0.1 + USCDI V2, SMART App Launch v2, Bulk Data v1)

## Paragraph (g)(10)(v)(A) - Authentication and authorization for patient and user scopes

1. AUT-PAT-4: [Standalone-Launch] The health IT developer demonstrates the ability of the Health IT Module to support SMART's public client profile.

    !!! note

        An example material for mkdocs admonition

    Other additional information...

2. AUT-PAT-24: [Both] The health IT developer demonstrates the ability of the Health IT Module to support a ".well-known/smartconfiguration.json" path as detailed in the implementation specification adopted in § 170.215(a)(3) and standard adopted in § 170.215(a)(1).

3. AUT-PAT-25: [Both] The health IT developer demonstrates the ability of the ".well-known/smart-configuration.json" path to support at least the following as detailed in the implementation specification adopted in § 170.215(a)(3):
    - "authorization_endpoint"
    - "token_endpoint"
    - "capabilities" including support for "launch-ehr", "launchstandalone",
        "client-public", "client-confidential-symmetric", "sso-openid-connect",
        "context-banner", "context-style", "context-ehr-patient",
        "context-standalone-patient", "permission-offline", "permission-patient",
        "permission-user", "authorize-post", "permission-v1";
    - "grant_types_supported" with support for "authorization_code" and
        "client_credentials"; and
    - "code_challenge_methods_supported" with support for "S256" and shall not include
        support for "plain"

    Additionally, the following "capabilities" must be supported if using US Core 5.0.1:
    
    - "context-ehr-encounter"

--8<-- "includes/abbreviations.md"
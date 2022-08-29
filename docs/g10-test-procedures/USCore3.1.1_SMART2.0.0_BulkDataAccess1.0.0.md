#(g)(10) Test Procedure using: US Core 3.1.1, SMART 2.0.0, Bulk Data Access 1.0.0

## Paragraph (g)(10)(iii) – Application registration
### Application Registration
1. APP-REG-1: 
The health IT developer demonstrates the Health IT Module supports application registration with an authorization server for the purposes of Electronic Health Information (EHI) access for single patients, including support for application registration functions to enable authentication and authorization in § 170.315(g)(10)(v). 


2. APP-REG-2: 
The health IT developer demonstrates the Health IT Module supports application registration with an authorization server for the purposes of EHI access for multiple patients including support for application registration functions to enable authentication and authorization in § 170.315(g)(10)(v). 


## Paragraph (g)(10)(iv) – Secure connection
### Secure Connection
1. SEC-CNN-1: 
For all transmissions between the Health IT Module and the application, the health IT developer demonstrates the use of a secure and trusted connection in accordance with the implementation specifications adopted in § 170.215(a)(2) and § 170.215(a)(3), including:
	- Using TLS version 1.2 or higher; and
	- Conformance to FHIR® Communications Security requirements.


## Paragraph (g)(10)(v)(A) – Authentication and authorization for patient and user scopes
### Authentication and Authorization for Patient and User Scopes
1. AUT-PAT-1: 
The health IT developer demonstrates the ability of the Health IT Module to support the following for “EHR-Launch,” “Standalone-Launch,” and “Both” (“EHR-Launch” and “Standalone-Launch”) as specified in the implementation specification adopted in § 170.215(a)(3).


2. AUT-PAT-2: 
[EHR-Launch] The health IT developer demonstrates the ability of the Health IT Module to initiate a “launch sequence” using the “launch-ehr" “SMART on FHIR® Core Capability” SMART EHR Launch mode detailed in the implementation specification adopted in § 170.215(a)(3), including:
	- Launching the registered launch URL of the application; and
	- Passing the parameters: “iss” and “launch”. 


3. AUT-PAT-3:  [Standalone-Launch] The health IT developer demonstrates the ability of the Health IT Module to launch using the “launch-standalone" “SMART on FHIR® Core Capability” SMART Standalone Launch mode detailed in the implementation specification adopted in § 170.215(a)(3).


4. AUT-PAT-4: 
[Standalone-Launch] The health IT developer demonstrates the ability of the Health IT Module to support SMART’s public client profile.


5. AUT-PAT-24: 
[Both] The health IT developer demonstrates the ability of the Health IT Module to support a “.well-known/smart-configuration.json” path as detailed in the implementation specification adopted in § 170.215(a)(3) and standard adopted in § 170.215(a)(1).


6. AUT-PAT-25: 
[Both] The health IT developer demonstrates the ability of the “.well-known/smart-configuration.json” path to support at least the following as detailed in the implementation specification adopted in § 170.215(a)(3):
	- “authorization_endpoint”;
	- “token_endpoint”;
	- “capabilities” including support for “launch-ehr", “launch-standalone”, “client-public”, “client-confidential-symmetric", “sso-openid-connect", “context-banner”, “context-style”, “context-ehr-patient", “context-standalone-patient", “permission-offline”, “permission-patient”, “permission-user”, “authorize-post”, “permission-v1”, "permission-v2";
	- “grant_types_supported” with support for “authorization_code” and “client_credentials”; and
	- “code_challenge_methods_supported” with support for “S256” and shall not include support for “plain”


7. AUT-PAT-26: 
[Both] The health IT developer demonstrates the ability of the Health IT Module to receive an authorization request according to the implementation specification adopted in § 170.215(a)(3), including support for the following parameters:
	- “response_type”;
	- “client_id”;
	- “redirect_uri”;
	- “launch” (for EHR-Launch mode only);
	- “scope”;
	- “state”;
	- “aud”;
	- “code_challenge”; and
	- “code_challenge_method”


8. AUT-PAT-28: 
	[Both] The health IT developer demonstrates the ability of the Health IT Module to support the receipt of the following scopes and capabilities according to the implementation specification adopted in § 170.215(a)(3) and standard adopted in § 170.215(b):
	- “openid” (to support “sso-openid-connect” “SMART on FHIR® Capability”);
	- “FHIR®User” (to support “sso-openid-connect” “SMART on FHIR® Capability”);
	- “need_patient_banner” (to support “context-banner” “SMART on FHIR® Capability” for EHR-Launch mode only);
	- “smart_style_url” (to support “context-style” “SMART on FHIR® Capability” for EHR-Launch mode only);
	- “launch/patient” (to support “context-standalone-patient” “SMART on FHIR® Capability” for Standalone-Launch mode only);
	- “launch” (for EHR-Launch mode only);
	- “offline_access” (to support “permission-offline” “SMART on FHIR® Capability”);
	- Patient-level scopes (to support “permission-patient” and “SMART on FHIR® Capability”); and
	- User-level scopes (to support “permission-user” “SMART on FHIR® Capability”).
	- SMARTv1 scope syntax for patient-level and user-level scopes (to support “permission-v1” “SMART on FHIR® Capability”)
	- SMARTv2 scope syntax for patient-level and user-level scopes (to support “permission-v2” “SMART on FHIR® Capability”)


9. AUT-PAT-10: 
[Both] The health IT developer demonstrates the ability of the Health IT Module to evaluate the authorization request and request end-user input, if applicable (required for patient-facing applications), including the ability for the end-user to authorize an application to receive EHI based on FHIR® resource-level scopes for all of the FHIR® resources associated with the profiles specified in the standard adopted in § 170.213 and implementation specification adopted in § 170.215(a)(2).
 
If using US Core 3.1.1, 4.0.0, or 5.0.1, these resources include:
    - “AllergyIntolerance”;
    - “CarePlan”;
    - “CareTeam”;
    - “Condition”;
    - “Device”;
    - “DiagnosticReport”;
    - “DocumentReference”;
    - “Goal”;
    - “Immunization”;
    - “Medication” (if supported);
    - “MedicationRequest”;
    - “Observation”;
    - “Patient”;
    - “Procedure”; and
    - “Provenance”.


10. AUT-PAT-29: 
[Both] The health IT developer demonstrates the ability of the Health IT Module to support for the purposes of backwards compatibility the use of SMART Application Launch Framework Implementation Guide Release 1.0.0 scopes as detailed in the implementation specification adopted in § 170.215(a)(3).


11. AUT-PAT-11: 
[Both] The health IT developer demonstrates the ability of the Health IT Module to evaluate the authorization request and request end-user input, if applicable (required for patient-facing applications), including either the ability for the end-user to explicitly enable / disable the “offline_access” scope or information communicating the application’s request for the “offline_access” scope.


12. AUT-PAT-12: 
[Both] The health IT developer demonstrates the ability of the Health IT Module to deny an application’s authorization request according to a patient’s preferences selected in steps 10, and 11, of this section in accordance with the implementation specification adopted in § 170.215(a)(3).


13. AUT-PAT-30: 
[EHR-Launch] The health IT developer demonstrates the ability of the Health IT Module to establish a patient in context if an application requests a clinical scope which is restricted to a single patient as detailed in the implementation specification adopted in § 170.215(a)(3).


14. AUT-PAT-13: 
[Both] The health IT developer demonstrates the ability of the Health IT Module to return an error response if the "aud" parameter provided by an application to the Health IT Module in Step 8, is not a valid FHIR® resource server associated with the Health IT Module's authorization server.


15. AUT-PAT-14: 
[Both] The health IT developer demonstrates the ability of the Health IT Module to grant an application access to EHI by returning an authorization code to the application according to the implementation specification adopted in § 170.215(a)(3), including the following parameters:
	- “code”; and
	- “state”.


16. AUT-PAT-31: 
[Both] The health IT developer demonstrates the ability of the Health IT Module to receive the following access token request parameters from an application according to the implementation specification adopted in § 170.215(a)(3): 
	- “grant_type”; 
	- “code”; 
	- “redirect_uri”; 
	- “code_verifier”; 
	- “client_id”; and 
	- Authorization header including “client_id” and “client_secret”.


17. AUT-PAT-32: 
[Both] The health IT developer demonstrates the ability of the Health IT Module to return an error response if an invalid “code_verifier” value is supplied with an access token request according to the implementation specification adopted in § 170.215(a)(3).


18. AUT-PAT-16: 
[Both] The health IT developer demonstrates the ability of the Health IT Module to return a JSON object to applications according to the implementation specification adopted in § 170.215(a)(3) and standard adopted in § 170.215(b), including the following:
	- “access_token”;
	- “token_type”;
	- “scope”;
	- “id_token”;
	- “refresh_token” (valid for a period of no shorter than three months);
	- HTTP “Cache-Control” response header field with a value of “no-store”;
	- HTTP “Pragma” response header field with a value of “no-cache”;
	- “patient” (to support “context-ehr-patient” and “context-standalone-patient” “SMART on FHIR® Core Capabilities”);
	- “need_patient_banner” (to support “context-banner” “SMART on FHIR® Core Capability” for EHR-Launch mode only); and
	- “smart_style_url” (to support “context-style” “SMART on FHIR® Core Capability” for EHR-Launch mode only).


19. AUT-PAT-17: 
[Both] The health IT developer demonstrates the ability of the Health IT Module to provide an OpenID Connect well-known URI in accordance with the implementation specification adopted in § 170.215(b), including:
	- All required fields populated according to implementation specification adopted in § 170.215(b); and
	- Valid JWKS populated according to implementation specification can be retrieved via JWKS URI.


20. AUT-PAT-18: 
[Both] The health IT developer demonstrates the ability of the Health IT Module to deny an application’s authorization request in accordance with the implementation specification adopted in § 170.215(a)(3).


21. AUT-PAT-19: 
[Both] The health IT developer demonstrates the ability of the Health IT Module to return a “Patient” FHIR® resource that matches the patient context provided in step AUT-PAT-9 of this section according to the implementation specification adopted in § 170.215(a)(2).


22. AUT-PAT-33: 
[EHR-Launch] The following must be supported if using US Core 5.0.1: The health IT developer demonstrates the ability of the Health IT Module to return an “Encounter” FHIR® resource that matches the encounter context provided in step AUT-PAT-9 of this section according to the implementation specification adopted in § 170.215(a)(2).


23. AUT-PAT-20: 
[Both] The health IT developer demonstrates the ability of the Health IT Module to grant an access token when a refresh token is supplied according to the implementation specification adopted in § 170.215(a)(2).


24. AUT-PAT-21: 
[Both] The health IT developer demonstrates the ability of the Health IT Module to grant a refresh token valid for a period of no less than three months to native applications capable of securing a refresh token.


### Subsequent Connections: Authentication and Authorization for Patient and User Scopes
1. AUT-PAT-22: 
The health IT developer demonstrates the ability of the Health IT Module to issue a refresh token valid for a new period of no shorter than three months without requiring re-authentication and re-authorization when a valid refresh token is supplied by the application according to the implementation specification adopted in § 170.215(a)(3).


2. AUT-PAT-23: 
The health IT developer demonstrates the ability of the Health IT Module to return an error response when supplied an invalid refresh token as specified in the implementation specification adopted in § 170.215(a)(3).


## Paragraph (g)(10)(vi) – Patient authorization revocation
### Patient Authorization Revocation
1. PAR-1: 
The health IT developer demonstrates the ability of the Health IT Module to revoke access to an authorized application at a patient’s direction, including a demonstration of the inability of the application with revoked access to receive patient EHI.


## Paragraph (g)(10)(v)(B) – Authentication and authorization for system scopes
### Authentication and Authorization for System Scopes
1. AUT-SYS-1: 
The health IT developer demonstrates the ability of the Health IT Module to support OAuth 2.0 client credentials grant flow in accordance with the implementation specification adopted in § 170.215(a)(4).


2. AUT-SYS-2: 
The health IT developer demonstrates the ability of the Health IT Module to support the following parameters according to the implementation specification adopted in § 170.215(a)(4):
	- “scope”; 
	- “grant_type”;
	- “client_assertion_type”; and
	- “client_assertion”.	 


3. AUT-SYS-3: 
The health IT developer demonstrates the ability of the Health IT Module to support the following JSON Web Token (JWT) Headers and Claims according to the implementation specification adopted in § 170.215(a)(4):
	- “alg” header;
	- “kid” header;
	- “typ” header;
	- “iss” claim;
	- “sub” claim;
	- “aud” claim;
	- “exp” claim; and
	- “jti” claim.


4. AUT-SYS-4: 
The health IT developer demonstrates the ability of the Health IT Module to receive and process the JSON Web Key (JWK) Set via a TLS-protected URL to support authorization for system scopes in § 170.315(g)(10)(v)(B).


5. AUT-SYS-5: 
The health IT developer demonstrates that the Health IT Module does not cache a JWK Set received via a TLS-protected URL for longer than the “cache-control” header sent by an application indicates.


6. AUT-SYS-6: 
The health IT developer demonstrates the ability of the Health IT Module to validate an application’s JWT, including its JSON Web Signatures, according to the implementation specification adopted in § 170.215(a)(4).


7. AUT-SYS-7: 
The health IT developer demonstrates the ability of the Health IT Module to respond with an “invalid_client” error for errors encountered during the authentication process according to the implementation specification adopted in § 170.215(a)(4).


8. AUT-SYS-8: 
The health IT developer demonstrates the ability of the Health IT Module to assure the scope granted based on the scope requested by an application is no greater than the pre-authorized scope for multiple patients according to the implementation specification adopted in § 170.215(a)(4).


9. AUT-SYS-9: 
 The health IT developer demonstrates the ability of the Health IT Module to issue an access token to an application as a JSON object in accordance with the implementation specification adopted in § 170.215(a)(4), including the following property names:
	- “access_token”;
	- “token_type”;
	- “expires_in”; and
	- “scope”.


10. AUT-SYS-10: 
The health IT developer demonstrates the ability of the Health IT Module to respond to errors using the appropriate error messages as specified in the implementation specification adopted in § 170.215(a)(4).


## Paragraph (g)(10)(vii) – Token introspection
### Token Introspection
1. TOK-INTRO-1: 
The health IT developer demonstrates the ability of the Health IT Module to receive and validate a token it has issued.


## Paragraph (g)(10)(ii) – Supported search operations
### Supported Search Operations for a Single Patient’s Data
1. SH-PAT-1: 
The health IT developer demonstrates the ability of the Health IT Module to support the “capabilities” interaction as specified in the standard adopted in § 170.215(a)(1), including support for a “CapabilityStatement” as specified in the standard adopted in § 170.215(a)(1) and implementation specification adopted in § 170.215(a)(2).


2. SH-PAT-2: 
The health IT developer demonstrates the ability of the Health IT Module to respond to requests for a single patient’s data consistent with the search criteria detailed in the “US Core Server CapabilityStatement” section of the implementation specification adopted in § 170.215(a)(2), including demonstrating search support for “SHALL” operations and parameters for all the data included in the standard adopted in § 170.213.


3. SH-PAT-3: 
The health IT developer demonstrates the ability of the Health IT Module to support a resource search for the provenance target “(_revIncludes: Provenance:target)” for all the FHIR® resources included in the standard adopted in § 170.213 and implementation specification adopted in § 170.215(a)(2) according to the “Basic Provenance Guidance” section of the implementation specification adopted in § 170.215(a)(2).


### Supported Search Operations for Multiple Patients’ Data
1. SH-PAT-4: 
The health IT developer demonstrates the ability of the Health IT Module to support the “capabilities” interaction as specified in the standard adopted in § 170.215(a)(1), including support for a “CapabilityStatement” as specified in the standard adopted in § 170.215(a)(1) and implementation specification adopted in § 170.215(a)(4). 


2. SH-PAT-5: 
The health IT developer demonstrates the ability of the Health IT Module to support requests for multiple patients’ data as a group using the “group-export” operation as detailed in the implementation specification adopted in § 170.215(a)(4).


## Paragraph (g)(10)(i) – Data response
### Data Response Checks for Single and Multiple Patients
1. DAT-PAT-1: 
For responses to data for single and multiple patients as described in steps 7, and 8, of this section respectively, the health IT developer demonstrates the ability of the Health IT Module to respond to requests for data according to the implementation specification adopted in § 170.215(a)(2), including the following steps.


2. DAT-PAT-2: 
The health IT developer demonstrates the ability of the Health IT Module to respond with data that meet the following conditions:
	- All data elements indicated with a cardinality of one or greater and / or “must support” are included;
	- Content is structurally correct;
	- All invariant rules are met;
	- All data elements with required “ValueSet” bindings contain codes within the bound “ValueSet”;
	- All information is accurate and without omission; and
	All references within the resources can be resolved and validated, as applicable, according to steps 2-6, of this section.


3. DAT-PAT-3: 
The health IT developer demonstrates the ability of the Health IT Module to support a “Provenance” FHIR® resource for all the FHIR® resources included in the standard adopted in § 170.213 and implementation specification adopted in § 170.215(a)(2) according to the “Basic Provenance Guidance” section of the implementation specification adopted in § 170.215(a)(2).


4. DAT-PAT-4: 
The health IT developer demonstrates the ability of the Health IT Module to support a “DocumentReference” and/or “DiagnosticReport” FHIR® resource for each of the “Clinical Notes” and “Diagnostic Reports” included in and according to the “Clinical Notes Guidance” section of the implementation specification adopted in § 170.215(a)(2).


5. DAT-PAT-5: 
If supported, and for responses to data for a single patient only, the health IT developer demonstrates the ability of the Health IT Module to support a “Medication” FHIR® resource according to the “Medication List Guidance” section of the implementation specification adopted in § 170.215(a)(2).


6. DAT-PAT-6: 
The health IT developer demonstrates the ability of the Health IT Module to support “Missing Data” according to the implementation specification adopted in § 170. 215(a)(2), including:
	- For non-coded data elements; and
	- For coded data elements, including support for the “DataAbsentReason” Code System.


### Response to Requests for a Single Patient’s Data
1. DAT-PAT-7: 
The health IT developer demonstrates the ability of the Health IT Module to return all of the data associated with requests for a single patient’s data according to the “US Core Server CapabilityStatement” section of the implementation specification adopted in § 170.215(a)(2) for all the data included in the standard adopted in § 170.213.


### Response to Requests for Multiple Patients' Data
1. DAT-PAT-8: 
The health IT developer demonstrates the ability of the Health IT Module to respond to requests for multiple patients’ data according to the implementation specification adopted in § 170.215(a)(4) for all of the FHIR® resources associated with the profiles and Data Elements specified in and according to the standard adopted in § 170.213 and implementation specification adopted in § 170.215(a)(2).:
	- “AllergyIntolerance”;
	- “CarePlan”;
	- “CareTeam”;
	- “Condition”;
	- “Device”;
	- “DiagnosticReport”;
	- “DocumentReference”;
	- “Encounter”;
	- “Goal”;
	- “Immunization”;
	- "Location" (if supported);
	- “Medication” (if supported);
	- “MedicationRequest”;
	- “Observation”;
	- “Organization”;
	- “Patient”;
	- “Practitioner”
	- “Procedure”; and
	- “Provenance”.


2. DAT-PAT-9: 
The health IT developer demonstrates the ability of the Health IT Module to limit the data returned to only those FHIR® resources for which the client is authorized according to the implementation specification adopted in § 170.215(a)(4).


3. DAT-PAT-10: 
The health IT developer demonstrates the ability of the Health IT Module to support a successful data response according to the implementation adopted in § 170.215(a)(4).


4. DAT-PAT-11: 
The health IT developer demonstrates the ability of the Health IT Module to support a data response error according to the implementation adopted in § 170.215(a)(4).


5. DAT-PAT-12: 
The health IT developer demonstrates the ability of the Health IT Module to support a bulk data delete request according to the implementation specification adopted in § 170.215(a)(4).


6. DAT-PAT-13: 
The health IT developer demonstrates the ability of the Health IT Module to support a bulk data status request according to the implementation specification adopted in § 170.215(a)(4).


7. DAT-PAT-14: 
The health IT developer demonstrates the ability of the Health IT Module to support a file request according to the implementation specification adopted in § 170.215(a)(4), including support for the “ndjson” format for files provided.


8. DAT-PAT-15: 
The health IT developer demonstrates that the information provided as part of this data response includes data for patients in the group identifier provided during the “group-export” request.


## Paragraph (g)(10)(viii) – Documentation
### API Documentation Requirements
1. API-DOC-1: 
The health IT developer supplies documentation describing the API(s) of the Health IT Module and includes at a minimum:
	- API syntax;
	- Function names;
	- Required and optional parameters supported and their data types;
	- Return variables and their types/structures;
	- Exceptions and exception handling methods and their returns;
	- Mandatory software components;
	- Mandatory software configurations; and
	- All technical requirements and attributes necessary for registration.


2. API-DOC-2: 
The health IT developer demonstrates that the documentation described in step 1, of this section is available via a publicly accessible hyperlink that does not require preconditions or additional steps to access.


3. API-DOC-3: 
To fulfill the API Maintenance of Certification requirement at § 170.404(b)(2), the health IT developer demonstrates the public location of its certified API technology service base URLs.



--8<-- "includes/abbreviations.md"
# Chameleon API Docs

Documentation for the Chameleon API routing and endpoints.

The documentation can be viewed locally by running any webserver in the `docs` directory:

```
ruby -run -e httpd docs -p 8000
```

## Status & Guidelines

### Outstanding Work
- Complete remaining 4 webhook examples: `tour.snoozed`, `survey.snoozed`, `helpbar.item.error`, `alert.triggered`

### Example Data Standards
When updating documentation, follow these standards:

#### **Dates**: Use 2029 dates consistently in ISO 8601 format (`2029-MM-DDTHH:mm:ss.sssZ`)

#### **Privacy**: Never use real user data - use fictional but realistic examples:
- Email format: `user@example.com`, `firstname.lastname@company.tld`
- Use example.com, example.io domains for fictional companies

#### **IDs**: Use consistent 24-character hex patterns: `5f3c4232c712de665632****`

### Suggested Improvements
**High Priority:**
- Add navigation and "Back to Overview" links
- Add visual callouts for warnings/tips
- Complete cURL examples for all endpoints

**Medium Priority:**  
- Add troubleshooting sections
- Enhance schema tables with "Required" column
- Create quick start guide

**Future Considerations:**
- Interactive API explorer
- Multi-language SDK examples
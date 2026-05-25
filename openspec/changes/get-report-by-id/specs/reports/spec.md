# Spec Delta

## ADD

### Endpoint

GET /reports/{id}

### Parameters

id:
- type: integer
- required: true

### Responses

200:
Return existing public report model

404:
{
  "detail": "Report not found"
}

### Constraints

- Existing `/reports` endpoint behavior remains unchanged
- Existing pagination behavior remains unchanged
- Reuse existing response model
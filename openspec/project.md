# Project Context

## Tech Stack
- Python
- FastAPI
- Pydantic
- In-memory dataset

## Conventions
- All routes return JSON
- Existing routes must remain unchanged
- Public models never expose internal fields
- Existing API behavior preserved

## Constraints
- Preserve `/reports` contract
- Preserve pagination behavior
- No breaking changes to existing endpoints
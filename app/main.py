"""FastAPI HTTP layer for the Reports app."""

from __future__ import annotations

from datetime import datetime

from fastapi import FastAPI, HTTPException, Query

from app.models import ReportListResponse, ReportPublic, ReportStatus
from app.reports import query, get_report_by_id

app = FastAPI(title="SDD Workshop — Reports API", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/reports", response_model=ReportListResponse)
def list_reports(
    status: ReportStatus | None = Query(None, description="Filter by status"),
    date_from: datetime | None = Query(None, description="Lower bound on created_at (inclusive)"),
    date_to: datetime | None = Query(None, description="Upper bound on created_at (inclusive)"),
    sort: str = Query("created_at", description="Sort field"),
    descending: bool = Query(True, description="Sort descending"),
    offset: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=200),
) -> ReportListResponse:
    """Return a paginated list of reports.

    Public fields only — `internal_id` and `owner_email` are stripped via
    `ReportPublic.from_internal`.
    """

    try:
        rows = query(
            status=status,
            date_from=date_from,
            date_to=date_to,
            sort=sort,
            descending=descending,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

    page = rows[offset : offset + limit]
    return ReportListResponse(
        items=[ReportPublic.from_internal(r) for r in page],
        total=len(rows),
        offset=offset,
        limit=limit,
    )
    
@app.get("/reports/{id}", response_model=ReportPublic)
def get_report(id: int) -> ReportPublic:
    """Return one report by ID."""

    report = get_report_by_id(id)

    if report is None:
        raise HTTPException(
            status_code=404,
            detail="Report not found",
        )

    return ReportPublic.from_internal(report)
from fastapi import APIRouter

from src.configs import project_meta

router = APIRouter(tags=["health"])


@router.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok", "version": project_meta.version}

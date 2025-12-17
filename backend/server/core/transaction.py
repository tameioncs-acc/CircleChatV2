from contextlib import contextmanager
from typing import Generator

from sqlalchemy.orm import Session


@contextmanager
def transaction(db: Session) -> Generator[Session, None, None]:
    """Context manager for database transactions.

    Automatically commits on success, rolls back on error.

    Usage:
        with transaction(db):
            db.add(entity1)
            db.add(entity2)
            # Commits both or rolls back both
    """
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise


class TransactionManager:
    """Mixin class for services that need transaction support."""

    def __init__(self, db: Session):
        self._db = db

    @contextmanager
    def with_transaction(self) -> Generator[Session, None, None]:
        """Execute operations within a transaction."""
        with transaction(self._db) as db:
            yield db

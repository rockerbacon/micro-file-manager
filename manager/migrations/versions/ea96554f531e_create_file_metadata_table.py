"""create file metadata table

Revision ID: ea96554f531e
Revises:
Create Date: 2023-09-22 10:35:46.300099

"""


from alembic import op
import sqlalchemy as sa
from typing import Sequence, Union


# revision identifiers, used by Alembic.
revision: str = "ea96554f531e"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "file_metadata",
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.Column("description", sa.String, nullable=True),
        sa.Column("mime_type", sa.String, nullable=False),
        sa.Column("name", sa.String, primary_key=True),
    )


def downgrade() -> None:
    op.drop_table("file_metadata")

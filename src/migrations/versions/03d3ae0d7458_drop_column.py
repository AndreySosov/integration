"""Drop column

Revision ID: 03d3ae0d7458
Revises: df7d9c0dc832
Create Date: 2024-09-09 23:14:25.381355

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '03d3ae0d7458'
down_revision: Union[str, None] = 'df7d9c0dc832'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('hotels', 'addr')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hotels', sa.Column('addr', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###

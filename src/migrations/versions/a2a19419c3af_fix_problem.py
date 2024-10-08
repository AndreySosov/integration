"""Fix problem

Revision ID: a2a19419c3af
Revises: 2796c0c28d10
Create Date: 2024-09-10 18:20:41.327243

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a2a19419c3af'
down_revision: Union[str, None] = '2796c0c28d10'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hashed_pass', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rooms',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('hotel_id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('services', sa.JSON(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('image_id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['hotel_id'], ['hotels.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bookings',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('room_id', sa.UUID(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('date_from', sa.DateTime(), nullable=True),
    sa.Column('date_to', sa.DateTime(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('total_cost', sa.Integer(), nullable=True),
    sa.Column('total_day', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['room_id'], ['rooms.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bookings')
    op.drop_table('rooms')
    op.drop_table('users')
    # ### end Alembic commands ###

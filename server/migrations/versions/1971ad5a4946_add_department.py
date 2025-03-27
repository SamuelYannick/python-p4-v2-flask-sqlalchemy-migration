"""add Department

Revision ID: 1971ad5a4946
Revises: d26e6019ed90
Create Date: 2025-03-27 11:03:22.172751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1971ad5a4946'
down_revision = 'd26e6019ed90'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###

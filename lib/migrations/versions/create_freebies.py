"""create freebies table

Revision ID: abc123freebie
Revises: 5f72c58bf48c
Create Date: 2025-03-17 12:00:00.000000
"""

from alembic import op
import sqlalchemy as sa

revision = 'abc123freebie'
down_revision = '5f72c58bf48c'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        'freebies',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('item_name', sa.String(), nullable=False),
        sa.Column('value', sa.Integer(), nullable=False),
        sa.Column('dev_id', sa.Integer(), sa.ForeignKey('devs.id'), nullable=False),
        sa.Column('company_id', sa.Integer(), sa.ForeignKey('companies.id'), nullable=False),
    )

def downgrade() -> None:
    op.drop_table('freebies')

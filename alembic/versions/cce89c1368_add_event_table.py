"""add event table

Revision ID: cce89c1368
Revises: 543ce7d10ffa
Create Date: 2013-09-16 12:13:12.141385

"""

# revision identifiers, used by Alembic.
revision = 'cce89c1368'
down_revision = '543ce7d10ffa'

from alembic import op
import sqlalchemy as sa

from datetime import datetime


def upgrade():
    op.create_table(
        'event', 
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('create_at', sa.DateTime, nullable=False, default=datetime.now),
        sa.Column('link', sa.String(255), nullable=False),
        sa.Column('content', sa.Text()),
    )


def downgrade():
    op.drop_table('event')

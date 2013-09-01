"""pages_to_page

Revision ID: 543ce7d10ffa
Revises: 47727c8dffb0
Create Date: 2013-09-01 11:53:45.484926

"""

# revision identifiers, used by Alembic.
revision = '543ce7d10ffa'
down_revision = '47727c8dffb0'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'page', 
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('uid', sa.String(255), index=True, unique=True),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('content', sa.Text()),
    )
    op.drop_table('pages')


def downgrade():
    pass

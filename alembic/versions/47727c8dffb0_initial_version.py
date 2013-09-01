"""initial version

Revision ID: 47727c8dffb0
Revises: None
Create Date: 2013-09-01 11:18:01.843574

"""

# revision identifiers, used by Alembic.
revision = '47727c8dffb0'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'pages', 
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('uid', sa.String(255), index=True, unique=True),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('content', sa.Text()),
    )


def downgrade():
    pass

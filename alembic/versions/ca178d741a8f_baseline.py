"""baseline

Revision ID: ca178d741a8f
Revises: 
Create Date: 2020-12-08 07:24:30.530214

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca178d741a8f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'bug',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('bug_tracker_url', sa.String(), nullable=False),
        sa.Column('root_cause', sa.String()),
        sa.Column('who', sa.String()),
        sa.Column('when', sa.DateTime(), default=sa.func.now()))


def downgrade():
    op.drop_table('bug')

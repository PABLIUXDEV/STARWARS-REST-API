"""empty message

Revision ID: b741ce420a31
Revises: c307f8426a50
Create Date: 2024-11-23 22:18:20.163693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b741ce420a31'
down_revision = 'c307f8426a50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('size', sa.String(length=100), nullable=False),
    sa.Column('climate', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Planet')
    # ### end Alembic commands ###

"""omar3

Revision ID: 07888ad20be5
Revises: 7890c22ee733
Create Date: 2022-03-26 15:38:30.483468

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07888ad20be5'
down_revision = '7890c22ee733'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Appuser', sa.Column('RoleId', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'Appuser', 'Roles', ['RoleId'], ['Id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Appuser', type_='foreignkey')
    op.drop_column('Appuser', 'RoleId')
    # ### end Alembic commands ###

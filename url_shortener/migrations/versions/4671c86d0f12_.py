
from alembic import op
import sqlalchemy as sa





def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('short_urls',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('original_url', sa.String(length=250), nullable=False),
    sa.Column('short_id', sa.String(length=15), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('short_id')
    )
    # ### end Alembic commands ###

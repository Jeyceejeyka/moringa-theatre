from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '20231010_create_roles_table'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Create roles table
    op.create_table(
        'roles',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('character_name', sa.String, nullable=False, unique=True)
    )

def downgrade():
    # Drop roles table
    op.drop_table('roles')

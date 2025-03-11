from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '20231010_add_uniqueness_constraints'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Add uniqueness constraint to Role
    op.create_unique_constraint('uq_character_name', 'roles', ['character_name'])
    
    # Add uniqueness constraint to Audition
    op.create_unique_constraint('uq_actor_role', 'auditions', ['actor', 'role_id'])

def downgrade():
    # Drop uniqueness constraint from Role
    op.drop_constraint('uq_character_name', 'roles', type_='unique')
    
    # Drop uniqueness constraint from Audition
    op.drop_constraint('uq_actor_role', 'auditions', type_='unique')

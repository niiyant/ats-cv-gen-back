"""Inicializacion DB

Revision ID: 9ff31d88befb
Revises: 
Create Date: 2025-02-19 00:01:29.952379

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9ff31d88befb'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password_hash', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_first_name'), 'users', ['first_name'], unique=False)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_last_name'), 'users', ['last_name'], unique=False)
    op.create_table('cv',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=True),
    sa.Column('telephone', sa.Integer(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('summary', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cv_id'), 'cv', ['id'], unique=False)
    op.create_index(op.f('ix_cv_role'), 'cv', ['role'], unique=False)
    op.create_index(op.f('ix_cv_summary'), 'cv', ['summary'], unique=True)
    op.create_index(op.f('ix_cv_telephone'), 'cv', ['telephone'], unique=False)
    op.create_table('academic',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('cv_id', sa.UUID(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('institution', sa.String(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['cv_id'], ['cv.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_academic_description'), 'academic', ['description'], unique=False)
    op.create_index(op.f('ix_academic_id'), 'academic', ['id'], unique=False)
    op.create_index(op.f('ix_academic_institution'), 'academic', ['institution'], unique=False)
    op.create_index(op.f('ix_academic_title'), 'academic', ['title'], unique=False)
    op.create_table('certifications',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('cv_id', sa.UUID(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('institution', sa.String(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['cv_id'], ['cv.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_certifications_description'), 'certifications', ['description'], unique=False)
    op.create_index(op.f('ix_certifications_id'), 'certifications', ['id'], unique=False)
    op.create_index(op.f('ix_certifications_institution'), 'certifications', ['institution'], unique=False)
    op.create_index(op.f('ix_certifications_name'), 'certifications', ['name'], unique=False)
    op.create_table('experience',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('cv_id', sa.UUID(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('company', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['cv_id'], ['cv.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_experience_company'), 'experience', ['company'], unique=False)
    op.create_index(op.f('ix_experience_description'), 'experience', ['description'], unique=False)
    op.create_index(op.f('ix_experience_id'), 'experience', ['id'], unique=False)
    op.create_index(op.f('ix_experience_role'), 'experience', ['role'], unique=False)
    op.create_table('language',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('cv_id', sa.UUID(), nullable=True),
    sa.Column('speech', sa.String(), nullable=True),
    sa.Column('level', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['cv_id'], ['cv.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_language_id'), 'language', ['id'], unique=False)
    op.create_index(op.f('ix_language_level'), 'language', ['level'], unique=False)
    op.create_index(op.f('ix_language_speech'), 'language', ['speech'], unique=False)
    op.create_table('profile',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('cv_id', sa.UUID(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['cv_id'], ['cv.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_profile_id'), 'profile', ['id'], unique=False)
    op.create_index(op.f('ix_profile_name'), 'profile', ['name'], unique=False)
    op.create_index(op.f('ix_profile_url'), 'profile', ['url'], unique=False)
    op.create_table('skill',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('cv_id', sa.UUID(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('level', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['cv_id'], ['cv.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_skill_id'), 'skill', ['id'], unique=False)
    op.create_index(op.f('ix_skill_level'), 'skill', ['level'], unique=False)
    op.create_index(op.f('ix_skill_title'), 'skill', ['title'], unique=False)
    op.create_table('soft_skill',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('cv_id', sa.UUID(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['cv_id'], ['cv.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_soft_skill_id'), 'soft_skill', ['id'], unique=False)
    op.create_index(op.f('ix_soft_skill_title'), 'soft_skill', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_soft_skill_title'), table_name='soft_skill')
    op.drop_index(op.f('ix_soft_skill_id'), table_name='soft_skill')
    op.drop_table('soft_skill')
    op.drop_index(op.f('ix_skill_title'), table_name='skill')
    op.drop_index(op.f('ix_skill_level'), table_name='skill')
    op.drop_index(op.f('ix_skill_id'), table_name='skill')
    op.drop_table('skill')
    op.drop_index(op.f('ix_profile_url'), table_name='profile')
    op.drop_index(op.f('ix_profile_name'), table_name='profile')
    op.drop_index(op.f('ix_profile_id'), table_name='profile')
    op.drop_table('profile')
    op.drop_index(op.f('ix_language_speech'), table_name='language')
    op.drop_index(op.f('ix_language_level'), table_name='language')
    op.drop_index(op.f('ix_language_id'), table_name='language')
    op.drop_table('language')
    op.drop_index(op.f('ix_experience_role'), table_name='experience')
    op.drop_index(op.f('ix_experience_id'), table_name='experience')
    op.drop_index(op.f('ix_experience_description'), table_name='experience')
    op.drop_index(op.f('ix_experience_company'), table_name='experience')
    op.drop_table('experience')
    op.drop_index(op.f('ix_certifications_name'), table_name='certifications')
    op.drop_index(op.f('ix_certifications_institution'), table_name='certifications')
    op.drop_index(op.f('ix_certifications_id'), table_name='certifications')
    op.drop_index(op.f('ix_certifications_description'), table_name='certifications')
    op.drop_table('certifications')
    op.drop_index(op.f('ix_academic_title'), table_name='academic')
    op.drop_index(op.f('ix_academic_institution'), table_name='academic')
    op.drop_index(op.f('ix_academic_id'), table_name='academic')
    op.drop_index(op.f('ix_academic_description'), table_name='academic')
    op.drop_table('academic')
    op.drop_index(op.f('ix_cv_telephone'), table_name='cv')
    op.drop_index(op.f('ix_cv_summary'), table_name='cv')
    op.drop_index(op.f('ix_cv_role'), table_name='cv')
    op.drop_index(op.f('ix_cv_id'), table_name='cv')
    op.drop_table('cv')
    op.drop_index(op.f('ix_users_last_name'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_first_name'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###

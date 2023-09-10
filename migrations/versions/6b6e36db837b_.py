"""empty message

Revision ID: 6b6e36db837b
Revises: 
Create Date: 2023-09-10 13:54:46.042660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b6e36db837b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Rol',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipoRol', sa.String(length=45), nullable=False),
    sa.Column('nombreRol', sa.String(length=45), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Usuario',
    sa.Column('idUsu', sa.Integer(), nullable=False),
    sa.Column('nombreUsuario', sa.String(length=45), nullable=False),
    sa.Column('apellidoUsuario', sa.String(length=45), nullable=False),
    sa.Column('telefonoUsuario', sa.String(length=45), nullable=False),
    sa.Column('emailUsuario', sa.String(length=45), nullable=False),
    sa.Column('contrasenaUsuario', sa.String(length=45), nullable=False),
    sa.Column('idRolFk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['idRolFk'], ['Rol.id'], ),
    sa.PrimaryKeyConstraint('idUsu')
    )
    op.create_table('Garantia',
    sa.Column('idGarantia', sa.Integer(), nullable=False),
    sa.Column('fechaGarantia', sa.Date(), nullable=False),
    sa.Column('descripcionGarantia', sa.Text(), nullable=False),
    sa.Column('tipoGarantia', sa.String(length=255), nullable=False),
    sa.Column('idUsuFk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['idUsuFk'], ['Usuario.idUsu'], ),
    sa.PrimaryKeyConstraint('idGarantia')
    )
    op.create_table('Contrato',
    sa.Column('idContrato', sa.String(length=20), nullable=False),
    sa.Column('tipoContrato', sa.String(length=50), nullable=False),
    sa.Column('descripcionContrato', sa.Text(), nullable=False),
    sa.Column('idGarantiaFk', sa.Integer(), nullable=True),
    sa.Column('idUsuFk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['idGarantiaFk'], ['Garantia.idGarantia'], ),
    sa.ForeignKeyConstraint(['idUsuFk'], ['Usuario.idUsu'], ),
    sa.PrimaryKeyConstraint('idContrato')
    )
    op.create_table('Pqrs',
    sa.Column('idPqrs', sa.Integer(), nullable=False),
    sa.Column('tipoPqrs', sa.String(length=255), nullable=False),
    sa.Column('descripcionPqrs', sa.Text(), nullable=False),
    sa.Column('idGarantiaFk', sa.Integer(), nullable=True),
    sa.Column('idContratoFk', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['idContratoFk'], ['Contrato.idContrato'], ),
    sa.ForeignKeyConstraint(['idGarantiaFk'], ['Garantia.idGarantia'], ),
    sa.PrimaryKeyConstraint('idPqrs')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Pqrs')
    op.drop_table('Contrato')
    op.drop_table('Garantia')
    op.drop_table('Usuario')
    op.drop_table('Rol')
    # ### end Alembic commands ###
"""Increase last value in sensor and sensorhistory

Revision ID: 481f304ccc1a
Revises: 38b868f7501a
Create Date: 2016-03-07 06:09:20.994327

"""

# revision identifiers, used by Alembic.
revision = '481f304ccc1a'
down_revision = '38b868f7501a'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('core_sensor', 'last_value',
               existing_type=mysql.VARCHAR(length=32),
               type_=sa.Unicode(length=255),
               existing_nullable=True)
    op.alter_column('core_sensor', 'value_max',
               existing_type=mysql.DOUBLE(asdecimal=True),
               type_=sa.Float(precision=53),
               existing_nullable=True)
    op.alter_column('core_sensor', 'value_min',
               existing_type=mysql.DOUBLE(asdecimal=True),
               type_=sa.Float(precision=53),
               existing_nullable=True)
    op.alter_column('core_sensor_history', 'original_value_num',
               existing_type=mysql.DOUBLE(asdecimal=True),
               type_=sa.Float(precision=53),
               existing_nullable=True)
    op.alter_column('core_sensor_history', 'value_num',
               existing_type=mysql.DOUBLE(asdecimal=True),
               type_=sa.Float(precision=53),
               existing_nullable=True)
    op.alter_column('core_sensor_history', 'value_str',
               existing_type=mysql.VARCHAR(length=32),
               type_=sa.Unicode(length=255),
               existing_nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('core_sensor_history', 'value_str',
               existing_type=sa.Unicode(length=255),
               type_=mysql.VARCHAR(length=32),
               existing_nullable=False)
    op.alter_column('core_sensor_history', 'value_num',
               existing_type=sa.Float(precision=53),
               type_=mysql.DOUBLE(asdecimal=True),
               existing_nullable=True)
    op.alter_column('core_sensor_history', 'original_value_num',
               existing_type=sa.Float(precision=53),
               type_=mysql.DOUBLE(asdecimal=True),
               existing_nullable=True)
    op.alter_column('core_sensor', 'value_min',
               existing_type=sa.Float(precision=53),
               type_=mysql.DOUBLE(asdecimal=True),
               existing_nullable=True)
    op.alter_column('core_sensor', 'value_max',
               existing_type=sa.Float(precision=53),
               type_=mysql.DOUBLE(asdecimal=True),
               existing_nullable=True)
    op.alter_column('core_sensor', 'last_value',
               existing_type=sa.Unicode(length=255),
               type_=mysql.VARCHAR(length=32),
               existing_nullable=True)
    op.alter_column('core_sensor', 'history_round',
               existing_type=sa.Float(precision=53),
               type_=mysql.DOUBLE(asdecimal=True),
               existing_nullable=True)
    ### end Alembic commands ###
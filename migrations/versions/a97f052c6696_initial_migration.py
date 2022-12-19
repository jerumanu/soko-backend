"""migartions 

<<<<<<<< HEAD:migrations/versions/dd29dd9d7c47_migartions.py
Revision ID: dd29dd9d7c47
Revises: 
Create Date: 2022-11-18 23:25:39.060371
========
Revision ID: a97f052c6696
Revises: 
Create Date: 2022-11-17 13:54:10.971844
>>>>>>>> payments:migrations/versions/a97f052c6696_initial_migration.py

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
<<<<<<<< HEAD:migrations/versions/dd29dd9d7c47_migartions.py
revision = 'dd29dd9d7c47'
========
revision = 'a97f052c6696'
>>>>>>>> payments:migrations/versions/a97f052c6696_initial_migration.py
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(' business',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('business_name', sa.String(length=50), nullable=True),
    sa.Column('business_desc', sa.String(length=50), nullable=True),
    sa.Column('specific_location', sa.String(), nullable=True),
    sa.Column('location', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('business_name'),
    sa.UniqueConstraint('id')
    )
    op.create_table(' loads',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tenegerydemand', sa.Integer(), nullable=True),
    sa.Column('autonomy', sa.Integer(), nullable=True),
    sa.Column('location', sa.String(length=50), nullable=True),
    sa.Column('latitude', sa.Integer(), nullable=True),
    sa.Column('longtitude', sa.Integer(), nullable=True),
    sa.Column('systemvolts', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('Faq',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('createdAt', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('batt',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('battv', sa.Integer(), nullable=True),
    sa.Column('dod', sa.Integer(), nullable=True),
    sa.Column('ah', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('blacklist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('refresh_token', sa.String(length=255), nullable=True),
    sa.Column('block_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
<<<<<<<< HEAD:migrations/versions/dd29dd9d7c47_migartions.py
    op.create_table('dereted',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('wp', sa.Integer(), nullable=True),
    sa.Column('tstc', sa.Integer(), nullable=True),
    sa.Column('vmp', sa.Integer(), nullable=True),
    sa.Column('voc', sa.Integer(), nullable=True),
    sa.Column('isc', sa.Integer(), nullable=True),
    sa.Column('tcoeff', sa.Integer(), nullable=True),
    sa.Column('fman', sa.Integer(), nullable=True),
    sa.Column('vcoeff', sa.Integer(), nullable=True),
    sa.Column('wpd', sa.Integer(), nullable=True),
========
    op.create_table('brand',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('createAt', sa.DateTime(), nullable=False),
>>>>>>>> payments:migrations/versions/a97f052c6696_initial_migration.py
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('name')
    )
<<<<<<<< HEAD:migrations/versions/dd29dd9d7c47_migartions.py
    op.create_table('engineer',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('profesion', sa.String(length=50), nullable=True),
    sa.Column('specification', sa.String(length=50), nullable=True),
    sa.Column('location', sa.String(length=50), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('website', sa.String(length=100), nullable=True),
    sa.Column('linkdin', sa.String(length=100), nullable=True),
    sa.Column('twitter', sa.String(length=50), nullable=True),
    sa.Column('instagram', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('starRating',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('rate', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
========
    op.create_table('solarType',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('createAt', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('name')
>>>>>>>> payments:migrations/versions/a97f052c6696_initial_migration.py
    )
    op.create_table('subscribe',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('createdAt', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id')
    )
    op.create_table('time_format',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.Column('end_time', sa.DateTime(), nullable=False),
    sa.Column('closed_all_day', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.Column('lastname', sa.String(length=64), nullable=True),
    sa.Column('firstname', sa.String(length=64), nullable=True),
    sa.Column('user_role', sa.String(length=30), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('mobile', sa.String(length=11), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('location', sa.String(length=64), nullable=True),
    sa.Column('about_me', sa.Text(), nullable=True),
    sa.Column('member_since', sa.DateTime(), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.Column('avatar_hash', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_table('blog',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('text', sa.String(length=255), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('blog_img', sa.String(), nullable=True),
    sa.Column('createAt', sa.DateTime(), nullable=False),
    sa.Column('author', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('category',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('createdAt', sa.DateTime(), nullable=False),
    sa.Column('author', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('invoice',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('phoneNumber', sa.String(), nullable=False),
    sa.Column('paymentType', sa.String(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transaction',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('receipt_id', sa.String(length=100), nullable=False),
    sa.Column('date_paid', sa.DateTime(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('merchant_request_id', sa.String(length=100), nullable=False),
    sa.Column('phoneNumber', sa.String(), nullable=False),
    sa.Column('paymentType', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=250), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('image', sa.String(length=256), nullable=True),
    sa.Column('product_owner', sa.Integer(), nullable=False),
    sa.Column('inStock', sa.Boolean(), nullable=False),
    sa.Column('condition', sa.String(), nullable=False),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('solarType_id', sa.Integer(), nullable=False),
    sa.Column('brand_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['brand_id'], ['brand.id'], ),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['product_owner'], ['user.id'], ),
    sa.ForeignKeyConstraint(['solarType_id'], ['solarType.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('comment', sa.String(length=250), nullable=False),
    sa.Column('comment_owner', sa.Integer(), nullable=False),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['comment_owner'], ['user.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favourite',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('timeStamp', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favourite')
    op.drop_table('comments')
    op.drop_table('product')
    op.drop_table('transaction')
    op.drop_table('invoice')
    op.drop_table('category')
    op.drop_table('blog')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('time_format')
    op.drop_table('subscribe')
<<<<<<<< HEAD:migrations/versions/dd29dd9d7c47_migartions.py
    op.drop_table('starRating')
    op.drop_table('engineer')
    op.drop_table('dereted')
========
    op.drop_table('solarType')
    op.drop_table('brand')
>>>>>>>> payments:migrations/versions/a97f052c6696_initial_migration.py
    op.drop_table('blacklist')
    op.drop_table('batt')
    op.drop_table('Faq')
    op.drop_table(' loads')
    op.drop_table(' business')
    # ### end Alembic commands ###

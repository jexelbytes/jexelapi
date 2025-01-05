alembic_init = """# A generic, single database configuration.

[alembic]
# path to migration scripts
# Use forward slashes (/) also on windows to provide an os agnostic path
script_location = migrations

# template used to generate migration file names; The default value is %%(rev)s_%%(slug)s
# Uncomment the line below if you want the files to be prepended with date and time
# see https://alembic.sqlalchemy.org/en/latest/tutorial.html#editing-the-ini-file
# for all available tokens
# file_template = %%(year)d_%%(month).2d_%%(day).2d_%%(hour).2d%%(minute).2d-%%(rev)s_%%(slug)s

# sys.path path, will be prepended to sys.path if present.
# defaults to the current working directory.
prepend_sys_path = .

# timezone to use when rendering the date within the migration file
# as well as the filename.
# If specified, requires the python>=3.9 or backports.zoneinfo library.
# Any required deps can installed by adding `alembic[tz]` to the pip requirements
# string value is passed to ZoneInfo()
# leave blank for localtime
# timezone =

# max length of characters to apply to the "slug" field
# truncate_slug_length = 40

# set to 'true' to run the environment during
# the 'revision' command, regardless of autogenerate
# revision_environment = false

# set to 'true' to allow .pyc and .pyo files without
# a source .py file to be detected as revisions in the
# versions/ directory
# sourceless = false

# version location specification; This defaults
# to migrations/versions.  When using multiple version
# directories, initial revisions must be specified with --version-path.
# The path separator used here should be the separator specified by "version_path_separator" below.
# version_locations = %(here)s/bar:%(here)s/bat:migrations/versions

# version path separator; As mentioned above, this is the character used to split
# version_locations. The default within new alembic.ini files is "os", which uses os.pathsep.
# If this key is omitted entirely, it falls back to the legacy behavior of splitting on spaces and/or commas.
# Valid values for version_path_separator are:
#
# version_path_separator = :
# version_path_separator = ;
# version_path_separator = space
# version_path_separator = newline
version_path_separator = os  # Use os.pathsep. Default configuration used for new projects.

# set to 'true' to search source files recursively
# in each "version_locations" directory
# new in Alembic version 1.10
# recursive_version_locations = false

# the output encoding used when revision files
# are written from script.py.mako
# output_encoding = utf-8

sqlalchemy.url = postgresql://%(DB_USER)s:%(DB_PASSWORD)s@%(HOST)s/%(DB_NAME)s


[post_write_hooks]
# post_write_hooks defines scripts or Python functions that are run
# on newly generated revision scripts.  See the documentation for further
# detail and examples

# format using "black" - use the console_scripts runner, against the "black" entrypoint
# hooks = black
# black.type = console_scripts
# black.entrypoint = black
# black.options = -l 79 REVISION_SCRIPT_FILENAME

# lint with attempts to fix using "ruff" - use the exec runner, execute a binary
# hooks = ruff
# ruff.type = exec
# ruff.executable = %(here)s/.venv/bin/ruff
# ruff.options = --fix REVISION_SCRIPT_FILENAME

# Logging configuration
[loggers]
keys = root,sqlalchemy,alembic

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARN
handlers = console
qualname =

[logger_sqlalchemy]
level = WARN
handlers =
qualname = sqlalchemy.engine

[logger_alembic]
level = INFO
handlers =
qualname = alembic

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
datefmt = %H:%M:%S
"""

env = """# SERVER
HOST=127.0.0.1
PORT=80
DEV_KEY=devkey

# DATABASE
DATABASE_TYPE='postgresql'
DATABASE_NAME='some_db'
DATABASE_USER='postgres'
DATABASE_PASS='postgres'
DBHOST='0.0.0.0'
DBPORT='5432'

# SWAGGER
IS_DEVELOP=True
SWAGGER_USER=admin
SWAGGER_PASS=admin

# JWT
JWT_SECRET=secret
JWT_ALGORITHM=HS256
JWT_EXPIRE_TIME = 600
JWT_REFRESH_EXPIRE_TIME = 600

# EMAIL CREDENTIALS
EMAIL=email@email.com
EMAIL_PASS=somepass
EMAIL_PORT=465
EMAIL_HOST=smtp.gmail.com

# AWS CREDENTIALS
AWS_S3_BUCKET=""
AWS_S3_KEY=""
AWS_S3_SECRET=""
AWS_S3_ZONE=""
"""

requirements = """alembic==1.14.0
annotated-types==0.7.0
anyio==4.7.0
boto3==1.35.92
botocore==1.35.92
CacheControl==0.14.1
cachetools==5.5.0
certifi==2024.12.14
cffi==1.17.1
charset-normalizer==3.4.1
click==8.1.8
colorama==0.4.6
configparser==7.1.0
cryptography==44.0.0
dnspython==2.7.0
email_validator==2.2.0
fastapi==0.115.6
firebase-admin==6.6.0
google-api-core==2.24.0
google-api-python-client==2.157.0
google-auth==2.37.0
google-auth-httplib2==0.2.0
google-cloud-core==2.4.1
google-cloud-firestore==2.19.0
google-cloud-storage==2.19.0
google-crc32c==1.6.0
google-resumable-media==2.7.2
googleapis-common-protos==1.66.0
grpcio==1.68.1
grpcio-status==1.68.1
h11==0.14.0
httplib2==0.22.0
idna==3.10
Jinja2==3.1.5
jmespath==1.0.1
Mako==1.3.8
MarkupSafe==3.0.2
msgpack==1.1.0
proto-plus==1.25.0
protobuf==5.29.2
psycopg2==2.9.10
pyasn1==0.6.1
pyasn1_modules==0.4.1
pycparser==2.22
pydantic==2.10.4
pydantic_core==2.27.2
PyJWT==2.10.1
PyMySQL==1.1.1
pyparsing==3.2.1
python-dateutil==2.9.0.post0
python-dotenv==1.0.1
python-multipart==0.0.20
requests==2.32.3
rsa==4.9
s3transfer==0.10.4
shutils==0.1.0
six==1.17.0
sniffio==1.3.1
SQLAlchemy==2.0.36
SQLAlchemy-Utils==0.41.2
starlette==0.41.3
typing_extensions==4.12.2
uritemplate==4.1.1
urllib3==2.3.0
uvicorn==0.34.0
"""
ALEMBIC_README="""Generic single-database configuration."""

ALEMBIC_SCRIPT='''"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision: str = ${repr(up_revision)}
down_revision: Union[str, None] = ${repr(down_revision)}
branch_labels: Union[str, Sequence[str], None] = ${repr(branch_labels)}
depends_on: Union[str, Sequence[str], None] = ${repr(depends_on)}


def upgrade() -> None:
    ${upgrades if upgrades else "pass"}


def downgrade() -> None:
    ${downgrades if downgrades else "pass"}
'''
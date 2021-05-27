from . import api

# INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
# INFO  [alembic.env] No changes in schema detected.
# 解决以上问题，要导入db, models，即使不用它
from ihome import db, models

@api.route("/index")
def index():
    return "index page"
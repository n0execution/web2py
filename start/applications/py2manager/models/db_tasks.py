db.define_table('company',
                Field('company_name', notnull=True, unique=True),
                Field('email'), 
                Field('phone', notnull=True), 
                Field('url'), 
                format = '%(company_name)s')

db.company.email.requires = IS_EMAIL()
db.company.url.requires = IS_EMPTY_OR(IS_URL())


db.define_table('project',
                Field('name', notnull=True),
                Field('employee_name', db.auth_user, default=auth.user_id),
                Field('company_name', 'reference company', notnull=True),
                Field('description', 'text', notnull=True),
                Field('start_date', 'date', notnull=True),
                Field('due_date', 'date', notnull=True),
                Field('completed', 'boolean', notnull=True),
                format = '%(company_name)s')


db.project.employee_name.readable = db.project.employee_name.writable = False

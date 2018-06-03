# encoding: utf-8
import json
from django.db import models
from .mysql_db_manager_v1 import DbUtils
from .mysql_db_manager_v2 import DbUtils as db2


# Create your models here.

class User(object):
    LOGIN_SQL = """
    SELECT id, name , password, sex , age, tel, remark  FROM cmdb_user 
    WHERE NAME = %s and PASSWORD = %s
    """

    LIST_SQL = """
    SELECT id, name , password, sex , age, tel, remark  FROM cmdb_user 
    """

    CHECK_USER_NAME_SQL = """
    select id from cmdb_user where name =%s and id !=%s
    """

    INSERT_USER_SQL = """
    INSERT INTO cmdb_user (name ,password,age,sex,tel,remark)
        VALUES (%s,%s,%s,%s,%s,%s)
    """

    def __init__(self, id, name, password, sex, age, tel, remark):
        self.id = id
        self.name = name
        self.password = password
        self.sex = sex
        self.age = age
        self.tel = tel
        self.remark = remark

    @classmethod
    def login_valid(cls, name, password):
        result = db2.get_one(cls.LOGIN_SQL, (name, password))
        # print(result)
        return cls.result_to_user(result) if result else None

    @classmethod
    def get_users(cls):
        result_list = db2.get_all(cls.LIST_SQL, None)
        user_list = [cls.result_to_user(result) for result in result_list]
        # print(user_list)
        return user_list

    @classmethod
    def result_to_user(cls,result):
        return User(id=result[0], name=result[1], password=result[2], sex=result[3], age=result[4], tel=result[5],
                    remark=result[6])

    @classmethod
    def valid_create_user(cls,post_info):
        add_user = User(id=0,name=post_info.get('name', '').strip(), password=post_info.get('password', '').strip(), sex=post_info.get('sex', '').strip(), age=post_info.get('age', '').strip(), tel=post_info.get('tel', '').strip(),
                    remark=post_info.get('remark', '').strip())
        password_confirm = post_info.get('password_confirm', '')

        is_valid = True
        errors = {}

        if add_user.name == '':
            is_valid = False
            errors['name'] = '用户名不能为空'
        else:
            result = db2.get_one(cls.CHECK_USER_NAME_SQL, (add_user.name, 0))
            if result:
                errors['name'] = '用户名已存在'
                is_valid = False

        if not add_user.age.isdigit():
            errors['age'] = '年龄格式错误'
            is_valid = False

        if add_user.password == '' or password_confirm != add_user.password:
            is_valid = False
            errors['password'] = '密码不能为空, 且两次输入密码必须相同'

        return is_valid, add_user, errors

    @classmethod
    def create_user(cls,add_user):
        result = db2.execute_sql(cls.INSERT_USER_SQL, (
            add_user.name, add_user.password, add_user.age, add_user.sex, add_user.tel, add_user.remark))
        return result

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'password': self.password,
            'sex': self.sex,
            'age': self.age,
            'tel': self.tel,
            'remark': self.remark
        }


LOGIN_SQL = """
SELECT id, name , password, sex , age, tel, remark  FROM cmdb_user 
WHERE NAME = %s and PASSWORD = %s
"""

LIST_SQL = """
SELECT id, name , password, sex , age, tel, remark  FROM cmdb_user 
"""

LIST_SQL_BY_CONDITIONS = """
SELECT id, name , password, sex , age, tel, remark  FROM cmdb_user 
WHERE name like %s
"""

CHECK_USER_NAME_SQL = """
select id from cmdb_user where name =%s and id !=%s
"""

INSERT_USER_SQL = """
INSERT INTO cmdb_user (name ,password,age,sex,tel,remark)
    VALUES (%s,%s,%s,%s,%s,%s)
"""

FIND_USER_BY_ID = """
SELECT id, name , password, sex , age, tel, remark  FROM cmdb_user 
WHERE id = %s
"""

UPDATE_USER_BY_ID = """
UPDATE cmdb_user SET 
  name = %s,
  sex = %s,
  age = %s,
  tel = %s,
  remark = %s
where id = %s
"""

UPDATE_USER_PASSWORD_BY_ID = """
UPDATE cmdb_user SET 
  password = %s
where id = %s
"""

DELETE_USER_BY_ID_SQL = """
DELETE FROM cmdb_user where id = %s
"""


def get_users():
    """
    result = get_all(LIST_SQL, None)
    users = []
    for item in result:
        users.append({
            'id': item[0],
            'name': item[1],
            'password': item[2],
            'sex': item[3],
            'age': item[4],
            'tel': item[5],
            'desc': item[6]
        })
    """
    return DbUtils.get_all(LIST_SQL, None)


def valid_login_model(name, password):
    result = DbUtils.get_one(LOGIN_SQL, (name, password))
    """
    return {
        'id': result[0],
        'name': result[1],
        'password': result[2],
        'sex': result[3],
        'age': result[4],
        'tel': result[5],
        'desc': result[6]
    } if result else None
    """
    return result if result else None


def valid_create_user(post_info):
    name = post_info.get('name', '')
    password = post_info.get('password', '')
    password_confirm = post_info.get('password_confirm', '')
    sex = post_info.get('sex', '')
    age = post_info.get('age', '')
    tel = post_info.get('tel', '')
    remark = post_info.get('remark', '')

    is_valid = True
    user = {}
    errors = {}

    user['name'] = name.strip()

    if user['name'] == '':
        is_valid = False
        errors['name'] = '用户名不能为空'
    else:
        result = DbUtils.get_one(CHECK_USER_NAME_SQL, (user['name'], 0))
        if result:
            errors['name'] = '用户名已存在'
            is_valid = False

    user['age'] = age.strip()
    if not user['age'].isdigit():
        errors['age'] = '年龄格式错误'
        is_valid = False

    user['tel'] = tel
    user['sex'] = sex
    user['password'] = password.strip()
    user['remark'] = remark

    if user['password'] == '' or password_confirm != user['password']:
        is_valid = False
        errors['password'] = '密码不能为空, 且两次输入密码必须相同'

    return is_valid, user, errors


def create_user(params):
    result = DbUtils.execute_sql(INSERT_USER_SQL, (
        params['name'], params['password'], params['age'], params['sex'], params['tel'], params['remark']))
    return result


def get_user(uid):
    result = DbUtils.get_one(FIND_USER_BY_ID, (uid,))
    return result


def valid_update_user(params):
    uid = params.get('id', '')
    name = params.get('name', '')
    tel = params.get('tel', '')
    age = params.get('age', '')
    sex = params.get('sex', '')
    remark = params.get('remark', '')
    is_valid = True
    user = {}
    errors = {}
    user_tmp = get_user(uid)

    if user_tmp is None:
        errors['id'] = '用户信息不存在'
        is_valid = False
    user['id'] = uid.strip()
    user['name'] = name.strip()

    result = DbUtils.get_one(CHECK_USER_NAME_SQL, (user['name'], user['id']))
    if result:
        errors['name'] = '用户名已存在'
        is_valid = False

    user['age'] = age.strip()
    if not user['age'].isdigit():
        errors['age'] = '年龄格式错误'
        is_valid = False

    user['tel'] = tel
    user['sex'] = sex
    user['remark'] = remark

    return is_valid, user, errors


def update_user(params):
    result = DbUtils.execute_sql(UPDATE_USER_BY_ID,
                                 (params['name'], params['sex'], params['age'], params['tel'], params['remark'],
                                  params['id']))
    return result


def delete_user(uid):
    result = DbUtils.execute_sql(DELETE_USER_BY_ID_SQL, (uid,))
    return result


def user_change_pwd_chk(params):
    old_pw = params.POST.get('password_old', '')
    new_pw = params.POST.get('password', '')
    new_pw_confirm = params.POST.get('password_confirm', '')
    login_user = params.session.get('login_user')
    is_valid = True
    errors = {}

    session_pwd = login_user['password']
    if old_pw != session_pwd:
        errors['0001'] = '原密码错误'
        is_valid = False
    if new_pw != new_pw_confirm:
        errors['0002'] = '两次输入密码不一致'
        is_valid = False

    return is_valid, new_pw, errors


def update_user_password(params):
    result = DbUtils.execute_sql(UPDATE_USER_PASSWORD_BY_ID,
                                 (params['password'], params['id']))
    return result


def search_users(conditions):
    return DbUtils.get_all(LIST_SQL_BY_CONDITIONS, ('%' + conditions + '%',))

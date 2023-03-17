from wtforms import Form, StringField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo


# Article Form Class
class ArticleForm(Form):
    title = StringField(
        '标题',
        validators=[
            # DataRequired(message= '标题长度应该在2-30字符之间'),
            DataRequired(message='长度不少于5个字符'),
            Length(min=2, max=30)
        ])
    content = TextAreaField(
        '内容', validators=[DataRequired(message='长度不少于5个字符'),
                          Length(min=5)])


# Register Form Class
class RegisterForm(Form):
    username = StringField('用户名',
                           validators=[
                               DataRequired(message='请输入用户名'),
                               Length(min=2, max=25, message='长度在2-25个字符之间')
                           ])
    email = StringField('邮箱',
                        validators=[
                            DataRequired(message="请输入邮箱"),
                            Email(message='请输入正确的邮箱格式')
                        ])
    password = PasswordField('密码',
                             validators=[
                                 DataRequired(message='密码不能为空'),
                                 Length(min=6, max=20, message='长度在6-20个字符之间'),
                             ])
    confirm = PasswordField('确认密码',
                            validators=[
                                DataRequired(message='密码不能为空'),
                                Length(min=6, max=20),
                                EqualTo('password', message='2次输入密码不一致')
                            ])

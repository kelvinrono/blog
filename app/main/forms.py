from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField,ValidationError
from wtforms.validators import Required
from ..models import User,Subscriber

class BlogsForm(FlaskForm):
    title = StringField('Blog Title')
    category = SelectField(u'Blog Categories', choices=[('Technology', 'Technology'),('Love', 'Love'),('Life', 'Life'),('Politics', 'Politics')])
    blog = TextAreaField('Blog')
    submit = SubmitField('Submit')
    
class CommentForm(FlaskForm):
    comment = TextAreaField('Comment')
    submit = SubmitField('Post Comments')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Add Your profile.',validators = [Required()])
    submit = SubmitField('Submit')

class SubscriberForm(FlaskForm):
    email = StringField('Enter your valid email address.',validators = [Required()])
    username = StringField('Username', validators = [Required()])
    submit = SubmitField('Subscribe')

    def validate_email(self,data_field):
        if Subscriber.query.filter_by(email = data_field.data).first():
            raise ValidationError('Your data already exists') 